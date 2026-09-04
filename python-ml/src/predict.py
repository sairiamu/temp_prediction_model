# import joblib
# from pathlib import Path
# from load_data import load_feeds
# from features import build_features

# def predict_next():
#     # Gets the directory where predict.py lives (the 'src' folder)
#     src_dir = Path(__file__).resolve().parent
    
#     # Builds absolute paths relative to the src folder
#     model_path = src_dir.parent / "models" / "model.joblib"
#     data_path = src_dir.parent / "data" / "feeds.csv"

#     bundle = joblib.load(model_path)
#     model, feature_cols = bundle["model"], bundle["features"]

#     df = load_feeds(data_path)
#     feat_df = build_features(df, target_col="temperature", n_lags=5)

#     latest = feat_df.iloc[[-1]][feature_cols]
#     prediction = model.predict(latest)[0]
#     print(f"Next predicted temperature: {prediction:.2f}")

# if __name__ == "__main__":
#     predict_next()


import joblib
import numpy as np
from pathlib import Path
from load_data import load_feeds
from features import build_features

def predict_next():
    src_dir = Path(__file__).resolve().parent
    model_path = src_dir.parent / "models" / "model.joblib"
    data_path = src_dir.parent / "data" / "feeds.csv"

    bundle = joblib.load(model_path)
    model, feature_cols = bundle["model"], bundle["features"]

    df = load_feeds(data_path)
    feat_df = build_features(df, target_col="temperature", n_lags=5)

    latest = feat_df.iloc[[-1]][feature_cols]
    
    # 1. Get the standard mean prediction
    prediction = model.predict(latest)[0]
    
    # 2. Calculate uncertainty/confidence using all trees in the forest
    # (Individual trees in scikit-learn expect 2D numpy arrays, so we use .values)
    tree_predictions = [tree.predict(latest.values)[0] for tree in model.estimators_]
    
    std_dev = np.std(tree_predictions)
    lower_bound = np.percentile(tree_predictions, 5)  # 90% interval lower limit
    upper_bound = np.percentile(tree_predictions, 95) # 90% interval upper limit

    # 3. Get overall feature importances to see what's driving the model
    importances = model.feature_importances_
    top_indices = np.argsort(importances)[-3:][::-1] # Top 3 features

    print("--- Prediction Results ---")
    print(f"Target variable:             Temperature")
    print(f"Predicted value:             {prediction:.2f}°")
    print(f"Model uncertainty (Std Dev): ±{std_dev:.2f}°")
    print(f"90% Confidence Interval:     [{lower_bound:.2f}°, {upper_bound:.2f}°]")
    
    print("\n--- Most Important Features ---")
    for idx in top_indices:
        print(f"* {feature_cols[idx]:<15}: {importances[idx]:.3f} (importance weight)")

if __name__ == "__main__":
    predict_next()




