#!/usr/bin/env python3
"""function for forward propogation"""

import numpy as np


def rnn(rnn_cell, X, h_0):
    """Forward propogation
    for a cell
    rnn_cell - exactly what it sounds like
    X - input array
    h_0 - initial hidden state of shape
    
    H - all hidden states
    Y - all outputs"""

    # Dimension extraction
    t, m, i = X.shape
    _, h = h_0.shape
    o = rnn_cell.Wy.shape[1] # output dimensionality

    # initialize hidden states and output arrays
    H = np.zeros((t + 1, m, h))
    Y = np.zeros((t, m, o))

    # initialize hidden state we have so far
    H[0] = h_0

    # forward prop per time step
    # I'm kind of weirdly tired of these ultra compressed variables that are passed in
    # I guess it makes sense though
    # From a readability stand point

    h_prev = h_0
    for step in range(t):
        x_t = X[step]
        h_next, y = rnn_cell.forward(h_prev, x_t)
        H[step + 1] = h_next
        Y[step] = y
        h_prev = h_next

    return H, Y