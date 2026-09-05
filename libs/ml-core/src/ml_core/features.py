import pandas as pd


def build_features(df: pd.DataFrame, target_col: str = "temperature", n_lags: int = 5) -> pd.DataFrame:
    out = df.copy()
    out["hour"] = out["created_at"].dt.hour
    out["minute"] = out["created_at"].dt.minute
    out["dow"] = out["created_at"].dt.dayofweek
    for col in ("temperature", "humidity"):
        for lag in range(1, n_lags + 1):
            out[f"{col}_lag{lag}"] = out[col].shift(lag)
    out["temp_roll_mean3"] = out["temperature"].rolling(3).mean()
    out["hum_roll_mean3"] = out["humidity"].rolling(3).mean()
    out["target"] = out[target_col].shift(-1)
    return out.dropna().reset_index(drop=True)
