from __future__ import annotations

import io
import json
import tempfile
import unittest
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import patch

from ai_market_universe.cli import ingest_csv, main, parse_as_of
from ai_market_universe.schemas import EvidenceTrack
from ai_market_universe.storage import ForecastStore

FIXTURE = Path(__file__).parent / "fixtures" / "pit_long_form.csv"
AS_OF_BEFORE_RESTATEMENT = datetime(2024, 11, 20, 21, tzinfo=UTC)
AS_OF_AFTER_RESTATEMENT = datetime(2024, 12, 20, 21, tzinfo=UTC)


def _by_key(records: list[dict[str, object]]) -> dict[tuple[str, str], dict[str, object]]:
    return {(str(row["ticker"]), str(row["field"])): row for row in records}


class CsvPointInTimeIngestTests(unittest.TestCase):
    def test_future_available_at_is_rejected(self) -> None:
        report = ingest_csv(FIXTURE, AS_OF_BEFORE_RESTATEMENT)
        records = report["records"]
        assert isinstance(records, list)
        ids = {row["source_record_id"] for row in records}
        self.assertNotIn("aapl-cons-eps-future", ids)
        cutoff = parse_as_of(str(report["as_of"]))
        for row in records:
            self.assertLessEqual(parse_as_of(str(row["available_at"])), cutoff)

    def test_restatement_hidden_until_available(self) -> None:
        before = _by_key(ingest_csv(FIXTURE, AS_OF_BEFORE_RESTATEMENT)["records"])
        after = _by_key(ingest_csv(FIXTURE, AS_OF_AFTER_RESTATEMENT)["records"])
        self.assertEqual(before[("AAPL", "consensus_eps")]["source_record_id"], "aapl-cons-eps-v1")
        self.assertEqual(before[("AAPL", "consensus_eps")]["value"], 2.10)
        self.assertEqual(after[("AAPL", "consensus_eps")]["source_record_id"], "aapl-cons-eps-v2")
        self.assertEqual(after[("AAPL", "consensus_eps")]["value"], 2.25)

    def test_missing_consensus_is_null(self) -> None:
        keyed = _by_key(ingest_csv(FIXTURE, AS_OF_BEFORE_RESTATEMENT)["records"])
        msft = keyed[("MSFT", "consensus_eps")]
        self.assertIsNone(msft["value"])
        self.assertNotIn(("JPM", "consensus_eps"), keyed)
        self.assertNotEqual(msft["value"], 0)
        self.assertNotEqual(msft["value"], 0.0)

    def test_path_writes_historical_backtest_never_synthetic_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store_path = Path(directory) / "ingest_forecasts.sqlite3"
            report = ingest_csv(FIXTURE, AS_OF_BEFORE_RESTATEMENT, store_path)
            self.assertEqual(report["evidence_track"], EvidenceTrack.HISTORICAL_BACKTEST.value)
            self.assertNotEqual(report["evidence_track"], EvidenceTrack.SYNTHETIC_FIXTURE.value)
            self.assertFalse(report["is_prospective_evidence"])
            self.assertNotIn("predicted_excess_return_90d", report)
            ForecastStore(store_path, EvidenceTrack.HISTORICAL_BACKTEST)
            with self.assertRaises(ValueError):
                ForecastStore(store_path, EvidenceTrack.SYNTHETIC_FIXTURE)

    def test_cli_prints_as_of_frame(self) -> None:
        argv = [
            "market-universe",
            "ingest-csv",
            "--csv",
            str(FIXTURE),
            "--as-of",
            AS_OF_BEFORE_RESTATEMENT.isoformat(),
        ]
        stdout = io.StringIO()
        with patch("sys.argv", argv), patch("sys.stdout", stdout):
            main()
        report = json.loads(stdout.getvalue())
        self.assertEqual(report["evidence_track"], "historical_backtest")
        self.assertTrue(report["records"])
        self.assertIn("AAPL", {row["ticker"] for row in report["records"]})


if __name__ == "__main__":
    unittest.main()
