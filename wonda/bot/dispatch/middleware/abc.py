from abc import ABC
from typing import Any, Generic, TypeVar

from wonda.bot.updates.base import BaseUpdate

_ = Any
T = TypeVar("T", bound=BaseUpdate)


class ABCMiddleware(ABC, Generic[T]):
    async def pre(self, update: T, ctx: dict) -> bool:
        """
        Controls whether an update can be handled further.
        Expected to return `True` if it can, `False` otherwise.
        """

    async def post(self, update: T, ctx: dict, responses: list[_]) -> _:
        """
        Receives results of handling, such as the final context
        and a list of handler responses.
        """

    def __repr__(self) -> str:
        return self.__class__.__name__
