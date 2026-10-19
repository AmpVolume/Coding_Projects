from dataclasses import dataclass

@dataclass
class Note:
    pitch: int
    start: int
    length: int = 1
    velocity: float = 1.0