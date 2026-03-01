from __future__ import annotations
from pathlib import Path
import pandas as pd

def load_csv(path: Path) -> pd.DataFrame:
    """
    Load CSV as strings first (stable cleaning + consistent behavior).
    Empty strings are treated as missing later.
    """
    return pd.read_csv(path, dtype=str, keep_default_na=False)

def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)