from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
    from wonda.bot.updates.base import BaseUpdate

_ = Any
T = TypeVar("T", bound="BaseUpdate")


class ABCHandler(ABC, Generic[T]):
    blocking: bool

    @abstractmethod
    async def filter(self, update: T, ctx: dict) -> bool:
        pass

    @abstractmethod
    async def handle(self, update: T, ctx: dict) -> _:
        pass
