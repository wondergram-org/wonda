from enum import Enum
from typing import Any

from aiohttp import FormData
from pydantic import BaseModel

from wonda.api.utils.file_util import File
from wonda.api.validators.abc import ABCRequestValidator
from wonda.modules import json


def translate(v: Any, rec: bool = False) -> Any:
    if isinstance(v, BaseModel):
        return (
            v.json(exclude_none=True, encoder=json.dumps)
            if not rec
            else v.dict(exclude_none=True)
        )
    elif isinstance(v, dict):
        return {k: translate(v, rec=True) for k, v in v.items() if v is not None}
    elif isinstance(v, list):
        return json.dumps([translate(i, rec=True) for i in v])
    elif isinstance(v, File):
        return v.content
    elif isinstance(v, Enum):
        return v.value
    elif isinstance(v, int):
        return str(v)
    elif v is None:
        pass
    return v


class TranslateFriendlyTypesRequestValidator(ABCRequestValidator):
    async def validate(self, request: dict) -> FormData:
        return FormData({k: translate(v) for k, v in request.items() if v is not None})


__all__ = ("TranslateFriendlyTypesRequestValidator",)
