from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from wonda.modules import logger

if TYPE_CHECKING:
    from wonda.bot.states.types import BaseStateGroup, StateRepr
    from wonda.tools.storage.abc import ABCStorage


class ABCStateDispenser(ABC):
    storage: "ABCStorage"

    @abstractmethod
    async def get(self, chat_id: int) -> "StateRepr | None":
        pass

    @abstractmethod
    async def set(self, chat_id: int, state: "BaseStateGroup", **payload) -> None:
        pass

    @abstractmethod
    async def finish(self, chat_id: int) -> None:
        pass

    async def cast(self, chat_id: int | None = None) -> "StateRepr | None":
        if chat_id is None:
            return None

        await logger.debug("State cast", id=chat_id)
        return await self.get(chat_id)
