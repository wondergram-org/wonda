from abc import ABC, abstractmethod
from asyncio import AbstractEventLoop
from typing import NoReturn

from wonda.api import ABCAPI
from wonda.bot.dispatch.dispatcher import ABCDispatcher
from wonda.bot.polling import ABCPolling


class ABCFramework(ABC):
    @abstractmethod
    def run_forever(self) -> None:
        pass
