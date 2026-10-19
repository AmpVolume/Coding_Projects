import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score

from forecasting import (
    FEATURES,
    CONFIDENCE_THRESHOLD,
    create_model
)

from indicators import add_indicators

from data import (
    download_stock_data,
    normalize_ticker
)


# -----------------------------
# DATA PREP
# -----------------------------

def prepare_model_data(ticker):

    ticker = normalize_ticker(ticker)

    data = download_stock_data(ticker)

    if data is None or len(data) == 0:
        return None, "No stock data found."

    data = add_indicators(data)

    # SAFETY: fix MultiIndex or weird yfinance formats
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.loc[:, ~data.columns.duplicated()].copy()

    close = data["Close"]

    # FIX: ensure Series (NOT DataFrame)
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    close = close.astype(float)

    # -----------------------------
    # LABEL CREATION (future prediction)
    # -----------------------------
    data["Future_Return"] = close.shift(-5) / close - 1
    data["Target"] = (data["Future_Return"] > 0.01).astype(int)

    # clean
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.dropna()

    if len(data) < 200:
        return None, "Not enough historical data."

    print("DATA RANGE:", data.index.min(), "->", data.index.max())

    return data, None


# -----------------------------
# PREDICTION
# -----------------------------

def predict_stock_direction(ticker):

    ticker = normalize_ticker(ticker)

    data, error = prepare_model_data(ticker)

    if error:
        return {
            "ticker": ticker,
            "error": error
        }

    X = data[FEATURES]
    y = data["Target"]

    split = int(len(data) * 0.8)

    model = create_model()
    model.fit(X.iloc[:split], y.iloc[:split])

    # -----------------------------
    # TEST ACCURACY
    # -----------------------------
    preds = model.predict(X.iloc[split:])
    accuracy = accuracy_score(y.iloc[split:], preds)

    # -----------------------------
    # LATEST PREDICTION
    # -----------------------------
    latest_features = X.iloc[[-1]]

    latest_prediction = int(model.predict(latest_features)[0])

    probs = model.predict_proba(latest_features)

    # FIX: handle weird shape safely
    if isinstance(probs, list):
        probs = np.array(probs)

    confidence = float(np.max(probs))

    # -----------------------------
    # FINAL SIGNAL
    # -----------------------------
    if confidence < CONFIDENCE_THRESHOLD:
        direction = "NO TRADE"
    else:
        direction = "UP" if latest_prediction == 1 else "DOWN"

    latest_close = float(data["Close"].iloc[-1])

    return {
        "ticker": ticker,
        "prediction": direction,
        "confidence": round(confidence, 4),
        "accuracy": round(float(accuracy), 4),
        "latest_close": round(latest_close, 2)
    }


# -----------------------------
# OPTIONAL BACKTEST WRAPPER
# -----------------------------

def backtest_strategy(ticker, starting_cash=10000):

    from strategy import backtest_strategy as run_backtest

    return run_backtest(ticker, starting_cash)