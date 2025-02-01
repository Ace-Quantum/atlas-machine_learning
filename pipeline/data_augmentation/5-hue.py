#!/usr/bin/env python3

"""I'm gonna go out on a limb
and say that this is going to be as easy as this
https://www.tensorflow.org/api_docs/python/tf/image/adjust_hue"""

import tensorflow as tf


def change_hue(image, delta):
    """Changes the hue"""

    return tf.image.adjust_hue(image, delta)
