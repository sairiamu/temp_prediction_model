from pathlib import Path
import joblib
import numpy as np
from .features import build_features
from .load_data import load_feeds


def predict_horizon(data_path: str | Path, model_path: str | Path, horizon: int = 1) -> list[float]:
    bundle = joblib.load(model_path)
    model, feature_cols = bundle["model"], bundle["features"]
    frame = build_features(load_feeds(data_path))
    current = frame.iloc[[-1]][feature_cols]
    predictions: list[float] = []
    for _ in range(horizon):
        predictions.append(float(model.predict(current)[0]))
    return predictions


def prediction_interval(model, features) -> tuple[float, float]:
    values = np.asarray([tree.predict(features)[0] for tree in model.estimators_])
    return float(np.percentile(values, 5)), float(np.percentile(values, 95))
