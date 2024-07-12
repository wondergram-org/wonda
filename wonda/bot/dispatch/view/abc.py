from abc import ABC, abstractmethod

from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Callable,
    Concatenate,
    Coroutine,
    Generic,
    ParamSpec,
    TypeVar,
)

from wonda.bot.dispatch.handler.func import FuncHandler
from wonda.bot.rules.abc import ABCRule

if TYPE_CHECKING:
    from wonda.api import ABCAPI
    from wonda.bot.dispatch import ABCHandler, ABCMiddleware
    from wonda.bot.states.manager.abc import ABCBaseStateManager
    from wonda.bot.updates.base import BaseUpdate
    from wonda.types.objects import Update

P = ParamSpec("P")
T = TypeVar("T", bound="BaseUpdate")
FuncType = Callable[Concatenate[T, P], Coroutine[Any, Any, Any]]


class ABCView(ABC, Generic[T]):
    handlers: list["ABCHandler[T]"]
    middleware: list["ABCMiddleware[T]"]
    auto_rules: list["ABCRule[T]"]

    def __init__(self) -> None:
        self.handlers, self.middleware, self.auto_rules = [], [], []

    def __call__(
        self, *rules: "ABCRule[T]", blocking: bool = True
    ) -> Callable[[FuncType[T, P]], FuncType[T, P]]:
        assert all(
            isinstance(rule, ABCRule) for rule in rules
        ), "All rules must be subclasses of ABCRule"

        def decorator(func: FuncType[T, P]):
            self.register_handler(
                FuncHandler(func, *self.auto_rules, *rules, blocking=blocking)
            )
            return func

        return decorator

    @abstractmethod
    def register_handler(self, handler: "ABCHandler[T]") -> None:
        """
        Registers a new handler in this view.
        """

    @abstractmethod
    def register_middleware(self, middleware: "ABCMiddleware[T]") -> None:
        """
        Registers a new middleware in this view.
        """

    @abstractmethod
    def load(self, view: "ABCView[T]") -> None:
        """
        Loads one view into another.
        """

    @abstractmethod
    async def filter(self, update: "Update") -> bool:
        """
        Checks if an update can be handled by this view.
        Must return either True or False.
        """

    @abstractmethod
    async def handle(
        self, update: "Update", ctx_api: "ABCAPI", state_manager: "ABCBaseStateManager"
    ) -> None:
        """
        Handles an update. Can raise an exception
        while handling is taking place.
        """
