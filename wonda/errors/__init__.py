from .base_exceptions import TelegramAPIError
from .code_exception import CodeException
from .error_handler import ABCErrorHandler, ErrorHandler


class FrameworkError(Exception):
    pass


class EnvironmentError(FrameworkError):
    pass


class InvalidTokenFormatError(FrameworkError):
    pass
