def bold(string: str) -> str:
    """
    Applies the bold font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    return f"<b>{string}</b>"


def italic(string: str) -> str:
    """
    Applies the italic font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    return f"<i>{string}</i>"


def underline(string: str) -> str:
    """
    Applies the underline font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    return f"<u>{string}</u>"


def strike(string: str) -> str:
    """
    Applies the strikethrough font style to the string.
    The resulting string will not be automatically escaped
    because it can contain nested markup.
    """
    return f"<s>{string}</s>"


def link(text: str, link: str) -> str:
    """
    Builds an inline link with an anchor.
    Escapes the passed URL and the link text.
    """
    return f'<a href="{escape(link)}">{escape(text)}</a>'


def mention(text: str, user_id: int) -> str:
    return link(text, f"tg://user?id={user_id}")


def code_block(code: str) -> str:
    """
    Formats the code block.
    Escapes HTML characters inside the block.
    """
    return f"<pre>{escape(code)}</pre>"


def code_block_with_lang(code: str, lang: str) -> str:
    lang = escape(lang).replace('"', "&quot;")
    return f'<pre><code class="language-{lang}">{escape(code)}</code></pre>'


def code_inline(string: str) -> str:
    """
    Formats the string as an inline code.
    Escapes HTML characters inside the block.
    """
    return f"<code>{escape(string)}</code>"


def spoiler(string: str) -> str:
    """
    Formats the string as a spoiler.
    """
    return f"<tg-spoiler>{string}</tg-spoiler>"


def escape(string: str) -> str:
    """
    Escapes the string as per Telegram HTML message style.
    Doesn't escape single and double quotes because they shouldn't
    be escaped by the spec.
    """
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
