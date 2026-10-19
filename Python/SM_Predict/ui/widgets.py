import tkinter as tk
from tkinter import ttk


def create_widgets(root):

    main_frame = ttk.Frame(root)
    main_frame.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=20,
        pady=20
    )

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(3, weight=1)

    title_label = ttk.Label(
        main_frame,
        text="AI Stock Predictor",
        style="Header.TLabel"
    )

    title_label.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=(0, 20)
    )

    input_frame = ttk.Frame(main_frame)

    input_frame.grid(
        row=1,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(0, 20)
    )

    input_frame.columnconfigure(0, weight=1)
    input_frame.columnconfigure(1, weight=1)

    ticker_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 14),
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    ticker_entry.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=5
    )

    ticker_entry.insert(0, "AAPL")

    cash_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 14),
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    cash_entry.grid(
        row=0,
        column=1,
        sticky="ew",
        padx=5
    )

    cash_entry.insert(0, "1000")

    predict_button = ttk.Button(
        main_frame,
        text="Run Prediction",
        style="Run.TButton"
    )

    predict_button.grid(
        row=2,
        column=0,
        columnspan=2,
        pady=(0, 20)
    )

    left_frame = ttk.Frame(
        main_frame,
        style="Card.TFrame"
    )

    left_frame.grid(
        row=3,
        column=0,
        sticky="nsew",
        padx=(0, 10)
    )

    right_frame = ttk.Frame(
        main_frame,
        style="Card.TFrame"
    )

    right_frame.grid(
        row=3,
        column=1,
        sticky="nsew"
    )

    price_label = ttk.Label(
        left_frame,
        text="$---",
        font=("Segoe UI", 32, "bold"),
        foreground="#22c55e"
    )

    price_label.pack(pady=20)

    result_label = ttk.Label(
        left_frame,
        text="Prediction",
        justify="left"
    )

    result_label.pack(anchor="w", padx=20, pady=10)

    strategy_label = ttk.Label(
        left_frame,
        text="Strategy",
        justify="left"
    )

    strategy_label.pack(anchor="w", padx=20, pady=10)

    trades_title = ttk.Label(
        right_frame,
        text="Recent Trades",
        font=("Segoe UI", 14, "bold")
    )

    trades_title.pack(pady=10)

    trades_text = tk.Text(
        right_frame,
        bg="#020617",
        fg="#e2e8f0",
        font=("Consolas", 11),
        relief="flat",
        wrap="none",
        height=20
    )

    trades_text.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    status_label = ttk.Label(
        main_frame,
        text="Ready.",
        foreground="#94a3b8"
    )

    status_label.grid(
        row=4,
        column=0,
        columnspan=2,
        pady=(15, 0)
    )

    return {
        "ticker_entry": ticker_entry,
        "cash_entry": cash_entry,
        "predict_button": predict_button,
        "price_label": price_label,
        "result_label": result_label,
        "strategy_label": strategy_label,
        "trades_text": trades_text,
        "status_label": status_label,
    }