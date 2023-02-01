from typing import TYPE_CHECKING, Dict, List, Union

from wonda.bot.dispatch.handlers.func import FromFuncHandler
from wonda.bot.dispatch.labelers.abc import (
    ABCLabeler,
    LabeledHandler,
    LabeledMessageHandler,
)
from wonda.bot.dispatch.view.message import MessageView
from wonda.bot.dispatch.view.raw import HandlerBasement, RawUpdateView
from wonda.bot.rules import ABCRule, IsGroup, IsPrivate

if TYPE_CHECKING:
    from wonda.bot.dispatch.view.abc import ABCView
    from wonda.bot.updates import BaseBotUpdate, BotUpdateType


class BotLabeler(ABCLabeler):
    def __init__(self) -> None:
        self.message_view = MessageView()
        self.raw_update_view = RawUpdateView()
        self.auto_rules: List["ABCRule"] = []

    def message(
        self, *rules: "ABCRule", blocking: bool = True
    ) -> "LabeledMessageHandler":
        assert all(
            isinstance(rule, ABCRule) for rule in rules
        ), "All rules must be subclasses of ABCRule or rule shortcuts"

        def decorator(func):
            self.message_view.handlers.append(
                FromFuncHandler(
                    func,
                    *rules,
                    *self.auto_rules,
                    blocking=blocking,
                )
            )
            return func

        return decorator

    def chat_message(
        self, *rules: "ABCRule", blocking: bool = True
    ) -> "LabeledMessageHandler":
        assert all(
            isinstance(rule, ABCRule) for rule in rules
        ), "All rules must be subclasses of ABCRule or rule shortcuts"

        def decorator(func):
            self.message_view.handlers.append(
                FromFuncHandler(
                    func,
                    IsGroup(),
                    *rules,
                    *self.auto_rules,
                    blocking=blocking,
                )
            )
            return func

        return decorator

    def private_message(
        self, *rules: "ABCRule", blocking: bool = True
    ) -> "LabeledMessageHandler":
        assert all(
            isinstance(rule, ABCRule) for rule in rules
        ), "All rules must be subclasses of ABCRule or rule shortcuts"

        def decorator(func):
            self.message_view.handlers.append(
                FromFuncHandler(
                    func,
                    IsPrivate(),
                    *rules,
                    *self.auto_rules,
                    blocking=blocking,
                )
            )
            return func

        return decorator

    def raw_update(
        self,
        update: Union["BotUpdateType", List["BotUpdateType"]],
        dataclass: "BaseBotUpdate",
        *rules: "ABCRule",
        blocking: bool = True,
    ) -> "LabeledHandler":
        assert all(
            isinstance(rule, ABCRule) for rule in rules
        ), "All rules must be subclasses of ABCRule or rule shortcuts"

        if not isinstance(update, list):
            update = [update]

        def decorator(func):
            for u in update:
                handler_basement = HandlerBasement(
                    dataclass,
                    FromFuncHandler(
                        func,
                        *rules,
                        *self.auto_rules,
                        blocking=blocking,
                    ),
                )
                update_handlers = self.raw_update_view.handlers.setdefault(u, [])
                update_handlers.append(handler_basement)
            return func

        return decorator

    def load(self, labeler: "BotLabeler") -> None:
        self.message_view.handlers.extend(labeler.message_view.handlers)
        self.message_view.middlewares.extend(labeler.message_view.middlewares)
        self.raw_update_view.middlewares.extend(labeler.raw_update_view.middlewares)

        for update, handler_basements in labeler.raw_update_view.handlers.items():
            update_handlers = self.raw_update_view.handlers.setdefault(update, [])
            update_handlers.extend(handler_basements)

    def views(self) -> Dict[str, "ABCView"]:
        return {"message": self.message_view, "raw": self.raw_update_view}
