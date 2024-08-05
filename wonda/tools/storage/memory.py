from time import time

from wonda.tools.storage.abc import ABCExpiringStorage, ABCStorage
from wonda.tools.storage.types import Ex, K, V


class MemoryStorage(ABCStorage[K, V]):
    def __init__(self) -> None:
        self.data: dict[K, V] = {}

    async def get(self, key: K, default: V | None = None) -> V | None:
        if await self.contains(key):
            return self.data[key]
        return default

    async def set(self, key: K, value: V) -> None:
        self.data[key] = value
        return None

    async def contains(self, key: K) -> bool:
        return key in self.data

    async def delete(self, key: K) -> None:
        if not await self.contains(key):
            raise KeyError("Storage does not contain this key")

        del self.data[key]
        return None


class MemoryExpiringStorage(ABCExpiringStorage[K, V]):
    def __init__(self) -> None:
        self.data: dict[K, tuple[V, Ex]] = {}

    async def get(self, key: K, default: V | None = None) -> V:
        if await self.contains(key):
            return self.data[key][0]

        if default is None:
            raise KeyError("There is no such key")

        return default

    async def set(self, key: K, value: V, ex: Ex = Ex("inf")) -> None:
        self.data[key] = value, ex + time()
        return None

    async def contains(self, key: K) -> bool:
        if key not in self.data:
            return False

        _, expires_at = self.data[key]

        if expires_at < time():
            del self.data[key]

        return key in self.data

    async def delete(self, key: K) -> None:
        if not await self.contains(key):
            raise KeyError("Storage does not contain this key")

        del self.data[key]
        return None
