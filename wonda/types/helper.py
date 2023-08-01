from msgspec import Struct, json


class Model(
    Struct,
    omit_defaults=True,
    rename=lambda n: n.rstrip("_") if n.endswith("_") else None,
):
    def dict(self) -> dict:
        return {k: getattr(self, k) for k in self.__struct_fields__}


def get_params(loc: dict):
    n = {k: v for k, v in loc.items() if k not in ("self", "kwargs") and v is not None}
    n.update(loc["kwargs"])
    return n


__all__ = ("Model", "get_params", "json")
