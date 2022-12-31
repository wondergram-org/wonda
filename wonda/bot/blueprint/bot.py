from typing import Optional, TYPE_CHECKING

from wonda.bot.blueprint.abc import ABCBlueprint
from wonda.bot.dispatch.labelers.default import BotLabeler
from wonda.bot.dispatch.router.bot import BotRouter
from wonda.modules import logger

if TYPE_CHECKING:
    from wonda.api import ABCAPI
    from wonda.bot.bot import Bot
    from wonda.bot.polling.abc import ABCPolling
    from wonda.bot.states import ABCStateDispenser


class BotBlueprint(ABCBlueprint):
    def __init__(
        self,
        name: Optional[str] = None,
        labeler: Optional[BotLabeler] = None,
        router: Optional[BotRouter] = None,
    ):
        if name is not None:
            self.name = name

        self.labeler = labeler or BotLabeler()
        self.router: BotRouter = router or BotRouter()
        self.constructed = False

    def construct(
        self, api: "ABCAPI", polling: "ABCPolling", state_dispenser: "ABCStateDispenser"
    ) -> "BotBlueprint":
        self.api = api
        self.polling = polling
        self.state_dispenser = state_dispenser
        self.constructed = True
        return self

    def load(self, framework: "Bot") -> "BotBlueprint":
        framework.labeler.load(self.labeler)  # type: ignore
        logger.debug(f"Loading {self.name} blueprint")
        return self.construct(
            framework.api, framework.polling, framework.state_dispenser
        )

    @property
    def on(self) -> BotLabeler:
        return self.labeler
