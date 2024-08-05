#!/usr/bin/env python3
"""Documentation"""
import numpy as np


def sensitivity(confusion):
    """documentation"""
    sensetivity_return = []
    num_classes = confusion.shape[0]

    for i in range(num_classes):
        true_pos = confusion[i, i]
        false_neg = np.sum(confusion[i, :]) - true_pos

        sens = true_pos / (true_pos + false_neg) if false_neg > 0 else 1
        sensetivity_return.append(round(sens, 8))

    return np.array(sensetivity_return)
