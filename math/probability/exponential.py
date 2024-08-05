#!/usr/bin/env python3
"""Here's some documentation"""


class Exponential:
    """more documentation"""

    def __init__(self, data=None, lambtha=1.0):
        """More!!! More pictures of spiderman!!!"""
        self.lambtha = float(lambtha)

        if data is None:
            if lambtha < 1:
                raise ValueError("lambtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = len(data) / sum(data)
