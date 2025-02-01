#!/usr/bin/env python3

"""I'm gonna go out on a limb
and say that this is going to be as easy as this
https://www.tensorflow.org/api_docs/python/tf/image/flip_left_right"""

import tensorflow as tf

def flip_image(image):
    """Returns a flipped image
    The image in question is a 3D tf.tensor"""

    return tf.image.flip_left_right(image)

