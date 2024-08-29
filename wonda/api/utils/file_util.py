from pathlib import Path

from wonda.types.objects import InputFile


class File:
    @staticmethod
    def from_bytes(source: bytes, name: str | None = None) -> InputFile:
        return InputFile(name or "untitled.bin", source)

    @staticmethod
    def from_path(source: str | Path, name: str | None = None) -> InputFile:
        source = Path(source)

        with source.open("rb") as f:
            return InputFile(name or source.name, f.read())
