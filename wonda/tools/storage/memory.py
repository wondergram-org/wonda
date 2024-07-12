from time import time

from wonda.tools.storage.abc import ABCExpiringStorage, ABCStorage
from wonda.tools.storage.types import Ex, Key, Value


class MemoryStorage(ABCStorage):
    def __init__(self) -> None:
        self.data: dict[Key, Value] = {}

    async def get(self, key: Key, default: Value = ...) -> Value | None:
        if await self.contains(key):
            return self.data[key]

        if default is ...:
            raise KeyError("There is no such key")

        return default

    async def set(self, key: Key, value: Value) -> None:
        self.data[key] = value
        return None

    async def contains(self, key: Key) -> bool:
        return key in self.data

    async def delete(self, key: Key) -> None:
        if not await self.contains(key):
            raise KeyError("Storage does not contain this key")

        del self.data[key]
        return None


class MemoryExpiringStorage(ABCExpiringStorage):
    def __init__(self) -> None:
        self.data: dict[Key, tuple[Value, Ex]] = {}

    async def get(self, key: Key, default: Value = ...) -> Value | None:
        if await self.contains(key):
            return self.data[key][0]

        if default is ...:
            raise KeyError("There is no such key")

        return default

    async def set(self, key: Key, value: Value, ex: Ex = Ex("inf")) -> None:
        self.data[key] = value, ex + time()
        return None

    async def contains(self, key: Key) -> bool:
        if key not in self.data:
            return False

        _, expires_at = self.data[key]

        if expires_at < time():
            del self.data[key]

        return key in self.data

    async def delete(self, key: Key) -> None:
        if not await self.contains(key):
            raise KeyError("Storage does not contain this key")

        del self.data[key]
        return None
