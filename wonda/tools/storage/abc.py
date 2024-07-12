from abc import ABC, abstractmethod

from wonda.tools.storage.types import Ex, Key, Value


class ABCBaseStorage(ABC):
    @abstractmethod
    async def get(self, key: Key, default: Value = ...) -> Value:
        pass

    @abstractmethod
    async def delete(self, key: Key) -> None:
        pass

    @abstractmethod
    async def contains(self, key: Key) -> bool:
        pass


class ABCStorage(ABCBaseStorage):
    @abstractmethod
    async def set(self, key: Key, value: Value) -> None:
        pass


class ABCExpiringStorage(ABCBaseStorage):
    @abstractmethod
    async def set(self, key: Key, value: Value, ex: Ex) -> None:
        pass
