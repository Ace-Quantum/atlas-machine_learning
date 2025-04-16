#!/usr/bin/env python3

"""pulls from a file and makes a dataframe"""

import pandas as pd


def from_file(filename, delimiter):
    """Pulls a file and makes a dataframe of it
    I will not be downloading datasets to test it"""

    df_return = pd.read_csv(filename, delimiter=delimiter)

    return df_return
