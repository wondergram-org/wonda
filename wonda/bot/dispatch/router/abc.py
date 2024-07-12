from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from wonda.api import ABCAPI
    from wonda.bot.dispatch.view.abc import ABCView
    from wonda.bot.states.manager.abc import ABCBaseStateManager
    from wonda.errors import ABCErrorHandler
    from wonda.types.objects import Update


class ABCRouter(ABC):
    views: dict[str, "ABCView"]
    state_manager: "ABCBaseStateManager"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    async def route(self, update: "Update", api: "ABCAPI") -> None:
        """
        Routes updates to their corresponding views.
        """
