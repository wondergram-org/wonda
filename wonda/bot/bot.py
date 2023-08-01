from asyncio import AbstractEventLoop, get_event_loop

from wonda.api import ABCAPI, API, Token
from wonda.bot.abc import ABCFramework
from wonda.bot.dispatch import (
    ABCDispatcher,
    ABCRouter,
    DefaultDispatcher,
    DefaultRouter,
)
from wonda.bot.polling import ABCPolling, BotPolling
from wonda.bot.states import ABCStateDispenser, DefaultStateDispenser
from wonda.errors import ABCErrorHandler, ErrorHandler
from wonda.modules import logger
from wonda.tools import LoopWrapper


class Bot(ABCFramework):
    def __init__(
        self,
        token: Token | None = None,
        api: API | None = None,
        dispatcher: DefaultDispatcher | None = None,
        router: ABCRouter | None = None,
        polling: ABCPolling | None = None,
        state_dispenser: ABCStateDispenser | None = None,
        error_handler: ABCErrorHandler | None = None,
        loop: AbstractEventLoop | None = None,
        loop_wrapper: LoopWrapper | None = None,
    ):
        self.error_handler = error_handler or ErrorHandler()
        self.loop_wrapper = loop_wrapper or LoopWrapper()

        self.api = api or API(token or Token(""))
        self.polling = polling or BotPolling(self.api, self.error_handler)

        self.dispatcher = dispatcher or DefaultDispatcher()
        self.state_dispenser = state_dispenser or DefaultStateDispenser()
        self.router = router or DefaultRouter(
            self.state_dispenser, self.error_handler, self.dispatcher.views()
        )
        self.loop = loop or get_event_loop()

    async def run_polling(
        self,
        offset: int = 0,
        allowed_updates: list[str] = [],
        *,
        drop_updates: bool = False,
    ) -> None:
        if drop_updates is True:
            await self.api.delete_webhook(drop_updates)

        await logger.info("Starting polling")

        async for update in self.polling.listen():  # type: ignore
            await self.router.route(update, self.api)

    def run_forever(self, **kwargs) -> None:
        self.loop_wrapper.add_task(self.run_polling(**kwargs))
        self.loop_wrapper.run_forever(self.loop)  # type: ignore

    @property
    def on(self) -> DefaultDispatcher:
        return self.dispatcher
