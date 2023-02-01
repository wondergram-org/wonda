from enum import Enum
from typing import Any

from pydantic import BaseModel, validator


class BaseStateGroup(str, Enum):
    def _generate_next_value_(name, *_) -> str:
        # Implement the logic to generate
        # the next value via `enum.auto`
        return name.lower()


def get_state_repr(state: BaseStateGroup) -> str:
    return f"{state.__class__.__name__}:{state.value}"


class StateRepr(BaseModel):
    chat_id: int
    state: str
    payload: dict = {}

    @validator("state", pre=True)
    def validate_state(cls, v: Any) -> str:
        if isinstance(v, BaseStateGroup):
            return get_state_repr(v)
        elif isinstance(v, str):
            return v
        raise ValueError(
            f"State value must be `string` or `BaseStateGroup`, got `{type(v)}`"
        )
