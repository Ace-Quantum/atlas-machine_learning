#!/usr/bin/env python3

"""Documentation"""
import numpy as np


def f1_score(confusion):
    """Documentation"""
    classes = confusion.shape[0]
    f1_scores = np.zeros(classes)

    sensitivity = __import__('1-sensitivity').sensitivity
    precision = __import__('2-precision').precision

    for i in range(classes):
        recall = sensitivity(confusion)

        prec = precision(confusion)
        prec_i = prec[i]

        if prec_i + recall[i] == 0:
            f1_scores[i] = 0.0
        else:
            f1_scores[i] = 2 * (prec_i * recall[i]) / (prec_i + recall[i])

    return f1_scores
