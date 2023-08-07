from abc import ABC, abstractmethod

from wonda.api import ABCAPI
from wonda.bot.dispatch.dispatcher import ABCDispatcher, DefaultDispatcher
from wonda.bot.polling import ABCPoller


class ABCFramework(ABC):
    api: "ABCAPI"
    dispatcher: "ABCDispatcher"
    poller: "ABCPoller"

    @abstractmethod
    def run_forever(self) -> None:
        pass

    @property
    def on(self) -> DefaultDispatcher:
        return self.dispatcher  # type: ignore
