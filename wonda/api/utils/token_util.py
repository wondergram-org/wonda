import os
from pathlib import Path

from typing_extensions import Any, Self

from wonda.errors import EnvironmentError, InvalidTokenFormatError

_ = Any


def parse_env(content: str) -> dict[str, _]:
    """
    Parses environment variables into a dict.
    """
    vars: dict[str, _] = {}

    for line in content:
        key, value = line.strip().split("=", 1)

        if not key.startswith("#"):
            vars.update({key: value})

    return vars


def is_invalid(token: str) -> bool:
    """
    Performs basic checks on the token validity.
    """
    return token.count(":") != 1 or not token.split(":")[0].isdigit()


class Token(str):
    ENV_PATH = ".env"
    VARIABLE_NAME = "BOT_TOKEN"

    def __new__(cls, token: str) -> Self:
        if is_invalid(token):
            raise InvalidTokenFormatError(
                "Invalid token format. Learn more at "
                "https://core.telegram.org/bots/api#making-requests"
            )
        return super().__new__(cls, token)

    @classmethod
    def from_file(
        cls, path: Path | str = ENV_PATH, var_name: str = VARIABLE_NAME
    ) -> Self:
        path = Path(path) if isinstance(path, str) else path

        with path.open() as f:
            env = parse_env(f.read())

        return cls.from_env(var_name, env)

    @classmethod
    def from_env(
        cls, var_name: str = VARIABLE_NAME, env_source: dict[str, _] | None = None
    ) -> Self:
        if token := (env_source or os.environ).get(var_name):
            return cls(token)

        raise EnvironmentError(f"Environment variable {var_name!r} not found")
