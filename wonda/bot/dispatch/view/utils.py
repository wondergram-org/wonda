from typing import TypeVar

from wonda.bot.updates.base import BaseUpdate
from wonda.types.objects import Update

T = TypeVar("T", bound=BaseUpdate)


def get_update_type(update: "Update") -> str:
    for k in update.__struct_fields__:
        v = getattr(update, k, None)

        if v is not None and k != "update_id":
            return k
    return ""


def get_update_model(update: Update, model: type[T]) -> T:
    specific_update = getattr(update, get_update_type(update))
    return model(**specific_update.as_dict())
