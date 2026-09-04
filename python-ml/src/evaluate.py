import matplotlib.pyplot as plt
import joblib
from load_data import load_feeds
from features import build_features

def evaluate():
    bundle = joblib.load("../models/model.joblib")
    model, feature_cols = bundle["model"], bundle["features"]

    df = load_feeds("../data/feeds.csv")
    feat_df = build_features(df, target_col="temperature", n_lags=5)

    split_idx = int(len(feat_df) * 0.8)
    test_df = feat_df.iloc[split_idx:]

    preds = model.predict(test_df[feature_cols])

    plt.figure(figsize=(10, 4))
    plt.plot(test_df["created_at"], test_df["target"], label="actual")
    plt.plot(test_df["created_at"], preds, label="predicted")
    plt.legend()
    plt.title("Temperature: actual vs predicted")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    evaluate()