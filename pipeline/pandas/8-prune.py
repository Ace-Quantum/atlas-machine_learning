#!/usr/bin/env python3

"""some nice data cleaning"""


def prune(df):
    """Drops nan values"""

    df_pruned = df.dropna(subset=["Close"])

    return df_pruned
