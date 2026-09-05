import numpy as np
from sklearn.ensemble import IsolationForest


def residual_anomalies(actual: np.ndarray, predicted: np.ndarray, threshold: float) -> np.ndarray:
    return np.abs(np.asarray(actual) - np.asarray(predicted)) > threshold


def fit_isolation_detector(values: np.ndarray) -> IsolationForest:
    detector = IsolationForest(random_state=42, contamination="auto")
    detector.fit(np.asarray(values).reshape(-1, 1))
    return detector
