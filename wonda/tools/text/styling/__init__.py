from .abc import ABCStyle
from .chain import StyleChain
from .styles import (
    BlockquoteStyle,
    BoldStyle,
    CodeStyle,
    CustomEmojiStyle,
    ExpandableBlockquoteStyle,
    InlineCodeStyle,
    InlineMentionStyle,
    ItalicStyle,
    LinkStyle,
    MentionStyle,
    PlainStyle,
    SpoilerStyle,
    StrikethroughStyle,
    UnderlineStyle,
)

Plain = PlainStyle
Bold = BoldStyle
Italic = ItalicStyle
Underline = UnderlineStyle
Strikethrough = StrikethroughStyle
Spoiler = SpoilerStyle
Blockquote = BlockquoteStyle
ExpandableBlockquote = ExpandableBlockquoteStyle
InlineCode = InlineCodeStyle
Code = CodeStyle
Link = LinkStyle
InlineMention = InlineMentionStyle
Mention = MentionStyle
CustomEmoji = CustomEmojiStyle
