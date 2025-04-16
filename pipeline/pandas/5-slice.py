#!/usr/bin/env python3

"""Slices a dataframe"""


def slice(df):
    """for some reason we want every 60th row
    Actually that makes a lot of sense"""

    df_sliced = df[["High", "Low", "Close", "Volume_(BTC)"]]

    df_sliced = df_sliced.iloc[::60, :]

    return df_sliced
