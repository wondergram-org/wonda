from abc import ABC, abstractmethod
from typing import AsyncIterator

from wonda.api.abc import ABCAPI
from wonda.errors import ABCErrorHandler


class ABCPolling(ABC):
    api: "ABCAPI"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    async def listen(self) -> AsyncIterator:
        """
        Receives and yields update objects
        """
        pass
