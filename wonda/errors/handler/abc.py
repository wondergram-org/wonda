from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable

AsyncFunc = Callable[..., Awaitable[Any]]


class ABCErrorHandler(ABC):
    error_handlers: dict[type[BaseException], AsyncFunc]
    undefined_error_handler: AsyncFunc | None

    @abstractmethod
    def register_error_handler(
        self, *error_types: type[BaseException]
    ) -> Callable[[AsyncFunc], AsyncFunc]:
        pass

    @abstractmethod
    def register_undefined_error_handler(self, handler: AsyncFunc) -> AsyncFunc:
        pass

    @abstractmethod
    async def handle(self, error: BaseException) -> Any:
        pass

    @abstractmethod
    def catch(self, func: AsyncFunc) -> AsyncFunc:
        pass
