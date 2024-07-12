from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T", bound=str | bytes)


@dataclass
class Translation(Generic[T]):
    name: str
    content: T


@dataclass
class Locale(Generic[T]):
    name: str
    translations: list[Translation[T]]

    def get_translation(self, name: str) -> T:
        try:
            suitable_translation = next(
                i.content for i in self.translations if name == i.name
            )
        except StopIteration:
            raise UnboundLocalError(
                "No translation of that name was found in the locale"
            )

        return suitable_translation
