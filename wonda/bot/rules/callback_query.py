from typing import List, Union

from wonda.bot.rules.abc import ABCRule
from wonda.bot.updates import CallbackQueryUpdate


class Data(ABCRule[CallbackQueryUpdate]):
    """
    `Data` is a rule that checks if callback data
    is in a given list of values.
    """

    def __init__(self, values: Union[str, List[str]]) -> None:
        self.values = values if isinstance(values, list) else [values]

    async def check(self, cq: CallbackQueryUpdate) -> bool:
        return cq.data in self.values
