from typing import Any

from wonda.api.validators.abc import ABCRequestValidator
from wonda.types.helper import translate


class TranslateTypesValidator(ABCRequestValidator):
    async def validate(self, data: dict) -> Any:
        return self.network_client.construct_form(
            {k: translate(v) for k, v in data.items() if v is not None}
        )


__all__ = ("TranslateTypesValidator",)
