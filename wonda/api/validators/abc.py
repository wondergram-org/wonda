from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from wonda.net.abc import ABCNetworkClient

if TYPE_CHECKING:
    from wonda.api.abc import ABCAPI


class ABCRequestValidator(ABC):
    def __init__(self, network_client: "ABCNetworkClient") -> None:
        self.network_client = network_client

    @abstractmethod
    async def validate(self, data: dict) -> Any:
        pass


class ABCResponseValidator(ABC):
    def __init__(self, ctx_api: "ABCAPI") -> None:
        self.ctx_api = ctx_api

    @abstractmethod
    async def validate(self, response: bytes) -> bytes:
        pass
