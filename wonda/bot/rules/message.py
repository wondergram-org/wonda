from re import compile, RegexFlag
from typing import Iterable, List, Optional, Union

from vbml import Pattern, Patcher

from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates import MessageUpdate


class Command(ABCRule[MessageUpdate]):
    def __init__(
        self, text: str, prefixes: Optional[Union[str, Iterable[str]]] = "/"
    ) -> None:
        if isinstance(prefixes, str):
            prefixes = [prefixes]

        self.text = text
        self.prefixes = prefixes

    async def check(self, msg: MessageUpdate) -> bool:
        if text := msg.text or msg.caption:
            for prefix in self.prefixes:
                if not text.startswith(prefix):
                    continue
                elif text.startswith(prefix + self.text + " "):
                    return {"args": text[len(prefix + self.text) + 1 :].split()}
                elif text == prefix + self.text:
                    return True
        return False


class FromChat(ABCRule[MessageUpdate]):
    """
    A rule which checks if the message was sent from a specified chat.
    If it's not, the rule will return False and the message will be ignored.
    """

    def __init__(self, chats: Union[int, List[int]]) -> None:
        self.chats = chats if isinstance(chats, list) else [chats]

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.chat.id in self.chats


class IsReply(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message is a reply.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.reply_to_message is not None


class IsForward(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message was forwarded.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.forward_date is not None


class IsGroup(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message was sent in the chat.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.chat.type in ["group", "supergroup"]


class IsPrivate(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message is private.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.chat.type == "private"


class Length(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message is longer than or equal to the given length.
    """

    def __init__(self, minimum_length: int) -> None:
        self.minimum_length = minimum_length

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False
        return self.minimum_length >= len(text)


class Levenshtein(ABCRule[MessageUpdate]):
    """
    A rule that compares message text with given strings
    using Levenshtein distance algorithm.
    """

    def __init__(
        self, lev_texts: Union[str, List[str]], max_distance: Optional[int] = 1
    ) -> None:
        if isinstance(lev_texts, str):
            lev_texts = [lev_texts]

        self.lev_texts = lev_texts
        self.max_distance = max_distance

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False

        return any(
            self.max_distance >= self.calculate(text, lev_text)
            for lev_text in self.lev_texts
        )

    @classmethod
    def calculate(cls, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            return cls.calculate(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]


class Mention(ABCRule[MessageUpdate]):
    """
    A rule that parses message entities and checks if the message contains mention(-s).
    If it does, the rule will return a list of mentioned usernames.
    """

    async def check(self, msg: MessageUpdate) -> Union[bool, dict]:
        if not msg.entities:
            return False

        m = [
            msg.text[e.offset : e.offset + e.length].strip("@")
            for e in msg.entities
            if e.type == "mention"
        ]

        return {"mentions": m} if m else False


class Regex(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message text matches the given regex.
    """

    def __init__(self, regex: str) -> None:
        self.regex = compile(regex)

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False
        return self.regex.match(text) is not None


class Text(ABCRule[MessageUpdate]):
    """
    A rule that checks if the message text is equal
    to or is in the list of given texts.
    """

    def __init__(
        self, texts: Union[str, List[str]], ignore_case: Optional[bool] = False
    ) -> None:
        if not isinstance(texts, list):
            texts = [texts]

        self.texts = texts
        self.ignore_case = ignore_case

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False

        if self.ignore_case:
            return text.lower() in list(map(str.lower, self.texts))
        return text in self.texts


class VBML(ABCRule[MessageUpdate]):
    """
    This rule matches message text against a list of given patterns
    using VBML. See more details at https://github.com/tesseradecade/vbml
    """

    PatternLike = Union[str, Pattern]

    def __init__(
        self,
        patterns: Union[PatternLike, Iterable[PatternLike]],
        patcher: Optional[Patcher] = Patcher(),
        flags: Optional[RegexFlag] = RegexFlag(0),
    ) -> None:
        if not isinstance(patterns, list):
            patterns = [patterns]

        self.patterns = [
            Pattern(pattern, flags=flags) if isinstance(pattern, str) else pattern
            for pattern in patterns
        ]
        self.patcher = patcher

    async def check(self, msg: MessageUpdate) -> Union[bool, dict]:
        text = msg.text or msg.caption

        if not text:
            return False

        for pattern in self.patterns:
            match = self.patcher.check(pattern, text)

            if match not in (None, False):
                return match
        return False
