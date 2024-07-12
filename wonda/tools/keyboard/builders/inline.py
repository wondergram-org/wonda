from wonda.tools.keyboard.base import BaseKeyboardBuilder
from wonda.tools.keyboard.elements import Callback
from wonda.types.objects import InlineKeyboardButton, InlineKeyboardMarkup


class InlineKeyboardBuilder(BaseKeyboardBuilder[InlineKeyboardButton]):
    """
    An inline keyboard builder. No options are available
    for this type of keyboard.
    """

    button_type = InlineKeyboardButton

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self.keyboard)


class PaginatedInlineKeyboardBuilder(InlineKeyboardBuilder):
    """
    A paginated inline keyboard builder.
    """

    def __init__(
        self, *, total_pages: int, current_page: int, callback_pattern: str
    ) -> None:
        super().__init__()
        self.total_pages = total_pages
        self.current_page = current_page
        self.callback_pattern = callback_pattern

        if self.total_pages < 1:
            raise ValueError("Value of `total_pages` should be at least 1")

        if self.current_page > self.total_pages or self.current_page <= 0:
            raise ValueError(
                "Current page value must be greater than zero and less than `total_pages`"
            )

    def build(self) -> InlineKeyboardMarkup:
        if self.last_row:
            self.row()

        if self.current_page > 1:
            self.add(Callback("«", self.callback_pattern.format(self.current_page - 1)))

        self.add(
            Callback(
                f"· {self.current_page} ·",
                self.callback_pattern.format(self.current_page),
            )
        )

        if self.current_page < self.total_pages:
            self.add(Callback("»", self.callback_pattern.format(self.current_page + 1)))

        return super().build()
