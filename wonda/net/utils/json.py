from typing import Any

from msgspec import json


def loads(s: str | bytes) -> Any:
    return json.decode(s)


def dumps(o: Any) -> str:
    return json.encode(o)
