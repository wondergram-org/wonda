from .abc import *
from .request import *
from .response import *

DEFAULT_REQUEST_VALIDATORS: list[ABCRequestValidator] = [TranslateTypesValidator()]
DEFAULT_RESPONSE_VALIDATORS: list[ABCResponseValidator] = [
    TelegramAPIErrorResponseValidator()
]
