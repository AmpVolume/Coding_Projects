import sys
import sqlite3
import hashlib
import math
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QDoubleSpinBox, QTableWidget,
    QTableWidgetItem, QMessageBox, QFrame, QHeaderView, QTabWidget,
    QFormLayout, QComboBox, QSplitter
)

# ============================================================
# NORTHSTAR STOCK PLATFORM
# Single-file desktop paper-trading application
# ============================================================

APP_NAME = "Northstar Trading"
DB_PATH = Path(__file__).with_name("paper_trading.db")

BG = "#0b1220"
PANEL = "#121c2e"
PANEL2 = "#172338"
TEXT = "#e8eef8"
MUTED = "#9aabc2"
GREEN = "#34d399"
RED = "#fb7185"
BLUE = "#60a5fa"

INITIAL_CASH = 100_000.00

# Illustrative prices only. These are NOT live market quotes.
DEMO_PRICES = {
    "AAPL": 227.50,
    "MSFT": 512.20,
    "NVDA": 181.40,
    "TSLA": 438.10,
    "SPY": 665.30,
    "AMZN": 228.50,
    "GOOGL": 245.00,
    "META": 715.00,
    "AMD": 165.00,
    "NFLX": 1_150.00,
}


# ============================================================
# DATABASE
# ============================================================

class TradingDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS account (
                id INTEGER PRIMARY KEY CHECK(id = 1),
                cash REAL NOT NULL
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS positions (
                symbol TEXT PRIMARY KEY,
                quantity REAL NOT NULL,
                avg_cost REAL NOT NULL
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                side TEXT NOT NULL,
                symbol TEXT NOT NULL,
                quantity REAL NOT NULL,
                price REAL NOT NULL,
                total REAL NOT NULL
            )
        """)

        self.conn.execute(
            "INSERT OR IGNORE INTO account(id, cash) VALUES(1, ?)",
            (INITIAL_CASH,)
        )
        self.conn.commit()

    def cash(self):
        row = self.conn.execute(
            "SELECT cash FROM account WHERE id = 1"
        ).fetchone()
        return float(row["cash"])

    def positions(self):
        return [
            dict(row) for row in self.conn.execute(
                "SELECT * FROM positions ORDER BY symbol"
            ).fetchall()
        ]

    def orders(self):
        return [
            dict(row) for row in self.conn.execute(
                "SELECT * FROM orders ORDER BY id DESC LIMIT 500"
            ).fetchall()
        ]

    def buy(self, symbol, quantity, price):
        symbol = symbol.upper().strip()
        quantity = float(quantity)
        price = float(price)

        if not symbol or quantity <= 0 or price <= 0:
            raise ValueError("Enter a valid ticker, quantity, and price.")

        total = round(quantity * price, 2)

        if total > self.cash():
            raise ValueError(
                f"Insufficient cash. Available: ${self.cash():,.2f}"
            )

        row = self.conn.execute(
            "SELECT quantity, avg_cost FROM positions WHERE symbol = ?",
            (symbol,)
        ).fetchone()

        held = float(row["quantity"]) if row else 0.0
        old_average = float(row["avg_cost"]) if row else 0.0

        new_quantity = held + quantity
        new_average = (
            held * old_average + quantity * price
        ) / new_quantity

        try:
            self.conn.execute(
                "UPDATE account SET cash = cash - ? WHERE id = 1",
                (total,)
            )

            self.conn.execute("""
                INSERT INTO positions(symbol, quantity, avg_cost)
                VALUES (?, ?, ?)
                ON CONFLICT(symbol) DO UPDATE SET
                    quantity = excluded.quantity,
                    avg_cost = excluded.avg_cost
            """, (symbol, new_quantity, new_average))

            self.record_order("BUY", symbol, quantity, price, total)
            self.conn.commit()

        except Exception:
            self.conn.rollback()
            raise

    def sell(self, symbol, quantity, price):
        symbol = symbol.upper().strip()
        quantity = float(quantity)
        price = float(price)

        if not symbol or quantity <= 0 or price <= 0:
            raise ValueError("Enter a valid ticker, quantity, and price.")

        row = self.conn.execute(
            "SELECT quantity FROM positions WHERE symbol = ?",
            (symbol,)
        ).fetchone()

        held = float(row["quantity"]) if row else 0.0

        if quantity > held + 1e-9:
            raise ValueError(
                f"You own {held:g} shares of {symbol}. "
                "Short selling is not enabled."
            )

        total = round(quantity * price, 2)
        remaining = held - quantity

        try:
            self.conn.execute(
                "UPDATE account SET cash = cash + ? WHERE id = 1",
                (total,)
            )

            if remaining <= 1e-9:
                self.conn.execute(
                    "DELETE FROM positions WHERE symbol = ?",
                    (symbol,)
                )
            else:
                self.conn.execute(
                    "UPDATE positions SET quantity = ? WHERE symbol = ?",
                    (remaining, symbol)
                )

            self.record_order("SELL", symbol, quantity, price, total)
            self.conn.commit()

        except Exception:
            self.conn.rollback()
            raise

    def record_order(self, side, symbol, quantity, price, total):
        self.conn.execute("""
            INSERT INTO orders(timestamp, side, symbol, quantity, price, total)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            side, symbol, quantity, price, total
        ))

    def reset(self):
        try:
            self.conn.execute(
                "UPDATE account SET cash = ? WHERE id = 1",
                (INITIAL_CASH,)
            )
            self.conn.execute("DELETE FROM positions")
            self.conn.execute("DELETE FROM orders")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    def close(self):
        self.conn.close()


# ============================================================
# DEMO MARKET DATA
# Replace this class with a real market-data API when ready.
# ============================================================

class MarketData:
    def quote(self, symbol):
        symbol = symbol.strip().upper()

        if not symbol:
            raise ValueError("Enter a stock ticker.")

        if not symbol.replace(".", "").isalnum():
            raise ValueError("Invalid stock ticker.")

        if symbol in DEMO_PRICES:
            price = DEMO_PRICES[symbol]
        else:
            seed = int(
                hashlib.sha256(symbol.encode()).hexdigest()[:8], 16
            )
            price = 20 + (seed % 48000) / 100

        return round(price, 2)

    def history(self, symbol, count=60):
        base = self.quote(symbol)
        seed = int(
            hashlib.sha256(symbol.encode()).hexdigest()[:8], 16
        )

        values = []

        for i in range(count):
            wave = math.sin((i + seed % 13) / 5.5) * 0.018
            drift = (i / max(count - 1, 1) - 0.5) * 0.025
            values.append(round(base * (1 + wave + drift), 2))

        values[-1] = base
        return values


# ============================================================
# REUSABLE UI COMPONENTS
# ============================================================

def money(value):
    return f"${value:,.2f}"


def styled_button(label, color=BLUE):
    button = QPushButton(label)
    button.setCursor(Qt.CursorShape.PointingHandCursor)
    button.setStyleSheet(f"""
        QPushButton {{
            background-color: {color};
            color: #08111e;
            border: none;
            border-radius: 7px;
            padding: 10px 16px;
            font-weight: bold;
        }}
        QPushButton:hover {{ background-color: #93c5fd; }}
        QPushButton:disabled {{ background-color: #526174; }}
    """)
    return button


def make_table(headers):
    table = QTableWidget()
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch
    )
    table.setEditTriggers(
        QTableWidget.EditTrigger.NoEditTriggers
    )
    table.setSelectionBehavior(
        QTableWidget.SelectionBehavior.SelectRows
    )
    table.setAlternatingRowColors(False)
    table.verticalHeader().setVisible(False)
    table.setStyleSheet(f"""
        QTableWidget {{
            background: {PANEL};
            color: {TEXT};
            gridline-color: #26344a;
            border: 1px solid #26344a;
            border-radius: 8px;
        }}
        QHeaderView::section {{
            background: {PANEL2};
            color: {MUTED};
            padding: 9px;
            border: none;
            font-weight: bold;
        }}
        QTableWidget::item {{ padding: 6px; }}
        QTableWidget::item:selected {{ background: #243c5b; }}
    """)
    return table


class StatCard(QFrame):
    def __init__(self, title, value="$0.00"):
        super().__init__()
        self.setStyleSheet(
            f"QFrame {{ background: {PANEL}; border-radius: 10px; }}"
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)

        heading = QLabel(title.upper())
        heading.setStyleSheet(f"color: {MUTED}; font-size: 11px;")

        self.value_label = QLabel(value)
        self.value_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.value_label.setStyleSheet(f"color: {TEXT};")

        layout.addWidget(heading)
        layout.addWidget(self.value_label)

    def set_value(self, value, color=TEXT):
        self.value_label.setText(value)
        self.value_label.setStyleSheet(
            f"color: {color}; font-size: 18px; font-weight: bold;"
        )


class PriceChart(QWidget):
    def __init__(self):
        super().__init__()
        self.values = []
        self.setMinimumHeight(250)

    def set_values(self, values):
        self.values = values
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QColor(PANEL))

        if len(self.values) < 2:
            painter.setPen(QColor(MUTED))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter,
                             "Price chart")
            return

        left, right, top, bottom = 20, self.width() - 20, 20, self.height() - 30
        low = min(self.values)
        high = max(self.values)

        if high == low:
            high += 1
            low -= 1

        painter.setPen(QPen(QColor("#26344a"), 1))

        for i in range(5):
            y = top + (bottom - top) * i / 4
            painter.drawLine(int(left), int(y), int(right), int(y))

        points = []

        for i, value in enumerate(self.values):
            x = left + (right - left) * i / (len(self.values) - 1)
            y = bottom - (value - low) / (high - low) * (bottom - top)
            points.append(QPointF(x, y))

        line_color = GREEN if self.values[-1] >= self.values[0] else RED
        painter.setPen(QPen(QColor(line_color), 2))

        for i in range(len(points) - 1):
            painter.drawLine(points[i], points[i + 1])

        painter.setPen(QColor(MUTED))
        painter.drawText(left, self.height() - 7, money(low))
        painter.drawText(right - 70, self.height() - 7, money(high))


# ============================================================
# MAIN APPLICATION
# ============================================================

class StockApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = TradingDatabase()
        self.market = MarketData()
        self.current_symbol = "AAPL"

        self.setWindowTitle(APP_NAME + " — Paper Trading")
        self.resize(1250, 800)
        self.setMinimumSize(950, 650)

        self.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background: {BG};
                color: {TEXT};
                font-family: Arial;
                font-size: 13px;
            }}
            QLineEdit, QComboBox, QDoubleSpinBox {{
                background: {PANEL2};
                color: {TEXT};
                border: 1px solid #34445d;
                border-radius: 6px;
                padding: 8px;
            }}
            QTabWidget::pane {{
                border: 1px solid #26344a;
                border-radius: 8px;
            }}
            QTabBar::tab {{
                background: {PANEL};
                color: {MUTED};
                padding: 12px 22px;
                margin-right: 3px;
            }}
            QTabBar::tab:selected {{
                background: {PANEL2};
                color: {TEXT};
                border-bottom: 2px solid {BLUE};
            }}
            QScrollBar:vertical {{
                background: {BG};
                width: 10px;
            }}
        """)

        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)
        layout.setContentsMargins(22, 18, 22, 18)
        layout.setSpacing(16)

        header = QHBoxLayout()

        title_box = QVBoxLayout()
        title = QLabel("NORTHSTAR")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {BLUE};")

        subtitle = QLabel("STOCK MARKET PAPER TRADING")
        subtitle.setStyleSheet(f"color: {MUTED}; font-size: 11px;")

        title_box.addWidget(title)
        title_box.addWidget(subtitle)
        header.addLayout(title_box)
        header.addStretch()

        demo_label = QLabel("● DEMO MODE — NOT LIVE")
        demo_label.setStyleSheet(f"color: {GREEN}; font-weight: bold;")
        header.addWidget(demo_label)

        reset_button = styled_button("Reset Account", "#fbbf24")
        reset_button.clicked.connect(self.reset_account)
        header.addWidget(reset_button)
        layout.addLayout(header)

        stats = QHBoxLayout()
        self.cash_card = StatCard("Available Cash")
        self.equity_card = StatCard("Account Equity")
        self.pnl_card = StatCard("Open Profit / Loss")
        self.return_card = StatCard("Total Return")

        for card in (
            self.cash_card, self.equity_card,
            self.pnl_card, self.return_card
        ):
            stats.addWidget(card)

        layout.addLayout(stats)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        self.build_trading_tab()
        self.build_portfolio_tab()
        self.build_history_tab()

        self.load_symbol("AAPL")
        self.refresh_all()

        self.statusBar().showMessage(
            "Paper trading only. Prices are illustrative, not live quotes."
        )

    # --------------------------------------------------------
    # Trading tab
    # --------------------------------------------------------

    def build_trading_tab(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(14, 14, 14, 14)

        search_row = QHBoxLayout()

        self.symbol_input = QLineEdit("AAPL")
        self.symbol_input.setPlaceholderText("Enter ticker, e.g. AAPL")
        self.symbol_input.returnPressed.connect(self.search_symbol)

        search_button = styled_button("Search Stock")
        search_button.clicked.connect(self.search_symbol)

        search_row.addWidget(self.symbol_input, 1)
        search_row.addWidget(search_button)
        layout.addLayout(search_row)

        self.tabs.addTab(page, "Trading")

        splitter = QSplitter(Qt.Orientation.Horizontal)

        chart_panel = QWidget()
        chart_layout = QVBoxLayout(chart_panel)
        chart_layout.setContentsMargins(0, 8, 12, 0)

        self.stock_title = QLabel("AAPL")
        self.stock_title.setFont(QFont("Arial", 22, QFont.Weight.Bold))

        self.stock_price = QLabel("$227.50")
        self.stock_price.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.stock_price.setStyleSheet(f"color: {GREEN};")

        warning = QLabel("Illustrative demo price — not a live quote")
        warning.setStyleSheet(f"color: {MUTED};")

        chart_layout.addWidget(self.stock_title)
        chart_layout.addWidget(self.stock_price)
        chart_layout.addWidget(warning)

        self.chart = PriceChart()
        chart_layout.addWidget(self.chart, 1)

        watch_title = QLabel("WATCHLIST")
        watch_title.setStyleSheet(f"color: {MUTED}; font-weight: bold;")
        chart_layout.addWidget(watch_title)

        self.watch_table = make_table(["Ticker", "Demo Price"])
        self.watch_table.setMaximumHeight(180)
        self.watch_table.cellDoubleClicked.connect(self.open_watch_symbol)
        chart_layout.addWidget(self.watch_table)

        trade_panel = QFrame()
        trade_panel.setMinimumWidth(250)
        trade_panel.setMaximumWidth(310)
        trade_panel.setStyleSheet(
            f"QFrame {{ background: {PANEL}; border-radius: 10px; }}"
        )

        trade_layout = QVBoxLayout(trade_panel)
        trade_layout.setContentsMargins(18, 18, 18, 18)

        trade_title = QLabel("PLACE PAPER TRADE")
        trade_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        trade_layout.addWidget(trade_title)

        form = QFormLayout()

        self.trade_symbol = QLabel("AAPL")
        self.trade_symbol.setStyleSheet(f"color: {BLUE}; font-weight: bold;")

        self.quantity_input = QDoubleSpinBox()
        self.quantity_input.setRange(0.01, 1_000_000)
        self.quantity_input.setDecimals(4)
        self.quantity_input.setSingleStep(1)
        self.quantity_input.setValue(1)

        self.order_type = QComboBox()
        self.order_type.addItems(["Market (simulated)"])

        self.estimated_total = QLabel("$227.50")
        self.estimated_total.setStyleSheet(
            f"color: {TEXT}; font-weight: bold;"
        )

        form.addRow("Ticker:", self.trade_symbol)
        form.addRow("Order type:", self.order_type)
        form.addRow("Shares:", self.quantity_input)
        form.addRow("Estimated total:", self.estimated_total)

        trade_layout.addLayout(form)

        self.quantity_input.valueChanged.connect(self.update_estimate)

        buy_button = styled_button("BUY / GO LONG", GREEN)
        sell_button = styled_button("SELL SHARES", RED)

        buy_button.clicked.connect(lambda: self.place_order("BUY"))
        sell_button.clicked.connect(lambda: self.place_order("SELL"))

        trade_layout.addSpacing(12)
        trade_layout.addWidget(buy_button)
        trade_layout.addWidget(sell_button)

        note = QLabel(
            "Buying uses demo cash. Selling is limited to shares you own. "
            "Short selling and leverage are disabled."
        )
        note.setWordWrap(True)
        note.setStyleSheet(f"color: {MUTED}; font-size: 11px;")
        trade_layout.addSpacing(12)
        trade_layout.addWidget(note)
        trade_layout.addStretch()

        splitter.addWidget(chart_panel)
        splitter.addWidget(trade_panel)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)

        layout.addWidget(splitter, 1)

    def search_symbol(self):
        symbol = self.symbol_input.text().strip().upper()

        try:
            self.market.quote(symbol)
            self.load_symbol(symbol)
        except ValueError as error:
            QMessageBox.warning(self, "Invalid Ticker", str(error))

    def load_symbol(self, symbol):
        symbol = symbol.upper().strip()

        try:
            price = self.market.quote(symbol)
            history = self.market.history(symbol)

            self.current_symbol = symbol
            self.stock_title.setText(symbol)
            self.stock_price.setText(money(price))
            self.trade_symbol.setText(symbol)
            self.symbol_input.setText(symbol)
            self.chart.set_values(history)

            self.refresh_watchlist()
            self.update_estimate()

        except ValueError as error:
            QMessageBox.warning(self, "Ticker Error", str(error))

    def update_estimate(self, *args):
        try:
            price = self.market.quote(self.current_symbol)
            quantity = self.quantity_input.value()
            self.estimated_total.setText(money(price * quantity))
        except ValueError:
            self.estimated_total.setText("$0.00")

    def place_order(self, side):
        symbol = self.current_symbol
        quantity = self.quantity_input.value()

        try:
            price = self.market.quote(symbol)

            if side == "BUY":
                self.db.buy(symbol, quantity, price)
            else:
                self.db.sell(symbol, quantity, price)

            QMessageBox.information(
                self,
                "Paper Order Executed",
                f"{side} order simulated successfully.\n\n"
                f"Ticker: {symbol}\n"
                f"Shares: {quantity:g}\n"
                f"Demo price: {money(price)}\n"
                f"Total: {money(quantity * price)}\n\n"
                "No real money or shares were traded."
            )

            self.refresh_all()

        except (ValueError, sqlite3.Error) as error:
            QMessageBox.warning(self, "Order Failed", str(error))

    def refresh_watchlist(self):
        symbols = list(DEMO_PRICES.keys())
        self.watch_table.setRowCount(len(symbols))

        for row, symbol in enumerate(symbols):
            price = self.market.quote(symbol)

            self.watch_table.setItem(row, 0, QTableWidgetItem(symbol))
            self.watch_table.setItem(row, 1, QTableWidgetItem(money(price)))

    def open_watch_symbol(self, row, column):
        item = self.watch_table.item(row, 0)
        if item:
            self.load_symbol(item.text())

    # --------------------------------------------------------
    # Portfolio tab
    # --------------------------------------------------------

    def build_portfolio_tab(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(14, 14, 14, 14)

        heading = QLabel("YOUR PORTFOLIO")
        heading.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(heading)

        self.positions_table = make_table([
            "Ticker", "Shares", "Average Cost", "Demo Price",
            "Market Value", "Open P/L"
        ])
        layout.addWidget(self.positions_table)

        self.tabs.addTab(page, "Portfolio")

    # --------------------------------------------------------
    # Order history tab
    # --------------------------------------------------------

    def build_history_tab(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(14, 14, 14, 14)

        heading = QLabel("ORDER HISTORY")
        heading.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(heading)

        self.history_table = make_table([
            "Order #", "Date / Time", "Side", "Ticker",
            "Shares", "Demo Price", "Total"
        ])
        layout.addWidget(self.history_table)

        self.tabs.addTab(page, "Order History")

    # --------------------------------------------------------
    # Refresh dashboard
    # --------------------------------------------------------

    def refresh_all(self):
        self.refresh_stats()
        self.refresh_positions()
        self.refresh_history()
        self.refresh_watchlist()
        self.update_estimate()

    def refresh_stats(self):
        cash = self.db.cash()
        positions = self.db.positions()

        market_value = sum(
            p["quantity"] * self.market.quote(p["symbol"])
            for p in positions
        )

        cost_basis = sum(
            p["quantity"] * p["avg_cost"]
            for p in positions
        )

        equity = cash + market_value
        pnl = market_value - cost_basis
        total_return = equity - INITIAL_CASH
        return_pct = total_return / INITIAL_CASH * 100

        self.cash_card.set_value(money(cash))
        self.equity_card.set_value(money(equity))
        self.pnl_card.set_value(
            money(pnl), GREEN if pnl >= 0 else RED
        )
        self.return_card.set_value(
            f"{money(total_return)} ({return_pct:+.2f}%)",
            GREEN if total_return >= 0 else RED
        )

    def refresh_positions(self):
        positions = self.db.positions()
        self.positions_table.setRowCount(len(positions))

        for row, position in enumerate(positions):
            symbol = position["symbol"]
            quantity = position["quantity"]
            average = position["avg_cost"]
            price = self.market.quote(symbol)
            value = quantity * price
            pnl = value - quantity * average

            values = [
                symbol,
                f"{quantity:g}",
                money(average),
                money(price),
                money(value),
                money(pnl)
            ]

            for column, value_text in enumerate(values):
                item = QTableWidgetItem(value_text)

                if column == 5:
                    item.setForeground(QColor(GREEN if pnl >= 0 else RED))

                self.positions_table.setItem(row, column, item)

    def refresh_history(self):
        orders = self.db.orders()
        self.history_table.setRowCount(len(orders))

        for row, order in enumerate(orders):
            values = [
                str(order["id"]),
                order["timestamp"],
                order["side"],
                order["symbol"],
                f'{order["quantity"]:g}',
                money(order["price"]),
                money(order["total"])
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                if column == 2:
                    item.setForeground(
                        QColor(GREEN if order["side"] == "BUY" else RED)
                    )

                self.history_table.setItem(row, column, item)

    # --------------------------------------------------------
    # Reset and shutdown
    # --------------------------------------------------------

    def reset_account(self):
        answer = QMessageBox.question(
            self,
            "Reset Paper Account",
            "Reset your account to $100,000 and permanently erase "
            "your paper positions and order history?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.db.reset()
            self.refresh_all()
            QMessageBox.information(
                self, "Account Reset",
                "Your paper account has been reset."
            )

    def closeEvent(self, event):
        self.db.close()
        event.accept()


# ============================================================
# START APPLICATION
# ============================================================

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    window = StockApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
