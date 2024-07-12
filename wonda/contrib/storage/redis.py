import importlib.util

from wonda.modules import JSONModule, json
from wonda.tools.storage.abc import ABCExpiringStorage
from wonda.tools.storage.types import Ex, Key, Value

redis = importlib.util.find_spec("redis")

if redis is None:

    class RedisExpiringStorage:
        def __init__(self, *args, **kwargs) -> None:
            raise ImportError("Get `redis` package before using Redis storage")

else:
    from redis.asyncio import Redis

    class RedisExpiringStorage(ABCExpiringStorage):
        def __init__(
            self,
            host: str | None = None,
            port: int | None = None,
            db: int | None = None,
            password: str | None = None,
            ssl: bool | None = None,
            json_processing_module: JSONModule | None = None,
        ) -> None:
            self.client = Redis(
                host=host or "localhost",
                port=port or 6379,
                db=db or 0,
                ssl=ssl or False,
                password=password,
            )
            self.json_processing_module = json_processing_module or json

        async def get(self, key: Key, default: Value = ...) -> Value:
            if await self.contains(key):
                v = await self.client.get(key)
                return self.json_processing_module.loads(v)

            if default is ...:
                raise KeyError("There is no such key")

            return default

        async def set(self, key: Key, value: Value, ex: Ex = Ex("inf")) -> None:
            await self.client.set(
                key, ex=ex, value=self.json_processing_module.dumps(value)
            )
            return None

        async def contains(self, key: Key) -> bool:
            result = await self.client.exists(key)
            return bool(result)

        async def delete(self, key: Key) -> None:
            if not await self.contains(key):
                raise KeyError("Storage does not contain this key")

            await self.client.delete(key)
            return None
