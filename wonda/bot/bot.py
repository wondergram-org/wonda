from asyncio import AbstractEventLoop, get_event_loop

from wonda.api import ABCAPI, DefaultAPI, Token
from wonda.api.poller import ABCPoller, DefaultPoller, PollerOptions
from wonda.bot.abc import ABCFramework
from wonda.bot.dispatch import (
    ABCDispatcher,
    ABCRouter,
    DefaultDispatcher,
    DefaultRouter,
    get_used_update_types,
)
from wonda.bot.states import ABCStateManager, DefaultStateManager
from wonda.errors import ABCErrorHandler, DefaultErrorHandler
from wonda.modules import logger
from wonda.tools import LoopWrapper


class Bot(ABCFramework):
    def __init__(
        self,
        token: Token | None = None,
        api: ABCAPI | None = None,
        dispatcher: ABCDispatcher | None = None,
        router: ABCRouter | None = None,
        state_manager: ABCStateManager | None = None,
        poller: ABCPoller | None = None,
        error_handler: ABCErrorHandler | None = None,
        loop_wrapper: LoopWrapper | None = None,
        loop: AbstractEventLoop | None = None,
    ):
        self.error_handler = error_handler or DefaultErrorHandler()
        self.loop_wrapper = loop_wrapper or LoopWrapper()
        self.untyped_api = api or DefaultAPI(token or Token(""))
        self.poller = poller or DefaultPoller(
            self.untyped_api, self.error_handler, PollerOptions(0, None)
        )
        self.dispatcher = dispatcher or DefaultDispatcher()
        self.state_manager = state_manager or DefaultStateManager()
        self.router = router or DefaultRouter(
            self.state_manager, self.error_handler, self.dispatcher.views
        )
        self.loop = loop or get_event_loop()

    async def run_polling(self, drop_updates: bool = False) -> None:
        if drop_updates:
            await self.untyped_api.request(
                "deleteWebhook", {"drop_pending_updates": True}
            )

        allowed_updates_empty = self.poller.options.allowed_updates is None
        if allowed_updates_empty:
            self.poller.options.allowed_updates = get_used_update_types(self.dispatcher)

        await logger.ainfo(
            "Starting",
            offset=self.poller.options.offset,
            allowed_updates=self.poller.options.allowed_updates,
        )
        async for update in self.poller.poll():
            self.loop.create_task(self.router.route(update, self.api))

    def run_forever(self, *, drop_updates: bool = False) -> None:
        self.loop_wrapper.add_task(self.run_polling(drop_updates=drop_updates))
        self.loop_wrapper.run_forever(self.loop)
