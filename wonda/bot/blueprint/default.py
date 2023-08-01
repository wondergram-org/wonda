from typing import TYPE_CHECKING

from wonda.bot.blueprint.abc import ABCBlueprint
from wonda.bot.dispatch.dispatcher.abc import ABCDispatcher
from wonda.bot.dispatch.dispatcher.default import DefaultDispatcher

if TYPE_CHECKING:
    from wonda.api import ABCAPI, API
    from wonda.bot import ABCStateDispenser, Bot


class DefaultBlueprint(ABCBlueprint):
    def __init__(self, dispatcher: "ABCDispatcher | None" = None) -> None:
        self.dispatcher = dispatcher or DefaultDispatcher()

    @classmethod
    def load_into(cls, framework: "Bot") -> "DefaultBlueprint":
        framework.dispatcher.load(cls.dispatcher)

        cls.state_dispenser = framework.state_dispenser
        cls.api = framework.api
        return cls

    @property
    def on(self) -> DefaultDispatcher:
        return self.dispatcher
