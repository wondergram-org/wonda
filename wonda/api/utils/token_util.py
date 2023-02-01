from os import getenv
from typing import NoReturn, Optional, Union


class Token(str):
    @classmethod
    def from_env(
        cls, var_name: Optional[str] = "WONDA_TOKEN"
    ) -> Union["Token", NoReturn]:
        if token := getenv(var_name):
            return cls(token)

        raise KeyError(f"Environment variable {var_name!r} not found")
