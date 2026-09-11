from __future__ import annotations

import sqlite3
import tempfile
import unittest
from datetime import UTC, datetime
from pathlib import Path

from ai_market_universe.schemas import EvidenceTrack, Forecast
from ai_market_universe.storage import ForecastStore

NOW = datetime(2025, 1, 3, 21, tzinfo=UTC)


def make_forecast(
    evidence_track: EvidenceTrack,
    *,
    ticker: str = "AAPL",
    cohort_id: str = "2025-01-03_v1",
) -> Forecast:
    return Forecast(
        evidence_track=evidence_track,
        cohort_id=cohort_id,
        ticker=ticker,
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


class ForecastStoreTrackIsolationTests(unittest.TestCase):
    def test_cannot_append_synthetic_into_historical_store(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ForecastStore(
                Path(directory) / "forecasts.sqlite3",
                EvidenceTrack.HISTORICAL_BACKTEST,
            )
            with self.assertRaises(ValueError) as raised:
                store.append(make_forecast(EvidenceTrack.SYNTHETIC_FIXTURE))
            self.assertIn("synthetic_fixture", str(raised.exception))
            self.assertIn("historical_backtest", str(raised.exception))
            self.assertEqual(store.manifest(), [])

    def test_cannot_append_historical_into_synthetic_store(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ForecastStore(
                Path(directory) / "forecasts.sqlite3",
                EvidenceTrack.SYNTHETIC_FIXTURE,
            )
            with self.assertRaises(ValueError) as raised:
                store.append(make_forecast(EvidenceTrack.HISTORICAL_BACKTEST))
            self.assertIn("historical_backtest", str(raised.exception))
            self.assertIn("synthetic_fixture", str(raised.exception))
            self.assertEqual(store.manifest(), [])

    def test_sqlite_insert_cannot_mix_tracks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "forecasts.sqlite3"
            ForecastStore(path, EvidenceTrack.HISTORICAL_BACKTEST)
            payload = make_forecast(EvidenceTrack.SYNTHETIC_FIXTURE).model_dump_json()
            with sqlite3.connect(path) as connection:
                with self.assertRaises(sqlite3.IntegrityError) as raised:
                    connection.execute(
                        "INSERT INTO forecasts("
                        "evidence_track,cohort_id,ticker,prediction_timestamp,"
                        "payload_json,payload_sha256"
                        ") VALUES (?,?,?,?,?,?)",
                        (
                            EvidenceTrack.SYNTHETIC_FIXTURE.value,
                            "2025-01-03_v1",
                            "AAPL",
                            NOW.isoformat(),
                            payload,
                            "deadbeef",
                        ),
                    )
            self.assertIn("cannot mix evidence tracks", str(raised.exception))

    def test_evidence_track_metadata_cannot_be_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "forecasts.sqlite3"
            ForecastStore(path, EvidenceTrack.HISTORICAL_BACKTEST)
            with sqlite3.connect(path) as connection:
                with self.assertRaises(sqlite3.IntegrityError):
                    connection.execute(
                        "UPDATE store_metadata SET value=? WHERE key='evidence_track'",
                        (EvidenceTrack.SYNTHETIC_FIXTURE.value,),
                    )
                with self.assertRaises(sqlite3.IntegrityError):
                    connection.execute(
                        "DELETE FROM store_metadata WHERE key='evidence_track'"
                    )


if __name__ == "__main__":
    unittest.main()
