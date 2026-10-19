from dataclasses import dataclass, field
from .note import Note

@dataclass
class Pattern:
    name: str = "Pattern"
    notes: list[Note] = field(default_factory=list)

    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self, note):
        self.notes.remove(note)