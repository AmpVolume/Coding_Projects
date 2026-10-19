import sounddevice as sd


class Mixer:

    SAMPLE_RATE = 44100

    def play(self, wave):

        sd.play(
            wave,
            self.SAMPLE_RATE
        )