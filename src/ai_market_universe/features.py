from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import numpy as np
import pandas as pd

from .point_in_time import PointInTimeError
from .schemas import FeatureSnapshot, FeatureValue, Provenance


@dataclass(frozen=True)
class FeatureDefinition:
    name: str
    family: str
    economic_rationale: str
    raw_source: str
    formula: str
    lookback: str
    publication_lag: str
    normalization: str


def load_registry(path: str) -> dict[str, FeatureDefinition]:
    rows = pd.read_csv(path).fillna("")
    return {row["name"]: FeatureDefinition(**row.to_dict()) for _, row in rows.iterrows()}


def _price_at_or_before(prices: pd.DataFrame, ticker: str, timestamp: pd.Timestamp) -> pd.DataFrame:
    history = prices.loc[
        (prices["ticker"] == ticker) & (prices["timestamp"] <= timestamp)
    ].sort_values("timestamp")
    if history.empty:
        raise PointInTimeError(f"no price history for {ticker} by {timestamp}")
    return history


def build_price_features(
    prices: pd.DataFrame,
    tickers: list[str],
    prediction_timestamp: datetime,
    benchmark: str = "SPY",
) -> pd.DataFrame:
    """Build close-to-close features using only observations through the cohort timestamp."""
    data = prices.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], utc=True)
    cutoff = pd.Timestamp(prediction_timestamp)
    cutoff = cutoff.tz_localize("UTC") if cutoff.tzinfo is None else cutoff.tz_convert("UTC")
    benchmark_history = _price_at_or_before(data, benchmark, cutoff)

    def trailing_return(history: pd.DataFrame, periods: int) -> float:
        if len(history) <= periods:
            return np.nan
        return float(history["adjusted_close"].iloc[-1] / history["adjusted_close"].iloc[-periods - 1] - 1)

    benchmark_20 = trailing_return(benchmark_history, 20)
    rows: list[dict[str, object]] = []
    for ticker in tickers:
        history = _price_at_or_before(data, ticker, cutoff)
        returns = history["adjusted_close"].pct_change().dropna()
        current = float(history["adjusted_close"].iloc[-1])
        window_60 = history["adjusted_close"].tail(60)
        momentum_20 = trailing_return(history, 20)
        realized_vol = (
            float(returns.tail(20).std(ddof=1) * np.sqrt(252)) if len(returns) >= 20 else np.nan
        )
        drawdown = float(current / float(window_60.max()) - 1) if len(window_60) >= 60 else np.nan
        rows.append(
            {
                "ticker": ticker,
                "prediction_timestamp": cutoff,
                "price_day_0": current,
                "momentum_20d": momentum_20,
                "momentum_60d": trailing_return(history, 60),
                "excess_momentum_20d": momentum_20 - benchmark_20,
                "realized_volatility_20d": realized_vol,
                "drawdown_60d": drawdown,
                "available_at": history["timestamp"].iloc[-1],
            }
        )
    result = pd.DataFrame(rows)
    if (result["available_at"] > result["prediction_timestamp"]).any():
        raise PointInTimeError("price feature contains future information")
    return result


def snapshot_from_price_feature_row(
    row: pd.Series,
    feature_schema_version: str = "v0.1",
    source: str = "total_return_prices",
) -> FeatureSnapshot:
    """Convert a normalized row to the versioned, provenance-preserving forecast input."""
    available_at = pd.Timestamp(row["available_at"]).to_pydatetime()
    prediction_timestamp = pd.Timestamp(row["prediction_timestamp"]).to_pydatetime()
    features: dict[str, FeatureValue] = {}
    for name in (
        "momentum_20d",
        "momentum_60d",
        "excess_momentum_20d",
        "realized_volatility_20d",
        "drawdown_60d",
    ):
        value = row[name]
        if pd.isna(value):
            features[name] = missing_feature(
                prediction_timestamp,
                f"insufficient price history for {name}",
            )
        else:
            features[name] = FeatureValue(
                value=float(value),
                available=True,
                provenance=Provenance(
                    as_of=prediction_timestamp,
                    source=source,
                    source_record_id=f"{row['ticker']}:{available_at.isoformat()}:{name}",
                    published_at=available_at,
                    effective_at=available_at,
                    available_at=available_at,
                    ingested_at=available_at,
                    point_in_time_verified=True,
                ),
                missing_reason=None,
            )
    return FeatureSnapshot(
        ticker=str(row["ticker"]),
        prediction_timestamp=prediction_timestamp,
        feature_schema_version=feature_schema_version,
        features=features,
    )


def missing_feature(
    as_of: datetime,
    reason: str,
    point_in_time_verified: bool = True,
) -> FeatureValue:
    """Represent a verified absence; this state is intentionally different from numeric zero."""
    return FeatureValue(
        value=None,
        available=False,
        missing_reason=reason,
        provenance=Provenance(
            as_of=as_of,
            source=None,
            source_record_id=None,
            published_at=None,
            effective_at=None,
            available_at=None,
            ingested_at=None,
            point_in_time_verified=point_in_time_verified,
        ),
    )


def complete_snapshot(
    snapshot: FeatureSnapshot,
    expected_feature_names: list[str],
    missing_reason: str,
) -> FeatureSnapshot:
    """Materialize absent registered fields as explicit unavailable values."""
    features = dict(snapshot.features)
    for name in expected_feature_names:
        if name not in features:
            features[name] = missing_feature(
                snapshot.prediction_timestamp,
                missing_reason,
                point_in_time_verified=True,
            )
    return FeatureSnapshot(
        ticker=snapshot.ticker,
        prediction_timestamp=snapshot.prediction_timestamp,
        feature_schema_version=snapshot.feature_schema_version,
        features=features,
    )
