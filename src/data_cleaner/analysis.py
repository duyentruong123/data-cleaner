import pandas as pd

def compute_volatility_analysis(df: pd.DataFrame) -> dict:
    """
    Compare temperature anomaly volatility between:
    - 1951–1980 baseline
    - 2001–present
    """
    # Aggregate to yearly mean
    yearly = (
        df.groupby("Year")["Temperature_Anomaly"]
        .mean()
        .reset_index()
    )

    baseline = yearly[(yearly["Year"] >= 1951) & (yearly["Year"] <= 1980)]
    modern = yearly[yearly["Year"] >= 2001]

    baseline_std = baseline["Temperature_Anomaly"].std()
    modern_std = modern["Temperature_Anomaly"].std()

    return {
        "baseline_std": baseline_std,
        "modern_std": modern_std,
        "difference": modern_std - baseline_std
    }