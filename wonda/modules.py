import structlog
from choicelib import choice_in_order
from typing_extensions import Protocol

structlog.configure(wrapper_class=structlog.stdlib.AsyncBoundLogger)
logger = structlog.get_logger()


class JSONModule(Protocol):
    def loads(self, s: str | bytes) -> dict:
        ...

    def dumps(self, o: dict | object) -> str:
        ...


json: JSONModule = choice_in_order(
    ["ujson", "hyperjson", "orjson"], do_import=True, default="json"
)

try:
    from uvloop import install

    install()
except ImportError:
    pass
