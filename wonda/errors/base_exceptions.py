from typing import Any

from .code_exception import CodeException


class TelegramAPIError(CodeException):
    def __init__(self, description: Any, params: dict):
        super().__init__(description)
        self.description = description
        self.params = params
