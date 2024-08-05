#!/usr/bin/env python3
"""Idk why they give us basecode but make us add
our own documentation"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Like seriously what are we doing here"""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.xticks(np.arange(0, 110, 10))
    plt.hist(
        student_grades,
        bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        edgecolor="black",
    )

    plt.show()
