#!/usr/bin/env python3
"""forward propogation for a deep rnn"""

import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Looks like we're using the same RNN cells as before
    which is kinda interesting ngl"""

    t, m, _ = X.shape
    l, _, h = h_0.shape

    H = np.zeros((t + 1, l, m, h))
    H[0] = h_0

    Y = []

    for time in range(t):
        x_t = X[time]
        h_prev = H[time]

        for layer in range(l):
            h_prev[layer], y_t = rnn_cells[layer].forward(h_prev[layer], x_t)
            x_t = h_prev[layer]

        H[time + 1] = h_prev
        Y.append(y_t)

    Y = np.array(Y)

    return H, Y