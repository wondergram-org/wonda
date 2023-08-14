from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wonda.bot.dispatch.view import ABCView


def get_used_update_types(disp: "ABCDispatcher") -> list[str]:
    update_types: list[str] = []

    for v in disp.views().values():
        if v.handlers or v.middlewares:
            update_types.extend(v.matches)
            
    return update_types


class ABCDispatcher(ABC):
    @abstractmethod
    def views(self) -> dict[str, "ABCView"]:
        pass

    @abstractmethod
    def load(self, dispatcher: "ABCDispatcher") -> None:
        pass
