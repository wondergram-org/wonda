import re
from asyncio import iscoroutinefunction
from typing import Callable, Iterable, List, Optional, Type, Union

from wonda.bot.rules.abc import ABCRule
from wonda.bot.states.types import BaseStateGroup, get_state_repr
from wonda.bot.updates import BaseBotUpdate


class Function(ABCRule[BaseBotUpdate]):
    """
    A rule that calls a sync/async function to check
    if the update should be handled. It can accept
    any update objects, but always returns a boolean.
    """

    def __init__(self, func: Callable[[BaseBotUpdate], bool]) -> None:
        self.func = func

    async def check(self, upd: BaseBotUpdate) -> bool:
        if iscoroutinefunction(self.func):
            return await self.func(upd)
        return self.func(upd)


class Has(ABCRule[BaseBotUpdate]):
    """
    A rule that checks if the update dataclass
    has the specified attributes at its upper level.
    """

    def __init__(self, attr_names: Union[str, List[str]]) -> None:
        self.attr_names = [attr_names] if isinstance(attr_names, str) else attr_names

    async def check(self, upd: BaseBotUpdate) -> bool:
        return all(bool(getattr(upd, attr, None)) for attr in self.attr_names)


class State(ABCRule[BaseBotUpdate]):
    def __init__(
        self,
        state: Optional[Union[BaseStateGroup, List[BaseStateGroup]]] = None,
    ):
        if not isinstance(state, list):
            state = [] if state is None else [state]
        self.state = [get_state_repr(s) for s in state]

    async def check(self, upd: BaseBotUpdate) -> bool:
        if upd.state_repr is None:
            return not self.state
        return upd.state_repr.state in self.state


class StateGroup(ABCRule[BaseBotUpdate]):
    def __init__(
        self,
        state_group: Union[Type[BaseStateGroup], List[Type[BaseStateGroup]]],
    ):
        if not isinstance(state_group, list):
            state_group = [] if state_group is None else [state_group]
        self.state_group = [group.__name__ for group in state_group]

    async def check(self, upd: BaseBotUpdate) -> bool:
        if upd.state_repr is None:
            return not self.state_group

        group_name = upd.state_repr.state.split(":", maxsplit=1)[0]
        return group_name in self.state_group


try:
    import vbml
except ImportError:
    vbml = None


if vbml:

    class VBML(ABCRule[BaseBotUpdate]):
        """
        Matches text, captions and queries against given VBML patterns.
        Docs: https://github.com/tesseradecade/vbml
        """

        PatternLike = Union[str, vbml.Pattern]

        def __init__(
            self,
            patterns: Union[PatternLike, Iterable[PatternLike]],
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

        async def check(self, upd: BaseBotUpdate) -> Union[bool, dict]:
            if any(
                (text := getattr(upd, src, None))
                for src in ("text", "caption", "data", "query", "question")
            ):
                for pattern in self.patterns:
                    match = self.patcher.check(pattern, text)

                    if match not in (None, False):
                        return match
