from abc import ABC, abstractmethod

from wonda.tools.storage.types import NO_KEY, TTL, Key, Value


class ABCBaseStorage(ABC):
    @abstractmethod
    def get(self, key: Key, default: Value = NO_KEY) -> Value:
        pass

    @abstractmethod
    def delete(self, key: Key) -> None:
        pass

    @abstractmethod
    def contains(self, key: Key) -> bool:
        pass


class ABCStorage(ABCBaseStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value) -> None:
        pass


class ABCExpiringStorage(ABCStorage):
    @abstractmethod
    async def put(self, key: Key, value: Value, ttl: TTL) -> None:
        pass
