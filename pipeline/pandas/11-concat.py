#!/usr/bin/env python3

"""Concatinates dataframes"""

import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """concats based on Timestamp
    I already wrote the set index like that so I'm leaving it
    I changed it because I thought that might be the issue"""

    # df1 = index(df1)
    # df2 = index(df2)

    # df2 = df2[]

    df_concat = pd.concat([df2, df1])

    return df_concat
