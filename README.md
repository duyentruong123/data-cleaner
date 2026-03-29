# NASA Temperature Analyzer
**CLI tool for cleaning and volatility analysis of NASA temperature anomaly data.**

This project provides a robust Command Line Interface (CLI) to process raw NASA GISTEMP data. It handles data cleaning, calculates rolling volatility (standard deviation) to identify significant climate shifts, and prepares the dataset for scientific visualization.

## Data Source
The dataset used in this analysis is the **GISS Surface Temperature Analysis (GISTEMP v4)**, provided by the NASA Goddard Institute for Space Studies.
**Source:** [NASA GISTEMP Data](https://data.giss.nasa.gov/gistemp/)

## Features
- Data Cleaning: Standardizes NASA-specific formatting for time-series analysis.
- Volatility Analysis: Computes statistical anomalies and variance in temperature trends.
- CLI Powered: Built with uv for high-performance dependency management and execution.

## Installation & Usage
To set up the project locally and run the analysis:

```bash
# 1. Install
uv pip install -e .

# 2. Run the analysis on the NASA dataset
uv run -m nasa_temp_analyzer data/raw/nasa_temperature.csv
