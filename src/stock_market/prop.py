import csv

import pandas as pd

from datetime import datetime

from prophet import Prophet
from prophet.plot import plot_components_plotly


prop = Prophet()


class Forecast:

    @staticmethod
    def get_new_csv_with_data():
        """
        Функция ничего не возвращает и не принимает.

        Просто работает с уже сформированным csv файлом содержащим фондовые
        данными и формирует новый csv для более удобной работы при построении
        временных рядов. Все это нужно потому, что метод get_data_from_stock_market
        сохраняет в market.csv данные в некорректном формате, а в Prophet нужен
        csv только с двумя полями (дата и цена, при том, дата изначально
        сохраняется в 'неправильном' формате). А полные данные, которые имеются
        в market.csv, также необходимы для построения корректного курса актива.
        """
        with open('../new_market.csv', 'w+', newline='') as new:
            # Читаем данные из собранного csv файла с фондовыми данными
            try:
                df_read = pd.read_csv('../market.csv')

                data_price = df_read['close']
                data_date = []
                for date in df_read['date']:
                    data_date.append(date[0:10])

                # Список заголовков для нового csv файла
                headerlist = ['ds', 'y']

                writer = csv.writer(new, delimiter=',')
                writer.writerows(zip(data_date, data_price ))
            except FileNotFoundError:
                return {"message": "Файл market.csv не найден или он "
                                   "отсутствует. Для получения прогноза курса, "
                                   "сначала нужно получить фондовые данные с "
                                   "помощью метода get_data_from_stock_market()"}

        df = pd.read_csv('../new_market.csv')
        df.to_csv('../new_market.csv', header=headerlist, index=False)
        return

    @staticmethod
    def get_forecast():
        """Функция отображает прогноз на будущие периоды."""
        try:
            Forecast.get_new_csv_with_data()
            df = pd.read_csv('../new_market.csv')

            # Преобразуем столбец с датой в объект datetime
            df['ds'] = pd.DatetimeIndex(df['ds'])

            prop.fit(df)
            future_dates = prop.make_future_dataframe(periods=36, freq='day')

            forecast = prop.predict(future_dates)
            forecast[["ds", 'yhat', 'yhat_lower', 'yhat_upper']]
            prop.plot(forecast, uncertainty=True)
        except FileNotFoundError:
            return {"message": "Файл с актуальными фондовыми данными не найден. "
                               "Возможно, он отсутствует."}


Forecast.get_new_csv_with_data()