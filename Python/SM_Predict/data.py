import yfinance as yf
import pandas as pd


def normalize_ticker(ticker: str) -> str:

    ticker = ticker.upper().strip()

    aliases = {
        "SP500": "SPY",
        "S&P500": "SPY",
        "S&P 500": "SPY",
        "^GSPC": "SPY",
        "NASDAQ": "QQQ",
        "^IXIC": "QQQ",
        "DOW": "DIA",
        "^DJI": "DIA",
    }

    return aliases.get(ticker, ticker)


def clean_yfinance_data(data: pd.DataFrame) -> pd.DataFrame:

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.loc[:, ~data.columns.duplicated()]

    return data.copy()


def download_stock_data(ticker: str):

    ticker = normalize_ticker(ticker)

    data = yf.download(
        ticker,
        period="10y",
        interval="1d",
        auto_adjust=True,
        progress=False,
        threads=True
    )

    data = clean_yfinance_data(data)

    return data