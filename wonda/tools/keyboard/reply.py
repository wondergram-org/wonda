from wonda.tools.keyboard.abc import ABCBuilder, Button
from wonda.types.objects import (
    ChatAdministratorRights,
    KeyboardButtonPollType,
    KeyboardButtonRequestChat,
    KeyboardButtonRequestUser,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    WebAppInfo,
)


class ReplyKeyboard(ABCBuilder):
    """
    A builder for reply keyboard markup.
    """

    def __init__(
        self,
        is_persistent: bool = False,
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
        selective: bool = False,
    ) -> None:
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.buttons = [[]]

    def build(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=self.keyboard,
            is_persistent=self.is_persistent,
            resize_keyboard=self.resize_keyboard,
            one_time_keyboard=self.one_time_keyboard,
            selective=self.selective,
        )

    @staticmethod
    def remove(selective: bool = None) -> ReplyKeyboardRemove:
        """
        A shortcut to remove a reply keyboard.
        """
        return ReplyKeyboardRemove(selective=selective, remove_keyboard=True)


class App(Button):
    """
    This button opens specified web app that will be able to send a “web_app_data”
    service message. Available in private chats only.
    """

    def __init__(self, text: str, web_app: WebAppInfo) -> None:
        super().__init__(text)
        self.web_app = web_app


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


class RequestUser(Button):
    """
    Pressing the button will open a list of users suitable for given criteria.
    Tapping on any user will send their identifier to the bot in a "user_shared"
    service message. Available in private chats only.
    """

    def __init__(
        self,
        text: str,
        request_id: int = None,
        is_bot: bool = None,
        is_premium: bool = None,
    ) -> None:
        super().__init__(text)
        self.request_user = KeyboardButtonRequestUser(
            request_id=request_id, user_is_bot=is_bot, user_is_premium=is_premium
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
        is_forum: bool = None,
        has_username: bool = None,
        is_created: bool = None,
        user_administrator_rights: ChatAdministratorRights = None,
        bot_administrator_rights: ChatAdministratorRights = None,
        bot_is_member: bool = None,
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
        )
