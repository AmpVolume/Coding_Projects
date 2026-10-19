from dataclasses import dataclass


@dataclass
class Instrument:

    name: str = "Pulse"

    waveform: str = "square"

    attack: float = 0.01
    decay: float = 0.05
    sustain: float = 0.8
    release: float = 0.1

    volume: float = 0.8