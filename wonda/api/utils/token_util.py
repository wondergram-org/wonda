import os
from pathlib import Path

from typing_extensions import Any, Self

from wonda.errors import EnvironmentError, InvalidTokenFormatError

_ = Any


def parse_env(lines: list[str]) -> dict[str, _]:
    """
    Parses environment variables into a dictionary.
    """
    return {
        key: value
        for line in lines
        if not line.startswith("#") and (parts := line.split("=", 1))
        for key, value in [parts]
    }


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

    @property
    def user_id(self) -> int:
        """
        The bot's user id extracted from the token.
        """
        return int(self.split(":")[0])

    @classmethod
    def from_env(cls, variable_name: str = VARIABLE_NAME) -> Self:
        """
        Creates a Token instance from an environment variable.
        """
        if token := os.getenv(variable_name):
            return cls(token)

        raise EnvironmentError(f"Environment variable {variable_name!r} not found")

    @classmethod
    def from_file(
        cls, source: str | Path = ENV_PATH, variable_name: str = VARIABLE_NAME
    ) -> Self:
        """
        Creates a Token instance from a file containing environment variables.
        """
        source = Path(source)

        with source.open() as f:
            environment = parse_env(f.readlines())

        if token := environment.get(variable_name):
            return cls(token)

        raise EnvironmentError(
            f"Could not find variable {variable_name!r} in file {source.name!r}"
        )
