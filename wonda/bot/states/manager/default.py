from wonda.bot.states.manager import ABCExpiringStateManager, ABCStateManager
from wonda.bot.states.types import StateRepr
from wonda.modules import logger
from wonda.tools.storage import (
    ABCExpiringStorage,
    ABCStorage,
    MemoryExpiringStorage,
    MemoryStorage,
)
from wonda.tools.storage.types import Ex


class DefaultStateManager(ABCStateManager):
    def __init__(self, storage: ABCStorage | None = None) -> None:
        self.storage = storage or MemoryStorage()

    async def set(self, id: int, state: str, **payload) -> None:
        return await self.storage.set(
            key=f"manager:{id}", value=StateRepr(state, id, payload)
        )
    
    async def get(self, id: int | None) -> StateRepr | None:
        return await self.storage.get(f"manager:{id}", default=None)

    async def clear(self, id: int) -> None:
        return await self.storage.delete(f"manager:{id}")

    async def cast(self, id: int | None = None) -> "StateRepr | None":
        await logger.adebug("State cast", id=id)
        return await self.get(id)


class DefaultExpiringStateManager(ABCExpiringStateManager):
    def __init__(self, storage: ABCExpiringStorage | None = None) -> None:
        self.storage = storage or MemoryExpiringStorage()

    async def set(self, id: int, state: str, ex: Ex, **payload) -> None:
        return await self.storage.set(
            ex=ex,
            key=f"manager:{id}",
            value=StateRepr(state, id, payload),
        )

    async def get(self, id: int) -> StateRepr:
        return await self.storage.get(f"manager:{id}", default=None)

    async def clear(self, id: int) -> None:
        return await self.storage.delete(f"manager:{id}")
