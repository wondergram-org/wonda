from typing import Any

from wonda.bot.blueprint.abc import ABCBlueprint
from wonda.bot.dispatch.dispatcher import ABCDispatcher, DefaultDispatcher


class DefaultBlueprint(ABCBlueprint):
    def __init__(self, dispatcher: "ABCDispatcher | None" = None) -> None:
        self.dispatcher = dispatcher or DefaultDispatcher()

    def load_into(self, framework: Any) -> "DefaultBlueprint":
        framework.dispatcher.load(self.dispatcher)

        self.state_dispenser = framework.state_dispenser
        self.api = framework.api
        return self

    @property
    def on(self) -> DefaultDispatcher:
        return self.dispatcher  # type: ignore
