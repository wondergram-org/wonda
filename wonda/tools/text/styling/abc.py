from abc import ABC, abstractmethod

from typing_extensions import TYPE_CHECKING, Generic, TypeVar, Union

from wonda.types.objects import MessageEntity

if TYPE_CHECKING:
    from wonda.tools.text.styling.chain import StyleChain

E = TypeVar("E", bound="MessageEntity")
Text = Union[str, "ABCStyle"]


class ABCStyle(ABC, Generic[E]):
    @abstractmethod
    def __add__(self, style: "ABCStyle[E]") -> "StyleChain[E]":
        """
        Combine two styles together. Returns a chain.
        """

    @abstractmethod
    def to_entities(self) -> list[E]:
        """
        Convert a style to a list of entity objects.
        """

    @abstractmethod
    def to_string(self) -> str:
        """
        Get the underlying text of a style.
        """
