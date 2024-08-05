#!/usr/bin/env python3
"""Idk where documentation goes"""

import tensorflow.compat.v1 as tf

tf.disable_eager_execution()


"""Idk where documentation goes"""


def create_placeholders(nx, classes):
    """Idk where documentation goes"""
    X = tf.placeholder(tf.float32, shape=(None, nx), name="x")
    Y = tf.placeholder(tf.float32, shape=(None, classes), name="y")
    return X, Y
