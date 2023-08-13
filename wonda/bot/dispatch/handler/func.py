import inspect
from typing import Any, Callable

from wonda.bot.rules import ABCRule
from wonda.bot.updates import BaseUpdate

from .abc import ABCHandler

_ = Any


class FuncHandler(ABCHandler):
    def __init__(
        self,
        func: Callable,
        rules: list[ABCRule],
        *,
        blocking: bool = True,
    ):
        self.blocking = blocking
        self.rules = rules
        self.func = func

    async def filter(self, update: "BaseUpdate", ctx: dict) -> bool:
        for rule in self.rules:
            result = await rule.check(update, ctx)
            if result is False or result is None:
                return False
            elif result is True:
                continue
            ctx |= result
        return True

    async def handle(self, update: "BaseUpdate", ctx: dict) -> _:
        sig = inspect.signature(self.func)

        args = [k for k in sig.parameters.keys()]
        accepts = {k: v for k, v in ctx.items() if k in args[1:]}

        return await self.func(update, **accepts)

    def __repr__(self):
        return f"<FuncHandler {self.func.__name__} blocking={self.blocking} rules={self.rules}>"
