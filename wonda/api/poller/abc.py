from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, AsyncIterator

if TYPE_CHECKING:
    from wonda.api.abc import ABCAPI
    from wonda.api.poller.options import PollerOptions
    from wonda.errors.handler.abc import ABCErrorHandler
    from wonda.types.objects import Update


class ABCPoller(ABC):
    api: "ABCAPI"
    options: "PollerOptions"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    def poll(self) -> AsyncIterator["Update"]:
        """
        Polls server for updates and yields them.
        """
