from wonda.api import ABCAPI
from wonda.bot.dispatch.router import ABCRouter
from wonda.bot.dispatch.view.abc import ABCView
from wonda.bot.states.dispenser.abc import ABCStateDispenser
from wonda.errors.error_handler.abc import ABCErrorHandler
from wonda.modules import logger
from wonda.types.objects import Update


class DefaultRouter(ABCRouter):
    def __init__(
        self,
        state_dispenser: "ABCStateDispenser",
        error_handler: "ABCErrorHandler",
        views: dict[str, "ABCView"],
    ) -> None:
        self.state_dispenser = state_dispenser
        self.error_handler = error_handler
        self.views = views

    async def route(self, update: "Update", ctx_api: "ABCAPI") -> None:
        await logger.debug("Routing", update=update)

        for view in self.views.values():
            try:
                if not await view.filter(update):
                    continue
                await view.handle(update, ctx_api, self.state_dispenser)
            except BaseException as e:
                await self.error_handler.handle(e)
