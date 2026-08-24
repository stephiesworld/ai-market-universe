from __future__ import annotations

import sqlite3
import tempfile
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd

from ai_market_universe.demo import run_demo
from ai_market_universe.evaluation import evaluate_predictions
from ai_market_universe.features import (
    build_price_features,
    complete_snapshot,
    missing_feature,
    snapshot_from_price_feature_row,
)
from ai_market_universe.labels import generate_forward_labels
from ai_market_universe.models import RidgeRegressor, temporal_split
from ai_market_universe.pead import build_pead_event_features
from ai_market_universe.point_in_time import PointInTimeError, assert_no_future_information
from ai_market_universe.schemas import EvidenceTrack, FeatureSnapshot, FeatureValue, Forecast, Provenance
from ai_market_universe.storage import ForecastStore
from ai_market_universe.universe import load_universe_as_of


NOW = datetime(2025, 1, 3, 21, tzinfo=UTC)


def _price_panel(closes: dict[str, list[float]], start: str = "2025-01-02") -> tuple[pd.DataFrame, pd.Timestamp]:
    length = len(next(iter(closes.values())))
    dates = pd.bdate_range(start, periods=length, tz="UTC")
    rows = [
        {"ticker": ticker, "timestamp": timestamp, "adjusted_close": float(price)}
        for ticker, prices in closes.items()
        for timestamp, price in zip(dates, prices)
    ]
    return pd.DataFrame(rows), dates[-1]


def forecast() -> Forecast:
    return Forecast(
        evidence_track=EvidenceTrack.PROSPECTIVE_LIVE_PAPER,
        cohort_id="2025-01-03_v1",
        ticker="AAPL",
        prediction_timestamp=NOW,
        price_day_0=100,
        spy_day_0=500,
        predicted_return_90d=0.08,
        predicted_excess_return_90d=0.03,
        prob_outperform_spy=0.61,
        confidence=0.55,
        bull_case_return=0.20,
        base_case_return=0.08,
        bear_case_return=-0.12,
        consensus_view="Expectations imply steady growth.",
        ai_view="Recent revisions are stronger than price action.",
        variant_perception="The market underweights revision breadth.",
        thesis="A measurable expectations gap may close within the horizon.",
        catalysts=("earnings",),
        risks=("multiple compression",),
        sector="Information Technology",
        model_version="ridge_v1",
        prompt_version="none_v0",
        feature_schema_version="v0.1",
        data_snapshot_version="fixture_v1",
        feature_snapshot={"momentum_60d": 0.05},
    )


class HarnessTests(unittest.TestCase):
    def test_point_in_time_guard_rejects_future_record(self) -> None:
        frame = pd.DataFrame(
            {"prediction_timestamp": [NOW], "available_at": [NOW + timedelta(seconds=1)]}
        )
        with self.assertRaises(PointInTimeError):
            assert_no_future_information(frame)

    def test_forward_labels_use_calendar_target_and_trading_close(self) -> None:
        prices = pd.DataFrame(
            [
                ("AAA", "2025-01-03T21:00:00Z", 100.0),
                ("AAA", "2025-01-13T21:00:00Z", 110.0),
                ("SPY", "2025-01-03T21:00:00Z", 200.0),
                ("SPY", "2025-01-13T21:00:00Z", 210.0),
            ],
            columns=["ticker", "timestamp", "adjusted_close"],
        )
        observations = pd.DataFrame({"ticker": ["AAA"], "prediction_timestamp": [NOW]})
        result = generate_forward_labels(prices, observations, horizons=(7,))
        self.assertAlmostEqual(result.loc[0, "realized_return_7d"], 0.10)
        self.assertAlmostEqual(result.loc[0, "realized_excess_return_7d"], 0.05)

    def test_evaluation_rewards_correct_rank(self) -> None:
        frame = pd.DataFrame(
            {
                "predicted_excess_return_90d": [-0.2, -0.1, 0.1, 0.3],
                "realized_excess_return_90d": [-0.3, -0.05, 0.05, 0.4],
            }
        )
        metrics = evaluate_predictions(frame)
        self.assertAlmostEqual(metrics["spearman_rank_ic"], 1.0)
        self.assertGreater(metrics["top_minus_bottom_spread"], 0)

    def test_constant_prediction_has_no_rank_metrics(self) -> None:
        frame = pd.DataFrame(
            {
                "predicted_excess_return_90d": [0.0, 0.0, 0.0],
                "realized_excess_return_90d": [-0.1, 0.0, 0.1],
            }
        )
        metrics = evaluate_predictions(frame)
        self.assertIsNone(metrics["spearman_rank_ic"])
        self.assertIsNone(metrics["top_minus_bottom_spread"])

    def test_pead_reaction_must_be_available(self) -> None:
        events = pd.DataFrame(
            {
                "event_id": ["AAA-2025Q1"],
                "ticker": ["AAA"],
                "announcement_timestamp": [NOW - timedelta(hours=2)],
                "prediction_timestamp": [NOW],
                "available_at": [NOW - timedelta(hours=2)],
                "eps_actual": [1.1],
                "eps_consensus": [1.0],
                "revenue_actual": [110.0],
                "revenue_consensus": [100.0],
            }
        )
        reactions = pd.DataFrame(
            {
                "event_id": ["AAA-2025Q1"],
                "ticker": ["AAA"],
                "earnings_day_abnormal_return": [0.02],
                "abnormal_volume": [1.5],
                "available_at": [NOW + timedelta(seconds=1)],
            }
        )
        with self.assertRaises(PointInTimeError):
            build_pead_event_features(events, reactions)

    def test_forecast_store_is_append_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ForecastStore(
                Path(directory) / "forecasts.sqlite3",
                EvidenceTrack.PROSPECTIVE_LIVE_PAPER,
            )
            store.append(forecast())
            loaded = store.load("2025-01-03_v1", "AAPL")
            self.assertEqual(loaded, forecast())
            with self.assertRaises(sqlite3.IntegrityError):
                store.append(forecast())
            with store.connect() as connection:
                with self.assertRaises(sqlite3.IntegrityError):
                    connection.execute("DELETE FROM forecasts")

    def test_missing_feature_is_not_numeric_zero(self) -> None:
        missing = missing_feature(NOW, "no point-in-time consensus vendor record")
        zero = FeatureValue(
            value=0.0,
            available=True,
            provenance=Provenance(
                as_of=NOW,
                source="verified_vendor",
                source_record_id="consensus-123",
                published_at=NOW - timedelta(minutes=10),
                effective_at=NOW,
                available_at=NOW - timedelta(minutes=10),
                ingested_at=NOW - timedelta(minutes=5),
                point_in_time_verified=True,
            ),
        )
        self.assertIsNone(missing.value)
        self.assertFalse(missing.available)
        self.assertEqual(zero.value, 0.0)
        self.assertTrue(zero.available)

    def test_expected_but_absent_feature_is_materialized(self) -> None:
        snapshot = FeatureSnapshot(
            ticker="AAPL",
            prediction_timestamp=NOW,
            feature_schema_version="v0.1",
            features={},
        )
        completed = complete_snapshot(
            snapshot,
            ["consensus_eps"],
            "no point-in-time consensus vendor record",
        )
        consensus = completed.features["consensus_eps"]
        self.assertIsNone(consensus.value)
        self.assertFalse(consensus.available)
        self.assertIsNone(consensus.provenance.source)

    def test_evidence_tracks_cannot_share_a_store(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "forecasts.sqlite3"
            ForecastStore(path, EvidenceTrack.PROSPECTIVE_LIVE_PAPER)
            with self.assertRaises(ValueError):
                ForecastStore(path, EvidenceTrack.HISTORICAL_BACKTEST)

    def test_universe_membership_is_resolved_as_of_date(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "universe.csv"
            path.write_text(
                "ticker,selection_rule,valid_from,valid_to\n"
                "OLD,rule,2020-01-01,2024-01-01\n"
                "NEW,rule,2024-01-01,\n",
                encoding="utf-8",
            )
            selected = load_universe_as_of(path, datetime(2023, 1, 1, tzinfo=UTC))
            self.assertEqual(selected["ticker"].tolist(), ["OLD"])

    def test_short_history_leaves_drawdown_and_volatility_unavailable(self) -> None:
        prices, cutoff = _price_panel(
            {
                "AAA": [100.0, 101.0, 99.0, 102.0, 103.0],
                "SPY": [200.0, 201.0, 199.0, 202.0, 203.0],
            }
        )
        result = build_price_features(prices, ["AAA"], cutoff)
        self.assertTrue(pd.isna(result.loc[0, "drawdown_60d"]))
        self.assertTrue(pd.isna(result.loc[0, "realized_volatility_20d"]))
        snapshot = snapshot_from_price_feature_row(result.iloc[0])
        for name in ("drawdown_60d", "realized_volatility_20d"):
            feature = snapshot.features[name]
            self.assertIsNone(feature.value)
            self.assertFalse(feature.available)

    def test_single_price_does_not_emit_zero_drawdown(self) -> None:
        prices, cutoff = _price_panel({"AAA": [100.0], "SPY": [200.0]})
        result = build_price_features(prices, ["AAA"], cutoff)
        self.assertTrue(pd.isna(result.loc[0, "drawdown_60d"]))
        self.assertFalse(result.loc[0, "drawdown_60d"] == 0.0)

    def test_full_windows_emit_drawdown_and_volatility_including_valid_zero(self) -> None:
        rising = [100.0 + day for day in range(60)]
        spy = [200.0 + 0.1 * day for day in range(60)]
        prices, cutoff = _price_panel({"AAA": rising, "SPY": spy})
        result = build_price_features(prices, ["AAA"], cutoff)
        self.assertAlmostEqual(result.loc[0, "drawdown_60d"], 0.0)
        self.assertFalse(pd.isna(result.loc[0, "realized_volatility_20d"]))
        snapshot = snapshot_from_price_feature_row(result.iloc[0])
        drawdown = snapshot.features["drawdown_60d"]
        self.assertEqual(drawdown.value, 0.0)
        self.assertTrue(drawdown.available)

    def test_volatility_requires_twenty_returns(self) -> None:
        twenty_prices = [100.0 + day for day in range(20)]
        prices, cutoff = _price_panel({"AAA": twenty_prices, "SPY": twenty_prices})
        short = build_price_features(prices, ["AAA"], cutoff)
        self.assertTrue(pd.isna(short.loc[0, "realized_volatility_20d"]))

        twenty_one_prices = [100.0 + day for day in range(21)]
        prices, cutoff = _price_panel({"AAA": twenty_one_prices, "SPY": twenty_one_prices})
        complete = build_price_features(prices, ["AAA"], cutoff)
        self.assertFalse(pd.isna(complete.loc[0, "realized_volatility_20d"]))
        self.assertTrue(pd.isna(complete.loc[0, "drawdown_60d"]))

    def test_drawdown_requires_sixty_prices(self) -> None:
        fifty_nine = [100.0 + day for day in range(59)]
        prices, cutoff = _price_panel({"AAA": fifty_nine, "SPY": fifty_nine})
        short = build_price_features(prices, ["AAA"], cutoff)
        self.assertTrue(pd.isna(short.loc[0, "drawdown_60d"]))

    def test_demo_uses_train_only_ridge_and_point_in_time_spy_close(self) -> None:
        fit_frames: list[pd.DataFrame] = []
        original_fit = RidgeRegressor.fit

        def capturing_fit(self, frame, target, columns):
            fit_frames.append(frame.copy())
            return original_fit(self, frame, target, columns)

        with tempfile.TemporaryDirectory() as directory:
            with patch.object(RidgeRegressor, "fit", capturing_fit):
                report = run_demo(directory)
            output = Path(directory)
            frame = pd.read_csv(output / "demo_research_frame.csv")
            train, validation, test = temporal_split(
                frame,
                report["split"]["train_end"],
                report["split"]["validation_end"],
            )
            self.assertEqual(len(fit_frames), 1)
            fit_timestamps = pd.to_datetime(fit_frames[0]["prediction_timestamp"], utc=True)
            train_end = pd.Timestamp(report["split"]["train_end"])
            self.assertEqual(len(fit_frames[0]), len(train))
            self.assertLessEqual(fit_timestamps.max(), train_end)
            self.assertFalse((fit_timestamps > train_end).any())

            last_val = pd.to_datetime(validation["prediction_timestamp"], utc=True).max()
            first_test = pd.to_datetime(test["prediction_timestamp"], utc=True).min()
            self.assertGreater(last_val + pd.Timedelta(days=90), first_test)

            store = ForecastStore(output / "demo_forecasts.sqlite3", EvidenceTrack.SYNTHETIC_FIXTURE)
            latest_timestamp = pd.to_datetime(frame["prediction_timestamp"], utc=True).max()
            latest = frame.loc[pd.to_datetime(frame["prediction_timestamp"], utc=True) == latest_timestamp]
            spy_values: list[float] = []
            for entry in store.manifest():
                loaded = store.load(entry["cohort_id"], entry["ticker"])
                expected = float(latest.loc[latest["ticker"] == entry["ticker"], "benchmark_day_0"].iloc[0])
                self.assertAlmostEqual(loaded.spy_day_0, expected, places=6)
                spy_values.append(loaded.spy_day_0)
            self.assertTrue(spy_values)
            self.assertTrue(np.allclose(spy_values, spy_values[0]))
            self.assertAlmostEqual(spy_values[0], 131.69, places=1)
            self.assertNotAlmostEqual(spy_values[0], 100.0, places=1)


if __name__ == "__main__":
    unittest.main()
