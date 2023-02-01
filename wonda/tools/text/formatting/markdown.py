MARKDOWN_ESCAPE_SYMBOLS = {
    "*": "\\*",
    "[": "\\[",
    "]": "\\]",
    "(": "\\(",
    ")": "\\)",
    "~": "\\~",
    "`": "\\`",
    ">": "\\>",
    "#": "\\#",
    "+": "\\+",
    "-": "\\-",
    "=": "\\=",
    "|": "\\|",
    "{": "\\{",
    "}": "\\}",
    ".": "\\.",
    "!": "\\!",
}


def bold(string: str) -> str:
    """
    Applies the bold font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    return f"*{string}*"


def italic(string: str) -> str:
    """
    Applies the italic font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    if string.startswith("__") and string.endswith("__"):
        return f"_{string[:len(string) - 1]}\r__"
    return f"_{string}_"


def underline(string: str) -> str:
    """
    Applies the underline font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    if string.startswith("_") and string.endswith("_"):
        return f"__{string}\r__"

    return f"__{string}__"


def strike(string: str) -> str:
    """
    Applies the strikethrough font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    return f"~{string}~"


def link(text: str, link: str) -> str:
    """
    Builds an inline link with an anchor.
    Escapes parentheses and backtick characters inside the URL.
    """
    return f"[{escape(text)}]({escape_link_url(link)})"


def mention(text: str, user_id: int) -> str:
    return link(text, f"tg://user?id={user_id}")


def code_block(code: str):
    """
    Formats the code block.
    Escapes ``` and `\` characters inside the block.
    """
    return f"```\n{escape_code(code)}\n```"


def code_block_with_lang(code: str, lang: str):
    """
    Formats the code block with a specific language syntax.
    Escapes ``` and `\` characters inside the block.
    """
    return f"```{escape(lang)}\n{escape_code(code)}\n```"


def code_inline(string: str):
    """
    Formats the string as an inline code.
    Escapes ``` and `\` characters inside the block.
    """
    return f"`{escape_code(string)}`"


def spoiler(string: str) -> str:
    """
    Formats the string as a spoiler.
    """
    return f"||{string}||"


def escape(string: str) -> str:
    for k, v in MARKDOWN_ESCAPE_SYMBOLS.items():
        string = string.replace(k, v)
    return string


def escape_code(string: str) -> str:
    return string.replace("\\", "\\\\").replace("`", "\\`")


def escape_link_url(string: str):
    return string.replace("`", "\\`").replace(")", "\\)")
