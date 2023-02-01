from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

from wonda.modules import logger

if TYPE_CHECKING:
    from wonda.bot.states.types import BaseStateGroup, StateRepr
    from wonda.tools.storage.abc import ABCStorage


class ABCStateDispenser(ABC):
    storage: "ABCStorage"

    @abstractmethod
    async def get(self, chat_id: int) -> Optional["StateRepr"]:
        pass

    @abstractmethod
    async def set(self, chat_id: int, state: "BaseStateGroup", **payload) -> None:
        pass

    @abstractmethod
    async def finish(self, chat_id: int) -> None:
        pass

    async def cast(self, chat_id: Optional[int]) -> Optional["StateRepr"]:
        if chat_id is None:
            return None

        logger.debug(f"State cast for identifier {chat_id}")
        return await self.get(chat_id)
