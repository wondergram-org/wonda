from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from wonda.bot.dispatch.handler.func import FuncHandler
from wonda.bot.dispatch.middlewares.abc import ABCMiddleware
from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates.base import BaseUpdate

if TYPE_CHECKING:
    from wonda.api import ABCAPI, API
    from wonda.bot.dispatch.handler.abc import ABCHandler
    from wonda.bot.states.dispenser.abc import ABCStateDispenser
    from wonda.types.objects import Update


_ = Any
T = TypeVar("T", bound=BaseUpdate)


def get_update_type(update: "Update") -> str:
    for k in update.__struct_fields__:
        v = getattr(update, k, None)

        # Handle None values and `update_id` field
        if v is not None and not isinstance(v, int):
            return k

    return ""


class ABCView(ABC, Generic[T]):
    matches: str | list[str]

    def __init__(self) -> None:
        self.handlers: list["ABCHandler"] = []
        self.middlewares: list["ABCMiddleware"] = []
        self.auto_rules: list["ABCRule"] = []

    def __init_subclass__(cls, matches: str | list[str]) -> None:
        cls.matches = [matches] if isinstance(matches, str) else matches

    def __call__(self, *rules: "ABCRule", blocking: bool = True):
        """ """
        assert all(
            isinstance(rule, ABCRule) for rule in rules
        ), "All rules must be subclasses of ABCRule"

        def decorator(func) -> None:
            self.handlers.append(
                FuncHandler(func, [*self.auto_rules, *rules], blocking=blocking)
            )

        return decorator

    @abstractmethod
    def get_state_key(self, update: T) -> int | None:
        pass

    async def filter(self, update: "Update") -> bool:
        """
        Checks if the update is of the type this view supports.
        """
        return get_update_type(update) in self.matches

    async def handle(
        self, update: "Update", ctx_api: "ABCAPI", state_dispenser: "ABCStateDispenser"
    ) -> None:
        """
        Handles the update, casting it into suitable model and saturating it with
        useful properties like contextual API and FSM representation.
        """

        upd = self.get_update_model(update)
        upd.ctx_api, upd.state_repr = ctx_api, await state_dispenser.cast(  # type: ignore
            self.get_state_key(upd)
        )

        ctx: dict[str, _] = {}
        responses: list[_] = []

        for middleware in self.middlewares:
            result = await middleware.pre(upd, ctx)

            if result is False:
                return

        for handler in self.handlers:
            if not await handler.filter(upd, ctx):
                continue

            response = await handler.handle(upd, ctx)
            responses.append(response)

        for middleware in self.middlewares:
            await middleware.post(upd, ctx, responses)

    def get_update_model(self, update: "Update") -> T:
        upd = getattr(update, get_update_type(update))
        return self.__orig_bases__[0].__args__[0](**upd.dict())  # type: ignore

    def register_middleware(self, middleware: ABCMiddleware):
        """
        Registers a middleware. You can use this as a decorator.
        """
        try:
            if not isinstance(middleware, ABCMiddleware):
                raise ValueError("Argument is not an instance of ABCMiddleware")
        except TypeError:
            raise ValueError("Argument is not a class")
        self.middlewares.append(middleware)
