from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class ABCRule(ABC, Generic[T]):
    @abstractmethod
    async def check(self, update: T, ctx: dict) -> bool:
        pass

    def __and__(self, other: "ABCRule") -> "AndRule":
        return AndRule(self, other)

    def __or__(self, other: "ABCRule") -> "OrRule":
        return OrRule(self, other)

    def __invert__(self) -> "NotRule":
        return NotRule(self)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class AndRule(ABCRule[T]):
    def __init__(self, *rules: ABCRule[T]) -> None:
        self.rules = rules

    async def check(self, update: T, ctx: dict) -> bool:
        ctx_copy = ctx.copy()

        for rule in self.rules:
            if not await rule.check(update, ctx_copy):
                return False

        ctx |= ctx_copy
        return True

    def __repr__(self):
        return f"<{self.__class__.__qualname__} rules={self.rules}>"


class NotRule(ABCRule[T]):
    def __init__(self, rule: ABCRule[T]) -> None:
        self.rule = rule

    async def check(self, update: T, ctx: dict) -> bool:
        ctx_copy = ctx.copy()
        return not await self.rule.check(update, ctx_copy)

    def __repr__(self):
        return f"<{self.__class__.__qualname__} rules={self.rules}>"


class OrRule(ABCRule[T]):
    def __init__(self, *rules: ABCRule[T]) -> None:
        self.rules = rules

    async def check(self, update: T, ctx: dict) -> bool:
        for rule in self.rules:
            ctx_copy = ctx.copy()

            if await rule.check(update, ctx):
                ctx |= ctx_copy
                return True
        return False

    def __repr__(self):
        return f"<{self.__class__.__qualname__} rules={self.rules}>"
