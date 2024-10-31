#!/usr/bin/env python3
"""Addition to the class from before"""

import numpy as np


class BidirectionalCell:
    """So this is interesting,
    we use a specialty cell for bidirectionality
    which makes sense"""

    def __init__(self, i, h, o):
        """initialization"""
        return None

    def forward(self, h_prev, x_t):
        """Forward propogation"""
        return None

    def backward(self, h_next, x_t):
        """calculates the hidden state
        of the backwards loop"""
        return None

    def output(self, H):
        """calculates outputs for RNNs"""
        return None
