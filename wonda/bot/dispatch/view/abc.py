from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, Union

from wonda.bot.dispatch.middlewares.base import BaseMiddleware
from wonda.bot.updates import BaseBotUpdate, BotUpdateType
from wonda.modules import logger

if TYPE_CHECKING:
    from wonda.api import ABCAPI, API
    from wonda.bot.dispatch.handlers.abc import ABCHandler
    from wonda.bot.states.dispenser.abc import ABCStateDispenser


class ABCView(ABC):
    handlers: Union[List["ABCHandler"], Dict[Any, List[Any]]]
    middlewares: List[Type["BaseMiddleware"]]

    @abstractmethod
    async def process_update(self, update: dict) -> bool:
        """
        Checks if the update is of the type
        that this view supports
        """
        pass

    @abstractmethod
    async def handle_update(
        self,
        update: dict,
        ctx_api: "ABCAPI",
        state_dispenser: "ABCStateDispenser",
    ) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_update_model(
        update: dict, ctx_api: Union["ABCAPI", "API"]
    ) -> "BaseBotUpdate":
        """
        Performs data validation and parses update
        into BaseBotUpdate subclass
        """
        pass

    async def pre_middleware(
        self,
        update: dict,
        context_variables: Optional[dict] = None,
    ) -> Optional[List[BaseMiddleware]]:
        """
        Runs all of the pre middleware methods
        and returns an exception if any error occurs
        """
        mw_instances = []

        for middleware in self.middlewares:
            mw_instance = middleware(update, view=self)
            await mw_instance.pre()
            if not mw_instance.can_forward:
                logger.debug(
                    f"Pre middleware {mw_instance} "
                    f"returned error {mw_instance.error}"
                )
                return None

            mw_instances.append(mw_instance)

            if context_variables is not None:
                context_variables.update(mw_instance.context_update)

        return mw_instances

    async def post_middleware(
        self,
        mw_instances: List[BaseMiddleware],
        handle_responses: Optional[List] = None,
        handlers: Optional[List["ABCHandler"]] = None,
    ):
        """
        Runs all of the post middleware methods
        and returns an exception if any error occurs
        """
        for middleware in mw_instances:
            middleware.handle_responses = (
                handle_responses or middleware.handle_responses
            )
            middleware.handlers = handlers or middleware.handlers

            await middleware.post()
            if not middleware.can_forward:
                logger.debug(
                    f"Post middleware {middleware} "
                    f"returned error {middleware.error!r}"
                )
                return middleware.error

    def register_middleware(self, middleware: Type[BaseMiddleware]):
        """
        Registers an uninitialized middleware.
        This can also work as a decorator if needed
        """
        try:
            if not issubclass(middleware, BaseMiddleware):
                raise ValueError("Argument is not a subclass of BaseMiddleware")
        except TypeError:
            raise ValueError("Argument is not a class")
        self.middlewares.append(middleware)

    @staticmethod
    def get_update_type(update: dict) -> BotUpdateType:
        """
        Extracts the update type assuming that it is
        always a second field in the object.

        This method is a workaround for getting update types
        because Telegram does not explicitly return them
        """
        update_type = list(update.keys())[1]
        return BotUpdateType(update_type)

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"handlers={self.handlers} "
            f"middlewares={self.middlewares} "
            f"handler_return_manager={self.handler_return_manager}"
        )
