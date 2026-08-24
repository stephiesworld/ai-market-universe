from __future__ import annotations

import argparse
import json
from pathlib import Path

from .demo import run_demo


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="market-universe")
    subparsers = parser.add_subparsers(dest="command", required=True)
    demo = subparsers.add_parser("demo", help="run the deterministic end-to-end research harness")
    demo.add_argument("--output-dir", default="artifacts/demo")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "demo":
        report = run_demo(Path(args.output_dir))
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
