#!/usr/bin/env python3
"""forward propogation for a deep rnn"""

import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Looks like we're using the same RNN cells as before
    which is kinda interesting ngl"""

    t, m, i = X.shape
    l = len(rnn_cells)
    h = h_0.shape[1]

    H = np.zeroes((t, l, m, h))
    Y = np.zeroes((t, m, l))

    for t_count in range(t):
        x_t = X[t_count]

        h_next = h_0[:, :, 0]
        for layer, cell in enumerate(rnn_cells):
            h_next, y = cell.forward(h_next, None, x_t)

            H[t_count, layer] = h_next
            Y[t_count, :, layer] = y

    return H, Y