from typing import Dict, NoReturn, Optional, Union

from wonda.tools.storage.abc import ABCStorage
from wonda.tools.storage.types import NO_KEY, Key, Value


class MemoryStorage(ABCStorage):
    def __init__(self) -> None:
        self.data: Dict[Key, Value] = {}

    async def get(self, key: Key, default: Value = NO_KEY) -> Union[Value, NoReturn]:
        if await self.contains(key):
            return self.data[key]

        if default is NO_KEY:
            raise KeyError("There is no such key")

        return default

    async def delete(self, key: Key) -> Optional[NoReturn]:
        if not await self.contains(key):
            raise KeyError("Storage doesn't contain this key")

        del self.data[key]
        return None

    async def put(self, key: Key, value: Value) -> None:
        self.data[key] = value
        return None

    async def contains(self, key: Key) -> bool:
        return key in self.data
