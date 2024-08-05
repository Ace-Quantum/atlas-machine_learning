#!/usr/bin/env python3
"""Idk where to put documentation"""
import tensorflow.compat.v1 as tf

tf.disable_eager_execution()
"""Idk where to put documentation"""


def create_train_op(loss, alpha):
    """Idk where to put documentation"""
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    train_op = optimizer.minimize(loss)

    return train_op
