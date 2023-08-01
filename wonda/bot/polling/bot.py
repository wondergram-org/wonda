from typing import AsyncIterator

from wonda.api import ABCAPI
from wonda.bot.polling.abc import ABCPolling
from wonda.errors import ABCErrorHandler, ErrorHandler, TelegramAPIError
from wonda.modules import logger
from wonda.types.objects import Update


class BotPolling(ABCPolling):
    def __init__(
        self,
        api: ABCAPI | None = None,
        error_handler: ABCErrorHandler | None = None,
    ):
        self.api = api
        self.error_handler = error_handler or ErrorHandler()

        self.stop = False
        self.offset = 0

    async def get_updates(self) -> list["Update"]:
        updates = []

        try:
            updates = await self.api.get_updates(offset=self.offset)
        except TelegramAPIError[401, 404] as e:
            await logger.critical(e)
            self.stop = True

        return updates

    async def listen(self) -> AsyncIterator["Update"]:
        while not self.stop:
            try:
                updates = await self.get_updates()
                for update in updates:
                    self.offset = update.update_id + 1
                    yield update
            except BaseException as e:
                await self.error_handler.handle(e)