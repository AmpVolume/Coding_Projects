#song.py
from dataclasses import dataclass, field

from .channel import Channel


@dataclass
class Song:

    title: str = "Untitled"

    bpm: int = 120

    channels: list[Channel] = field(
        default_factory=list
    )

    def add_channel(self, channel):
        self.channels.append(channel)