from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from .features import build_features
from .load_data import load_feeds


def train(data_path: str | Path, model_path: str | Path, n_estimators: int = 100) -> None:
    frame = build_features(load_feeds(data_path))
    feature_cols = [column for column in frame.columns if column not in {"created_at", "entry_id", "target"}]
    split = int(len(frame) * 0.8)
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=8, random_state=42)
    model.fit(frame.iloc[:split][feature_cols], frame.iloc[:split]["target"])
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "features": feature_cols}, model_path)
