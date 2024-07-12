from wonda.api import ABCAPI, API
from wonda.bot.states import StateRepr


class BaseUpdate:
    untyped_ctx_api: ABCAPI | None = None
    state_repr: StateRepr | None = None

    @property
    def ctx_api(self) -> API:
        return self.untyped_ctx_api  # type: ignore

    def get_state_key(self) -> int | None:
        return None
