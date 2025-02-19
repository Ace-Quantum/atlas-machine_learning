#!/usr/bin/env python3

"""flip and switch"""


def flip_switch(df):
    """sort in reverse chronological and then transpose"""

    df_flip_switch = df.sort_values(ascending=False)

    df_flip_switch = df_flip_switch.transpose()

    return df_flip_switch
