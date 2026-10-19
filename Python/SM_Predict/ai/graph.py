import sys
import numpy as np
import sounddevice as sd
import time

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem
)

from PySide6.QtGui import QColor, QPen, QBrush
from PySide6.QtCore import Qt, QTimer

SAMPLE_RATE = 44100


# =========================
# SYNTH
# =========================
class NESPulseSynth:
    def generate(self, frequency=440, duration=0.2, duty=0.5):
        t = np.arange(int(SAMPLE_RATE * duration)) / SAMPLE_RATE
        wave = ((t * frequency) % 1 < duty).astype(np.float32)
        return (wave * 2 - 1) * 0.2


class AudioEngine:
    def __init__(self):
        self.synth = NESPulseSynth()

    def play_note(self, frequency, duration=0.2):
        audio = self.synth.generate(frequency, duration)
        sd.play(audio, SAMPLE_RATE)


# =========================
# NOTE ITEM
# =========================
class NoteItem(QGraphicsRectItem):
    def __init__(self, x, y, w, h, row, col, piano):
        super().__init__(x, y, w, h)

        self.row = row
        self.col = col
        self.piano = piano

        self.setBrush(QBrush(QColor(0, 200, 255)))
        self.setPen(QPen(Qt.NoPen))

        self.setAcceptedMouseButtons(Qt.LeftButton)

    def mousePressEvent(self, event):
        self.scene().removeItem(self)
        event.accept()


# =========================
# PIANO ROLL
# =========================
class PianoRoll(QGraphicsView):

    def __init__(self, audio):
        super().__init__()

        self.audio = audio

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.cell_w = 32
        self.cell_h = 20

        self.rows = 36
        self.cols = 64

        self.notes = []  # store notes for playback

        self.playhead_x = 0

        self.draw_grid()

        # timer for playback
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)

        self.playing = False
        self.start_time = 0

    # -------------------------
    # GRID
    # -------------------------
    def draw_grid(self):
        pen = QPen(QColor(80, 80, 80))

        w = self.cols * self.cell_w
        h = self.rows * self.cell_h

        for r in range(self.rows + 1):
            y = r * self.cell_h
            self.scene.addLine(0, y, w, y, pen)

        for c in range(self.cols + 1):
            x = c * self.cell_w
            self.scene.addLine(x, 0, x, h, pen)

    # -------------------------
    # NOTES
    # -------------------------
    def row_to_freq(self, row):
        midi = 84 - row
        return 440 * (2 ** ((midi - 69) / 12))

    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())

        col = int(pos.x() // self.cell_w)
        row = int(pos.y() // self.cell_h)

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        x = col * self.cell_w
        y = row * self.cell_h

        # check existing note
        items = self.scene.items(pos)
        for item in items:
            if isinstance(item, NoteItem):
                self.scene.removeItem(item)
                self.notes.remove(item)
                return

        note = NoteItem(x, y, self.cell_w, self.cell_h, row, col, self)

        self.scene.addItem(note)
        self.notes.append(note)

        self.audio.play_note(self.row_to_freq(row))

    # -------------------------
    # PLAYBACK
    # -------------------------
    def start(self):
        self.playing = True
        self.playhead_x = 0
        self.start_time = time.time()
        self.timer.start(50)

    def stop(self):
        self.playing = False
        self.timer.stop()

    def tick(self):
        if not self.playing:
            return

        # move playhead
        self.playhead_x += 2

        # loop
        if self.playhead_x > self.cols * self.cell_w:
            self.playhead_x = 0

        # trigger notes
        for note in self.notes:
            if abs(note.col * self.cell_w - self.playhead_x) < 2:
                freq = self.row_to_freq(note.row)
                self.audio.play_note(freq)


# =========================
# MAIN WINDOW
# =========================
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.audio = AudioEngine()

        self.setWindowTitle("UltraBox - DAW Prototype")
        self.resize(1200, 800)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        self.piano = PianoRoll(self.audio)
        layout.addWidget(self.piano)

        # PLAY BUTTON
        self.play_btn = QPushButton("Play")
        self.stop_btn = QPushButton("Stop")

        self.play_btn.clicked.connect(self.piano.start)
        self.stop_btn.clicked.connect(self.piano.stop)

        layout.addWidget(self.play_btn)
        layout.addWidget(self.stop_btn)


# =========================
# RUN
# =========================
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())