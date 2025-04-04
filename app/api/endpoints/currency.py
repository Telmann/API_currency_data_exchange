from fastapi import APIRouter, Depends

from app.api.endpoints.user import authorize
from app.utils.external_api import get_currency_list, currencies_exchange, get_live_list
from app.api.schemas.user import Payload
from app.api.schemas.currency import CurrenciesToExchange

router = APIRouter(prefix='/currency', tags=['currency'])


@router.get('/list')
async def get_currency(user: Payload = Depends(authorize)):
    return await get_currency_list()


@router.get('/exchange')
async def get_exchange_currency(user: Payload = Depends(authorize)):
    return await get_live_list()


@router.post('/exchange')
async def exchange_currency(currencies_to_exchange: CurrenciesToExchange, user: Payload = Depends(authorize)):
    return await currencies_exchange(currencies_to_exchange)