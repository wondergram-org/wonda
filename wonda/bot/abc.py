from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wonda.api import ABCAPI, DefaultAPI
    from wonda.api.poller.abc import ABCPoller
    from wonda.bot.dispatch.dispatcher import ABCDispatcher, DefaultDispatcher
    from wonda.bot.states.manager.abc import ABCStateManager


class ABCFramework(ABC):
    untyped_api: "ABCAPI"
    dispatcher: "ABCDispatcher"
    state_manager: "ABCStateManager"
    poller: "ABCPoller"

    @property
    def api(self) -> "DefaultAPI":
        return self.untyped_api  # type: ignore

    @property
    def on(self) -> "DefaultDispatcher":
        return self.dispatcher  # type: ignore

    @abstractmethod
    def run_forever(self) -> None:
        pass
