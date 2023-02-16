from typing import Any, Optional, Union

from pydantic import BaseModel

from wonda.api import ABCAPI, API
from wonda.bot.states import StateRepr


class BaseBotUpdate(BaseModel):
    state_repr: Optional[StateRepr] = None
    unprepared_ctx_api: Optional[Any] = None

    @property
    def ctx_api(self) -> Optional[Union["ABCAPI", "API"]]:
        return getattr(self, "unprepared_ctx_api")

    def get_state_key(self) -> Union[int, None]:
        return None
