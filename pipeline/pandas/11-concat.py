#!/usr/bin/env python3

"""Concatinates dataframes"""

import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """concats based on Timestamp
    I already wrote the set index like that so I'm leaving it"""

    df1 = df1.set_index('Timestamp')
    df2 = df2.set_index('Timestamp')

    df2 = df2.truncate(after=1417411920)

    df_concat = pd.concat([df2, df1])

    return df_concat
