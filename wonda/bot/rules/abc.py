from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union

T = TypeVar("T")


class ABCRule(ABC, Generic[T]):
    @abstractmethod
    async def check(self, update: T) -> Union[bool, dict]:
        pass

    def __and__(self, other: "ABCRule") -> "AndRule":
        return AndRule(self, other)

    def __or__(self, other: "ABCRule") -> "OrRule":
        return OrRule(self, other)

    def __invert__(self) -> "NotRule":
        return NotRule(self)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class AndRule(ABCRule[T]):
    def __init__(self, *rules: ABCRule[T]) -> None:
        self.rules = rules

    async def check(self, update: T) -> Union[bool, dict]:
        context = {}

        for rule in self.rules:
            check_response = await rule.check(update)
            if check_response is False:
                return check_response
            elif isinstance(check_response, dict):
                context.update(check_response)

        return context

    def __repr__(self):
        return f"<{self.__class__.__qualname__} rules={self.rules}>"


class NotRule(ABCRule[T]):
    def __init__(self, *rules: ABCRule[T]) -> None:
        self.rules = rules

    async def check(self, update: T) -> bool:
        for rule in self.rules:
            check_response = await rule.check(update)
            if check_response is False:
                return True
        return False

    def __repr__(self):
        return f"<{self.__class__.__qualname__} rules={self.rules}>"


class OrRule(ABCRule[T]):
    def __init__(self, *rules: ABCRule[T]) -> None:
        self.rules = rules

    async def check(self, update: T) -> None:
        for rule in self.rules:
            check_response = await rule.check(update)
            if check_response is not False:
                return check_response
        return False

    def __repr__(self):
        return f"<{self.__class__.__qualname__} rules={self.rules}>"
