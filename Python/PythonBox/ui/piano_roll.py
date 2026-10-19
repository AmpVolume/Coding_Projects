from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem
)

from PySide6.QtGui import (
    QColor,
    QPen,
    QBrush
)

from audio.audio_engine import AudioEngine

from core.song import Song
from core.channel import Channel
from core.pattern import Pattern
from core.instrument import Instrument
from core.note import Note


class PianoRoll(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.cell_width = 32
        self.cell_height = 20

        self.rows = 36
        self.cols = 64

        self.audio = AudioEngine()

        # Song Model
        self.song = Song()

        instrument = Instrument()

        channel = Channel(
            name="Lead",
            instrument=instrument
        )

        pattern = Pattern()

        channel.patterns.append(pattern)

        self.song.channels.append(channel)

        self.pattern = pattern

        self.draw_grid()

    def draw_grid(self):

        pen = QPen(QColor(80, 80, 80))

        width = self.cols * self.cell_width
        height = self.rows * self.cell_height

        for row in range(self.rows + 1):
            self.scene.addLine(
                0,
                row * self.cell_height,
                width,
                row * self.cell_height,
                pen
            )

        for col in range(self.cols + 1):
            self.scene.addLine(
                col * self.cell_width,
                0,
                col * self.cell_width,
                height,
                pen
            )

    def row_to_freq(self, row):

        midi = 84 - row

        return 440.0 * (
            2 ** ((midi - 69) / 12)
        )

    def render_pattern(self):

        # Remove old note rectangles
        for item in self.scene.items():

            if isinstance(item, QGraphicsRectItem):
                self.scene.removeItem(item)

        # Draw notes from Pattern
        for note in self.pattern.notes:

            row = self.rows - note.pitch
            col = note.start

            rect = QGraphicsRectItem(
                col * self.cell_width,
                row * self.cell_height,
                note.length * self.cell_width,
                self.cell_height
            )

            rect.setBrush(
                QBrush(QColor(0, 200, 255))
            )

            rect.setPen(
                QPen(QColor(0, 120, 180))
            )

            rect.note_ref = note

            self.scene.addItem(rect)

    def mousePressEvent(self, event):

        pos = self.mapToScene(event.pos())

        col = int(pos.x() // self.cell_width)
        row = int(pos.y() // self.cell_height)

        if row < 0 or row >= self.rows:
            return

        if col < 0 or col >= self.cols:
            return

        # Delete existing note
        for item in self.scene.items():

            if not isinstance(item, QGraphicsRectItem):
                continue

            item_row = int(
                item.rect().y() // self.cell_height
            )

            item_col = int(
                item.rect().x() // self.cell_width
            )

            if item_row == row and item_col == col:

                if hasattr(item, "note_ref"):
                    self.pattern.remove_note(
                        item.note_ref
                    )

                self.render_pattern()

                print(self.pattern.notes)

                return

        # Create new note
        pitch = self.rows - row

        note = Note(
            pitch=pitch,
            start=col,
            length=1
        )

        self.pattern.add_note(note)

        freq = self.row_to_freq(row)

        self.audio.play_note(freq)

        self.render_pattern()

        print(self.pattern.notes)