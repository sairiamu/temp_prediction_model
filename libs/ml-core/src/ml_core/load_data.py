from pathlib import Path
import pandas as pd


def load_feeds(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["created_at"])
    df = df.drop(columns=["latitude", "longitude", "elevation", "status"], errors="ignore")
    df = df.rename(columns={"field1": "temperature", "field2": "humidity"})
    return df.sort_values("created_at").dropna(subset=["temperature", "humidity"]).reset_index(drop=True)
