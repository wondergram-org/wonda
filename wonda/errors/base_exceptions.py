from typing import Any

from pydantic.validators import str_validator

from .code_exception import CodeException


class TelegramAPIError(CodeException):
    def __init__(self, description: Any, params: dict):
        super().__init__(description)
        self.description = str_validator(description)
        self.params = params
