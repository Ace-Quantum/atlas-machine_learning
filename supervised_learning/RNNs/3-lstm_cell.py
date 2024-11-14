#!/usr/bin/env python3
"""class constructor for a LSTM unit"""

import numpy as np


class LSTMCell:
    """why is it a class for a cell
    when this is supposed to represent a unit?
    Is there a difference between the two?"""

    def __init__(self, i, h, o):
        """initialization
        i - data dim
        h - hidden state dim
        o - output dim"""
        
        # forgor gate params
        self.Wf = np.random.normal(size=(i + h, h))
        self.bf = np.zeros((1, h))

        # update/ input gate params
        self.Wu = np.random.normal(size=(i + h, h))
        self.bu = np.zeros((1, h))

        # intermediate cell state params
        self.Wc = np.random.normal(size=(i + h, h))
        self.bc = np.zeros((1, h))

        # output gate params
        self.Wo = np.random.normal(size=(i + h, h))
        self.bo = np.zeros((1, h))

        # output layer params
        self.Wy = np.random.normal(size=(h, o))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, c_prev, x_t):
        """forward propogation"""
        f = np.tanh(
            np.dot(self.Wf, x_t) + self.bf + np.dot(
                self.Wu, h_prev) + self.bu
        )

        i = np.sigmoid(np.dot(
            self.Wc, x_t) + self.bc + np.dot(
                self.Wo, h_prev) + self.bo
        )

        c_next = f * c_prev + i * np.tanh(np.dot(self.Wy, h_prev) + self.by)

        h_next = np.tanh(c_next)
        y = np.dot(self.Wy, h_next) + self.by

        return h_next, c_next, y


