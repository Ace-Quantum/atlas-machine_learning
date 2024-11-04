#!/usr/bin/env python3
"""Class construction for a GRUCell"""

import numpy as np


class GRUCell:
    """class for a GRUCell
    AKA 'Gated Recurrent Unit"""

    def __init__(self, i, h, o):
        """Initialization
        i - data dim
        h - hidden state dim
        o - output dim"""

        # initialize w & b for update gate
        self.Wz = np.random.normal(size=(i + h, h))
        self.bz = np.zeros((1, h))

        # initialize w & b for reset gate
        self.Wr = np.random.normal(size=(i + h, h))
        self.br = np.zeros((1, h))

        # initialize w & b for intermediate hidden state
        self.Wh = np.random.normal(size=(i + h, h))
        self.bh = np.zeros((1, h))

        # initialize w & b for output
        # output has w & b?
        self.Wy = np.random.normal(size=(h, o))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """forward propogation for a single step
        h_prev - previous hidden state
        x_t - input data for cell

        h_next - next hidden state
        y - output of cell"""

        # concat that inate
        h_x = np.concatenate((h_prev, x_t), axis=1)

        # compute update gaate
        z_t = self.sigmoid(np.dot(h_x, self.Wz) + self.bz)

        # compute reset gate
        r_t = self.sigmoid(np.dot(h_x, self.Wr) + self.br)

        # compute hidden state h~
        h_reset = np.concatenate((r_t * h_prev, x_t), axis=1)
        h_tilde = np.tanh(np.dot(h_reset, self.Wh) + self.bh)

        # compute next hidden state
        h_next = (1 - z_t) * h_prev + z_t * h_tilde

        # compute output
        y = self.softmax(np.dot(h_next, self.Wy) + self.by)

        return h_next, y

    # Here's some static methods
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e_x / np.sum(e_x, axis=1, keepdims=True)
