import numpy as np



def add_indicators(data):

    close = data["Close"].squeeze()
    volume = data["Volume"].squeeze()

    data["Return"] = close.pct_change()

    data["EMA_20"] = close.ewm(span=20).mean()
    data["EMA_50"] = close.ewm(span=50).mean()

    data["SMA_20"] = close.rolling(20).mean()
    data["SMA_50"] = close.rolling(50).mean()

    data["Price_vs_EMA20"] = close / data["EMA_20"] - 1
    data["Price_vs_EMA50"] = close / data["EMA_50"] - 1

    data["EMA_Trend"] = (
        data["EMA_20"] / data["EMA_50"]
    ) - 1

    data["Momentum_5"] = close.pct_change(5)
    data["Momentum_10"] = close.pct_change(10)
    data["Momentum_20"] = close.pct_change(20)

    data["Volatility_10"] = (
        data["Return"].rolling(10).std()
    )

    data["Volatility_20"] = (
        data["Return"].rolling(20).std()
    )

    data["Volume_Change"] = (
        volume.pct_change().clip(-10, 10)
    )

    data["Volume_Ratio"] = (
        volume / volume.rolling(20).mean()
    )

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    rs = (
        gain.rolling(14).mean() /
        loss.rolling(14).mean()
    )

    data["RSI_14"] = 100 - (100 / (1 + rs))

    data = data.replace([np.inf, -np.inf], np.nan)

    return data