from typing import Any, Callable

Key = str
Ex = float

Value = Any
Dumper, Loader = Callable[[Value], str], Callable[[str], Value]
