from typing import Any, Callable, NewType

NO_KEY = object()

Key = NewType("Key", str)
TTL = NewType("TTL", float)

Value = Any
Dumper, Loader = Callable[[Value], str], Callable[[str], Value]
