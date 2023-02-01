from .base_exceptions import TelegramAPIError
from .code_exception import CodeException
from .error_handler import ABCErrorHandler, ErrorHandler
from .swear_handler import swear


class WondaError(Exception):
    pass
