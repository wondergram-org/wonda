from wonda.bot.dispatch.middleware.abc import ABCMiddleware
from wonda.bot.updates.types import MessageUpdate
from wonda.tools.storage import ABCExpiringStorage, MemoryExpiringStorage


class RateLimitingMiddleware(ABCMiddleware[MessageUpdate]):
    """
    Limits how often your bot should handle messages from a user.
    """
    def __init__(self, ex: int, storage: ABCExpiringStorage | None = None) -> None:
        self.ex, self.storage = ex, storage or MemoryExpiringStorage()

    async def pre(self, m: MessageUpdate, _) -> bool:
        assert m.from_, "Field `from` is empty"

        if await self.storage.contains(f"limiter:{m.from_.id}"):
            return False

        await self.storage.set(f"limiter:{m.from_.id}", True, ex=self.ex)
        return True
