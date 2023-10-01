import pytest
import httpx

from database.db_config import MARKETSTACK
from src.main import app


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