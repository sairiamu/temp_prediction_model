from pathlib import Path
import joblib
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from .features import build_features
from .load_data import load_feeds


def evaluate(data_path: str | Path, model_path: str | Path) -> dict[str, float]:
    bundle = joblib.load(model_path)
    frame = build_features(load_feeds(data_path))
    split = int(len(frame) * 0.8)
    actual = frame.iloc[split:]["target"]
    predicted = bundle["model"].predict(frame.iloc[split:][bundle["features"]])
    return {"mae": float(mean_absolute_error(actual, predicted)), "rmse": float(root_mean_squared_error(actual, predicted))}
