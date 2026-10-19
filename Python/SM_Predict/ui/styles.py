from tkinter import ttk



def setup_styles(root):

    root.configure(bg="#0f172a")

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "TFrame",
        background="#0f172a"
    )

    style.configure(
        "TLabel",
        background="#0f172a",
        foreground="white",
        font=("Segoe UI", 11)
    )

    style.configure(
        "Header.TLabel",
        font=("Segoe UI", 22, "bold"),
        foreground="#38bdf8"
    )

    style.configure(
        "Card.TFrame",
        background="#1e293b"
    )