from wonda.tools.keyboard.abc import ABCButton
from wonda.types.objects import (
    CallbackGame,
    ChatAdministratorRights,
    KeyboardButtonPollType,
    KeyboardButtonRequestChat,
    KeyboardButtonRequestUsers,
    LoginUrl,
    WebAppInfo,
)


class Button(ABCButton):
    """
    A basic text button.
    """

    def __init__(self, text: str) -> None:
        self.text = text

    def dict(self) -> dict:
        """
        Returns the button data.
        """
        return {k: v for k, v in self.__dict__.items() if v is not None}


class App(Button):
    """
    This button opens specified web app which will be able to send an arbitrary message
    on behalf of the user using the method `answerWebAppQuery`. Available only
    in private chats between a user and the bot.
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
            (
                "switch_inline_query_current_chat"
                if current_chat
                else "switch_inline_query"
            ),
            query,
        )


class URL(Button):
    """
    When this button is pressed, HTTP or tg:// link is opened.
    """

    def __init__(self, text: str, url: str) -> None:
        super().__init__(text)
        self.url = url


class Contact(Button):
    """
    When pressed, the user's phone number will be sent as a contact.
    Available in private chats only.
    """

    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.request_contact = True


class Location(Button):
    """
    When pressed, the user's current location will be sent.
    Available in private chats only.
    """

    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.request_location = True


class Poll(Button):
    """
    When pressed, the user will be asked to create a poll of specified type
    and send it to the bot. Available in private chats only.
    """

    def __init__(self, text: str, type: str) -> None:
        super().__init__(text)
        self.request_poll = KeyboardButtonPollType(type=type)


class RequestUsers(Button):
    """
    Pressing the button will open a list of users suitable for given criteria.
    Tapping on any user will send their identifier to the bot in a "user_shared"
    service message. Available in private chats only.
    """

    def __init__(
        self,
        text: str,
        request_id: int,
        is_bot: bool | None = None,
        is_premium: bool | None = None,
        max_quantity: int | None = None,
        request_name: bool | None = None,
        request_username: bool | None = None,
        request_photo: bool | None = None,
    ) -> None:
        super().__init__(text)
        self.request_users = KeyboardButtonRequestUsers(
            request_id=request_id,
            max_quantity=max_quantity,
            user_is_bot=is_bot,
            user_is_premium=is_premium,
            request_name=request_name,
            request_username=request_username,
            request_photo=request_photo,
        )


class RequestChat(Button):
    """
    Pressing the button will open a list of chats suitable for given criteria.
    Tapping on any chat will send its identifier to the bot in a "chat_shared"
    service message. Available in private chats only.
    """

    def __init__(
        self,
        text: str,
        request_id: int,
        is_channel: bool,
        is_forum: bool | None = None,
        has_username: bool | None = None,
        is_created: bool | None = None,
        user_administrator_rights: "ChatAdministratorRights | None" = None,
        bot_administrator_rights: "ChatAdministratorRights | None" = None,
        bot_is_member: bool | None = None,
        request_title: bool | None = None,
        request_username: bool | None = None,
        request_photo: bool | None = None,
    ) -> None:
        super().__init__(text)
        self.request_chat = KeyboardButtonRequestChat(
            request_id=request_id,
            chat_is_channel=is_channel,
            chat_is_forum=is_forum,
            chat_has_username=has_username,
            chat_is_created=is_created,
            user_administrator_rights=user_administrator_rights,
            bot_administrator_rights=bot_administrator_rights,
            bot_is_member=bot_is_member,
            request_title=request_title,
            request_username=request_username,
            request_photo=request_photo,
        )


__all__ = (
    "URL",
    "App",
    "Button",
    "Callback",
    "Contact",
    "Game",
    "Location",
    "Login",
    "Pay",
    "Poll",
    "RequestChat",
    "RequestUsers",
    "Switch",
)
