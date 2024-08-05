#!/usr/bin/env python3
"""Documentation"""
import tensorflow as tf


def create_momentum_op(alpha, beta1):
    """Documentation"""

    optimizer = tf.keras.optimizers.SGD(learning_rate=alpha, momentum=beta1)

    return optimizer
