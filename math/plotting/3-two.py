#!/usr/bin/env python3
"""Some formatting! For the grade!"""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """By that I mean documentation!"""

    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of Radioactive Elements")
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.plot(x, y1, linestyle="dashed", c="r", label="C-14")
    plt.plot(x, y2, c="g", label="Ra-226")
    plt.legend(loc="upper right")

    # plt.plot(x, y1, y2)
    plt.show()
