#!/usr/bin/env python3

"""Takes the tail of a df and makes it a numpy array"""

def array(df):

    df_tail_sample = df[['High', 'Close']]

    df_tail_sample = df_tail_sample.tail(n=10)

    np_array = df_tail_sample.to_numpy

    return np_array
