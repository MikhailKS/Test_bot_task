import time

from fastapi import APIRouter, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_pagination import add_pagination, Page, Params, paginate
from fastapi_pagination.utils import disable_installed_extensions_check

from backend.database.db_connection import collection_messages
from backend.models.models import MessagesModel
from backend.schemas.schemas import list_serial

router = APIRouter(tags=['Telegram Message'])
add_pagination(router)


@router.get("/api/v1/messages/", response_model=Page[MessagesModel], )
@cache()
async def get_messages(
        params: Params = Depends()
) -> Page[MessagesModel]:
    disable_installed_extensions_check()
    time.sleep(2)
    cursor = collection_messages.find()
    todos = list_serial(cursor)
    return paginate(todos, params=params)


@router.post('/api/v1/messages/')
async def save_message(models_object: MessagesModel):
    collection_messages.insert_one(dict(models_object))
    await FastAPICache.clear()
