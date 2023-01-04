from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseButton:
    """
    A text-only keyboard button interface.
    All other keyboard button types should inherit this class.
    """

    def __init__(self, text: str) -> None:
        self.text = text

    def get_data(self) -> dict:
        """
        Returns the button data.
        """
        return {k: v for k, v in self.__dict__.items() if v is not None}


class ABCBuilder(ABC):
    """
    An abstract keyboard builder interface.
    """

    buttons: List[List[BaseButton]]

    @abstractmethod
    def build(self) -> str:
        """
        Builds the keyboard.
        """
        pass

    @classmethod
    def empty(cls) -> str:
        """
        Returns an empty keyboard.
        """
        return cls().build()

    def add(self, button: BaseButton) -> "ABCBuilder":
        """
        Adds a button to the keyboard.
        """
        if not len(self.buttons):
            self.row()

        self.last_row.append(button)
        return self

    def row(self) -> "ABCBuilder":
        """
        Adds a row to the keyboard.
        Panics if the last row was empty.
        """
        if len(self.buttons) and not len(self.last_row):
            raise ValueError("Last row is empty")

        self.buttons.append([])
        return self

    def merge(self, builder: "ABCBuilder") -> "ABCBuilder":
        self.buttons.extend(builder.buttons)
        return self

    @property
    def last_row(self) -> List[BaseButton]:
        """
        Convenience property to get the last button row.
        """
        return self.buttons[-1]

    @property
    def keyboard(self) -> List[List[Dict[str, Any]]]:
        """
        Convenience property to get the keyboard data.
        """
        return [[button.get_data() for button in row] for row in self.buttons]

    def __repr__(self) -> str:
        return self.build()
