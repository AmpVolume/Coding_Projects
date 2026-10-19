import re
import requests
from bs4 import BeautifulSoup

URL = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

def print_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Pull all visible text pieces from the Google Doc
    tokens = [
        t.strip()
        for t in soup.stripped_strings
        if t.strip()
    ]

    # Keep only x numbers, block characters, and y numbers
    data = []
    for token in tokens:
        if token.isdigit() or token in {"█", "░", "▀"}:
            data.append(token)

    points = []

    for i in range(0, len(data) - 2, 3):
        try:
            x = int(data[i])
            char = data[i + 1]
            y = int(data[i + 2])

            if char in {"█", "░", "▀"}:
                points.append((x, y, char))
        except ValueError:
            continue

    if not points:
        print("No valid points found.")
        print("Debug tokens:", tokens[:50])
        return

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = " " if char == "░" else char

    print("\nDecoded Message:\n")

    for y in range(max_y, -1, -1):
        row = "".join(grid[y])
        row = row.replace("░", " ")
        print(row.rstrip())


if __name__ == "__main__":
    print_secret_message(URL)