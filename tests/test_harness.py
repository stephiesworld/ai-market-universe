from __future__ import annotations

import sqlite3
import tempfile
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pandas as pd

from ai_market_universe.evaluation import evaluate_predictions
from ai_market_universe.features import complete_snapshot, missing_feature
from ai_market_universe.labels import generate_forward_labels
from ai_market_universe.pead import build_pead_event_features
from ai_market_universe.point_in_time import PointInTimeError, assert_no_future_information
from ai_market_universe.schemas import EvidenceTrack, FeatureSnapshot, FeatureValue, Forecast, Provenance
from ai_market_universe.storage import ForecastStore
from ai_market_universe.universe import load_universe_as_of


NOW = datetime(2025, 1, 3, 21, tzinfo=UTC)


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


if __name__ == "__main__":
    unittest.main()
