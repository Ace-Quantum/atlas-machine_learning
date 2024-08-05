#!/usr/bin/env python3
"""Here's some documentation!"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Oh wow, more documentation?"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    # Farrah = fruit[:, 0]
    # Fred = fruit[:, 1]
    # Felicia = fruit[:, 2]

    children = ["Farrah", "Fred", "Felicia"]

    apples = fruit[0]
    bananas = fruit[1]
    oranges = fruit[2]
    peaches = fruit[3]

    plt.bar(children, apples, color="red", label="apples", width=0.5)
    plt.bar(
        children,
        bananas,
        bottom=apples,
        color="yellow",
        label="bananas",
        width=0.5
    )
    plt.bar(
        children,
        oranges,
        bottom=apples + bananas,
        color="#ff8000",
        label="oranges",
        width=0.5,
    )
    plt.bar(
        children,
        peaches,
        bottom=apples + bananas + oranges,
        color="#ffe5b4",
        label="peaches",
        width=0.5,
    )

    plt.ylabel("Quantity of Fruit")
    plt.title("Number of Fruit per Person")
    plt.ylim(0, 80)
    plt.legend(loc="upper right")

    plt.show()
