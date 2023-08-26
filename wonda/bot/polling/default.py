from typing import AsyncIterator

from wonda.api.abc import ABCAPI
from wonda.bot.polling.abc import ABCPoller
from wonda.errors import ABCErrorHandler, ErrorHandler, TelegramAPIError
from wonda.modules import logger
from wonda.types.helper import json
from wonda.types.objects import Update


class DefaultPoller(ABCPoller):
    def __init__(
        self, api: ABCAPI, error_handler: ABCErrorHandler | None = None
    ) -> None:
        self.api, self.error_handler = api, error_handler or ErrorHandler()

        self.offset: int = 0
        self.allowed_updates: list[str] = []

        self.stop = False

    async def get_updates(self) -> list[Update]:
        updates = b"[]"

        try:
            updates = await self.api.request(
                "getUpdates",
                {"offset": self.offset, "allowed_updates": self.allowed_updates},
            )
        except TelegramAPIError[401, 404] as e:
            await logger.critical(e)
            self.stop = True

        return json.decode(updates, type=list[Update])

    async def poll(self) -> AsyncIterator[Update]:
        await logger.debug(
            "Starting", offset=self.offset, allowed_updates=self.allowed_updates
        )

        while not self.stop:
            try:
                updates = await self.get_updates()

                for update in updates:
                    self.offset = update.update_id + 1
                    yield update
            except BaseException as e:
                await self.error_handler.handle(e)
