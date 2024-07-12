from difflib import SequenceMatcher
from typing import Iterable

from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates import MessageUpdate
from wonda.types.enums import ChatType


class Command(ABCRule[MessageUpdate]):
    """
    Checks if the message contains a command. When the command is found,
    its arguments get stored in the `args` context field.
    """

    def __init__(self, *texts: str, prefixes: Iterable[str] = ("/",)) -> None:
        self.texts, self.prefixes = texts, prefixes

    async def check(self, m: MessageUpdate, ctx: dict) -> bool:
        text = m.text or m.caption

        if not text:
            return False

        prefix, text, _, args = self.parse_cmd(text)

        if prefix not in self.prefixes or text not in self.texts:
            return False

        ctx["args"] = args
        return True

    @staticmethod
    def parse_cmd(text: str) -> tuple[str, str, str, list[str]]:
        head, *tail = text.split()
        pfx, (cmd, _, tag) = head[0], head[1:].partition("@")
        return pfx, cmd, tag, tail


class From(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent from the user or the public chat 
    with given ID or username.
    """

    def __init__(self, *chats: int | str) -> None:
        self.chats = set(chats)

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.chat.id in self.chats or m.chat.username in self.chats


class FromChannel(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent in a channel.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.chat.type == ChatType.CHANNEL


class FromGroup(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent in a group.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)


class FromTopic(ABCRule[MessageUpdate]):
    """
    Checks if the message was sent in a forum topic.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return bool(m.message_thread_id)


class Fuzzy(ABCRule[MessageUpdate]):
    """
    Checks if the message text compares closely with one of the given strings.
    """

    def __init__(self, *texts: str, min_ratio: float = 0.7) -> None:
        self.texts = texts
        self.min_ratio = min_ratio

    async def check(self, m: MessageUpdate, _) -> bool:
        text = m.text or m.caption

        if not text:
            return False

        closest = max(self.get_string_similarity_ratio(t, text) for t in self.texts)
        return closest >= self.min_ratio

    @staticmethod
    def get_string_similarity_ratio(a: str, b: str) -> float:
        return SequenceMatcher(isjunk=None, a=a, b=b).ratio()


class HasMediaSpoiler(ABCRule[MessageUpdate]):
    """
    Checks if the message has media that was marked with a spoiler.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return bool(m.has_media_spoiler)


class HasProtectedContent(ABCRule[MessageUpdate]):
    """
    Checks if the message has protected content and can't be forwarded.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return bool(m.has_protected_content)


class IsAutomaticForward(ABCRule[MessageUpdate]):
    """
    Checks if the message is a channel post automatically forwarded to 
    the connected discussion group.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return bool(m.is_automatic_forward)


class IsForward(ABCRule[MessageUpdate]):
    """
    Checks if the message was forwarded.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return bool(m.forward_origin)


class IsReply(ABCRule[MessageUpdate]):
    """
    Checks if the message is a reply.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return bool(m.reply_to_message)


class IsPrivate(ABCRule[MessageUpdate]):
    """
    Checks if the message is private.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.chat.type == ChatType.PRIVATE


class IsSuccessfulPayment(ABCRule[MessageUpdate]):
    """
    Checks if the message is a service message about a successful payment.
    """
    async def check(self, m: MessageUpdate, _) -> bool:
        return m.successful_payment is not None


class WasEdited(ABCRule[MessageUpdate]):
    """
    Checks if the message was edited.
    """

    async def check(self, m: MessageUpdate, _) -> bool:
        return m.edit_date is not None


__all__ = (
    "Command",
    "From",
    "FromChannel",
    "FromGroup",
    "FromTopic",
    "Fuzzy",
    "HasMediaSpoiler",
    "HasProtectedContent",
    "IsAutomaticForward",
    "IsForward",
    "IsReply",
    "IsPrivate",
    "IsSuccessfulPayment",
    "WasEdited",
)
