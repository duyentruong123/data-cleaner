import argparse


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="data_cleaner",
        description="CLI tool to profile and clean CSV files.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # profile command
    subparsers.add_parser("profile", help="Analyze a CSV file")

    # clean command
    subparsers.add_parser("clean", help="Clean a CSV file")

    # validate command
    subparsers.add_parser("validate", help="Validate a CSV file")

    parser.parse_args(argv)

    print("data_cleaner CLI is working ✅")
    return 0