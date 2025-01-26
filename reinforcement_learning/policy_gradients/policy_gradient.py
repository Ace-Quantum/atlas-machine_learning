#!/usr/bin/env python3

"""Yep we still don't know what we're doing here.
But we'll give it the old college try"""

import numpy as np


def policy(matrix, weight):
    """I guess all it is is a multiplication of the matrixes"""
    logits = np.dot(matrix, weight)

    exp_logits = np.exp(logits - np.max(logits))
    softmax_probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

    return softmax_probs
