#channel.py
from dataclasses import dataclass, field

from .pattern import Pattern
from .instrument import Instrument


@dataclass
class Channel:

    name: str

    instrument: Instrument

    patterns: list[Pattern] = field(
        default_factory=list
    )