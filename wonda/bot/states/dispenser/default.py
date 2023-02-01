from typing import Optional

from wonda.bot.states.dispenser import ABCStateDispenser
from wonda.bot.states.types import BaseStateGroup, StateRepr
from wonda.tools.storage import ABCStorage, MemoryStorage


class BotStateDispenser(ABCStateDispenser):
    def __init__(self, storage: Optional[ABCStorage] = None):
        self.storage = storage or MemoryStorage()

    async def get(self, chat_id: int) -> Optional[StateRepr]:
        return await self.storage.get(f"fsm_state:{chat_id}", default=None)

    async def set(self, chat_id: int, state: BaseStateGroup, **payload) -> None:
        return await self.storage.put(
            f"fsm_state:{chat_id}",
            StateRepr(chat_id=chat_id, state=state, payload=payload),
        )

    async def finish(self, chat_id: int) -> None:
        return await self.storage.delete(f"fsm_state:{chat_id}")
