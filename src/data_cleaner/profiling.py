from __future__ import annotations
from dataclasses import dataclass
import pandas as pd

@dataclass
class ProfileSummary:
    rows: int
    cols: int
    duplicates: int
    missing_by_col: dict[str, int]

def profile_dataframe(df: pd.DataFrame) -> ProfileSummary:
    rows, cols = df.shape
    duplicates = int(df.duplicated().sum())

    missing_by_col: dict[str, int] = {}
    # Treat "" as missing for profiling (because we loaded dtype=str)
    for c in df.columns:
        s = df[c].replace("", pd.NA)
        missing_by_col[str(c)] = int(s.isna().sum())

    return ProfileSummary(rows=rows, cols=cols, duplicates=duplicates, missing_by_col=missing_by_col)

def format_profile(summary: ProfileSummary) -> str:
    lines = []
    lines.append(f"Rows: {summary.rows}")
    lines.append(f"Columns: {summary.cols}")
    lines.append(f"Duplicate rows: {summary.duplicates}")
    lines.append("")
    lines.append("Missing values per column:")
    any_missing = False
    for col, miss in summary.missing_by_col.items():
        if miss > 0:
            any_missing = True
            lines.append(f"- {col}: {miss}")
    if not any_missing:
        lines.append("- None")
    return "\n".join(lines)