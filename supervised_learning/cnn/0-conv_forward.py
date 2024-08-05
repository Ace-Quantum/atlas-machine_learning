#!/usr/bin/env python3
"""Documentation"""

import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """A_prev is a numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
        containing the output of the previous layer
    m is the number of examples
    h_prev is the height of the previous layer
    w_prev is the width of the previous layer
    c_prev is the number of channels in the previous layer
    W is a numpy.ndarray of shape (kh, kw, c_prev, c_new)
        containing the kernels for the convolution
    kh is the filter height
    kw is the filter width
    c_prev is the number of channels in the previous layer
    c_new is the number of channels in the output
    b is a numpy.ndarray of shape (1, 1, 1, c_new)
        containing the biases applied to the convolution
    activation is an activation function applied to the convolution
    padding is a string that is either same or valid,
        indicating the type of padding used
    stride is a tuple of (sh, sw) containing the strides for the convolution
    sh is the stride for the height
    sw is the stride for the width

    Returns: the output of the convolutional layer"""

    (m, h_prev, w_prev, c_prev) = A_prev.shape
    (kh, kw, _, c_new) = W.shape
    (sh, sw) = stride

    if padding == "same":
        h_out = h_prev
        w_out = w_prev
        pad_h = ((h_out - 1) * sh + kh - h_prev) // 2
        pad_w = ((w_out - 1) * sw + kw - w_prev) // 2
    elif padding == "valid":
        h_out = (h_prev - kh) // sh + 1
        w_out = (w_prev - kw) // sw + 1
        pad_h = 0
        pad_w = 0

    A_prev_pad = np.pad(
        A_prev, ((0, 0), (pad_h, pad_h), (pad_w, pad_w), (0, 0)), "constant"
    )

    Z = np.zeros((m, h_out, w_out, c_new))

    for i in range(m):
        for h in range(h_out):
            for w in range(w_out):
                for c in range(c_new):
                    h_start = h * sh
                    h_end = h_start + kh
                    w_start = w * sw
                    w_end = w_start + kw

                    A_slice = A_prev_pad[i, h_start:h_end, w_start:w_end, :]
                    Z[i, h, w, c] = np.sum(
                        A_slice * W[..., c]) + float(b[..., c])

    ret_output = activation(Z)

    return ret_output
