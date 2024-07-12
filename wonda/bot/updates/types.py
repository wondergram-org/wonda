from enum import Enum

from wonda.bot.updates.base import BaseUpdate
from wonda.tools.text.styling.abc import ABCStyle, Text
from wonda.types.helper import get_params
from wonda.types.objects import (
    BusinessConnection,
    BusinessMessagesDeleted,
    CallbackQuery,
    ChatBoostRemoved,
    ChatBoostUpdated,
    ChatJoinRequest,
    ChatMemberUpdated,
    ChosenInlineResult,
    ForceReply,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResult,
    InlineQueryResultsButton,
    LinkPreviewOptions,
    Message,
    MessageEntity,
    MessageReactionCountUpdated,
    MessageReactionUpdated,
    Poll,
    PollAnswer,
    PreCheckoutQuery,
    ReactionType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
    ShippingOption,
    ShippingQuery,
)


class BotUpdateType(Enum):
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    EDITED_CHANNEL_POST = "edited_channel_post"
    BUSINESS_CONNECTION = "business_connection"
    BUSINESS_MESSAGE = "business_message"
    EDITED_BUSINESS_MESSAGE = "edited_business_message"
    DELETED_BUSINESS_MESSAGES = "deleted_business_messages"
    MESSAGE_REACTION = "message_reaction"
    MESSAGE_REACTION_COUNT = "message_reaction_count"
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
    CHAT_BOOST = "chat_boost"
    REMOVED_CHAT_BOOST = "removed_chat_boost"


class MessageUpdate(BaseUpdate, Message):
    async def answer(
        self,
        text: Text,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: (
            InlineKeyboardMarkup
            | ReplyKeyboardMarkup
            | ReplyKeyboardRemove
            | ForceReply
            | None
        ) = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        entities: list[MessageEntity] | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        params = get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params["message_thread_id"] = self.message_thread_id

        if "business_connection_id" not in params and self.business_connection_id:
            params["business_connection_id"] = self.business_connection_id

        if "entities" not in params and isinstance(text, ABCStyle):
            params.update({"text": text.to_string(), "entities": text.to_entities()})

        return await self.ctx_api.send_message(chat_id=self.chat.id, **params)

    async def reply(
        self,
        text: Text,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: (
            InlineKeyboardMarkup
            | ReplyKeyboardMarkup
            | ReplyKeyboardRemove
            | ForceReply
            | None
        ) = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        entities: list[MessageEntity] | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        params = get_params(locals())

        if "message_thread_id" not in params and self.is_topic_message:
            params.update({"message_thread_id": self.message_thread_id})

        if "business_connection_id" not in params and self.business_connection_id:
            params.update({"business_connection_id": self.business_connection_id})

        if "entities" not in params and isinstance(text, ABCStyle):
            params.update({"text": text.to_string(), "entities": text.to_entities()})

        return await self.ctx_api.send_message(
            chat_id=self.chat.id, reply_to_message_id=self.message_id, **params
        )

    async def forward(
        self,
        chat_id: int | str,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        **kwargs,
    ) -> Message:
        return await self.ctx_api.forward_message(
            message_id=self.message_id,
            from_chat_id=self.chat.id,
            **get_params(locals()),
        )

    async def delete(self, **kwargs) -> bool:
        return await self.ctx_api.delete_message(
            message_id=self.message_id, chat_id=self.chat.id, **get_params(locals())
        )

    async def react(
        self, reaction: list[ReactionType], is_big: bool | None = None, **kwargs
    ) -> bool:
        return await self.ctx_api.set_message_reaction(
            message_id=self.message_id, chat_id=self.chat.id, **get_params(locals())
        )

    async def pin(self, disable_notification: bool | None = None, **kwargs) -> bool:
        return await self.ctx_api.pin_chat_message(
            message_id=self.message_id, chat_id=self.chat.id, **get_params(locals())
        )

    def get_state_key(self) -> int | None:
        return self.from_.id if self.from_ else None


class CallbackQueryUpdate(BaseUpdate, CallbackQuery):
    async def answer(
        self,
        text: str | None = None,
        url: str | None = None,
        show_alert: bool | None = None,
        cache_time: int | None = None,
        **kwargs,
    ) -> bool:
        return await self.ctx_api.answer_callback_query(
            callback_query_id=self.id, **get_params(locals())
        )

    async def edit_text(
        self,
        text: Text,
        reply_markup: InlineKeyboardMarkup | None = None,
        parse_mode: str | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        inline_message_id: str | None = None,
        entities: list[MessageEntity] | None = None,
        **kwargs,
    ) -> Message | bool:
        params = get_params(locals())

        if "entities" not in params and isinstance(text, ABCStyle):
            params.update({"text": text.to_string(), "entities": text.to_entities()})

        assert self.message is not None, "Message is not available"
        return await self.ctx_api.edit_message_text(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id,
            inline_message_id=self.inline_message_id,
            **params,
        )

    async def edit_caption(
        self,
        caption: Text,
        *,
        reply_markup: InlineKeyboardMarkup | None = None,
        parse_mode: str | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        caption_entities: list[MessageEntity] | None = None,
        **kwargs,
    ) -> Message | bool:
        params = get_params(locals())

        if "caption_entities" not in params and isinstance(caption, ABCStyle):
            params.update(
                {"caption": caption.to_string(), "caption_entities": caption.to_entities()}
            )

        assert self.message is not None, "Message is not available"
        return await self.ctx_api.edit_message_caption(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id,
            inline_message_id=self.inline_message_id,
            **get_params(locals()),
        )

    async def edit_reply_markup(
        self, reply_markup: InlineKeyboardMarkup | None = None, **kwargs
    ) -> Message | bool:
        assert self.message is not None, "Message is not available"
        return await self.ctx_api.edit_message_reply_markup(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id,
            inline_message_id=self.inline_message_id,
            **get_params(locals()),
        )

    def get_state_key(self) -> int:
        return self.from_.id


class InlineQueryUpdate(BaseUpdate, InlineQuery):
    async def answer(
        self,
        results: list[InlineQueryResult],
        next_offset: str | None = None,
        is_personal: bool | None = None,
        cache_time: int | None = None,
        button: InlineQueryResultsButton | None = None,
        **kwargs,
    ) -> bool:
        return await self.ctx_api.answer_inline_query(
            inline_query_id=self.id, **get_params(locals())
        )

    def get_state_key(self) -> int:
        return self.from_.id


class ChatJoinRequestUpdate(BaseUpdate, ChatJoinRequest):
    async def approve(self, **kwargs) -> bool:
        return await self.ctx_api.approve_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_.id, **get_params(locals())
        )

    async def decline(self, **kwargs) -> bool:
        return await self.ctx_api.decline_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_.id, **get_params(locals())
        )

    def get_state_key(self) -> int:
        return self.from_.id


class PreCheckoutQueryUpdate(BaseUpdate, PreCheckoutQuery):
    async def answer(
        self, ok: bool, error_message: str | None = None, **kwargs
    ) -> bool:
        return await self.ctx_api.answer_pre_checkout_query(
            pre_checkout_query_id=self.id, **get_params(locals())
        )

    def get_state_key(self) -> int:
        return self.from_.id


class ShippingQueryUpdate(BaseUpdate, ShippingQuery):
    async def answer(
        self,
        ok: bool,
        shipping_options: list[ShippingOption] | None = None,
        error_message: str | None = None,
        **kwargs,
    ) -> bool:
        return await self.ctx_api.answer_shipping_query(
            shipping_query_id=self.id, **get_params(locals())
        )

    def get_state_key(self) -> int:
        return self.from_.id


class ChatMemberUpdate(BaseUpdate, ChatMemberUpdated):
    def get_state_key(self) -> int:
        return self.from_.id


class ChosenInlineResultUpdate(BaseUpdate, ChosenInlineResult):
    def get_state_key(self) -> int:
        return self.from_.id


class PollAnswerUpdate(BaseUpdate, PollAnswer):
    def get_state_key(self) -> int | None:
        return self.user.id if self.user else None


class MessageReactionUpdate(BaseUpdate, MessageReactionUpdated):
    def get_state_key(self) -> int | None:
        return self.user.id if self.user else None


class BusinessConnectionUpdate(BaseUpdate, BusinessConnection): ...


class DeletedBusinessMessagesUpdate(BaseUpdate, BusinessMessagesDeleted): ...


class MessageReactionCountUpdate(BaseUpdate, MessageReactionCountUpdated): ...


class ChatBoostUpdate(BaseUpdate, ChatBoostUpdated): ...


class RemovedChatBoostUpdate(BaseUpdate, ChatBoostRemoved): ...


class PollUpdate(BaseUpdate, Poll): ...


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
