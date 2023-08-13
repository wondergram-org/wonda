from difflib import SequenceMatcher
from re import Pattern, compile, match

from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates import MessageUpdate
from wonda.types.enums import ChatType, MessageEntityType
from wonda.types.objects import User


class Command(ABCRule[MessageUpdate]):
    """
    A rule that handles bot commands. It takes in a list of
    valid command texts and checks if the message
    contains one of those commands.
    """

    me: User | None = None

    def __init__(self, texts: str | list[str], prefixes: str | list[str] = "/") -> None:
        self.texts = texts if isinstance(texts, list) else [texts]
        self.prefixes = prefixes if isinstance(prefixes, list) else [prefixes]

    async def check(self, m: MessageUpdate, ctx: dict) -> bool:
        if text := m.text or m.caption:
            prefix, text, tag, args = self.parse(text)

            if m.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                # Make a one-time request to get the bot info
                # so we can compare it's short name to the tag
                # contained in the command.
                self.me = self.me or await m.ctx_api.get_me()

                if not tag or tag.lower() != self.me.username.lower():  # type: ignore
                    return False

            if prefix not in self.prefixes or text not in self.texts:
                return False

            ctx["args"] = args
            return True
        return False

    @staticmethod
    def parse(text: str):
        head, *tail = text.split()
        pfx, (cmd, _, tag) = head[0], head[1:].partition("@")
        return pfx, cmd, tag, tail


class From(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent from user or public chat
    with given username(-s).
    """

    def __init__(self, usernames: str | list[str]) -> None:
        self.usernames = usernames if isinstance(usernames, list) else [usernames]

    async def check(self, m: MessageUpdate, _) -> bool:
        username = m.from_.username if m.from_ is not None else m.chat.username
        return username in self.usernames


class Fuzzy(ABCRule[MessageUpdate]):
    """
    Compares message text with the given text
    and returns the closest match.
    """

    def __init__(self, texts: str | list[str], min_ratio: float = 0.7) -> None:
        self.texts = texts if isinstance(texts, list) else [texts]
        self.min_ratio = min_ratio

    async def check(self, m: MessageUpdate, _) -> bool:
        text = m.text or m.caption

        if not text:
            return False

        closest = max(SequenceMatcher(None, t, text).ratio() for t in self.texts)
        return closest >= self.min_ratio


class IsReply(ABCRule[MessageUpdate]):
    """
    Checks if the message is a reply.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.reply_to_message is not None


class IsForward(ABCRule[MessageUpdate]):
    """
    Checks if the message was forwarded.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.forward_date is not None


class FromGroup(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent in a group.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)


class IsPrivate(ABCRule[MessageUpdate]):
    """
    Checks if the message is private.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.chat.type == ChatType.PRIVATE


class Length(ABCRule[MessageUpdate]):
    """
    Checks if the message is longer than or equal to the given length.
    """

    def __init__(self, min_length: int) -> None:
        self.min_length = min_length

    async def check(self, m: MessageUpdate, _) -> bool:
        text = m.text or m.caption

        if not text:
            return False

        return len(text) >= self.min_length


class Mention(ABCRule[MessageUpdate]):
    """
    Parses message entities and checks if the message contains mention(-s).
    Returns a list of mentioned usernames.
    """

    async def check(self, m: MessageUpdate, ctx: dict) -> bool:
        text = m.text or m.caption
        entities = m.entities or m.caption_entities

        if entities is None or text is None:
            return False

        mentions = [
            text[e.offset : e.offset + e.length].strip("@")
            for e in entities
            if e.type == MessageEntityType.MENTION
        ]

        ctx["mentions"] = mentions
        return True


PatternLike = str | Pattern


class Regex(ABCRule[MessageUpdate]):
    """
    Checks if the message text matches the given regex.
    """

    def __init__(self, expr: PatternLike | list[PatternLike]) -> None:
        self.expr: list[Pattern[str]] = []

        match expr:
            case Pattern() as p:
                self.expr += [p]
            case str(p):
                self.expr += [compile(p)]
            case _:
                self.expr += [
                    compile(expr) if isinstance(expr, str) else e for e in expr  # type: ignore
                ]

    async def check(self, m: MessageUpdate, ctx: dict) -> bool:
        text = m.text or m.caption

        if not text:
            return False

        for e in self.expr:
            if result := match(e, text):
                ctx["match"] = result.groups()
                return True

        return False


class WasEdited(ABCRule[MessageUpdate]):
    """
    Checks if the message was edited.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.edit_date is not None
