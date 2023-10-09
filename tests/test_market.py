import pytest
import httpx

from database.db_config import MARKETSTACK
from src.main import app
from src.stock_market.graph import AssetPrice
from conftest import client
from src.stock_market.routers import build_linear_or_candle_graph


# async def test_get_data_from_stock_market():
#     """Тест на получение данных с фондового рынка."""
#     url_marketstack = "http://api.marketstack.com/v1/eod" \
#                       f"?access_key={MARKETSTACK}" \
#                       f"&symbols=AAPL" \
#                       f"&date_from=2023-09-10" \
#                       f"&date_to=2023-09-27"
#     async with httpx.AsyncClient(app=app, base_url="/api-market/get_data") as client:
#         response = await client.get(url_marketstack)
#         assert response.status_code == 200
#
# async def test_get_and_broadcast_data_from_stock_market_to_api():
#     """
#     Тест на получение данных с фондового рынка и передача в API на
#     роутер.
#     """
#     async with httpx.AsyncClient(app=app,
#                                  base_url="http://127.0.0.1:8000") as client:
#         tiker = "AAPL"
#         response = await client.get(f"/api-market/get_data?tiker={tiker}")
#
#         assert response.status_code == 200
#
# async def test_get_course():
#     """
#     Тестирует создание объекта класса, отвечающего за построение графика.
#
#     Если в объекте класса вызвать метод get_graph(), то произойдет
#     построение графика (при условии наличия необходимого файла с котировками).
#     """
#     asset_c = AssetPrice("src/market.csv", "AAPL")
#     assert asset_c
#
# async def test_get_graph_course_action():
#     """
#     Тест роутера отвечающего за построение исторического курса акции.
#
#     Тест проходит. НО! В самом роуте нужно поменять маршрут до файла
#     (market.csv) с market.csv на src/market.csv. При смене маршрута до файла,
#     приходит ответ на тест 200 и открывается график с курсом.
#     """
#     response = client.get("/api-market/build_graph")
#     assert response.status_code == 200
#     assert await build_linear_or_candle_graph() == {'message': "Построен график с курсом интересующего актива."}

