from asyncio import AbstractEventLoop, get_event_loop

from wonda.api import API, Token
from wonda.bot.abc import ABCFramework
from wonda.bot.dispatch import (
    ABCDispatcher,
    ABCRouter,
    DefaultDispatcher,
    DefaultRouter,
    get_used_update_types,
)
from wonda.bot.polling import ABCPoller, DefaultPoller
from wonda.bot.states import ABCStateDispenser, DefaultStateDispenser
from wonda.errors import ABCErrorHandler, ErrorHandler
from wonda.tools import LoopWrapper


class Bot(ABCFramework):
    def __init__(
        self,
        token: Token | None = None,
        api: API | None = None,
        dispatcher: ABCDispatcher | None = None,
        router: ABCRouter | None = None,
        polling: ABCPoller | None = None,
        state_dispenser: ABCStateDispenser | None = None,
        error_handler: ABCErrorHandler | None = None,
        loop: AbstractEventLoop | None = None,
        loop_wrapper: LoopWrapper | None = None,
    ):
        self.error_handler = error_handler or ErrorHandler()
        self.loop_wrapper = loop_wrapper or LoopWrapper()

        self.api = api or API(token or Token(""))
        self.poller = polling or DefaultPoller(self.api, self.error_handler)

        self.dispatcher = dispatcher or DefaultDispatcher()
        self.state_dispenser = state_dispenser or DefaultStateDispenser()
        self.router = router or DefaultRouter(
            self.state_dispenser, self.error_handler, self.dispatcher.views()
        )
        self.loop = loop or get_event_loop()

    async def run_polling(self, *, drop_updates: bool = False) -> None:
        if drop_updates is True:
            await self.api.request("deleteWebhook", {"drop_pending_updates": True})

        self.poller.offset, self.poller.allowed_updates = 0, get_used_update_types(  # type: ignore
            self.dispatcher
        )

        async for update in self.poller.poll():
            self.loop.create_task(self.router.route(update, self.api))

    def run_forever(self, *, drop_updates: bool = False) -> None:
        self.loop_wrapper.add_task(self.run_polling(drop_updates=drop_updates))
        self.loop_wrapper.run_forever(self.loop)
