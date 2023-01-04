from wonda.modules import json
from wonda.tools.keyboard.abc import ABCBuilder, BaseButton
from wonda.types.objects import KeyboardButtonPollType, WebAppInfo


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

    def build(self) -> str:
        return json.dumps(
            {
                "keyboard": self.keyboard,
                "is_persistent": self.is_persistent,
                "resize_keyboard": self.resize_keyboard,
                "one_time_keyboard": self.one_time_keyboard,
                "selective": self.selective,
            }
        )


class Contact(BaseButton):
    """
    When pressed, the user's phone number will be sent as a contact.
    Available in private chats only.
    """

    request_contact: bool = True

    def __init__(self, text: str) -> None:
        super().__init__(text)


class Location(BaseButton):
    """
    When pressed, the user's current location will be sent.
    Available in private chats only.
    """

    request_location: bool = True

    def __init__(self, text: str) -> None:
        super().__init__(text)


class Poll(BaseButton):
    """
    When pressed, the user will be asked to create a poll of specified type
    and send it to the bot. Available in private chats only.
    """

    def __init__(self, text: str, request_poll: KeyboardButtonPollType) -> None:
        super().__init__(text)
        self.request_poll = request_poll.dict()


class App(BaseButton):
    """
    This button opens specified web app that will be able to send a “web_app_data”
    service message. Available in private chats only.
    """

    def __init__(self, text: str, web_app: WebAppInfo) -> None:
        super().__init__(text)
        self.web_app = web_app.dict()
