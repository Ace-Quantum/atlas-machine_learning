#!/usr/bin/env python3
# This code was made with this tutorial
# https://www.kaggle.com/code/someadityamandal/bitcoin-time-series-forecasting/notebook

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotly import tools
# import plotly.plotly as py
from chart_studio import plotly
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import gc

import matplotlib.pyplot as plt
import seaborn as sns

from subprocess import check_output
# print(check_output(["ls", "./data"]).decode("utf8"))

import datetime, pytz

def dateparse (time_in_secs):
    return pytz.utc.localize(datetime.datetime.fromtimestamp(float(time_in_secs)))

data = pd.read_csv('./data/coinbaseUSD.csv', parse_dates=[0], date_parser=dateparse)

# data.info()

# print(data.head())

data['Volume_(BTC)'].fillna(value=0, inplace=True)
data['Volume_(Currency)'].fillna(value=0, inplace=True)
data['Weighted_Price'].fillna(value=0, inplace=True)

data['Open'].fillna(method='ffill', inplace=True)
data['High'].fillna(method='ffill', inplace=True)
data['Low'].fillna(method='ffill', inplace=True)
data['Close'].fillna(method='ffill', inplace=True)

# print(data.head())


