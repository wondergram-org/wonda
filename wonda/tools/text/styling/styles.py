from typing_extensions import Any, Union

from wonda.tools.text.styling import ABCStyle, StyleChain
from wonda.types.objects import MessageEntity, MessageEntityType, User

_ = Any
Text = Union[str, "ABCStyle"]


class PlainStyle(ABCStyle[MessageEntity]):
    """
    A plain text style. It is ignored by the entity builder but affects text offsets.
    """

    entity_type: MessageEntityType | None = None

    def __init__(self, text: Text) -> None:
        self.text = text

    def __init_subclass__(cls, entity_type: str | None = None) -> None:
        if entity_type is not None:
            cls.entity_type = MessageEntityType(entity_type)

    def __add__(self, style: ABCStyle[MessageEntity]) -> StyleChain[MessageEntity]:
        return StyleChain(self, style)

    def __eq__(self, style: object) -> bool:
        if not isinstance(style, PlainStyle):
            return False

        return type(self) is type(style) and self.to_string() == style.to_string()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"
        )

    def dict(self) -> dict[str, _]:
        return {k: v for k, v in self.__dict__.items() if k != "text"}

    def to_entities(self) -> list[MessageEntity]:
        entities = []

        if self.entity_type is not None:
            entities.append(
                MessageEntity(self.entity_type, 0, len(self.to_string()), **self.dict())
            )

        if isinstance(self.text, ABCStyle):
            entities.extend(self.text.to_entities())

        return entities

    def to_string(self) -> str:
        return self.text.to_string() if isinstance(self.text, ABCStyle) else self.text


class BoldStyle(PlainStyle, entity_type="bold"):
    """
    A bold text style.
    """


class ItalicStyle(PlainStyle, entity_type="italic"):
    """
    An italic text style.
    """


class UnderlineStyle(PlainStyle, entity_type="underline"):
    """
    An underline text style.
    """


class StrikethroughStyle(PlainStyle, entity_type="strikethrough"):
    """
    A strikethrough text style.
    """


class SpoilerStyle(PlainStyle, entity_type="spoiler"):
    """
    A text spoiler.
    """


class BlockquoteStyle(PlainStyle, entity_type="blockquote"):
    """
    A blockquote.
    """


class ExpandableBlockquoteStyle(PlainStyle, entity_type="expandable_blockquote"):
    """
    An expandable blockquote.
    """


class InlineCodeStyle(PlainStyle, entity_type="code"):
    """
    An inline code block.
    """


class CodeStyle(PlainStyle, entity_type="pre"):
    """
    A code block.
    """

    def __init__(self, text: Text, language: str | None = None):
        super().__init__(text)
        self.language = language


class LinkStyle(PlainStyle, entity_type="text_link"):
    """
    A link style.
    """

    def __init__(self, text: Text, url: str):
        super().__init__(text)
        self.url = url


class InlineMentionStyle(LinkStyle):
    """
    An inline mention of a user.
    """

    def __init__(self, text: Text, user_id: int):
        super().__init__(text, f"tg://user?id={user_id}")


class MentionStyle(PlainStyle, entity_type="text_mention"):
    """
    A mention of a user without a username.
    """

    def __init__(self, text: Text, user: User):
        super().__init__(text)
        self.user = user


class CustomEmojiStyle(PlainStyle, entity_type="custom_emoji"):
    """
    A custom emoji style.
    """

    def __init__(self, text: Text, custom_emoji_id: str):
        super().__init__(text)
        self.custom_emoji_id = custom_emoji_id
