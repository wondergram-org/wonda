from abc import ABC, abstractmethod
from typing import Any, Self


class ABCKeyboardBuilder(ABC):
    """
    A keyboard builder interface.
    """

    @abstractmethod
    def add(self, button: "ABCButton") -> Self:
        """
        Adds a button to the keyboard.
        """
        pass

    @abstractmethod
    def row(self) -> Self:
        """
        Adds a row to the keyboard. Panics if the last row was empty.
        """
        pass

    @abstractmethod
    def build(self) -> Any:
        """
        Builds the keyboard.
        """
        pass


class ABCButton(ABC):
    @abstractmethod
    def dict(self) -> Any:
        """
        Returns the button data.
        """
        pass
