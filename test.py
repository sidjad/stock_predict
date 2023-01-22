#import csv 
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

import mplfinance as fplt

df = pd.read_csv("output.csv", index_col=0, parse_dates=True)

apple_df = df

print(apple_df.head())


#print("MPLFinance Version : {}".format(fplt.__version__))

sma = fplt.make_addplot(apple_df[["SMA", "EMA"]])

fplt.plot(
            apple_df,
            type='candle',
            addplot = sma,
            title='Apple, March - 2020',
            ylabel='Price ($)'
        )