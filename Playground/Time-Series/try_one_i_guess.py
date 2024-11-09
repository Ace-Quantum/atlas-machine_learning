#!/usr/bin/env python3

import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True
)
# csv_path, _ = os.path.splitext(zip_path)

# # ------- this section was given to me by chatgpt -------
# {{{{{{{{This code, in fact, did not work}}}}}}}}
# csv_path = zip_path.replace('.zip', '.csv')

# if not os.path.isfile(csv_path):
#     raise FileNotFoundError(f"CSV file not found at {csv_path}")

# # ------- End of AI section -------

df = pd.read_csv(csv_path)

df = df[5::6]

date_time = pd.to_datetime(df.pop('Date Time'), format='%d.%m.%Y %H:%M:%S')

df.head()
