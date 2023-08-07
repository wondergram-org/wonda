import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from wonda.api import ABCAPI
    from wonda.bot.dispatch.view.abc import ABCView
    from wonda.bot.states.dispenser.abc import ABCStateDispenser
    from wonda.errors import ABCErrorHandler
    from wonda.types.objects import Update


class ABCRouter(ABC):
    views: dict[str, "ABCView"]
    state_dispenser: "ABCStateDispenser"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    async def route(self, update: "Update", api: "ABCAPI") -> typing.Any:
        """
        Routes updates to their corresponding views
        """
