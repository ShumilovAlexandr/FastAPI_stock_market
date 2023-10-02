import numpy as nm
import pandas as pd

import plotly.graph_objects as go

df = pd.read_csv("./market.csv")

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                                     open=df['open'],
                                     high=df['high'],
                                     low=df['low'],
                                     close=df['close'])])
fig.show()


