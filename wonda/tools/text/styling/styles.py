from typing_extensions import Any, Union

from wonda.tools.text.styling import ABCStyle, StyleChain
from wonda.types.objects import MessageEntity, MessageEntityType, User

_ = Any
Text = Union[str, "ABCStyle"]


class TextStyle(ABCStyle[MessageEntity]):
    entity_type: MessageEntityType | None = None

    def __init__(self, text: Text) -> None:
        self.text = text

    def __init_subclass__(cls, entity_type: str | None = None) -> None:
        if entity_type is not None:
            cls.entity_type = MessageEntityType(entity_type)

    def __add__(self, style: ABCStyle[MessageEntity]) -> StyleChain[MessageEntity]:
        return StyleChain(self, style)

    def __eq__(self, style: object) -> bool:
        if not isinstance(style, TextStyle):
            return False

        return type(self) is type(style) and self.to_string() == style.to_string()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"

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


class PlainStyle(TextStyle):
    """
    A plain text style. It is ignored by the entity builder but affects text offsets.
    """


class BoldStyle(TextStyle, entity_type="bold"):
    """
    A bold text style.
    """


class ItalicStyle(TextStyle, entity_type="italic"):
    """
    An italic text style.
    """


class UnderlineStyle(TextStyle, entity_type="underline"):
    """
    An underline text style.
    """


class StrikethroughStyle(TextStyle, entity_type="strikethrough"):
    """
    A strikethrough text style.
    """


class SpoilerStyle(TextStyle, entity_type="spoiler"):
    """
    A text spoiler.
    """


class BlockquoteStyle(TextStyle, entity_type="blockquote"):
    """
    A blockquote.
    """


class ExpandableBlockquoteStyle(TextStyle, entity_type="expandable_blockquote"):
    """
    An expandable blockquote.
    """


class InlineCodeStyle(TextStyle, entity_type="code"):
    """
    An inline code block.
    """


class CodeStyle(TextStyle, entity_type="pre"):
    """
    A code block.
    """

    def __init__(self, text: Text, language: str | None = None):
        super().__init__(text)
        self.language = language


class LinkStyle(TextStyle, entity_type="text_link"):
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


class MentionStyle(TextStyle, entity_type="text_mention"):
    """
    A mention of a user without a username.
    """

    def __init__(self, text: Text, user: User):
        super().__init__(text)
        self.user = user


class CustomEmojiStyle(TextStyle, entity_type="custom_emoji"):
    """
    A custom emoji style.
    """

    def __init__(self, text: Text, custom_emoji_id: str):
        super().__init__(text)
        self.custom_emoji_id = custom_emoji_id
