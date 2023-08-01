from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from wonda.bot.updates.base import BaseUpdate

_ = Any
T = TypeVar("T", bound=BaseUpdate)


class ABCMiddleware(ABC, Generic[T]):
    @abstractmethod
    async def pre(self, update: T, ctx: dict) -> bool:
        pass

    @abstractmethod
    async def post(self, update: T, ctx: dict, responses: list[_]) -> None:
        pass
