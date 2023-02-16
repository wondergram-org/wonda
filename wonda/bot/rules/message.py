import re
from difflib import SequenceMatcher
from typing import List, Tuple, Union

from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates import MessageUpdate
from wonda.types.enums import ChatType, MessageEntityType


class Command(ABCRule[MessageUpdate]):
    """
    A rule that handles bot commands. It takes in a list of
    valid command texts and checks if the message
    contains one of those commands.
    """

    def __init__(
        self, texts: Union[str, List[str]], prefixes: Union[str, List[str]] = "/"
    ) -> None:
        self.texts = texts if isinstance(texts, list) else [texts]
        self.prefixes = prefixes if isinstance(prefixes, list) else [prefixes]

    async def check(self, msg: MessageUpdate) -> Union[bool, dict]:
        if text := msg.text or msg.caption:
            prefix, text, tag, args = self.parse(text)

            if msg.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                bot = await msg.ctx_api.get_me()

                if tag and tag.lower() != bot.username.lower():
                    return False

            if prefix not in self.prefixes or text not in self.texts:
                return False

            return {"args": args}

    @staticmethod
    def parse(text: str) -> Tuple[str]:
        head, *tail = text.split()
        pfx, (cmd, _, tag) = head[0], head[1:].partition("@")
        return pfx, cmd, tag, tail


class From(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent from user or public chat
    with given username(-s).
    """

    def __init__(self, chats: Union[str, List[str]]) -> None:
        self.chats = chats if isinstance(chats, list) else [chats]

    async def check(self, msg: MessageUpdate) -> bool:
        return bool(set(self.chats) & {msg.chat.username, msg.from_.username})


class Fuzzy(ABCRule[MessageUpdate]):
    """
    Compares message text with the given text
    and returns the closest match.
    """

    def __init__(self, texts: Union[str, List[str]], min_ratio: int = 0.7) -> None:
        self.texts = texts if isinstance(texts, list) else [texts]
        self.min_ratio = min_ratio

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False

        closest = max(SequenceMatcher(None, t, text).ratio() for t in self.texts)
        return closest >= self.min_ratio


class IsReply(ABCRule[MessageUpdate]):
    """
    Checks if the message is a reply.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.reply_to_message is not None


class IsForward(ABCRule[MessageUpdate]):
    """
    Checks if the message was forwarded.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.forward_date is not None


class IsGroup(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent in the chat.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]


class IsPrivate(ABCRule[MessageUpdate]):
    """
    Checks if the message is private.
    """

    async def check(self, msg: MessageUpdate) -> bool:
        return msg.chat.type == ChatType.PRIVATE


class Length(ABCRule[MessageUpdate]):
    """
    Checks if the message is longer than or equal to the given length.
    """

    def __init__(self, min_length: int) -> None:
        self.min_length = min_length

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False

        return len(text) >= self.min_length


class Mention(ABCRule[MessageUpdate]):
    """
    Parses message entities and checks if the message contains mention(-s).
    Returns a list of mentioned usernames.
    """

    async def check(self, msg: MessageUpdate) -> Union[bool, dict]:
        if not msg.entities:
            return False

        mentions = [
            msg.text[e.offset : e.offset + e.length].strip("@")
            for e in msg.entities
            if e.type == MessageEntityType.MENTION
        ]

        return {"mentions": mentions}


class Regex(ABCRule[MessageUpdate]):
    """
    Checks if the message text matches the given regex.
    """

    PatternLike = Union[str, re.Pattern]

    def __init__(self, expr: Union[PatternLike, List[PatternLike]]) -> None:
        if isinstance(expr, re.Pattern):
            expr = [expr]
        elif isinstance(expr, str):
            expr = [compile(expr)]
        else:
            expr = [compile(e) if isinstance(e, str) else e for e in expr]

        self.expr = expr

    async def check(self, msg: MessageUpdate) -> bool:
        text = msg.text or msg.caption

        if not text:
            return False

        for e in self.expr:
            if result := re.match(e, text):
                return {"match": result.groups()}

        return False
