import numpy as nm
import pandas as pd

import plotly.graph_objects as go


class AssetPrice:

    """
    Класс используется для построения графика изменения курса актива.

    :param path_lib - путь до сохраненного файла с котировками.
    :param tiker - тикер запрашиваемого актива.
    """

    def __init__(self, path_lib, tiker):
        self.path_lib = path_lib
        self.tiker = tiker

    def get_graph(self):
        df = pd.read_csv(self.path_lib)
        fig = go.Figure(data=[go.Candlestick(x=df['date'],
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])
        fig.update_layout(
            title='Изменение котировок актива во времени',
            yaxis_title=f'Курс актива {self.tiker}'

        )
        fig.show()

