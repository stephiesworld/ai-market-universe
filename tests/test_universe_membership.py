from __future__ import annotations

import tempfile
import unittest
from datetime import UTC, datetime
from pathlib import Path

from ai_market_universe.universe import load_universe_as_of

REPO_ROOT = Path(__file__).resolve().parents[1]
UNIVERSE_V0 = REPO_ROOT / "configs" / "universe_v0.csv"
SMOKE_TICKERS = ["AAPL", "MSFT", "JPM", "XOM", "JNJ"]


class UniverseMembershipTests(unittest.TestCase):
    def test_v0_columns_include_effective_dates_without_extra_names(self) -> None:
        header = UNIVERSE_V0.read_text(encoding="utf-8").splitlines()[0]
        columns = header.split(",")
        self.assertIn("valid_from", columns)
        self.assertIn("valid_to", columns)
        members = load_universe_as_of(str(UNIVERSE_V0), datetime(2024, 6, 15, tzinfo=UTC))
        self.assertEqual(members["ticker"].tolist(), SMOKE_TICKERS)

    def test_v0_name_is_absent_before_valid_from(self) -> None:
        before = load_universe_as_of(str(UNIVERSE_V0), datetime(2023, 12, 31, tzinfo=UTC))
        at_start = load_universe_as_of(str(UNIVERSE_V0), datetime(2024, 1, 1, tzinfo=UTC))
        self.assertEqual(before["ticker"].tolist(), [])
        self.assertEqual(at_start["ticker"].tolist(), SMOKE_TICKERS)

    def test_name_is_absent_after_valid_to(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "universe.csv"
            path.write_text(
                "ticker,selection_rule,valid_from,valid_to\n"
                "OLD,rule,2020-01-01,2024-01-01\n"
                "NEW,rule,2024-01-01,\n",
                encoding="utf-8",
            )
            before_old = load_universe_as_of(path, datetime(2019, 12, 31, tzinfo=UTC))
            during_old = load_universe_as_of(path, datetime(2023, 12, 31, 23, 59, tzinfo=UTC))
            at_old_end = load_universe_as_of(path, datetime(2024, 1, 1, tzinfo=UTC))
            after_old = load_universe_as_of(path, datetime(2024, 6, 1, tzinfo=UTC))
            self.assertEqual(before_old["ticker"].tolist(), [])
            self.assertEqual(during_old["ticker"].tolist(), ["OLD"])
            self.assertEqual(at_old_end["ticker"].tolist(), ["NEW"])
            self.assertEqual(after_old["ticker"].tolist(), ["NEW"])
            self.assertNotIn("OLD", after_old["ticker"].tolist())
            self.assertNotIn("NEW", before_old["ticker"].tolist())
