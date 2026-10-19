from model import prepare_model_data
from forecasting import FEATURES, CONFIDENCE_THRESHOLD, create_model

def backtest_strategy(ticker, starting_cash=10000):

    data, error = prepare_model_data(ticker)

    if error:
        return {"error": error}

    X = data[FEATURES]
    y = data["Target"]

    split = int(len(data) * 0.7)

    model = create_model()
    model.fit(X.iloc[:split], y.iloc[:split])

    cash = starting_cash
    shares = 0

    trades = []

    wins = 0
    losses = 0

    close = data["Close"]

    # FIX: force proper Series
    if hasattr(close, "iloc") and len(close.shape) > 1:
        close = close.iloc[:, 0]

    close = close.astype(float)

    for i in range(split, len(X) - 1):

        x_row = X.iloc[[i]]

        pred = model.predict(x_row)[0]

        prob = model.predict_proba(x_row)[0]
        confidence = float(max(prob))

        if confidence < CONFIDENCE_THRESHOLD:
            continue

        price = float(close.iloc[i])
        next_price = float(close.iloc[i + 1])
        date = str(data.index[i].date())

        if pred == 1:

            if cash > 0:

                shares = cash / price
                cash = 0

                trades.append({
                    "date": date,
                    "action": "BUY",
                    "price": float(price),
                    "confidence": float(confidence)
                })

        else:

            if shares > 0:

                cash = shares * price
                shares = 0

                trades.append({
                    "date": date,
                    "action": "SELL",
                    "price": float(price),
                    "confidence": float(confidence)
                })

        if (next_price > price) == (pred == 1):
            wins += 1
        else:
            losses += 1

    final_price = float(close.iloc[-1])

    final_value = cash + shares * final_price

    return {
        "starting_cash": starting_cash,
        "final_value": round(final_value, 2),
        "strategy_return_percent": round((final_value - starting_cash) / starting_cash * 100, 2),
        "win_rate": round(wins / (wins + losses) if (wins + losses) else 0, 4),
        "wins": wins,
        "losses": losses,
        "total_trades": len(trades),
        "last_10_trades": list(trades[-10:])   # 🔥 FORCE LIST SAFETY
    }