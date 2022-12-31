from asyncio import AbstractEventLoop, get_event_loop
from typing import List, NoReturn, Optional, Union

from wonda.api import ABCAPI, API, Token
from wonda.bot.abc import ABCFramework
from wonda.bot.dispatch import (
    ABCLabeler,
    ABCRouter,
    BotLabeler,
    BotRouter,
)
from wonda.bot.states import BotStateDispenser
from wonda.bot.polling import ABCPolling, BotPolling
from wonda.errors import ABCErrorHandler, ErrorHandler
from wonda.modules import logger
from wonda.tools import LoopWrapper


class Bot(ABCFramework):
    def __init__(
        self,
        token: Optional[Token] = None,
        api: Optional[ABCAPI] = None,
        polling: Optional[ABCPolling] = None,
        router: Optional[ABCRouter] = None,
        labeler: Optional[ABCLabeler] = None,
        loop: Optional[AbstractEventLoop] = None,
        loop_wrapper: Optional[LoopWrapper] = None,
        error_handler: Optional[ABCErrorHandler] = None,
    ):
        self.api: Union[ABCAPI, API] = API(token) if token is not None else api  # type: ignore
        self.error_handler = error_handler or ErrorHandler()
        self.loop_wrapper = loop_wrapper or LoopWrapper()
        self.labeler = labeler or BotLabeler()
        self.state_dispenser = BotStateDispenser()
        self._polling = polling or BotPolling(self.api)
        self._router = router or BotRouter()
        self._loop = loop

    async def run_polling(
        self,
        *,
        offset: int = 0,
        drop_updates: bool = False,
        allowed_updates: List[str] = [],
    ) -> NoReturn:
        if drop_updates:
            await self.api.delete_webhook(drop_updates)

        self.polling.offset, self.polling.allowed_updates = offset, allowed_updates
        logger.info("Starting polling")

        async for update in self.polling.listen():  # type: ignore
            self.loop.create_task(self.router.route(update, self.api))

    def run_forever(self) -> None:
        self.loop_wrapper.add_task(self.run_polling())
        self.loop_wrapper.run_forever(self.loop)  # type: ignore

    @property
    def on(self) -> "ABCLabeler":
        return self.labeler

    @property
    def polling(self) -> "ABCPolling":
        return self._polling.construct(self.api)

    @property
    def router(self) -> "ABCRouter":
        return self._router.construct(
            views=self.labeler.views(),
            state_dispenser=self.state_dispenser,
            error_handler=self.error_handler,
        )

    @property
    def loop(self) -> AbstractEventLoop:
        if self._loop is None:
            self._loop = get_event_loop()
        return self._loop

    @loop.setter
    def loop(self, new_loop: AbstractEventLoop):
        self._loop = new_loop

    @router.setter
    def router(self, new_router: "ABCRouter"):
        self._router = new_router

    @polling.setter
    def polling(self, value):
        self._polling = value
