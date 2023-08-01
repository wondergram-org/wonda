from wonda.bot.dispatch.dispatcher.abc import ABCDispatcher
from wonda.bot.dispatch.view.abc import ABCView
from wonda.bot.dispatch.view.impl import (
    CallbackQueryView,
    ChatJoinRequestView,
    ChatMemberView,
    ChosenInlineResultView,
    InlineQueryView,
    MessageView,
    PollAnswerView,
    PollView,
    PreCheckoutQueryView,
    ShippingQueryView,
)


class DefaultDispatcher(ABCDispatcher):
    def __init__(self) -> None:
        self.message = MessageView()
        self.callback_query = CallbackQueryView()
        self.inline_query = InlineQueryView()
        self.chat_join_request = ChatJoinRequestView()
        self.chat_member = ChatMemberView()
        self.chosen_inline_result = ChosenInlineResultView()
        self.pre_checkout_query = PreCheckoutQueryView()
        self.shipping_query = ShippingQueryView()
        self.poll_answer = PollAnswerView()
        self.poll = PollView()

    def load(self, dispatcher: "ABCDispatcher") -> None:
        pass

    def views(self) -> dict[str, "ABCView"]:
        return {k: v for k, v in vars(self).items() if isinstance(v, ABCView)}
