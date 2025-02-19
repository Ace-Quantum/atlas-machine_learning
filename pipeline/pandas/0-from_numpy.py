#!/usr/bin/env python3

"""imports a numpy array and returns it as a pandas array"""

import pandas as pd


def from_numpy(array):
    """Same as the note earlier"""

    df_return = pd.DataFrame(array)

    return df_return
