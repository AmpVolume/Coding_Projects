from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout
)


class Transport(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.play_btn = QPushButton(
            "Play"
        )

        self.stop_btn = QPushButton(
            "Stop"
        )

        layout.addWidget(
            self.play_btn
        )

        layout.addWidget(
            self.stop_btn
        )

        self.setLayout(layout)