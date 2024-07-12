from abc import ABC, abstractmethod

from typing_extensions import Any, Self


class ABCNetworkClient(ABC):
    @staticmethod
    @abstractmethod
    def construct_form(data: dict) -> Any:
        pass

    @abstractmethod
    async def request_text(
        self, url: str, method: str = "get", data: dict | None = None, **kw
    ) -> str:
        pass

    @abstractmethod
    async def request_json(
        self, url: str, method: str = "get", data: dict | None = None, **kw
    ) -> dict:
        pass

    @abstractmethod
    async def request_bytes(
        self, url: str, method: str = "get", data: dict | None = None, **kw
    ) -> bytes:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
