import numpy as np


class ADSR:

    def apply(
        self,
        wave,
        attack,
        decay,
        sustain,
        release
    ):

        n = len(wave)

        env = np.ones(n)

        a = int(n * attack)
        d = int(n * decay)
        r = int(n * release)

        if a > 0:
            env[:a] = np.linspace(
                0,
                1,
                a
            )

        return wave * env