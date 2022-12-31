from typing import Dict

from wonda.api.abc import ABCAPI
from wonda.bot.dispatch.router import ABCRouter
from wonda.bot.dispatch.view import ABCView
from wonda.bot.states.dispenser import ABCStateDispenser
from wonda.errors.error_handler import ABCErrorHandler
from wonda.modules import logger


class BotRouter(ABCRouter):
    async def route(self, update: dict, ctx_api: "ABCAPI") -> None:
        logger.debug(f"Routing update {update}")

        for view in self.views.values():
            try:
                if not await view.process_update(update):
                    continue
                await view.handle_update(update, ctx_api, self.state_dispenser)
            except BaseException as e:
                await self.error_handler.handle(e)

    def construct(
        self,
        views: Dict[str, "ABCView"],
        state_dispenser: "ABCStateDispenser",
        error_handler: "ABCErrorHandler",
    ) -> "BotRouter":
        self.views = views
        self.state_dispenser = state_dispenser
        self.error_handler = error_handler
        return self
