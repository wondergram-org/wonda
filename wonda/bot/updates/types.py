from enum import Enum

from wonda.bot.updates.base import BaseUpdate
from wonda.types.helper import get_params
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


class MessageUpdate(BaseUpdate, Message):
    async def answer(
        self,
        text: str,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        **kwargs,
    ) -> Message:
        params = get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params["message_thread_id"] = self.message_thread_id

        return await self.ctx_api.send_message(chat_id=self.chat.id, **params)

    async def reply(
        self,
        text: str,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        **kwargs,
    ) -> Message:
        params = get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params["message_thread_id"] = self.message_thread_id

        return await self.ctx_api.send_message(
            chat_id=self.chat.id, reply_to_message_id=self.message_id, **params
        )

    async def forward(
        self,
        chat_id: int | str,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        **kwargs,
    ) -> Message:
        params = get_params(locals())

        return await self.ctx_api.forward_message(
            from_chat_id=self.chat.id, message_id=self.message_id, **params
        )


class CallbackQueryUpdate(BaseUpdate, CallbackQuery):
    async def answer(
        self,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None,
        **kwargs,
    ) -> bool:
        params = get_params(locals())
        return await self.ctx_api.answer_callback_query(
            callback_query_id=self.id, **params
        )


class InlineQueryUpdate(BaseUpdate, InlineQuery):
    async def answer(
        self,
        results: list[InlineQueryResult],
        switch_pm_text: str | None = None,
        switch_pm_parameter: str | None = None,
        next_offset: str | None = None,
        is_personal: bool | None = None,
        cache_time: int | None = None,
        **kwargs,
    ) -> bool:
        params = get_params(locals())
        return await self.ctx_api.answer_inline_query(inline_query_id=self.id, **params)


class ChatJoinRequestUpdate(BaseUpdate, ChatJoinRequest):
    async def approve(self, **kwargs) -> bool:
        params = get_params(locals())
        return await self.ctx_api.approve_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_.id, **params
        )

    async def decline(self, **kwargs) -> bool:
        params = get_params(locals())
        return await self.ctx_api.decline_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_.id, **params
        )


class ChatMemberUpdate(BaseUpdate, ChatMemberUpdated):
    pass


class ChosenInlineResultUpdate(BaseUpdate, ChosenInlineResult):
    pass


class PreCheckoutQueryUpdate(BaseUpdate, PreCheckoutQuery):
    pass


class ShippingQueryUpdate(BaseUpdate, ShippingQuery):
    pass


class PollAnswerUpdate(BaseUpdate, PollAnswer):
    pass


class PollUpdate(BaseUpdate, Poll):
    pass


__all__ = (
    "BaseUpdate",
    "BotUpdateType",
    "MessageUpdate",
    "CallbackQueryUpdate",
    "InlineQueryUpdate",
    "ChatJoinRequestUpdate",
    "ChatMemberUpdate",
    "ChosenInlineResultUpdate",
    "PreCheckoutQueryUpdate",
    "ShippingQueryUpdate",
    "PollAnswerUpdate",
    "PollUpdate",
)
