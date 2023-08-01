from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from wonda.bot.dispatch.view import ABCView
    from wonda.bot.updates import MessageUpdate

LabeledMessageHandler = Callable[..., Callable[["MessageUpdate"], Any]]
LabeledHandler = Callable[..., Callable[[Any], Any]]


class ABCDispatcher(ABC):
    @abstractmethod
    def views(self) -> dict[str, "ABCView"]:
        pass

    @abstractmethod
    def load(self, dispatcher: Any) -> None:
        pass
