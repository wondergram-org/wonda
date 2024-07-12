from asyncio import iscoroutinefunction
from functools import reduce
from re import Pattern, compile, match
from typing import Any, Callable, TypeVar

from wonda.bot.rules.abc import ABCRule
from wonda.bot.states.types import BaseStateGroup, get_state_repr
from wonda.bot.updates import BaseUpdate

T = TypeVar("T", bound=BaseUpdate)


class Function(ABCRule[T]):
    """
    Invokes a predicate function to decide whether the update should be handled.
    """

    def __init__(self, func: Callable[[T, dict[str, Any]], bool]) -> None:
        self.func = func

    async def check(self, upd: T, ctx: dict) -> bool:
        return (
            await self.func(upd, ctx)
            if iscoroutinefunction(self.func)
            else self.func(upd, ctx)
        )


class Has(ABCRule[T]):
    """
    Checks if the update model has all the specified fields.
    """

    def __init__(self, *attr_names: str) -> None:
        self.attr_names = attr_names

    async def check(self, upd: T, _) -> bool:
        try:
            return all(
                bool(reduce(getattr, a.split("."), upd)) for a in self.attr_names
            )
        except AttributeError:
            return False


class Regex(ABCRule[T]):
    """
    Validates text of the update against regex patterns.
    """

    def __init__(self, *expr: Pattern | str) -> None:
        self.expr = tuple(compile(e) if isinstance(e, str) else e for e in expr)

    async def check(self, upd: T, ctx: dict) -> bool:
        if not any(
            text := getattr(upd, src, "")
            for src in ("text", "caption", "data", "query", "question")
        ):
            return False

        for e in self.expr:
            response = match(e, text)

            if response is None:
                return False
            
            if matches := response.groupdict():
                ctx |= matches
            elif matches := response.group() or response.groups():
                ctx |= {"matches": tuple(matches)}
            
            return True

        return False


class State(ABCRule[T]):
    """
    Checks that the user is in one of the specified states.
    """

    def __init__(self, *states: BaseStateGroup) -> None:
        self.states = tuple(get_state_repr(s) for s in states)

    async def check(self, upd: T, _) -> bool:
        if upd.state_repr is None:
            return not bool(self.states)

        return upd.state_repr.state in self.states


class StateGroup(ABCRule[T]):
    """
    Checks that the state the user is in belongs
    to one of the specified groups.
    """

    def __init__(self, *groups: type[BaseStateGroup]) -> None:
        self.groups = tuple(g.__name__ for g in groups)

    async def check(self, upd: T, _) -> bool:
        if upd.state_repr is None:
            return not self.groups

        group = upd.state_repr.state.split(":", maxsplit=1)[0]
        return group in self.groups


class Text(ABCRule[T]):
    """
    Checks if the text of the update matches one of the of the given texts.
    """

    def __init__(self, *texts: str, ignore_case: bool = False) -> None:
        self.ignore_case = ignore_case
        self.texts = texts if not ignore_case else tuple(map(str.lower, texts))

    async def check(self, upd: T, _) -> bool:
        if not any(
            text := getattr(upd, src, "")
            for src in ("text", "caption", "data", "query", "question")
        ):
            return False

        return (text if not self.ignore_case else text.lower()) in self.texts


__all__ = ("Function", "Has", "Regex", "State", "StateGroup", "Text")
