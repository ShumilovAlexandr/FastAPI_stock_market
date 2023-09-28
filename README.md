Инструменты и технологии: Python, FastAPI, машинное обучение (ARIMA, LSTM, Prophet)

Подход к решению проекта: 
~~Первым шагом является выбор любого из нескольких доступных поставщиков
данных о фондовом рынке, таких как Alpha Vantage, Yahoo Finance и Quandl,
и регистрация для получения ключа API. Затем вы создадите новое 
приложение FastAPI, используя интерфейс командной строки или редактор 
кода Python. Затем, используя ключ API, вы будете извлекать финансовые 
данные из API финансовых данных с помощью HTTP-запросов. Данные могут 
быть в формате JSON или CSV.~~ 
Получив финансовые данные, вы обработаете
их с помощью библиотек Python, таких как NumPy, Pandas и Plotly, а 
также выполните вычисления, проанализируете тенденции и создадите 
визуализации. Вы будете внедрять алгоритмы прогнозирования временных 
рядов, такие как ARIMA, LSTM или Prophet, для прогнозирования 
будущих тенденций фондового рынка, используя библиотеки Python, такие
как statsmodels, Keras или Prophet. Вы будете определять конечные 
точки API, используя синтаксис декоратора FastAPI, указывая метод 
запроса и модель ответа. Например, вы можете определить конечную 
точку для получения данных фондового рынка для данного биржевого 
символа. Последний шаг - протестировать ваш API и развернуть его с 
помощью любого популярного облачного сервиса, такого как AWS.