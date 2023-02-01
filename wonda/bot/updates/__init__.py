from .base import BaseBotUpdate
from .types import *

Message = MessageUpdate
CallbackQuery = CallbackQueryUpdate
InlineQuery = InlineQueryUpdate
ChatJoinRequest = ChatJoinRequestUpdate
ChatMember = ChatMemberUpdate
ChosenInlineResult = ChosenInlineResultUpdate
MyChatMember = MyChatMemberUpdate
PreCheckoutQuery = PreCheckoutQueryUpdate
ShippingQuery = ShippingQueryUpdate
PollAnswer = PollAnswerUpdate
Poll = PollUpdate

__all__ = (
    "BaseBotUpdate",
    "BotUpdateType",
    "Message",
    "CallbackQuery",
    "InlineQuery",
    "ChatJoinRequest",
    "ChatMember",
    "ChosenInlineResult",
    "MyChatMember",
    "PreCheckoutQuery",
    "ShippingQuery",
    "PollAnswer",
    "Poll",
)
