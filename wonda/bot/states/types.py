from enum import Enum

from msgspec import Struct


class BaseStateGroup(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, *_) -> str:
        # Implement the logic to generate
        # the next value via `enum.auto`
        return name.lower()


def get_state_repr(state: BaseStateGroup) -> str:
    return f"{state.__class__.__name__}:{state.value}"


class StateRepr(Struct):
    state: str
    chat_id: int
    payload: dict = {}

    def __post_init__(self) -> None:
        self.state = (
            self.state
            if not isinstance(self.state, BaseStateGroup)
            else get_state_repr(self.state)
        )
