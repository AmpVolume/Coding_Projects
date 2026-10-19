import threading
import time
from tkinter import messagebox

from model import (
    predict_stock_direction,
    backtest_strategy,
    normalize_ticker
)


def run_prediction(widgets):

    ticker = widgets["ticker_entry"].get().strip().upper()

    if not ticker:
        messagebox.showerror("Error", "Enter a ticker.")
        return

    try:
        cash = float(widgets["cash_entry"].get())
    except:
        messagebox.showerror("Error", "Invalid cash amount.")
        return

    widgets["status_label"].config(
        text="Running prediction..."
    )

    widgets["predict_button"].config(
        state="disabled"
    )

    threading.Thread(
        target=worker,
        args=(widgets, normalize_ticker(ticker), cash),
        daemon=True
    ).start()


def worker(widgets, ticker, cash):

    try:

        start = time.time()

        prediction = predict_stock_direction(ticker)

        backtest = backtest_strategy(
            ticker,
            cash
        )

        print("Prediction:", prediction)
        print("Backtest:", backtest)

        def update_ui():

            if not isinstance(prediction, dict):

                widgets["result_label"].config(
                    text="Prediction returned invalid data."
                )

                widgets["predict_button"].config(
                    state="normal"
                )

                return

            if "error" in prediction:

                widgets["result_label"].config(
                    text=prediction["error"]
                )

                widgets["predict_button"].config(
                    state="normal"
                )

                return

            widgets["price_label"].config(
                text=f"${float(prediction.get('latest_close', 0)):.2f}"
            )

            widgets["result_label"].config(
                text=(
                    f"Prediction: "
                    f"{prediction.get('prediction', 'N/A')}\n\n"
                    f"Confidence: "
                    f"{float(prediction.get('confidence', 0)):.2f}"
                )
            )

            if isinstance(backtest, dict):

                widgets["strategy_label"].config(
                    text=(
                        f"Strategy Return: "
                        f"{backtest.get('strategy_return_percent', 0)}%\n\n"
                        f"Win Rate: "
                        f"{backtest.get('win_rate', 0):.2f}\n\n"
                        f"Wins: {backtest.get('wins', 0)}\n"
                        f"Losses: {backtest.get('losses', 0)}\n"
                        f"Trades: {backtest.get('total_trades', 0)}"
                    )
                )

                widgets["trades_text"].config(
                    state="normal"
                )

                widgets["trades_text"].delete(
                    "1.0",
                    "end"
                )

                trades = backtest.get(
                    "last_10_trades",
                    []
                )

                if not isinstance(trades, list):
                    trades = []

                for trade in trades:

                    if not isinstance(trade, dict):
                        continue

                    widgets["trades_text"].insert(
                        "end",
                        (
                            f"{trade.get('date', 'N/A')} | "
                            f"{trade.get('action', 'N/A')} | "
                            f"${float(trade.get('price', 0)):.2f}\n"
                        )
                    )

                widgets["trades_text"].config(
                    state="disabled"
                )

            widgets["status_label"].config(
                text=f"Completed in "
                     f"{time.time()-start:.2f}s"
            )

            widgets["predict_button"].config(
                state="normal"
            )

        widgets["predict_button"].after(
            0,
            update_ui
        )

    except Exception as e:

        print("FULL ERROR:", e)

        widgets["predict_button"].after(
            0,
            lambda: messagebox.showerror(
                "Error",
                str(e)
            )
        )

        widgets["predict_button"].after(
            0,
            lambda: widgets["predict_button"].config(
                state="normal"
            )
        )