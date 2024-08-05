#!/usr/bin/env python3

"""documentation here"""


def moving_average(data, beta):
    """documentation here"""

    moving_averages = []

    v_t = 0

    if len(data) == 0:
        return moving_averages

    for i in range(len(data)):
        v_t = beta * v_t + (1 - beta) * data[i]
        moving_averages.append(v_t / (1 - beta ** (i + 1)))

    return moving_averages
