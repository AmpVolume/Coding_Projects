import numpy as np
import sounddevice as sd


class AudioEngine:

    SAMPLE_RATE = 44100

    def play_note(self, freq):

        duration = 0.25

        t = np.linspace(
            0,
            duration,
            int(self.SAMPLE_RATE * duration),
            False
        )

        wave = np.sin(
            2 * np.pi * freq * t
        )

        wave *= 0.2

        sd.play(
            wave,
            self.SAMPLE_RATE
        )