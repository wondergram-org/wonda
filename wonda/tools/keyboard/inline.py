from wonda.tools.keyboard.abc import ABCBuilder, Button
from wonda.types.objects import CallbackGame, InlineKeyboardMarkup, LoginUrl, WebAppInfo


class InlineKeyboard(ABCBuilder):
    """
    A builder for an inline keyboard.
    No options are available for this type of keyboard.
    """

    def __init__(self) -> None:
        self.buttons = [[]]

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=self.keyboard)


class App(Button):
    """
    This button opens specified web app which will be able to send
    an arbitrary message on behalf of the user using the method `answerWebAppQuery`.
    Available only in private chats between a user and the bot.
    """

    def __init__(self, text: str, web_app: WebAppInfo) -> None:
        super().__init__(text)
        self.web_app = web_app


class Callback(Button):
    """
    A button that sends a callback query to the bot when pressed.
    """

    def __init__(self, text: str, data: str) -> None:
        super().__init__(text)
        self.callback_data = data


class Game(Button):
    """
    This button will launch a game in the chat when pressed.
    This type of button must always be the first button in the first row.
    """

    def __init__(self, text: str, game: CallbackGame) -> None:
        super().__init__(text)
        self.callback_game = game


class Login(Button):
    """
    A button containing a login URL. This button will open a web page
    with the specified URL and ask the user to log in. Can be used
    as a replacement for the Telegram Login Widget.
    """

    def __init__(self, text: str, login_url: LoginUrl) -> None:
        super().__init__(text)
        self.login_url = login_url


class Pay(Button):
    """
    A pay button. This type of button must always be the first button
    in the first row and can only be used in invoice messages.
    """

    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.pay = True


class Switch(Button):
    """
    Pressing the button will open specified inline query in the chat,
    either current or selected by the user.
    """

    def __init__(self, text: str, query: str, current_chat: bool = False) -> None:
        super().__init__(text)

        setattr(
            self,
            "switch_inline_query_current_chat"
            if current_chat
            else "switch_inline_query",
            query,
        )


class URL(Button):
    """
    When this button is pressed, HTTP or tg:// link is opened.
    """

    def __init__(self, text: str, url: str) -> None:
        super().__init__(text)
        self.url = url
