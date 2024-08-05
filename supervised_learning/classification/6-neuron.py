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
        return -(1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(
            1.0000001 - A))

    def evaluate(self, X, Y):
        """I can't believe it was this easy"""
        pred = self.forward_prop(X)
        pred_rounded = np.where(pred >= 0.5, 1, 0)

        ret_cost = self.cost(Y, pred)

        return pred_rounded, ret_cost

    # def backward_prop(self, A, Y):

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Time to finally learn what gradient descent is"""

        m_len = Y.shape[1]

        # receive clarification on this one
        dZ = A - Y

        dW = (1 / m_len) * np.dot(dZ, X.T)
        db = (1 / m_len) * np.sum(np.sum(dZ, axis=1))

        # print(type(db))

        # Why multiply by alpha?
        self.__W -= alpha * dW
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Ok so now we're getting into the hard stuff"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")

        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        for epoch in range(iterations):
            A = self.forward_prop(X)
            # cost = self.cost(Y, A)

            self.gradient_descent(X, Y, A, alpha)

        return self.evaluate(X, Y)
