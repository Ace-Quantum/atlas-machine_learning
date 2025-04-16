#!/usr/bin/env python3

"""Some more preprocessing
Honestly it kind of doesn't make sense to have this project
after the preprocessing paper project"""


def fill(df):
    """fills in values"""

    df_filled = df.drop("Weighted_Price", axis=1)

    df_filled.loc[:, ["Close"]] = df_filled.loc[:, ["Close"]].ffill()

    df_filled["High"] = df_filled["High"].fillna(df_filled["Close"])
    df_filled["Low"] = df_filled["Low"].fillna(df_filled["Close"])
    df_filled["Open"] = df_filled["Open"].fillna(df_filled["Close"])

    df_filled[["Volume_(BTC)", "Volume_(Currency)"]] = df_filled[
        ["Volume_(BTC)", "Volume_(Currency)"]
    ].fillna(value=0)

    return df_filled
