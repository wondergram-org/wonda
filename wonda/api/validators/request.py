from typing import Any

from aiohttp import FormData

from wonda.api.utils.file_util import InputFile
from wonda.api.validators.abc import ABCRequestValidator
from wonda.types.helper import Model, json


def translate(v: Any) -> Any:
    if isinstance(v, Model):
        return json.encode(v).decode()
    elif isinstance(v, dict):
        return {n: translate(p) for n, p in v.items() if v is not None}
    elif isinstance(v, list):
        return [translate(i) for i in v]
    elif isinstance(v, InputFile):
        return (v.name, v.content)
    elif v is None:
        pass
    return v


class TranslateTypesValidator(ABCRequestValidator):
    async def validate(self, request: dict) -> FormData:
        return FormData({k: translate(v) for k, v in request.items() if v is not None})


__all__ = ("TranslateTypesValidator",)
