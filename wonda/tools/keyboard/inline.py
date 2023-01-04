from wonda.modules import json
from wonda.tools.keyboard.abc import ABCBuilder, BaseButton
from wonda.types.objects import CallbackGame, LoginUrl, WebAppInfo


class InlineKeyboard(ABCBuilder):
    """
    A builder for an inline keyboard.
    No options are available for this type of keyboard.
    """

    def __init__(self) -> None:
        self.buttons = [[]]

    def build(self) -> str:
        return json.dumps({"inline_keyboard": self.keyboard})


class Pay(BaseButton):
    """
    A pay button. This type of button must always be the first button
    in the first row and can only be used in invoice messages.
    """

    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.pay = True


class URL(BaseButton):
    """
    When this button is pressed, HTTP or tg:// link is opened.
    """

    def __init__(self, text: str, url: str) -> None:
        super().__init__(text)
        self.url = url


class Callback(BaseButton):
    """
    A button that sends a callback query to the bot when pressed.
    """

    def __init__(self, text: str, callback_data: str) -> None:
        super().__init__(text)
        self.callback_data = callback_data


class App(BaseButton):
    """
    This button opens specified web app which will be able to send
    an arbitrary message on behalf of the user using the method answerWebAppQuery.
    Available only in private chats between a user and the bot.
    """

    def __init__(self, text: str, web_app: WebAppInfo) -> None:
        super().__init__(text)
        self.web_app = web_app.dict()


class Login(BaseButton):
    """
    A button containing a login URL. This button will open a web page
    with the specified URL and ask the user to log in. Can be used
    as a replacement for the Telegram Login Widget.
    """

    def __init__(self, text: str, login_url: LoginUrl) -> None:
        super().__init__(text)
        self.login_url = login_url.dict()


class Switch(BaseButton):
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


class Game(BaseButton):
    """
    This button will launch a game in the chat when pressed.
    This type of button must always be the first button in the first row.
    """

    def __init__(self, text: str, callback_game: CallbackGame) -> None:
        super().__init__(text)
        self.callback_game = callback_game.dict()
