import numpy as np


class Oscillator:

    SAMPLE_RATE = 44100

    def square(self, freq, duration):

        t = np.arange(
            int(duration * self.SAMPLE_RATE)
        ) / self.SAMPLE_RATE

        wave = (
            (t * freq) % 1 < 0.5
        ).astype(np.float32)

        return wave * 2 - 1

    def sine(self, freq, duration):

        t = np.arange(
            int(duration * self.SAMPLE_RATE)
        ) / self.SAMPLE_RATE

        return np.sin(
            2 * np.pi * freq * t
        )