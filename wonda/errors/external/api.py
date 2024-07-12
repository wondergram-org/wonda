from .code import CodeException


class APIException(CodeException):
    def __init__(self, description: str | None, code: int | None) -> None:
        super().__init__(description)
        self.description = description
        self.code = code
