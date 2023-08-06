from typing import Any

from wonda.api.validators.abc import ABCRequestValidator
from wonda.types.helper import Model


def translate(v):
    if isinstance(v, dict):
        return {n: translate(p) for n, p in v.items() if v is not None}
    elif isinstance(v, list):
        return [translate(i) for i in v]
    elif isinstance(v, Model):
        return v.json()
    elif isinstance(v, int):
        return str(v)
    return v


class TranslateTypesValidator(ABCRequestValidator):
    async def validate(self, data: dict) -> Any:
        data = {k: translate(v) for k, v in data.items() if v is not None}
        return self.network_client.construct_form(data)


__all__ = ("TranslateTypesValidator",)
