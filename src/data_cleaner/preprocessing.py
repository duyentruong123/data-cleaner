import pandas as pd


def clean_nasa_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean NASA temperature dataset:
    - Remove metadata rows
    - Replace "***" with NaN
    - Convert monthly columns to numeric
    - Reshape to long format
    """

    # Remove metadata rows (keep only rows with valid year)
    df = df[df["Year"].astype(str).str.match(r"\d{4}", na=False)].copy()

    # Replace NASA missing marker
    df.replace("***", pd.NA, inplace=True)
    
    # 1. Define only the real months
    month_cols = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # only include Year + those 12 months, ignores the "J-D", "D-N", etc.
    df = df[["Year"] + month_cols].copy()

    # Convert numeric columns
    for col in df.columns:
        if col != "Year":
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Melt to long format
    df_long = df.melt(
        id_vars="Year",
        var_name="Month",
        value_name="Temperature_Anomaly"
    )

    df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")

    # return df_long.dropna(subset=["Temperature_Anomaly"])
    return df_long