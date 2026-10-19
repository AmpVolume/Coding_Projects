from .oscillator import Oscillator
from .envelope import ADSR


class Synth:

    def __init__(self):

        self.osc = Oscillator()
        self.env = ADSR()

    def note(
        self,
        freq,
        duration,
        instrument
    ):

        if instrument.waveform == "square":

            wave = self.osc.square(
                freq,
                duration
            )

        else:

            wave = self.osc.sine(
                freq,
                duration
            )

        return self.env.apply(
            wave,
            instrument.attack,
            instrument.decay,
            instrument.sustain,
            instrument.release
        )