from pathlib import Path

from wonda.types.objects import InputFile


class File:
    def __init__(self, content: bytes, name: str | None = None) -> None:
        self.content, self.name = content, name

    @classmethod
    def from_bytes(cls, source: bytes, name: str | None = None) -> InputFile:
        return InputFile(name or f"untitled.bin", source)

    @classmethod
    def from_path(cls, source: str | Path, name: str | None = None) -> InputFile:
        source = Path(source) if isinstance(source, str) else source

        with source.open("rb") as f:
            return InputFile(name or source.name, f.read())
