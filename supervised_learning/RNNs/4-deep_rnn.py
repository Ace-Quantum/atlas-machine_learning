#!/usr/bin/env python3
"""forward propogation for a deep rnn"""

import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Looks like we're using the same RNN cells as before
    which is kinda interesting ngl"""

    t, m, i = X.shape
    l, _, h = h_0.shape

    H = np.zeros((t + 1, l, m, h))
    H[0] = h_0

    Y = []

    for time in range(t):
        x_t = X[time]
        h_prev = H[time]

        for layer in range(l):
            rnn_cell = rnn_cells[layer]
            h_prev_layer = h_prev[layer]

            h_next, y = rnn_cell.forward(h_prev_layer, x_t)

            H[time + 1, layer] = h_next

            x_t = h_next

    Y = np.array(Y)

    return H, Y