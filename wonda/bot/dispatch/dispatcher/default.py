from wonda.bot.dispatch.dispatcher.abc import ABCDispatcher
from wonda.bot.dispatch.view import ABCView, DefaultView
from wonda.bot.updates import (
    BusinessConnection,
    CallbackQuery,
    ChatBoost,
    ChatJoinRequest,
    ChatMember,
    ChosenInlineResult,
    DeletedBusinessMessages,
    InlineQuery,
    Message,
    MessageReaction,
    MessageReactionCount,
    Poll,
    PollAnswer,
    PreCheckoutQuery,
    RemovedChatBoost,
    ShippingQuery,
)


class DefaultDispatcher(ABCDispatcher):
    def __init__(self) -> None:
        self.message = DefaultView(Message, ["message", "edited_message"])
        self.channel_post = DefaultView(
            Message, ["channel_post", "edited_channel_post"]
        )
        self.business_message = DefaultView(
            Message, ["business_message", "edited_business_message"]
        )
        self.callback_query = DefaultView(CallbackQuery, "callback_query")
        self.inline_query = DefaultView(InlineQuery, "inline_query")
        self.message_reaction = DefaultView(MessageReaction, "message_reaction")
        self.message_reaction_count = DefaultView(
            MessageReactionCount, "message_reaction_count"
        )
        self.business_connection = DefaultView(
            BusinessConnection, "business_connection"
        )
        self.deleted_business_messages = DefaultView(
            DeletedBusinessMessages, "deleted_business_messages"
        )
        self.chat_join_request = DefaultView(ChatJoinRequest, "chat_join_request")
        self.chat_member = DefaultView(ChatMember, ["chat_member", "my_chat_member"])
        self.chosen_inline_result = DefaultView(
            ChosenInlineResult, "chosen_inline_result"
        )
        self.pre_checkout_query = DefaultView(PreCheckoutQuery, "pre_checkout_query")
        self.shipping_query = DefaultView(ShippingQuery, "shipping_query")
        self.chat_boost = DefaultView(ChatBoost, "chat_boost")
        self.removed_chat_boost = DefaultView(RemovedChatBoost, "removed_chat_boost")
        self.poll_answer = DefaultView(PollAnswer, "poll_answer")
        self.poll = DefaultView(Poll, "poll")

    

    def load(self, dispatcher: "ABCDispatcher") -> None:
        assert self != dispatcher, "Dispatcher can't be loaded in itself"

        for v in self.views.keys():
            view: "ABCView" = getattr(self, v)

            external_view: "ABCView | None" = getattr(dispatcher, v, None)
            assert (
                external_view
            ), f"External dispatcher should have {v!r} view available"
            view.load(external_view)

    @property
    def views(self) -> dict[str, "ABCView"]:
        return {
            name: view
            for name, view in self.__dict__.items()
            if isinstance(view, ABCView)
        }
