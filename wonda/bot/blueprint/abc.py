from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from wonda.bot.abc import ABCFramework

if TYPE_CHECKING:
    from wonda.api import ABCAPI
    from wonda.bot.dispatch.dispatcher import ABCDispatcher
    from wonda.bot.states import ABCStateDispenser


class ABCBlueprint(ABCFramework):
    api: "ABCAPI"
    dispatcher: "ABCDispatcher"
    state_dispenser: "ABCStateDispenser"

    @abstractmethod
    def load_into(self, framework: Any) -> "ABCBlueprint":
        pass

    def run_forever(self) -> None:
        raise NotImplementedError("Running polling from blueprints is not implemented")
