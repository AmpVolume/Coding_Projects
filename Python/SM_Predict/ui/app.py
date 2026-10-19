import tkinter as tk
from tkinter import ttk

from ui.styles import setup_styles
from ui.widgets import create_widgets
from ui.handlers import run_prediction


def run_app():

    root = tk.Tk()

    root.title("AI Stock Predictor")

    root.geometry("1000x700")
    root.minsize(850, 600)

    root.configure(bg="#0f172a")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    setup_styles(root)

    widgets = create_widgets(root)

    widgets["predict_button"].config(
        command=lambda: run_prediction(widgets)
    )

    root.mainloop()