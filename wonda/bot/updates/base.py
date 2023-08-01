from wonda.api import API
from wonda.bot.states import StateRepr


class BaseUpdate:
    ctx_api: API
    state_repr: StateRepr | None
