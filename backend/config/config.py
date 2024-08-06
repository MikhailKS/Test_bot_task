from dataclasses import dataclass
from environs import Env

@dataclass
class MongoDbConfig:
    host: str
    port: str

    def construct_mongo_url(
            self,
            host: str = None,
            port:str = None
    ) -> str:

        if not host:
            host = self.host
        if not port:
            port = self.port

        url = f"mongodb://{host}:{port}/"

        return url

@dataclass
class RedisConfig:
    host: str
    port: str

    def construct_redis_url(
            self,
            host: str = None,
            port:str = None
    ) -> str:

        if not host:
            host = self.host
        if not port:
            port = self.port

        url = f"redis://{host}:{port}/"

        return url


@dataclass
class Config:
    mongodb_config: MongoDbConfig
    redis_config: RedisConfig

def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
            mongodb_config=MongoDbConfig(
                host=env.str('HOST_DB'),
                port=env.str('PORT_DB')
            ),
            redis_config=RedisConfig(
                host=env.str('REDIS_HOST'),
                port=env.str('REDIS_PORT')
            )
    )

config = load_config('.env')
