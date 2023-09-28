import httpx

from fastapi import (APIRouter,
                     Depends,
                     status,
                     HTTPException)

from database.db_conn import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_config import MARKETSTACK


router_market = APIRouter(
    prefix="/api-market",
    tags=["api-market"]
)


@router_market.get("/get_data")
async def get_and_save_data_from_stock_market(tiker: str):
    """
    Получение данных с API Marketstack.

    После получения данных, сохраняю их в рабочей папке для дальнейшего
    построения интересующих меня графиков
    """
    url_marketstack = "http://api.marketstack.com/v1/eod" \
                      f"?access_key={MARKETSTACK}" \
                      f"&symbols={tiker}" \
                      f"&date_from=2023-09-10" \
                      f"&date_to=2023-09-27"
    try:
        res = httpx.get(url_marketstack)
        return res.json()
    except httpx.RequestError:
        raise HTTPException(status_code=400,
                            detail="Ошибка при попытке получения данных с "
                                   "рынка.")

