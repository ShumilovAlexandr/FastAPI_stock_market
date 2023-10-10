import pandas as pd

from prophet import Prophet
import matplotlib.pyplot as plt

prop = Prophet()

df = pd.read_csv('../new_market.csv')

# Преобразуем столбец с датой в объект datetime
df['ds'] = pd.DatetimeIndex(df['ds'])

prop.fit(df)

future_price = prop.make_future_dataframe(periods=365)
forecast = prop.predict(future_price)
fig = prop.plot(forecast, uncertainty=True)
fig2 = prop.plot_components(forecast)


plt.show()











# import pandas as pd
#
# from prophet import Prophet
# from prophet.plot import plot_components_plotly, plot_plotly
#
#
# prop = Prophet(yearly_seasonality=True,
#                weekly_seasonality=True,
#                seasonality_mode = 'multiplicative')
#
#
# df = pd.read_csv('../new_market.csv')
# # Преобразуем столбец с датой в объект datetime
# df['ds'] = pd.DatetimeIndex(df['ds'])
#
# prop.fit(df)
#
# future_dates = prop.make_future_dataframe(periods=12, freq='m')
#
# forecast = prop.predict(future_dates)
#
# # # Визуализация прогноза
# fig = plot_plotly(prop, forecast)
# fig.update_layout(title_text="Курс акции")
# fig.show()

# # Визуализация компонентов прогнозов
# fig_components = plot_components_plotly(prop, forecast)
# fig_components.update_layout(title_text='Компоненты прогнозов')
# fig_components.show()



# forecast[["ds", 'yhat', 'yhat_lower', 'yhat_upper']].tail()

