from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from wonda.bot.abc import ABCFramework

if TYPE_CHECKING:
    from wonda.api import ABCAPI
    from wonda.bot.dispatch.dispatcher import ABCDispatcher
    from wonda.bot.states import ABCStateManager


class ABCBlueprint(ABCFramework):
    dispatcher: "ABCDispatcher"
    state_manager: "ABCStateManager"
    untyped_api: "ABCAPI"

    @abstractmethod
    def load_into(self, framework: Any) -> "ABCBlueprint":
        pass

    def run_forever(self) -> None:
        raise NotImplementedError("Running polling from blueprints is not implemented")
