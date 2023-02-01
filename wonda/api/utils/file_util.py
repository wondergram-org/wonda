from io import BytesIO
from pathlib import Path
from typing import Optional, Union


class File:
    def __init__(self, content: Union[str, bytes], name: Optional[str] = None) -> None:
        self.name, self.content = name, content

    @classmethod
    def from_bytes(
        cls, data: Union[bytes, BytesIO], name: Optional[str] = None
    ) -> "File":
        content = data.getvalue() if isinstance(data, BytesIO) else data
        return cls(name=name or "unnamed.bin", content=content)

    @classmethod
    def from_path(cls, source: Union[str, Path], name: Optional[str] = None) -> "File":
        path = Path(source) if isinstance(source, str) else path

        with open(path, "rb") as f:
            return cls(name=name or path.name, content=f.read())

    def __repr__(self) -> str:
        return f"File(name={self.name!r})"
