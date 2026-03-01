from __future__ import annotations

import argparse
from pathlib import Path

from .csv_io import load_csv
from .profiling import profile_dataframe, format_profile


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="data_cleaner",
        description="Profile and clean messy CSV datasets.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # profile command
    profile_p = subparsers.add_parser("profile", help="Analyze a CSV file (missing values, duplicates).")
    profile_p.add_argument("csv", type=Path)

    # keep placeholders for later commits
    subparsers.add_parser("clean", help="(Coming soon) Clean a CSV file.")
    subparsers.add_parser("validate", help="(Coming soon) Validate a CSV file.")

    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "profile":
        df = load_csv(args.csv)
        summary = profile_dataframe(df)
        print(format_profile(summary))
        return 0

    # clean/validate not implemented yet
    print("This command is not implemented yet.")
    return 1