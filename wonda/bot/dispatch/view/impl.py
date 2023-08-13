from wonda.bot.dispatch.view.abc import ABCView
from wonda.bot.updates.types import (
    CallbackQueryUpdate,
    ChatJoinRequestUpdate,
    ChatMemberUpdate,
    ChosenInlineResultUpdate,
    InlineQueryUpdate,
    MessageUpdate,
    PollAnswerUpdate,
    PollUpdate,
    PreCheckoutQueryUpdate,
    ShippingQueryUpdate,
)


class MessageView(
    ABCView[MessageUpdate],
    matches=["message", "edited_message", "channel_post", "edited_channel_post"],
):
    def get_state_key(self, m: MessageUpdate) -> int | None:
        return m.from_.id if m.from_ else None


class CallbackQueryView(ABCView[CallbackQueryUpdate], matches="callback_query"):
    def get_state_key(self, c: CallbackQueryUpdate) -> int | None:
        return c.from_.id


class InlineQueryView(ABCView[InlineQueryUpdate], matches="inline_query"):
    def get_state_key(self, i: InlineQueryUpdate) -> int | None:
        return i.from_.id


class ChatJoinRequestView(ABCView[ChatJoinRequestUpdate], matches="chat_join_request"):
    def get_state_key(self, c: ChatJoinRequestUpdate) -> int | None:
        return c.from_.id


class ChatMemberView(
    ABCView[ChatMemberUpdate], matches=["chat_member", "my_chat_member"]
):
    def get_state_key(self, c: ChatMemberUpdate) -> int:
        return c.from_.id


class ChosenInlineResultView(
    ABCView[ChosenInlineResultUpdate], matches="chosen_inline_result"
):
    def get_state_key(self, c: ChosenInlineResultUpdate) -> int:
        return c.from_.id


class PreCheckoutQueryView(
    ABCView[PreCheckoutQueryUpdate], matches="pre_checkout_query"
):
    def get_state_key(self, p: PreCheckoutQueryUpdate) -> int:
        return p.from_.id


class ShippingQueryView(ABCView[ShippingQueryUpdate], matches="shipping_query"):
    def get_state_key(self, s: ShippingQueryUpdate) -> int:
        return s.from_.id


class PollAnswerView(ABCView[PollAnswerUpdate], matches="poll_answer"):
    def get_state_key(self, p: PollAnswerUpdate) -> int:
        return p.user.id


class PollView(ABCView[PollUpdate], matches="poll"):
    def get_state_key(self, _) -> None:
        return None
