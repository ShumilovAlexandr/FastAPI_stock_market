import httpx
import pandas as pd
import datetime

from fastapi import (APIRouter,
                     Depends,
                     status,
                     HTTPException)
from pathlib import Path

from database.db_conn import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_config import MARKETSTACK


router_market = APIRouter(
    prefix="/api-market",
    tags=["api-market"]
)



@router_market.get("/get_data")
async def get_data_from_stock_market(tiker: str):
    """
    Получение данных с API Marketstack.

    После получения данных, сохраняю данные в корневой папке в excel файле.
    """
    date_now = str(datetime.datetime.now().date())
    url_marketstack = "http://api.marketstack.com/v1/eod" \
                      f"?access_key={MARKETSTACK}" \
                      f"&symbols={tiker}" \
                      f"&date_from=2020-01-01" \
                      f"&date_to={date_now}" \
                      f"&limit=1000" \
                      f"&total=1000" \
                      f"&count=1000"
    try:
        data = httpx.get(url_marketstack).json()["data"]
        df = pd.DataFrame(data, columns=["open", "high", "low", "close",
                                         "symbol", "date"])
        df.to_csv('./market.csv', header=True, index=False)
        return data
    except httpx.RequestError:
        raise HTTPException(status_code=400,
                            detail="Ошибка при попытке получения данных с "
                                   "рынка.")

@router_market.get("/build_graph")
async def build_linear_or_candle_graph(tiker: str):
    """
    Получение ранее сохраненных данных из файла с директории и построение либо
    линейного, либо свечного графика.
    """
    try:
        pass
        # TODO вот тут надо написать функционал для построения графика






    except httpx.RequestError:
        raise HTTPException(status_code=400,
                            detail="Ошибка при попытке получения данных с "
                                   "рынка.")


