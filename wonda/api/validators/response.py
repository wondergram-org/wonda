from typing import TYPE_CHECKING, Any, NoReturn, Union

from wonda.api.validators.abc import ABCResponseValidator
from wonda.errors import TelegramAPIError

if TYPE_CHECKING:
    from wonda.api import ABCAPI, API


class TelegramAPIErrorResponseValidator(ABCResponseValidator):
    async def validate(
        self, _, data: dict, response: Any, ctx_api: Union["ABCAPI", "API"]
    ) -> Union[Any, NoReturn]:
        if response.get("ok"):
            return response.get("result")

        code, msg = response.get("error_code"), response.get("description")
        raise TelegramAPIError[code](msg, data)


__all__ = ("TelegramAPIErrorResponseValidator",)
