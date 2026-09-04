import pandas as pd

# -> pd.DataFrame
def load_feeds(path: str):
    df = pd.read_csv(path, parse_dates=["created_at"])
    df = df.drop(columns=["latitude", "longitude", "elevation", "status"])
    df = df.rename(columns={"field1": "temperature", "field2": "humidity"})
    df = df.sort_values("created_at").reset_index(drop=True)
    df = df.dropna(subset=["temperature", "humidity"])
    # return df
    # print(f"Loaded {len(df)} rows from {path}")
    return df