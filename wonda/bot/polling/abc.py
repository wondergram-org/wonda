from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, AsyncIterator

if TYPE_CHECKING:
    from wonda.api.abc import ABCAPI
    from wonda.errors import ABCErrorHandler
    from wonda.types.objects import Update


class ABCPolling(ABC):
    api: "ABCAPI"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    async def listen(self) -> AsyncIterator["Update"]:
        """
        Receives and yields update objects
        """
        pass
