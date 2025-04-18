from dataclasses import dataclass
from pathlib import Path
from typing import Generic, TypeVar

T = TypeVar("T", bound=str | bytes)


@dataclass
class Translation(Generic[T]):
    """
    Represents a single translation entry. Used to store a named translation
    with content of type `T` that is either a string or bytes.
    """

    name: str
    content: T


@dataclass
class Locale(Generic[T]):
    """
    Represents a locale with a list of translations. Provides helper methods
    for translation retrieval.
    """

    name: str
    translations: list[Translation[T]]

    def __call__(self, name: str) -> T:
        """
        Alias for the `.get_translation()` method.
        """
        return self.get_translation(name)

    def get_translation(self, name: str) -> T:
        """
        Retrieves translation with the matching name.
        """
        try:
            suitable_translation = next(
                i.content for i in self.translations if name == i.name
            )
        except StopIteration:
            raise UnboundLocalError(
                "No translation of that name was found in the locale"
            )

        return suitable_translation


@dataclass
class FileContent:
    """
    A container for file content with path information.
    """

    path: Path
    content: str | bytes

    @classmethod
    def from_file(cls, path: Path) -> "FileContent":
        """
        Creates an instance from a file path.
        """
        content = (
            path.read_text()
            if path.suffix in (".txt", ".html", ".md")
            else path.read_bytes()
        )
        return cls(path=path, content=content)
