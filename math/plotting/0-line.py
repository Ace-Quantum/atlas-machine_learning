#!/usr/bin/env python3
"""Oh heck was the documentation supposed to go here?"""
import numpy as np
import matplotlib.pyplot as plt

"""Here's some documentation"""


def line():
    """And some more despite this being code from the project itself"""

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.axis([0, 10, -50, 1050])
    plt.plot(y, color="red")

    plt.show()
