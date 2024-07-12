from dataclasses import dataclass


@dataclass
class PollerOptions:
    offset: int | None = None
    allowed_updates: list[str] | None = None
