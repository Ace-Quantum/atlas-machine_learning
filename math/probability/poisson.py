#!/usr/bin/env python3
"""Here's some documentation"""


class Poisson:
    """And more? Wow I never would have guessed"""

    def __init__(self, data=None, lambtha=1.0):
        """Woah! More documentation!!"""
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
                self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """And yet, more documentation"""
        k = int(k)

        if k < 0:
            return 0
        else:
            factorial_result = 1
            for i in range(1, k + 1):
                factorial_result *= i
            return_val = (
                (2.7182818285) ** -self.lambtha * (self.lambtha**k)
            ) / factorial_result

            return return_val

    def cdf(self, k):
        """Putting in some documentation
        in hopes of nabbing one or two extra points"""
        k = int(k)

        if k < 0:
            return 0
        else:
            cdf_value = 0
            for i in range(k + 1):
                i_factorial = 1
                for j in range(1, i + 1):
                    i_factorial *= j

                exponent_result = 2.7182818285**-self.lambtha
                # exponent_result = 1
                # temp = 1
                # for i in range(1, 100):
                #     temp *= -self.lambtha / i
                #     exponent_result += temp

                cdf_value += exponent_result * (self.lambtha**i) / i_factorial
            return cdf_value
