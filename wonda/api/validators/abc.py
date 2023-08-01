from abc import ABC, abstractmethod
from typing import NoReturn


class ABCRequestValidator(ABC):
    @abstractmethod
    async def validate(self, data: dict) -> dict | NoReturn:
        pass


class ABCResponseValidator(ABC):
    @abstractmethod
    async def validate(self, response: bytes) -> bytes | NoReturn:
        pass
