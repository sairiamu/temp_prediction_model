# from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, root_mean_squared_error
# import joblib

# from load_data import load_feeds
# from features import build_features

# def get_feature_cols(df):
#     exclude = {"created_at", "entry_id", "target"}
#     return [c for c in df.columns if c not in exclude]

# def train():
#     df = load_feeds("../data/feeds.csv")
#     feat_df = build_features(df, target_col="temperature", n_lags=5)

#     feature_cols = get_feature_cols(feat_df)
#     X = feat_df[feature_cols]
#     y = feat_df["target"]

#     split_idx = int(len(feat_df) * 0.8)
#     X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
#     y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

#     # warm_start lets us grow the forest in chunks and measure progress
#     # after each chunk, instead of only seeing the final result.
#     model = RandomForestRegressor(
#         n_estimators=0,
#         max_depth=8,
#         random_state=42,
#         warm_start=True,
#     )

#     step = 20
#     max_estimators = 300

#     print(f"{'n_estimators':>12} | {'train_MAE':>10} | {'val_MAE':>10} | {'val_RMSE':>10}")
#     print("-" * 52)

#     for n in range(step, max_estimators + 1, step):
#         model.n_estimators = n
#         model.fit(X_train, y_train)

#         train_preds = model.predict(X_train)
#         val_preds = model.predict(X_test)

#         train_mae = mean_absolute_error(y_train, train_preds)
#         val_mae = mean_absolute_error(y_test, val_preds)
#         val_rmse = root_mean_squared_error(y_test, val_preds)

#         print(f"{n:>12} | {train_mae:>10.3f} | {val_mae:>10.3f} | {val_rmse:>10.3f}")

#     print("-" * 52)
#     print(f"Final -> MAE: {val_mae:.3f} | RMSE: {val_rmse:.3f}")

#     joblib.dump({"model": model, "features": feature_cols}, "../models/model.joblib")
#     return model, feature_cols

# if __name__ == "__main__":
#     train()



from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
import joblib
from pathlib import Path

from load_data import load_feeds
from features import build_features

# Dynamically resolve the path to the python-ml directory (parent of src)
BASE_DIR = Path(__file__).resolve().parent.parent
print(f"BASE_DIR resolved to: {BASE_DIR}")


def get_feature_cols(df):
    exclude = {"created_at", "entry_id", "target"}
    return [c for c in df.columns if c not in exclude]

def train():
    # Construct the absolute path to the data file
    data_path = BASE_DIR / "data" / "feeds.csv"
    df = load_feeds(data_path)
    
    feat_df = build_features(df, target_col="temperature", n_lags=5)

    feature_cols = get_feature_cols(feat_df)
    X = feat_df[feature_cols]
    y = feat_df["target"]

    split_idx = int(len(feat_df) * 0.8)
    
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    model = RandomForestRegressor(
        n_estimators=0,
        max_depth=8,
        random_state=42,
        warm_start=True,
    )

    step = 20
    max_estimators = 300

    print(f"{'n_estimators':>12} | {'train_MAE':>10} | {'val_MAE':>10} | {'val_RMSE':>10}")
    print("-" * 52)

    for n in range(step, max_estimators + 1, step):
        model.n_estimators = n
        model.fit(X_train, y_train)

        train_preds = model.predict(X_train)
        val_preds = model.predict(X_test)

        train_mae = mean_absolute_error(y_train, train_preds)
        val_mae = mean_absolute_error(y_test, val_preds)
        val_rmse = root_mean_squared_error(y_test, val_preds)

        print(f"{n:>12} | {train_mae:>10.3f} | {val_mae:>10.3f} | {val_rmse:>10.3f}")

    print("-" * 52)
    print(f"Final -> MAE: {val_mae:.3f} | RMSE: {val_rmse:.3f}")

    # Ensure the models directory exists, then save
    models_dir = BASE_DIR / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "features": feature_cols}, models_dir / "model.joblib")
    
    return model, feature_cols

if __name__ == "__main__":
    train()


