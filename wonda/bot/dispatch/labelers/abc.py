from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Union

if TYPE_CHECKING:
    from wonda.bot.dispatch.view import ABCView
    from wonda.bot.rules import ABCRule
    from wonda.bot.updates import BaseBotUpdate, BotUpdateType, MessageUpdate

LabeledMessageHandler = Callable[..., Callable[["MessageUpdate"], Any]]
LabeledHandler = Callable[..., Callable[[Any], Any]]


class ABCLabeler(ABC):
    @abstractmethod
    def message(self, *rules: "ABCRule") -> "LabeledMessageHandler":
        pass

    @abstractmethod
    def chat_message(self, *rules: "ABCRule") -> "LabeledMessageHandler":
        pass

    @abstractmethod
    def private_message(self, *rules: "ABCRule") -> "LabeledMessageHandler":
        pass

    @abstractmethod
    def raw_update(
        self,
        update: Union["BotUpdateType", List["BotUpdateType"]],
        dataclass: "BaseBotUpdate",
        *rules: "ABCRule",
        **custom_rules,
    ) -> "LabeledHandler":
        pass

    @abstractmethod
    def views(self) -> Dict[str, "ABCView"]:
        pass

    @abstractmethod
    def load(self, labeler: "ABCLabeler") -> None:
        pass
