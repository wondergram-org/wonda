from functools import wraps
from typing import TYPE_CHECKING, Any, Callable

from .abc import ABCErrorHandler

if TYPE_CHECKING:
    from .abc import AsyncFunc

from wonda.modules import logger


class DefaultErrorHandler(ABCErrorHandler):
    def __init__(
        self, redirect_arguments: bool = False, raise_exceptions: bool = False
    ):
        self.error_handlers = {}
        self.undefined_error_handler = None

        self.redirect_arguments = redirect_arguments
        self.raise_exceptions = raise_exceptions

    def register_error_handler(
        self, *error_types: type[BaseException]
    ) -> Callable[["AsyncFunc"], "AsyncFunc"]:
        def decorator(handler: "AsyncFunc") -> "AsyncFunc":
            for error_type in error_types:
                self.error_handlers[error_type] = handler
            return handler

        return decorator

    def register_undefined_error_handler(self, handler: "AsyncFunc") -> "AsyncFunc":
        self.undefined_error_handler = handler
        return handler

    def lookup_handler(self, for_type: type[BaseException]) -> "AsyncFunc | None":
        for error_type in self.error_handlers:
            if issubclass(for_type, error_type):
                return self.error_handlers[error_type]
        return None

    async def handle(self, error: BaseException, *args, **kwargs) -> Any:
        handler = self.lookup_handler(type(error)) or self.undefined_error_handler

        if not handler:
            if self.raise_exceptions:
                raise error
            await logger.aexception("Failed", error=error)
            return

        if self.redirect_arguments:
            return await handler(error, *args, **kwargs)
        return await handler(error)

    def catch(self, func: "AsyncFunc") -> "AsyncFunc":
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                await func(*args, **kwargs)
            except BaseException as error:
                return await self.handle(error, *args, **kwargs)

        return wrapper
