from xgboost import XGBClassifier


FEATURES = [
    "Return",
    "EMA_20",
    "EMA_50",
    "SMA_20",
    "SMA_50",
    "Price_vs_EMA20",
    "Price_vs_EMA50",
    "EMA_Trend",
    "Momentum_5",
    "Momentum_10",
    "Momentum_20",
    "Volatility_10",
    "Volatility_20",
    "Volume_Change",
    "Volume_Ratio",
    "RSI_14",
]


CONFIDENCE_THRESHOLD = 0.55



def create_model():

    return XGBClassifier(
        n_estimators=150,
        max_depth=4,
        learning_rate=0.07,
        subsample=0.8,
        colsample_bytree=0.8,
        tree_method="hist",
        n_jobs=-1,
        eval_metric="logloss"
    )