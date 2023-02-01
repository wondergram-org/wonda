from enum import Enum
from typing import List, Optional, Union

from wonda.bot.updates.base import BaseBotUpdate
from wonda.types.methods import APIMethods
from wonda.types.objects import (
    CallbackQuery,
    ChatJoinRequest,
    ChatMemberUpdated,
    ChosenInlineResult,
    ForceReply,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResult,
    Message,
    MessageEntity,
    Poll,
    PollAnswer,
    PreCheckoutQuery,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ShippingQuery,
)


class BotUpdateType(Enum):
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    EDITED_CHANNEL_POST = "edited_channel_post"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_RESULT = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    POLL = "poll"
    POLL_ANSWER = "poll_answer"
    MY_CHAT_MEMBER = "my_chat_member"
    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"


class MessageUpdate(BaseBotUpdate, Message):
    async def answer(
        self,
        text: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        params = APIMethods.get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params["message_thread_id"] = self.message_thread_id

        return await self.ctx_api.send_message(chat_id=self.chat.id, **params)

    async def reply(
        self,
        text: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        params = APIMethods.get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params["message_thread_id"] = self.message_thread_id

        return await self.ctx_api.send_message(
            chat_id=self.chat.id, reply_to_message_id=self.message_id, **params
        )

    async def forward(
        self,
        chat_id: Union[int, str],
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        **kwargs
    ) -> Message:
        params = APIMethods.get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params["message_thread_id"] = self.message_thread_id

        return await self.ctx_api.forward_message(
            from_chat_id=self.chat.id, message_id=self.message_id, **params
        )

    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class CallbackQueryUpdate(BaseBotUpdate, CallbackQuery):
    async def answer(
        self,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
        **kwargs
    ) -> bool:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.answer_callback_query(
            callback_query_id=self.id, **params
        )

    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class InlineQueryUpdate(BaseBotUpdate, InlineQuery):
    async def answer(
        self,
        results: List[InlineQueryResult],
        switch_pm_text: Optional[str] = None,
        switch_pm_parameter: Optional[str] = None,
        next_offset: Optional[str] = None,
        is_personal: Optional[bool] = None,
        cache_time: Optional[int] = None,
        **kwargs
    ) -> bool:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.answer_inline_query(inline_query_id=self.id, **params)

    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class ChatJoinRequestUpdate(BaseBotUpdate, ChatJoinRequest):
    async def approve(self, **kwargs) -> bool:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.approve_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_.id, **params
        )

    async def decline(self, **kwargs) -> bool:
        params = APIMethods.get_params(locals())
        return await self.ctx_api.decline_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_.id, **params
        )

    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class ChatMemberUpdate(BaseBotUpdate, ChatMemberUpdated):
    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class ChosenInlineResultUpdate(BaseBotUpdate, ChosenInlineResult):
    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class MyChatMemberUpdate(BaseBotUpdate, ChatMemberUpdated):
    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class PreCheckoutQueryUpdate(BaseBotUpdate, PreCheckoutQuery):
    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class ShippingQueryUpdate(BaseBotUpdate, ShippingQuery):
    def get_state_key(self) -> Optional[int]:
        return self.from_.id


class PollAnswerUpdate(BaseBotUpdate, PollAnswer):
    def get_state_key(self) -> Optional[int]:
        return self.user.id


class PollUpdate(BaseBotUpdate, Poll):
    pass


__all__ = (
    "BaseBotUpdate",
    "BotUpdateType",
    "MessageUpdate",
    "CallbackQueryUpdate",
    "InlineQueryUpdate",
    "ChatJoinRequestUpdate",
    "ChatMemberUpdate",
    "ChosenInlineResultUpdate",
    "MyChatMemberUpdate",
    "PreCheckoutQueryUpdate",
    "ShippingQueryUpdate",
    "PollAnswerUpdate",
    "PollUpdate",
)
