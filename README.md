# 🌡️ Temperature Prediction Model

A simple machine learning project for predicting the **next temperature reading** from historical temperature and humidity sensor data.

The project uses a **Random Forest Regressor** with time-based, lag, and rolling statistical features. It is designed as a practical introduction to applying machine learning to real-world sensor/time-series data.

## 🚀 Overview

The model learns patterns from historical environmental measurements and predicts the next temperature value.

The pipeline is:

```text
Sensor Data
    ↓
CSV Dataset
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Random Forest Regression
    ↓
Model Evaluation
    ↓
Next Temperature Prediction
```

The project uses temperature and humidity readings as the primary signals and creates additional features from previous observations and timestamps.

## ✨ Features

* 📊 Loads temperature and humidity data from CSV
* 🧹 Cleans and sorts sensor data chronologically
* 🕐 Extracts time-based features
* 🔄 Creates lag features from previous readings
* 📈 Calculates rolling averages
* 🌲 Trains a Random Forest regression model
* 📉 Evaluates predictions using MAE and RMSE
* 💾 Saves the trained model using Joblib
* 🔮 Predicts the next temperature reading
* 📐 Estimates prediction uncertainty from the Random Forest trees
* 🧠 Displays the most important model features
* 📊 Visualizes actual vs. predicted temperature

## 🧠 Machine Learning Approach

This project treats temperature prediction as a **regression problem**.

The model predicts:

```text
Next Temperature
```

using information such as:

```text
Current Temperature
Current Humidity
Previous Temperature Readings
Previous Humidity Readings
Hour
Minute
Day of Week
Rolling Temperature Average
Rolling Humidity Average
```

### Model

The main model is:

**Random Forest Regressor**

Configuration currently used:

```text
n_estimators = 300
max_depth = 8
random_state = 42
```

The training process grows the forest incrementally using `warm_start`, allowing the validation performance to be observed as more trees are added.

## 🔧 Feature Engineering

The feature engineering pipeline creates several types of features.

### Time Features

From the timestamp:

* `hour`
* `minute`
* `dow` — day of week

### Lag Features

The model uses the previous five readings for both temperature and humidity:

```text
temperature_lag1
temperature_lag2
temperature_lag3
temperature_lag4
temperature_lag5

humidity_lag1
humidity_lag2
humidity_lag3
humidity_lag4
humidity_lag5
```

### Rolling Features

Three-reading rolling averages are calculated for:

```text
temp_roll_mean3
hum_roll_mean3
```

### Prediction Target

The target is the **next temperature reading**:

```text
target = temperature.shift(-1)
```

This effectively turns the historical sensor data into a one-step-ahead forecasting problem.

## 📁 Project Structure

```text
temp_prediction_model/
│
├── python-ml/
│   │
│   ├── data/
│   │   └── feeds.csv
│   │
│   ├── models/
│   │   └── model.joblib
│   │
│   ├── src/
│   │   ├── evaluate.py
│   │   ├── features.py
│   │   ├── load_data.py
│   │   ├── predict.py
│   │   └── train.py
│   │
│   ├── notebook.ipynb
│   └── requirements.txt
│
└── .gitignore
```

The repository currently keeps the machine-learning implementation inside the `python-ml` directory.

## 🛠️ Technologies

* **Python**
* **Pandas** — data loading and manipulation
* **NumPy** — numerical operations
* **Scikit-learn** — machine learning
* **Matplotlib** — visualization
* **Joblib** — model serialization

The project pins these dependencies in `requirements.txt`.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sairiamu/temp_prediction_model.git
cd temp_prediction_model/python-ml
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🏋️ Train the Model

From the `python-ml` directory:

```bash
python src/train.py
```

The training script:

1. Loads `data/feeds.csv`
2. Cleans and sorts the measurements
3. Creates time, lag, and rolling features
4. Splits the data chronologically
5. Trains the Random Forest
6. Calculates MAE and RMSE
7. Saves the trained model to:

```text
models/model.joblib
```

The project uses an **80/20 chronological split**, with the first 80% used for training and the remaining 20% used for validation/testing.

## 🔮 Make a Prediction

After training:

```bash
python src/predict.py
```

The prediction script loads the saved model and latest available sensor data, then predicts the next temperature reading.

Example output:

```text
--- Prediction Results ---
Target variable: Temperature
Predicted value: 27.43°
Model uncertainty (Std Dev): ±0.31°
90% Confidence Interval: [26.98°, 27.91°]

--- Most Important Features ---
* temperature_lag1 : 0.XXX
* humidity_lag1    : 0.XXX
* temp_roll_mean3  : 0.XXX
```

The uncertainty estimate is derived from the predictions of the individual trees in the Random Forest rather than from a separate probabilistic model.

## 📊 Evaluate the Model

Run:

```bash
python src/evaluate.py
```

The evaluation script compares actual and predicted temperatures and displays them as a plot.

```text
Actual Temperature
        vs
Predicted Temperature
```

It also helps visually determine how closely the model follows the actual temperature measurements.

## 📡 Data Format

The project expects sensor data containing timestamp, temperature, and humidity information.

The existing loader maps:

```text
field1 → temperature
field2 → humidity
```

and uses:

```text
created_at
```

as the timestamp.

Other metadata columns such as latitude, longitude, elevation, and status are removed during preprocessing.

A simplified input looks like:

```csv
created_at,field1,field2
2026-01-01 10:00:00,25.4,68.2
2026-01-01 10:01:00,25.5,68.0
2026-01-01 10:02:00,25.7,67.8
```

## 🔬 How It Works

Suppose the latest sensor readings are:

```text
Temperature = 26.5°C
Humidity    = 64%
```

The system also looks at previous readings:

```text
T-1
T-2
T-3
T-4
T-5
```

and corresponding humidity readings.

These values, together with the time information and rolling averages, become the model's input features.

The Random Forest then estimates:

```text
Next Temperature = f(
    current conditions,
    previous temperature,
    previous humidity,
    time patterns
)
```

## 📌 Current Scope

This is intentionally a **simple machine-learning project**, not a production weather forecasting system.

It focuses on demonstrating the fundamental workflow:

```text
Data → Features → Model → Evaluation → Prediction
```

It is particularly useful for experimenting with:

* IoT sensor data
* Environmental monitoring
* Time-series feature engineering
* Regression
* Random Forest models
* ML model persistence
* Prediction uncertainty

## 🔮 Possible Improvements

Future versions could add:

* [ ] More weather variables
* [ ] Longer historical windows
* [ ] Better time-series validation
* [ ] Hyperparameter tuning
* [ ] Linear Regression baseline
* [ ] XGBoost / LightGBM comparison
* [ ] LSTM-based forecasting
* [ ] Prediction API
* [ ] Web dashboard
* [ ] Real-time IoT data ingestion
* [ ] Automated model retraining
* [ ] Docker deployment
* [ ] Model monitoring
* [ ] Cloud deployment

A particularly useful next step would be connecting the model directly to an IoT data source so that new sensor readings can automatically trigger predictions.

## 🎯 Learning Objectives

This project demonstrates several fundamental ML concepts:

```text
Supervised Learning
       ↓
Regression
       ↓
Time-Series Data
       ↓
Feature Engineering
       ↓
Random Forest
       ↓
Model Evaluation
       ↓
Inference
```

It is therefore a small but complete example of an end-to-end machine-learning workflow.

## 📄 License

MIT

## 👨‍💻 Author

**sairiamu**

GitHub:

https://github.com/sairiamu

---

⭐ If this project is useful, consider giving the repository a star.
