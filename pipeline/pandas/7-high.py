#!/usr/bin/env python3

"""sorts by high price in descending order"""


def high(df):

    df_sort = df.sort_values(by=["High"], ascending=False)

    return df_sort
