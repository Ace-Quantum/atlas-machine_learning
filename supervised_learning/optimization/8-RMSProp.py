#!/usr/bin/env python3
"""Documentation"""

import tensorflow as tf

"""Documentation"""


def create_RMSProp_op(alpha, beta2, epsilon):
    """Documentation"""

    return tf.keras.optimizers.RMSprop(
        learning_rate=alpha,
        rho=beta2,
        epsilon=epsilon)
