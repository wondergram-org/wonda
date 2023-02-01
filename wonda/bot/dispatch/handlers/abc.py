from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from wonda.types import BaseBotUpdate


class ABCHandler(ABC):
    blocking: bool

    @abstractmethod
    async def filter(self, update: "BaseBotUpdate") -> Union[dict, bool]:
        pass

    @abstractmethod
    async def handle(self, update: "BaseBotUpdate", **context) -> Any:
        pass
