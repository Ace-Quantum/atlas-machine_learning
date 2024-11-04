#!/usr/bin/env python3
'''Class construction for RNNcells'''
import numpy as np


class RNNCell:
    """Cell class for RNN cells
    I'm actually not sure yet how these are different
    than normal NN cells
    But that's what this project aims to teach us"""

    def __init__(self, i, h, o):
        """Initialization
        i - dimensionality of data
        h - dimensionality of the hidden state
        o - dimensionality of outputs
        Wh - concatinated hidden state/input data weight
        bh - concatinated hidden state/input data bias
        Wy - output weight
        by - output bias
        Initialized in random normal distribution
        Weights used on the right side of matrix multiplication
        Biases initialized to zero"""

        # Initializing weights and biases
        # Easy stuff so far
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))

        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """Forward propogation
        self: truly the most important
        h_prev - previous hidden state
        x_t - input data
        h_next - new hidden state
        y - 'output of cell'
        ^^^ I feel like this doesn't explain much
        but it's all I've got"""

        # tacking the new onto the old
        h_x = np.concatenate((h_prev, x_t), axis=1)

        # compute next hidden state
        # I have questions about this
        h_next = np.tanh(np.dot(h_x, self.Wh) + self.bh)

        # compute output
        y = np.dot(h_next, self.Wy) + self.by
        y = np.exp(y) / np.sum(np.exp(y), axis=1, keepdims=True)

        return h_next, y
