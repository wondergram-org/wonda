from msgspec import Raw, Struct, json

from wonda.api.validators.abc import ABCResponseValidator
from wonda.errors import TelegramAPIError


class Response(Struct):
    ok: bool
    result: Raw = Raw()
    error_code: int | None = None
    description: str | None = None


class TelegramAPIErrorResponseValidator(ABCResponseValidator):
    async def validate(self, result: bytes) -> bytes:
        response = json.decode(result, type=Response)

        if response.ok:
            return response.result

        raise TelegramAPIError[response.error_code](
            response.description, response.error_code
        )


__all__ = ("TelegramAPIErrorResponseValidator",)
