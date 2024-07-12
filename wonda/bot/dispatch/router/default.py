from wonda.api import ABCAPI
from wonda.bot.dispatch.router import ABCRouter
from wonda.bot.dispatch.view.abc import ABCView
from wonda.bot.states.manager.abc import ABCBaseStateManager
from wonda.errors.handler.abc import ABCErrorHandler
from wonda.modules import logger
from wonda.types.objects import Update


class DefaultRouter(ABCRouter):
    def __init__(
        self,
        state_manager: "ABCBaseStateManager",
        error_handler: "ABCErrorHandler",
        views: dict[str, "ABCView"],
    ) -> None:
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.views = views

    async def route(self, update: "Update", api: "ABCAPI") -> None:
        await logger.ainfo("Routing", update=update)

        for view in self.views.values():
            try:
                if not await view.filter(update):
                    continue
                await view.handle(update, api, self.state_manager)
            except BaseException as e:
                await self.error_handler.handle(e)
