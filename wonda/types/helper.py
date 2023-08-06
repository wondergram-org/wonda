from msgspec import Struct, json

rename = lambda n: n.rstrip("_") if n.endswith("_") else None


class Model(Struct, rename=rename, omit_defaults=True):
    def json(self, encoding: str = "utf-8", errors: str = "strict") -> str:
        return json.encode(self).decode(encoding, errors)

    def dict(self) -> dict:
        return {k: getattr(self, k) for k in self.__struct_fields__}


def get_params(loc: dict):
    n = {k: v for k, v in loc.items() if k not in ("self", "kwargs") and v is not None}
    n.update(loc["kwargs"])
    return n


__all__ = ("Model", "get_params", "json")
