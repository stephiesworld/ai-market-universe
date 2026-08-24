from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from .evaluation import evaluate_predictions
from .features import build_price_features, complete_snapshot, snapshot_from_price_feature_row
from .labels import generate_forward_labels
from .models import MomentumBaseline, RidgeRegressor, ZeroExcessBaseline, temporal_split
from .schemas import EvidenceTrack, Forecast
from .storage import ForecastStore


TICKERS = ["AAPL", "MSFT", "JPM", "XOM", "JNJ"]
SECTORS = {
    "AAPL": "Information Technology",
    "MSFT": "Information Technology",
    "JPM": "Financials",
    "XOM": "Energy",
    "JNJ": "Health Care",
}
FEATURE_COLUMNS = [
    "momentum_20d",
    "momentum_60d",
    "excess_momentum_20d",
    "realized_volatility_20d",
    "drawdown_60d",
]
DEFERRED_POINT_IN_TIME_FEATURES = [
    "consensus_eps",
    "consensus_revenue",
    "estimate_revision_30d",
    "forward_pe",
]


def synthetic_prices(seed: int = 11) -> pd.DataFrame:
    """Deterministic fixture data for plumbing tests; never presented as market evidence."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2022-01-03", periods=620, tz="UTC")
    rows: list[dict[str, object]] = []
    market_shocks = rng.normal(0.00025, 0.008, len(dates))
    for index, ticker in enumerate(["SPY", *TICKERS]):
        idiosyncratic = rng.normal(0.00005 * (index - 2), 0.006 + 0.001 * index, len(dates))
        returns = market_shocks if ticker == "SPY" else 0.75 * market_shocks + idiosyncratic
        for day in range(2, len(returns)):
            returns[day] += 0.06 * returns[day - 1] + 0.025 * returns[day - 2]
        prices = 100 * np.exp(np.cumsum(returns))
        rows.extend(
            {"ticker": ticker, "timestamp": timestamp, "adjusted_close": float(price)}
            for timestamp, price in zip(dates, prices)
        )
    return pd.DataFrame(rows)


def build_research_frame() -> pd.DataFrame:
    prices = synthetic_prices()
    dates = sorted(prices.loc[prices["ticker"] == "SPY", "timestamp"].unique())
    cohort_dates = dates[90:-75:5]
    features = pd.concat(
        [build_price_features(prices, TICKERS, date) for date in cohort_dates],
        ignore_index=True,
    )
    observations = features[["ticker", "prediction_timestamp"]]
    labels = generate_forward_labels(prices, observations, horizons=(90,))
    return features.merge(
        labels.drop(columns=["price_day_0"]),
        on=["ticker", "prediction_timestamp"],
        validate="one_to_one",
    )


def run_demo(output_dir: str | Path) -> dict[str, object]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    frame = build_research_frame().sort_values("prediction_timestamp")
    unique_dates = sorted(frame["prediction_timestamp"].unique())
    train_end = unique_dates[int(len(unique_dates) * 0.60)]
    validation_end = unique_dates[int(len(unique_dates) * 0.80)]
    train, validation, test = temporal_split(frame, train_end, validation_end)

    ridge = RidgeRegressor(alpha=20.0).fit(
        pd.concat([train, validation], ignore_index=True),
        pd.concat([train, validation], ignore_index=True)["realized_excess_return_90d"],
        FEATURE_COLUMNS,
    )
    models = [ZeroExcessBaseline(), MomentumBaseline(), ridge]
    report: dict[str, object] = {
        "warning": "Results use deterministic synthetic fixture data and are pipeline checks, not market evidence.",
        "evidence_track": EvidenceTrack.SYNTHETIC_FIXTURE.value,
        "is_prospective_evidence": False,
        "split": {
            "train_end": str(train_end),
            "validation_end": str(validation_end),
            "test_rows": len(test),
        },
        "models": {},
    }
    prediction_frames = []
    for model in models:
        scored = test.copy()
        scored["model"] = model.name
        scored["predicted_excess_return_90d"] = model.predict(scored)
        report["models"][model.name] = evaluate_predictions(scored)
        prediction_frames.append(scored)

    pd.concat(prediction_frames, ignore_index=True).to_csv(output / "demo_predictions.csv", index=False)
    latest_timestamp = frame["prediction_timestamp"].max()
    latest = frame.loc[frame["prediction_timestamp"] == latest_timestamp].copy()
    latest["predicted_excess_return_90d"] = ridge.predict(latest)
    store_path = output / "demo_forecasts.sqlite3"
    if store_path.exists():
        store_path.unlink()
    store = ForecastStore(store_path, EvidenceTrack.SYNTHETIC_FIXTURE)
    for row in latest.itertuples(index=False):
        score = float(row.predicted_excess_return_90d)
        probability = float(1 / (1 + np.exp(-score / 0.05)))
        confidence = float(min(0.85, 0.35 + abs(score) * 2))
        snapshot_row = pd.Series(row._asdict())
        snapshot = snapshot_from_price_feature_row(
            snapshot_row,
            source="synthetic_total_return_prices",
        )
        snapshot = complete_snapshot(
            snapshot,
            DEFERRED_POINT_IN_TIME_FEATURES,
            "no historical point-in-time vendor record connected",
        )
        store.append(
            Forecast(
                evidence_track=EvidenceTrack.SYNTHETIC_FIXTURE,
                cohort_id=f"synthetic_{latest_timestamp.date()}_ridge_v1",
                ticker=row.ticker,
                prediction_timestamp=pd.Timestamp(latest_timestamp).to_pydatetime(),
                price_day_0=float(row.price_day_0),
                spy_day_0=100.0,
                predicted_return_90d=score,
                predicted_excess_return_90d=score,
                prob_outperform_spy=probability,
                confidence=confidence,
                bull_case_return=score + 0.12,
                base_case_return=score,
                bear_case_return=score - 0.12,
                consensus_view="Synthetic fixture assumes no explicit consensus view.",
                ai_view="Transparent ridge baseline applied to price-only fixture features.",
                variant_perception="Not applicable to synthetic fixture data.",
                thesis="Engineering-only forecast used to verify the immutable forecast contract.",
                catalysts=(),
                risks=("synthetic data", "price-only feature set"),
                sector=SECTORS[row.ticker],
                model_version="ridge_v1",
                prompt_version="none_v0",
                feature_schema_version="v0.1",
                data_snapshot_version="synthetic_fixture_v1",
                feature_snapshot=snapshot.model_dump(mode="json"),
            )
        )
    store.export_manifest(output / "demo_forecast_manifest.json")
    report["immutable_forecasts"] = len(store.manifest())
    (output / "demo_metrics.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    frame.to_csv(output / "demo_research_frame.csv", index=False)
    return report
