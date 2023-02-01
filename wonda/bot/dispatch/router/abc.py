import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from wonda.api.abc import ABCAPI
    from wonda.bot.dispatch.view.abc import ABCView
    from wonda.bot.states.dispenser.abc import ABCStateDispenser
    from wonda.errors import ABCErrorHandler


class ABCRouter(ABC):
    views: typing.Dict[str, "ABCView"]
    state_dispenser: "ABCStateDispenser"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    async def route(self, update: dict, api: "ABCAPI") -> typing.Any:
        """
        Routes updates to their corresponding views
        """
        pass

    @abstractmethod
    def construct(
        self,
        views: typing.Dict[str, "ABCView"],
        state_dispenser: "ABCStateDispenser",
        error_handler: "ABCErrorHandler",
    ) -> "ABCRouter":
        pass

    def add_view(self, name: str, view: "ABCView") -> None:
        self.views[name] = view

    def view(self, name: str) -> typing.Callable[..., typing.Type["ABCView"]]:
        def decorator(view: typing.Type["ABCView"]):
            self.add_view(name, view())
            return view

        return decorator
