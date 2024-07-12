from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wonda.bot.states.types import StateRepr
    from wonda.tools.storage.abc import ABCExpiringStorage, ABCStorage
    from wonda.tools.storage.types import Ex


class ABCBaseStateManager(ABC):
    @abstractmethod
    async def get(self, id: int) -> "StateRepr | None":
        """
        Gets state for the given chat.
        """
        pass

    @abstractmethod
    async def clear(self, id: int) -> None:
        """
        Clears given chat of any state.
        """
        pass


class ABCStateManager(ABCBaseStateManager):
    storage: "ABCStorage"

    @abstractmethod
    async def set(self, id: int, state: str, **payload) -> None:
        """
        Sets state for the given chat.
        """


class ABCExpiringStateManager(ABCBaseStateManager):
    storage: "ABCExpiringStorage"

    @abstractmethod
    async def set(self, id: int, state: str, ex: "Ex", **payload) -> None:
        """
        Sets expiring state for the given chat.
        """
