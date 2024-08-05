from abc import ABC, abstractmethod
from typing import Generic

from wonda.tools.storage.types import Ex, K, V


class ABCBaseStorage(ABC, Generic[K, V]):
    @abstractmethod
    async def get(self, key: K, default: V | None = None) -> V | None:
        pass

    @abstractmethod
    async def delete(self, key: K) -> None:
        pass

    @abstractmethod
    async def contains(self, key: K) -> bool:
        pass


class ABCStorage(ABCBaseStorage[K, V]):
    @abstractmethod
    async def set(self, key: K, value: V) -> None:
        pass


class ABCExpiringStorage(ABCBaseStorage[K, V]):
    @abstractmethod
    async def set(self, key: K, value: V, ex: Ex) -> None:
        pass
