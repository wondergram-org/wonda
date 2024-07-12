from typing_extensions import TYPE_CHECKING, Any, TypeVar

from wonda.bot.dispatch.handler import ABCHandler
from wonda.bot.dispatch.middleware.abc import ABCMiddleware
from wonda.bot.dispatch.view.abc import ABCView
from wonda.bot.dispatch.view.utils import get_update_model, get_update_type
from wonda.bot.updates.base import BaseUpdate
from wonda.modules import logger

if TYPE_CHECKING:
    from wonda.api.abc import ABCAPI
    from wonda.bot.states.manager.abc import ABCBaseStateManager
    from wonda.types.objects import Update


_ = Any
T = TypeVar("T", bound="BaseUpdate")


class DefaultView(ABCView[T]):
    def __init__(self, model: type[T], matches: str | list[str]):
        matches = [matches] if isinstance(matches, str) else matches
        self.model, self.matches = model, matches
        super().__init__()

    def register_handler(self, handler: "ABCHandler[T]") -> None:
        assert isinstance(
            handler, ABCHandler
        ), "Handler should be an instance of ABCHandler"
        self.handlers.append(handler)

    def register_middleware(self, middleware: "ABCMiddleware[T]") -> None:
        assert isinstance(
            middleware, ABCMiddleware
        ), "Middleware should be an instance of ABCMiddleware"
        self.middleware.append(middleware)

    def load(self, view: "ABCView[T]") -> None:
        self.middleware.extend(view.middleware)
        self.auto_rules.extend(view.auto_rules)
        self.handlers.extend(view.handlers)

    async def filter(self, update: "Update") -> bool:
        return get_update_type(update) in self.matches

    async def handle(
        self, update: "Update", ctx_api: "ABCAPI", state_manager: "ABCBaseStateManager"
    ) -> None:
        ctx: dict[str, _] = {}
        responses: list[_] = []

        upd = get_update_model(update, self.model)
        upd.untyped_ctx_api, upd.state_repr = ctx_api, await state_manager.get(
            upd.get_state_key()
        )

        for middleware in self.middleware:
            result = await middleware.pre(upd, ctx)

            if result is False:
                return

        for handler in self.handlers:
            result = await handler.filter(upd, ctx)

            if result is False:
                continue

            response = await handler.handle(upd, ctx)
            responses.append(response)

            if handler.blocking:
                break

        for middleware in self.middleware:
            await middleware.post(upd, ctx, responses)

        await logger.ainfo("Handled", update_id=update.update_id, view=self)

    def __repr__(self) -> str:
        return (
            f"DefaultView[{self.model.__name__}]"
            f"(middleware={self.middleware}, handlers={self.handlers})"
        )
