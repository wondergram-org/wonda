from wonda.tools.keyboard.base import BaseKeyboardBuilder
from wonda.types.objects import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


class ReplyKeyboardBuilder(BaseKeyboardBuilder[KeyboardButton]):
    """
    A builder for a keyboard with custom reply options.
    """

    button_type = KeyboardButton

    def __init__(
        self,
        *,
        is_persistent: bool | None = None,
        resize_keyboard: bool | None = None,
        one_time_keyboard: bool | None = None,
        selective: bool | None = None,
    ) -> None:
        super().__init__()
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    def build(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=self.keyboard,
            is_persistent=self.is_persistent,
            resize_keyboard=self.resize_keyboard,
            one_time_keyboard=self.one_time_keyboard,
            selective=self.selective,
        )

    @staticmethod
    def remove(selective: bool | None = None) -> ReplyKeyboardRemove:
        """
        A shortcut to remove a reply keyboard.
        """
        return ReplyKeyboardRemove(selective=selective, remove_keyboard=True)
