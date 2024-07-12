from .base import BaseUpdate
from .types import (
    BusinessConnectionUpdate,
    CallbackQueryUpdate,
    ChatBoostUpdate,
    ChatJoinRequestUpdate,
    ChatMemberUpdate,
    ChosenInlineResultUpdate,
    DeletedBusinessMessagesUpdate,
    InlineQueryUpdate,
    MessageReactionCountUpdate,
    MessageReactionUpdate,
    MessageUpdate,
    PollAnswerUpdate,
    PollUpdate,
    PreCheckoutQueryUpdate,
    RemovedChatBoostUpdate,
    ShippingQueryUpdate,
)

Message = MessageUpdate
CallbackQuery = CallbackQueryUpdate
InlineQuery = InlineQueryUpdate
MessageReaction = MessageReactionUpdate
MessageReactionCount = MessageReactionCountUpdate
BusinessConnection = BusinessConnectionUpdate
DeletedBusinessMessages = DeletedBusinessMessagesUpdate
ChatJoinRequest = ChatJoinRequestUpdate
ChatMember = ChatMemberUpdate
ChatBoost = ChatBoostUpdate
RemovedChatBoost = RemovedChatBoostUpdate
ChosenInlineResult = ChosenInlineResultUpdate
PreCheckoutQuery = PreCheckoutQueryUpdate
ShippingQuery = ShippingQueryUpdate
PollAnswer = PollAnswerUpdate
Poll = PollUpdate
