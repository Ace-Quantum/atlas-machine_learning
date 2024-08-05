#!/usr/bin/env python3

"""Documents here! Getcher Documents!"""

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

        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

        # self.nx = nx

    @property
    def W(self):
        """W"""
        return self.__W

    @property
    def b(self):
        """b"""
        return self.__b

    @property
    def A(self):
        """A"""
        return self.__A

    def forward_prop(self, X):
        """AAAA
        Why does it feel like
        I'll never be enough
        for the checker"""
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """Calculates the cost of battle"""
        m = len(Y[0])
        return -(1/m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
