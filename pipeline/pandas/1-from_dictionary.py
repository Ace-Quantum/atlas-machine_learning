#!/usr/bin/env python3

"""First time in a while that we've hardcoded something"""

import pandas as pd


dict_df = {"First": [0.0, 0.5, 1.0, 1.5],
           "Second": ["one", "two", "three", "four"]}

rows = ["A", "B", "C", "D"]

df = pd.DataFrame.from_dict(dict_df)

df.index = rows
