import httpx
import pandas as pd
import datetime

from fastapi import (APIRouter,
                     Depends,
                     status,
                     HTTPException)
from fastapi.responses import JSONResponse

from database.db_conn import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_config import MARKETSTACK
from stock_market.graph import AssetPrice
from stock_market.prop import get_stock_forecast


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
                      f"&date_from=2017-01-01" \
                      f"&date_to={date_now}" \
                      f"&limit=1500" \
                      f"&total=1500" \
                      f"&count=1500"
    try:
        data = httpx.get(url_marketstack).json()["data"]
        df = pd.DataFrame(data,
                          columns=["open", "high", "low", "close",
                                    "symbol", "date"])
        df.to_csv('../market.csv', header=True, index=False)
        return data
    except httpx.RequestError:
        raise HTTPException(status_code=400,
                            detail="Ошибка при попытке получения данных с "
                                   "рынка.")

@router_market.get("/build_graph")
async def build_linear_or_candle_graph():
    """
    Метод для построения свечного графика. Нужен для наглядности отображения текущих котировок.
    """
    try:
        df = pd.read_csv("../market.csv")

        # Получаем тикер для вывода на графике.
        tiker_activ = df['symbol'][0]
        graph = AssetPrice("../market.csv", tiker_activ)

        # Отрисовывает сам график
        graph.get_graph()
        return JSONResponse(content={'message': "В новой вкладке построен график с "
                                        "курсом интересующего актива."})
    except httpx.RequestError:
        raise HTTPException(status_code=400,
                            detail="Ошибка при попытке построения графика.")

@router_market.get("/data/get_forecast")
async def get_stock_market():
    """
    Получить будущий прогноз курса акции с помощью временных рядов
    """
    try:
        await get_stock_forecast()
    except:
        raise HTTPException(status_code=500,
                            detail="Ошибка при попытке построения графика.")
