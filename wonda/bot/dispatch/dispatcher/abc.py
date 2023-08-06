from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wonda.bot.dispatch.view import ABCView


class ABCDispatcher(ABC):
    @abstractmethod
    def views(self) -> dict[str, "ABCView"]:
        pass

    @abstractmethod
    def load(self, dispatcher: "ABCDispatcher") -> None:
        pass
