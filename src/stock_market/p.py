import pandas as pd

from prophet import Prophet
import matplotlib.pyplot as plt

# prop = Prophet()
#
# df = pd.read_csv('../new_market.csv')
#
# # Преобразуем столбец с датой в объект datetime
# df['ds'] = pd.DatetimeIndex(df['ds'])
#
# prop.fit(df)
#
# future_price = prop.make_future_dataframe(periods=365)
# forecast = prop.predict(future_price)
# fig = prop.plot(forecast, uncertainty=True)
# fig2 = prop.plot_components(forecast)
#
#
# plt.show()
df = pd.read_csv('../new_market.csv')
holidays = pd.read_csv('../holidays.csv')

prop = Prophet(holidays=holidays)
prop.add_country_holidays(country_name='UnitedStates')
prop.add_seasonality(name='weekly', period=7, fourier_order=5)

# Выбросы, которые выбиваются из общего тренда на графике. Для более
# "правильного" прогнозирования, их нужно удалить.
df.loc[(df['ds'] > '2022-10-17') & (df['ds'] < '2022-10-21'), 'y'] = None
df.loc[(df['ds'] > '2022-10-24') & (df['ds'] < '2022-10-26'), 'y'] = None
df.loc[(df['ds'] > '2022-11-01') & (df['ds'] < '2022-11-04'), 'y'] = None
df.loc[(df['ds'] > '2022-11-07') & (df['ds'] < '2022-11-09'), 'y'] = None



# df.loc[(df['ds'] > '2023-01-01') & (df['ds'] < '2023-02-20'), 'y'] = None
# df.loc[(df['ds'] > '2023-08-01') & (df['ds'] < '2023-09-25'), 'y'] = None

prop.fit(df)

future_price = prop.make_future_dataframe(periods=365)
forecast = prop.predict(future_price)

fig = prop.plot(forecast, uncertainty=True)
fig2 = prop.plot_components(forecast)

plt.show()

