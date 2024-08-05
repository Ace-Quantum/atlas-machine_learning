#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Documentation"""

    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    oh = int((h - kh) / sh) + 1
    ow = int((w - kw) / sw) + 1

    pool_images = np.zeros((m, oh, ow, c))

    for i in range(m):
        for y in range(oh):
            for x in range(ow):

                start_y = y * sh
                end_y = start_y + kh
                start_x = x * sw
                end_x = start_x + kw

                window = images[i, start_y:end_y, start_x:end_x, :]

                if mode == 'max':
                    pool_images[i, y, x, :] = np.max(window, axis=(0, 1))
                elif mode == 'avg':
                    pool_images[i, y, x, :] = np.mean(window, axis=(0, 1))

    return pool_images
