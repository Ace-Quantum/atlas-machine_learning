#!/usr/bin/env python3

"""renames things"""

import pandas as pd

def rename(df):
    """renames Timestamp to Datetime
    convers timestamps to datetime values
    only returns datetime and close columns"""

    df_return = df.rename(columns={"Timestamp": "Datetime"})

    df_return['Datetime'] = pd.to_datetime(df_return['Datetime'])

    return(df_return)
