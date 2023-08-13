from typing import Any

from wonda.tools.keyboard.abc import ABCButton, ABCKeyboardBuilder
from wonda.types.objects import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

_ = Any


class BaseKeyboardBuilder(ABCKeyboardBuilder):
    """
    A basic keyboard builder which implements independent logic for
    `.add()` and `.row()` methods
    """

    button_type: _

    def __init__(self) -> None:
        self.rows: list[list[ABCButton]] = [[]]

    @property
    def keyboard(self) -> list[list[_]]:
        """
        Keyboard markup to be sent.
        """
        return [
            [self.button_type(**button.dict()) for button in row] for row in self.rows
        ]

    @property
    def last_row(self) -> list[ABCButton]:
        """
        Convenience property to get the last button row.
        """
        return self.rows[-1]

    def add(self, button: ABCButton) -> "BaseKeyboardBuilder":
        if not len(self.rows):
            self.row()

        self.last_row.append(button)
        return self

    def row(self) -> "BaseKeyboardBuilder":
        if len(self.rows) and not len(self.last_row):
            raise ValueError("Last row is empty")

        self.rows.append([])
        return self

    def build(self) -> _:
        raise NotImplementedError("`.build()` method implemenation is builder specific")


class InlineKeyboardBuilder(BaseKeyboardBuilder):
    """
    A builder for an inline keyboard. No options are available
    for this type of keyboard.
    """

    button_type = InlineKeyboardButton

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self.keyboard)


class ReplyKeyboardBuilder(BaseKeyboardBuilder):
    """
    A builder for a keyboard with custom reply options.
    """

    button_type = KeyboardButton

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
        self.rows = [[]]

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
