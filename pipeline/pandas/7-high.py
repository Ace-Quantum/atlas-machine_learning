#!/usr/bin/env python3

"""sorts by high price in descending order"""


def high(df):
    """Would be first try if I rememberd this"""

    df_sort = df.sort_values(by=["High"], ascending=False)

    return df_sort
