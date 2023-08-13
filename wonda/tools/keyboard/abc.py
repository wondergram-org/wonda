from abc import ABC, abstractmethod
from typing import Any


class ABCKeyboardBuilder(ABC):
    """
    A keyboard builder interface.
    """

    @abstractmethod
    def add(self, button: "ABCButton") -> "ABCKeyboardBuilder":
        """
        Adds a button to the keyboard.
        """

    @abstractmethod
    def row(self) -> "ABCKeyboardBuilder":
        """
        Adds a row to the keyboard. Panics if the last row was empty.
        """

    @abstractmethod
    def build(self) -> Any:
        """
        Builds the keyboard.
        """


class ABCButton(ABC):
    @abstractmethod
    def dict(self) -> Any:
        """
        Returns the button data.
        """
