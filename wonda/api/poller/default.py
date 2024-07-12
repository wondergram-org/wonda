from typing import AsyncIterator

from wonda.api.abc import ABCAPI
from wonda.api.poller.abc import ABCPoller
from wonda.api.poller.options import PollerOptions
from wonda.errors import ABCErrorHandler, APIException
from wonda.errors.handler.default import DefaultErrorHandler
from wonda.modules import logger
from wonda.types.helper import from_json
from wonda.types.objects import Update


class DefaultPoller(ABCPoller):
    def __init__(
        self,
        api: ABCAPI,
        error_handler: ABCErrorHandler | None = None,
        poller_options: PollerOptions | None = None,
    ) -> None:
        self.stop = False

        self.api = api
        self.options = poller_options or PollerOptions(0, [])
        self.error_handler = error_handler or DefaultErrorHandler()

    async def get_updates(
        self, offset: int | None = None, allowed_updates: list[str] | None = None
    ) -> list[Update]:
        updates = b"[]"

        try:
            updates = await self.api.request(
                "getUpdates", {"offset": offset, "allowed_updates": allowed_updates}
            )
        except APIException[401, 404] as e:
            await logger.acritical(e)
            self.stop = True

        return from_json(updates, type=list[Update])

    async def poll(self) -> AsyncIterator[Update]:
        offset, allowed_updates = self.options.offset, self.options.allowed_updates

        while not self.stop:
            try:
                updates = await self.get_updates(offset, allowed_updates)

                if not updates:
                    continue

                for update in updates:
                    yield update

                offset = updates[-1].update_id + 1
            except BaseException as e:
                await self.error_handler.handle(e)
