from typing import AsyncIterator, List, Optional

from wonda.api import ABCAPI
from wonda.bot.polling.abc import ABCPolling
from wonda.errors import ABCErrorHandler, ErrorHandler, TelegramAPIError
from wonda.modules import logger


class BotPolling(ABCPolling):
    def __init__(
        self,
        api: Optional[ABCAPI] = None,
        error_handler: Optional[ABCErrorHandler] = None,
    ):
        self.api = api
        self._error_handler = error_handler or ErrorHandler()
        self._stop = False

        self.offset = 0
        self.allowed_updates = []

    async def get_updates(self) -> Optional[List[dict]]:
        raw_updates = []

        try:
            raw_updates = await self.api.request(
                "getUpdates",
                {"offset": self.offset, "allowed_updates": self.allowed_updates},
            )
        except TelegramAPIError[401, 404] as e:
            logger.critical(e)
            self.stop()

        return raw_updates

    async def listen(self) -> AsyncIterator[dict]:
        while not self._stop:
            try:
                updates = await self.get_updates()
                for update in updates:
                    self.offset = update["update_id"] + 1
                    yield update
            except BaseException as e:
                await self._error_handler.handle(e)

    def stop(self) -> None:
        self._stop = True

    def construct(
        self, api: "ABCAPI", error_handler: Optional["ABCErrorHandler"] = None
    ) -> "BotPolling":
        self._api = api
        if error_handler is not None:
            self._error_handler = error_handler
        return self

    @property
    def api(self) -> "ABCAPI":
        if self._api is None:
            self.stop()
            raise NotImplementedError(
                "You must construct polling with API "
                "before trying to access the API property of BotPolling"
            )
        return self._api

    @api.setter
    def api(self, new_api: "ABCAPI"):
        self._api = new_api
