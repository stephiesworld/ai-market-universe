from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from .demo import run_demo
from .providers import CsvPointInTimeProvider
from .schemas import EvidenceTrack
from .storage import ForecastStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="market-universe")
    subparsers = parser.add_subparsers(dest="command", required=True)
    demo = subparsers.add_parser("demo", help="run the deterministic end-to-end research harness")
    demo.add_argument("--output-dir", default="artifacts/demo")
    ingest = subparsers.add_parser(
        "ingest-csv",
        help="resolve a long-form PIT CSV as of a frozen timestamp (no forecast/alpha output)",
    )
    ingest.add_argument("--csv", required=True, help="path to long-form point-in-time CSV")
    ingest.add_argument("--as-of", required=True, dest="as_of", help="ISO-8601 prediction timestamp")
    ingest.add_argument(
        "--store",
        default=None,
        help="optional SQLite path locked to historical_backtest for this ingest",
    )
    return parser


def parse_as_of(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def ingest_csv(
    csv_path: str | Path,
    as_of: datetime,
    store_path: str | Path | None = None,
) -> dict[str, object]:
    """Load vendor-neutral PIT rows and print the knowable as-of frame.

    This path is historical_backtest plumbing only: it never labels output as
    synthetic_fixture and it does not emit model scores or alpha claims.
    """
    timestamp = parse_as_of(as_of.isoformat()) if as_of.tzinfo is None else as_of.astimezone(UTC)
    frame = CsvPointInTimeProvider(csv_path).observations_as_of(timestamp)
    report: dict[str, object] = {
        "evidence_track": EvidenceTrack.HISTORICAL_BACKTEST.value,
        "is_prospective_evidence": False,
        "as_of": timestamp.isoformat(),
        "csv": str(Path(csv_path)),
        "records": json.loads(frame.to_json(orient="records", date_format="iso")),
    }
    if store_path is not None:
        path = Path(store_path)
        ForecastStore(path, EvidenceTrack.HISTORICAL_BACKTEST)
        report["store"] = str(path)
    return report


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "demo":
        report = run_demo(Path(args.output_dir))
        print(json.dumps(report, indent=2))
    elif args.command == "ingest-csv":
        report = ingest_csv(
            Path(args.csv),
            parse_as_of(args.as_of),
            Path(args.store) if args.store else None,
        )
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
