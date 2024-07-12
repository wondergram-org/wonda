import inspect
from typing import Any, Callable, Concatenate, Coroutine, ParamSpec, TypeVar

from wonda.bot.rules import ABCRule
from wonda.bot.updates import BaseUpdate
from wonda.modules import logger

from .abc import ABCHandler

_ = Any
P = ParamSpec("P")
T = TypeVar("T", bound=BaseUpdate)
FuncType = Callable[Concatenate[T, P], Coroutine[Any, Any, Any]]


class FuncHandler(ABCHandler[T]):
    def __init__(self, func: FuncType, *rules: ABCRule[T], blocking: bool = True):
        self.func, self.blocking, self.rules = func, blocking, list(rules)

    async def filter(self, update: T, ctx: dict) -> bool:
        for rule in self.rules:
            result = await rule.check(update, ctx)
            if result is False or result is None:
                return False
            elif result is True:
                continue
            ctx |= result
        return True

    async def handle(self, update: T, ctx: dict) -> _:
        sig = inspect.signature(self.func)

        args = [k for k in sig.parameters.keys()]
        accepts = {k: v for k, v in ctx.items() if k in args[1:]}

        return await self.func(update, **accepts)

    def __repr__(self):
        return f"FuncHandler(func={self.func.__name__}, blocking={self.blocking}, rules={self.rules})"
