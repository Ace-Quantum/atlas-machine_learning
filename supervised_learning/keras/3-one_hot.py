#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def one_hot(labels, classes=None):
    """Documentation"""
    if classes is not None:
        class_num = classes
    else:
        classes = np.max(labels) + 1

    matrix = K.utils.to_categorical(labels, class_num)

    return matrix
