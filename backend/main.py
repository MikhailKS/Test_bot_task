import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from backend.config.config import config
from backend.routers.router_v1 import router



app = FastAPI(
    title="Telegram Bot API"
)


app.include_router(router=router)


@app.on_event('startup')
async def startup_event():
    reids = aioredis.from_url(
        url=config.redis_config.construct_redis_url(),
        encoding='utf-8',
        decode_responses=False
    )
    FastAPICache.init(RedisBackend(reids), prefix='fastapi-cache')



if __name__ == '__main__':
    uvicorn.run('backend.main:app', reload=True)