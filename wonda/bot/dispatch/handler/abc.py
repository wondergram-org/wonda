from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from wonda.bot.updates.base import BaseUpdate


class ABCHandler(ABC):
    blocking: bool

    @abstractmethod
    async def filter(self, update: "BaseUpdate", ctx: dict) -> Any:
        pass

    @abstractmethod
    async def handle(self, update: "BaseUpdate", ctx: dict) -> Any:
        pass
