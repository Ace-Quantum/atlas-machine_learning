#!/usr/bin/env python3

"""After that last one it's kind of insulting
to be given a 2 bullet point task"""


def index(df):
    """sets timestamp as the index"""

    df.set_index('Timestamp')

    return df
