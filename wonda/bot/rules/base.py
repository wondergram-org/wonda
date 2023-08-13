import re
from asyncio import iscoroutinefunction
from functools import reduce
from typing import Callable

from wonda.bot.rules.abc import ABCRule
from wonda.bot.states.types import BaseStateGroup, get_state_repr
from wonda.bot.updates import BaseUpdate


class Function(ABCRule[BaseUpdate]):
    """
    Calls a function to check whether the update should be handled.
    Accepts any update objects, but always returns a boolean.
    """

    def __init__(self, func: Callable[[BaseUpdate], bool]) -> None:
        self.func = func

    async def check(self, upd: BaseUpdate, _) -> bool:
        if iscoroutinefunction(self.func):
            return await self.func(upd)
        return self.func(upd)


class Has(ABCRule[BaseUpdate]):
    """
    Checks if the specified attributes are present in the update dataclass.
    """

    def __init__(self, attr_names: str | list[str]) -> None:
        self.attr_names = [attr_names] if isinstance(attr_names, str) else attr_names

    async def check(self, upd: BaseUpdate, _) -> bool:
        try:
            return all(
                bool(reduce(getattr, attr.split("."), upd)) for attr in self.attr_names
            )
        except AttributeError:
            return False


class State(ABCRule[BaseUpdate]):
    """
    Checks that the user's state is currently set to one of the specified values.
    """

    def __init__(
        self, state: BaseStateGroup | list[BaseStateGroup] | None = None
    ) -> None:
        if not isinstance(state, list):
            state = [] if state is None else [state]
        self.state = [get_state_repr(s) for s in state]

    async def check(self, upd: BaseUpdate, _) -> bool:
        if upd.state_repr is None:
            return not self.state
        return upd.state_repr.state in self.state


class StateGroup(ABCRule[BaseUpdate]):
    """
    Checks that the state set for the current user belongs to one of the specified groups.
    """

    def __init__(
        self,
        state_group: type[BaseStateGroup] | list[type[BaseStateGroup]],
    ) -> None:
        if not isinstance(state_group, list):
            state_group = [] if state_group is None else [state_group]
        self.state_group = [group.__name__ for group in state_group]

    async def check(self, upd: BaseUpdate, _) -> bool:
        if upd.state_repr is None:
            return not self.state_group

        group_name = upd.state_repr.state.split(":", maxsplit=1)[0]
        return group_name in self.state_group


class Text(ABCRule[BaseUpdate]):
    """
    Checks if text contents of the update are exactly one of the specified variants.
    """

    def __init__(self, texts: str | list[str], ignore_case: bool = False) -> None:
        if not isinstance(texts, list):
            texts = [texts]

        self.texts = texts
        self.ignore_case = ignore_case

    async def check(self, upd: BaseUpdate, _) -> bool:
        if any(
            (text := getattr(upd, src, ""))
            for src in ("text", "caption", "data", "query", "question")
        ):
            return (
                text in self.texts
                if not self.ignore_case
                else text.lower() in list(map(str.lower, self.texts))
            )
        return False


try:
    import vbml
except ImportError:
    vbml = None


if vbml:
    PatternLike = type[str | vbml.Pattern]

    class Match(ABCRule[BaseUpdate]):
        """
        Parses and validates text, captions and queries.
        Learn more at: https://github.com/tesseradecade/vbml
        """

        def __init__(
            self,
            patterns: PatternLike | list[PatternLike],
            patcher: vbml.Patcher = vbml.Patcher(),
            flags: re.RegexFlag = re.RegexFlag(0),
        ) -> None:
            if not isinstance(patterns, list):
                patterns = [patterns]

            self.patterns = [
                vbml.Pattern(p, flags=flags) if isinstance(p, str) else p
                for p in patterns
            ]
            self.patcher = patcher

        async def check(self, upd: BaseUpdate, ctx: dict) -> bool:
            if any(
                (text := getattr(upd, src, ""))
                for src in ("text", "caption", "data", "query", "question")
            ):
                for pattern in self.patterns:
                    match = self.patcher.check(pattern, text)

                    if match not in (None, False):
                        ctx |= match
                        return True
            return False
