#!/usr/bin/env python3

"""Building the network itself"""

import numpy as np

"""Idk I'm just putting documentation everywhere"""


class NeuralNetwork:
    """One day AI will take over the world.
    Let's hope they're nice about it"""

    def __init__(self, nx, nodes):
        """crickets"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros(shape=(nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """W1"""
        return self.__W1

    @property
    def b1(self):
        """b1"""
        return self.__b1

    @property
    def A1(self):
        """A1"""
        return self.__A1

    @property
    def W2(self):
        """W2"""
        return self.__W2

    @property
    def b2(self):
        """b2"""
        return self.__b2

    @property
    def A2(self):
        """A2"""
        return self.__A2

    def forward_prop(self, X):
        """AAAA
        Why does it feel like
        I'll never be enough
        for the checker"""

        Z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))

        Z2 = np.dot(self.__W2, self.A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """Calculates the cost of battle"""
        m = len(Y[0])
        return -(1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(
            1.0000001 - A))

    def evaluate(self, X, Y):
        """I can't believe it was this easy"""
        pred1, pred2 = self.forward_prop(X)
        pred_rounded2 = np.where(pred2 >= 0.5, 1, 0)

        ret_cost2 = self.cost(Y, pred2)

        return pred_rounded2, ret_cost2

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """update weights and biases"""

        m_len = Y.shape[1]

        dZ2 = A2 - Y

        dW2 = (1 / m_len) * np.dot(dZ2, A1.T)
        db2 = (1 / m_len) * np.sum(dZ2, axis=1, keepdims=True)

        dZ1 = np.dot(self.__W2.T, dZ2) * (A1 * (1 - A1))

        dW1 = (1 / m_len) * np.dot(dZ1, X.T)
        db1 = (1 / m_len) * np.sum(dZ1, axis=1, keepdims=True)

        self.__W1 -= alpha * dW1
        self.__b1 -= alpha * db1
        self.__W2 -= alpha * dW2
        self.__b2 -= alpha * db2

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
            A1, A2 = self.forward_prop(X)

            self.gradient_descent(X, Y, A1, A2, alpha)

        # print("We made it this far")
        return self.evaluate(X, Y)
