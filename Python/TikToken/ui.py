# ui.py

import tkinter as tk
from tkinter import messagebox
import Example
import reduce


def run_tokenizer():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Error", "Enter some text")
        return

    tokens = Example.tokenize(text)
    num = Example.count_tokens(tokens)
    decoded = Example.decode_tokens(tokens)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"Tokens ID: {tokens}\n")
    output_box.insert(tk.END, f"Tokens Count: {num}\n")
    output_box.insert(tk.END, f"Decoded: {decoded}\n\n")

    # Analyze
    token_count, suggestions = reduce.analyze_text(text)

    output_box.insert(tk.END, "Suggestions:\n")
    for s in suggestions:
        output_box.insert(tk.END, f"- {s}\n")


def run_compression():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Error", "Enter some text")
        return

    compressed = reduce.compress_text(text)

    input_box.delete("1.0", tk.END)
    input_box.insert(tk.END, compressed)


# UI
root = tk.Tk()
root.title("AI Token Optimizer")
root.geometry("650x550")

tk.Label(root, text="Input").pack()

input_box = tk.Text(root, height=6)
input_box.pack(fill=tk.BOTH, padx=10)

tk.Button(root, text="Analyze + Tokenize", command=run_tokenizer).pack(pady=5)
tk.Button(root, text="Auto Compress", command=run_compression).pack(pady=5)

tk.Label(root, text="Output").pack()

output_box = tk.Text(root, height=12)
output_box.pack(fill=tk.BOTH, padx=10)

root.mainloop()