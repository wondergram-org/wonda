import os
from typing import Any

from wonda.errors import EnvironmentError, InvalidTokenFormatError

_ = Any


class Token(str):
    def __new__(cls, token: str) -> "Token":
        if token.count(":") != 1 or not token.split(":")[0].isdigit():
            raise InvalidTokenFormatError(
                "https://core.telegram.org/bots/api#making-requests"
            )
        return super().__new__(cls, token)

    @staticmethod
    def read_from_file(path: str) -> None:
        with open(path, "r") as file:
            vars = dict(  # type: ignore
                tuple(i.strip().split("=", 1)) for i in file if not i.startswith("#")
            )

        os.environ.update(vars)
        return None

    @classmethod
    def from_env(
        cls, var_name: str = "BOT_TOKEN", path_to_file: str | None = None
    ) -> "Token":
        if path_to_file is not None:
            cls.read_from_file(path_to_file)

        if token := os.environ.get(var_name):
            return cls(token)

        raise EnvironmentError(f"Environment variable {var_name!r} not found")
