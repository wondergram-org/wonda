from typing_extensions import Any, Generic, Self, TypeVar

from wonda.tools.keyboard.abc import ABCButton, ABCKeyboardBuilder
from wonda.types.objects import InlineKeyboardButton, KeyboardButton

_ = Any
B = TypeVar("B", bound=InlineKeyboardButton | KeyboardButton)


class BaseKeyboardBuilder(ABCKeyboardBuilder, Generic[B]):
    """
    A basic keyboard builder which implements independent logic for
    `.add()` and `.row()` methods
    """

    button_type: type[B]

    def __init__(self) -> None:
        self.rows: list[list[ABCButton]] = [[]]

    @property
    def keyboard(self) -> list[list[B]]:
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

    def add(self, button: ABCButton) -> Self:
        if not len(self.rows):
            self.row()

        self.last_row.append(button)
        return self

    def row(self) -> Self:
        if len(self.rows) and not len(self.last_row):
            raise ValueError("Last row is empty")

        self.rows.append([])
        return self

    def merge(self, builder: Self) -> Self:
        self.rows.extend(builder.rows)
        return self

    def adjust(self, width: int = 0) -> Self:
        assert width > 0, "Width must be greater than 0"
        buttons = [button for row in self.rows for button in row]

        self.rows = [buttons[i : i + width] for i in range(0, len(buttons), width)]
        return self

    def build(self) -> _:
        raise NotImplementedError(
            "Implementation of `.build()` is absent. Use keyboard builders "
            "that have this method implemented, like `ReplyKeyboardBuilder` "
            "or `InlineKeyboardBuilder`"
        )
