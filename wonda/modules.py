import logging
from typing import IO, Any, AnyStr, Protocol

import structlog

structlog.stdlib.recreate_defaults(log_level=logging.INFO)
logger = structlog.get_logger()


class JSONModule(Protocol):
    def loads(self, string: AnyStr) -> dict: ...

    def dumps(self, object: Any) -> str: ...

    def load(self, file: IO) -> dict: ...

    def dump(self, object: Any, file: IO) -> None: ...

try:
    from uvloop import install

    install()
except ImportError:
    ...
