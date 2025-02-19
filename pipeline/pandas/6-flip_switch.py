#!/usr/bin/env python3

"""flip and switch"""


def flip_switch(df):
    """sort in reverse chronological and then transpose"""

    df_flip_switch = df.sort_values(by=['Datetime'], ascending=False)

    df_flip_switch = df_flip_switch.T

    return df_flip_switch
