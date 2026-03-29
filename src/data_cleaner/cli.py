import argparse
from pathlib import Path

from .csv_io import load_csv, save_csv
from .preprocessing import clean_nasa_dataset
from .analysis import compute_volatility_analysis
from .reporting import generate_text_report, save_visualizations


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="NASA Temperature Volatility Analysis Tool"
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Path to NASA temperature CSV file"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/cleaned_temperature.csv"),
        help="Path to save cleaned dataset"
    )

    args = parser.parse_args(argv)

    print("Loading dataset...")
    df = load_csv(args.input)

    print("Cleaning dataset...")
    df_clean = clean_nasa_dataset(df)

    print("Running analysis...")
    results = compute_volatility_analysis(df_clean)

    print("Saving cleaned dataset...")
    save_csv(df_clean, args.output)

    print("Generating visualization...")
    results_path = Path("data/results")
    plot_file = save_visualizations(df_clean, results_path)

    print("\n=== ANALYSIS REPORT ===\n")
    report = generate_text_report(results)
    print(report)

    print(f"\nVisual trend saved to: {plot_file}")

    return 0