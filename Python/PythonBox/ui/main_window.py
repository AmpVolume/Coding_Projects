from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout
)

from .transport import Transport
from .timeline import Timeline
from .piano_roll import PianoRoll


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "UltraBox"
        )

        self.resize(
            1400,
            900
        )

        central = QWidget()

        self.setCentralWidget(
            central
        )

        layout = QVBoxLayout()

        central.setLayout(
            layout
        )

        self.transport = Transport()
        self.timeline = Timeline()
        self.piano_roll = PianoRoll()

        layout.addWidget(
            self.transport
        )

        layout.addWidget(
            self.timeline
        )

        layout.addWidget(
            self.piano_roll
        )