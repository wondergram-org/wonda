from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class ABCRule(ABC, Generic[T]):
    @abstractmethod
    async def check(self, upd: T, ctx: dict) -> bool:
        pass

    def __and__(self, other: "ABCRule[T]") -> "AndRule[T]":
        return AndRule(self, other)

    def __or__(self, other: "ABCRule[T]") -> "OrRule[T]":
        return OrRule(self, other)

    def __invert__(self) -> "NotRule[T]":
        return NotRule(self)

    def __repr__(self) -> str:
        return self.__class__.__name__


class ABCCompositeRule(ABCRule[T]):
    def __init__(self, *rules: ABCRule[T]) -> None:
        self.rules = rules

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(repr(i) for i in self.rules)})"


class NotRule(ABCRule[T]):
    """
    Negates the result of a given rule.
    """

    def __init__(self, rule: ABCRule[T]) -> None:
        self.rule = rule

    async def check(self, upd: T, ctx: dict) -> bool:
        ctx_copy = ctx.copy()
        return not await self.rule.check(upd, ctx_copy)

    def __repr__(self) -> str:
        return f"NotRule({self.rule})"


class AndRule(ABCCompositeRule[T]):
    """
    Checks if all given rules succeed.
    """

    async def check(self, upd: T, ctx: dict) -> bool:
        ctx_copy = ctx.copy()

        for rule in self.rules:
            if not await rule.check(upd, ctx_copy):
                return False

        ctx |= ctx_copy
        return True


class OrRule(ABCCompositeRule[T]):
    """
    Checks if one of the given rules succeeds.
    """

    async def check(self, upd: T, ctx: dict) -> bool:
        for rule in self.rules:
            ctx_copy = ctx.copy()

            if await rule.check(upd, ctx):
                ctx |= ctx_copy
                return True

        return False


__all__ = ("ABCRule", "AndRule", "NotRule", "OrRule")
