from typing import Callable, TypeVar

K = TypeVar("K")
Ex = float

V = TypeVar("V")
Dumper, Loader = Callable[[V], str], Callable[[str], V]
