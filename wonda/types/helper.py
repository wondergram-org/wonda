from typing import TypeVar

import msgspec
from msgspec import Raw, Struct, json

T = TypeVar("T")


def rename(n: str) -> str | None:
    return n.rstrip("_") if n.endswith("_") else None


class Model(Struct, rename=rename, omit_defaults=True):
    def to_dict(self):
        return msgspec.to_builtins(self)

    def as_dict(self):
        return msgspec.structs.asdict(self)


class Response(Model):
    ok: bool
    result: Raw = Raw()
    error_code: int | None = None
    description: str | None = None


def from_json(v: bytes, *, type: type[T]) -> T:
    return json.decode(v, type=type)


def to_json(v) -> str:
    return bytes.decode(json.encode(v))


def translate(v):
    v = msgspec.to_builtins(v, builtin_types=(bytes,))

    if type(v) in (dict, list):
        return to_json(v)

    return v


def get_params(loc: dict):
    n = {k: v for k, v in loc.items() if k not in ("self", "kwargs") and v is not None}
    n.update(loc["kwargs"])
    return n


__all__ = ("Model", "get_params", "from_json", "to_json")
