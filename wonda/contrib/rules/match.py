import importlib.util
from re import RegexFlag
from typing import Generic, TypeVar

from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates.types import BaseUpdate

T = TypeVar("T", bound=BaseUpdate)

vbml = importlib.util.find_spec("vbml")

if vbml is None:

    class Match(Generic[T]):
        def __init__(self, *args, **kwargs) -> None:
            raise ImportError("Get `vbml` package before using Match rule")

else:
    from vbml import Patcher, Pattern

    class Match(ABCRule[T], Generic[T]):
        """
        Checks if the text of the update matches with any given pattern.
        If a match is found, parses its arguments to the handler context.
        """

        def __init__(
            self,
            *patterns: "Pattern | str",
            patcher: "Patcher | None" = None,
            flags: RegexFlag | None = None,
        ) -> None:
            self.patcher = patcher or Patcher()
            self.patterns = [
                Pattern(p, flags=flags) if isinstance(p, str) else p for p in patterns
            ]
            self.flags = flags or RegexFlag(0)

        async def check(self, upd: T, ctx: dict) -> bool:
            if not any(
                text := getattr(upd, src, None)
                for src in ("text", "caption", "data", "query", "question")
            ):
                return False

            for pattern in self.patterns:
                match = self.patcher.check(pattern, text)

                if match is not None and match is not False:
                    ctx |= match
                    return True

            return False
