#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Documentation"""

    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        pad_h = (sh * (h - 1) + kh - h) // 2
        pad_w = (sw * (w - 1) + kw - w) // 2
    elif padding == 'valid':
        pad_h, pad_w = 0, 0
    else:
        pad_h, pad_w = padding

    pad_images = np.pad(
        images, ((0, 0), (pad_h, pad_h),
                 (pad_w, pad_w), (0, 0)), mode="constant"
    )

    output_h = (h + 2 * pad_h - kh) // sh + 1
    output_w = (w + 2 * pad_w - kw) // sw + 1

    con_images = np.zeros((m, output_h, output_w, nc))

    for k in range(nc):
        for i in range(output_h):
            for j in range(output_w):

                s_i = i * sh
                s_j = j * sw
                n_i = s_i + kh
                n_j = s_j + kw

                con_images[:, i, j, k] = np.sum(
                    pad_images[:, s_i:n_i, s_j:n_j, :] * kernels[:, :, :, k],
                    axis=(1, 2, 3)
                )

    return con_images
