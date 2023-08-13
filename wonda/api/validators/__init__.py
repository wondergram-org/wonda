from .abc import *
from .request import *
from .response import *

DEFAULT_REQUEST_VALIDATORS: list[type[ABCRequestValidator]] = [TranslateTypesValidator]
DEFAULT_RESPONSE_VALIDATORS: list[type[ABCResponseValidator]] = [
    TelegramAPIErrorResponseValidator
]
