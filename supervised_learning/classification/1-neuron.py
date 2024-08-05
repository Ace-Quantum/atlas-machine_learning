#!/usr/bin/env python3

"""Documentation here for good measure"""

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

        self.nx = nx

    @property
    def W(self):
        """W"""
        self.__W = np.random.normal(size=(1, self.nx))
        return self.__W

    @property
    def b(self):
        """b"""
        if not hasattr(self, "__b"):
            self.__b = 0
        return self.__b

    @property
    def A(self):
        """A"""
        if not hasattr(self, "__A"):
            self.__A = 0
        return self.__A
