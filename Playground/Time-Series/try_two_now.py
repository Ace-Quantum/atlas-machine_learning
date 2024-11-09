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

start = datetime.datetime(2015, 1, 1, 0, 0, 0, 0, pytz.UTC)
end = datetime.datetime(2018, 11, 11, 0, 0, 0, 0, pytz.UTC)

weekly_rows = data[(data['Timestamp'] >= start) & (data['Timestamp'] <= end)].groupby(
    [pd.Grouper(key='Timestamp', freq='W-MON')]).first().reset_index()
# This feels like a code golfing line
# I'm going to try to make it multiple lines when I do the actual project

# print(weekly_rows.head())

trace1 = go.Scatter(
    x = weekly_rows['Timestamp'],
    y = weekly_rows['Open'].astype(float),
    mode = 'lines',
    name = 'Open'
)

trace2 = go.Scatter(
    x = weekly_rows['Timestamp'],
    y = weekly_rows['Close'].astype(float),
    mode = 'lines',
    name = 'Close'
)

trace3 = go.Scatter(
    x = weekly_rows['Timestamp'],
    y = weekly_rows['Weighted_Price'].astype(float),
    mode = 'lines',
    name = 'Weighted Avg'
)

layout = dict(
    title='Bitcoin history abriged 2015-2018 w/ slider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(
                    count=1,
                    label='1m',
                    step='month',
                    stepmode='backward'
                ),
                dict(
                    count=6,
                    label='6m',
                    step='month',
                    stepmode='backward'
                ),
                dict(
                    count=36,
                    label='3y',
                    step='month',
                    stepmode='backward'
                ),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)
# Okay that was NOT fun to type
# Is there an easier way or is that just how formatting is?

data = [trace1, trace2, trace3]
fig = dict(data=data, layout=layout)
iplot(fig, filename = "time series ranger")

# fig.show()