#!/usr/bin/env python3

"""Perhaps documentation needs to be here?"""

import numpy as np

"""Documentation is here"""


class Neuron:
    """Idk what to put here but it's kinda cool
    that we're building a fancy calculator
    that can recognize digits"""

    def __init__(self, nx):
        """Oh look more documentation"""

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0
