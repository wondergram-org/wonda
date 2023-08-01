from redis.asyncio import Redis

from wonda.modules import JSONModule, json
from wonda.tools.storage import ABCExpiringStorage
from wonda.tools.storage.types import Ex, Key, Value


class RedisStorage(ABCExpiringStorage):
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int | None = None,
        password: str | None = None,
        ssl: bool = False,
        json_processing_module: JSONModule = json,
    ) -> None:
        self.client = Redis(host=host, port=port, db=db, password=password, ssl=ssl)
        self.json_processing_module = json_processing_module

    async def get(self, key: Key, default: Value = ...) -> Value:
        if await self.contains(key):
            v = await self.client.get(key)
            return self.json_processing_module.loads(v)

        if default is ...:
            raise KeyError("There is no such key")

        return default

    async def put(self, key: Key, value: Value, ex: Ex = Ex("inf")) -> None:
        await self.client.set(
            key=key, ex=ex, value=self.json_processing_module.dumps(value)
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
