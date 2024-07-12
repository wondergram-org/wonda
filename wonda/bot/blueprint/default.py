from wonda.bot.abc import ABCFramework
from wonda.bot.blueprint.abc import ABCBlueprint
from wonda.bot.dispatch.dispatcher import ABCDispatcher, DefaultDispatcher


class DefaultBlueprint(ABCBlueprint):
    def __init__(self, dispatcher: "ABCDispatcher | None" = None) -> None:
        self.dispatcher = dispatcher or DefaultDispatcher()

    def load_into(self, framework: "ABCFramework") -> "DefaultBlueprint":
        self.state_manager = framework.state_manager
        self.untyped_api = framework.api

        framework.dispatcher.load(self.dispatcher)
        return self
