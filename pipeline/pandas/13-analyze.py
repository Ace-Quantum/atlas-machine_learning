#!/usr/bin/env python3

"""Had to skip the last 2
Let's hope that they're not worth too much"""


def analyze(df):
    """computes descriptive statistics for columns"""

    df_stats = df.drop('Timestamp', axis=1)

    stats = df.describe()

    return stats
