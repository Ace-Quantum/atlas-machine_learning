#!/usr/bin/env python3

"""I'm gonna go out on a limb
and say that this is going to be as easy as this
https://www.tensorflow.org/api_docs/python/tf/image/adjust_contrast
Ok so not quite, I do have to make a random number."""

import tensorflow as tf


def change_contrast(image, lower, upper):
    """We'll see if they allow numpy
    They might not though."""

    return tf.image.random_contrast(image, lower, upper)
