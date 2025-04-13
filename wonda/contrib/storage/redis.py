import importlib.util

from wonda.net.utils import json
from wonda.tools.storage.abc import ABCExpiringStorage
from wonda.tools.storage.types import Ex, K, V

redis = importlib.util.find_spec("redis")

if redis is None:

    class RedisExpiringStorage:
        def __init__(self, *args, **kwargs) -> None:
            raise ImportError("Get `redis` package before using Redis storage")

else:
    from redis.asyncio import Redis

    class RedisExpiringStorage(ABCExpiringStorage[K, V]):
        def __init__(
            self,
            host: str | None = None,
            port: int | None = None,
            db: int | None = None,
            password: str | None = None,
            ssl: bool | None = None,
        ) -> None:
            self.client = Redis(
                host=host or "localhost",
                port=port or 6379,
                db=db or 0,
                ssl=ssl or False,
                password=password,
            )

        async def get(self, key: K, default: V | None = None) -> V | None:
            if await self.contains(key):
                v = await self.client.get(key)
                return json.loads(v)

            if default is None:
                raise KeyError("There is no such key")

            return default

        async def set(self, key: K, value: V, ex: Ex = Ex("inf")) -> None:
            await self.client.set(key, ex=ex, value=json.dumps(value))
            return None

        async def contains(self, key: K) -> bool:
            result = await self.client.exists(key)
            return bool(result)

        async def delete(self, key: K) -> None:
            if not await self.contains(key):
                raise KeyError("Storage does not contain this key")

            await self.client.delete(key)
            return None
