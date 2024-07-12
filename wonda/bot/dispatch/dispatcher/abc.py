from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from wonda.bot.dispatch.view import ABCView

if TYPE_CHECKING:
    from wonda.bot.updates.types import (
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


class ABCDispatcher(ABC):
    """
    An interface for distributing received updates to their respective views.
    """

    message: ABCView["MessageUpdate"]
    """
    This view is used to handle message updates. It receives `message` and
    `edited_message` updates. Edited message updates can be sent even when
    the fields changes are made to are not available for your bot.
    """

    channel_post: ABCView["MessageUpdate"]
    """
    A view for handling channel posts. It receives `channel_post` and
    `edited_channel_post` updates. Edited message updates can be sent
    even when the fields changes are made to are not available
    for your bot.
    """

    business_connection: ABCView["BusinessConnectionUpdate"]
    """
    This view is used to handle updates related to business connections.
    For example, the connection or disconnection of the bot from
    a business account.
    """

    business_message: ABCView["MessageUpdate"]
    """
    A view for handling messages from connected business accounts.
    It receives `business_message` and `edited_business_message` updates.
    """

    deleted_business_messages: ABCView["DeletedBusinessMessagesUpdate"]
    """
    This view is used to handle messages deleted from a business account.
    """

    chat_member: ABCView["ChatMemberUpdate"]
    """
    This view is for handling changes to the state of a chat member,
    such as joining or leaving a chat. It receives `chat_member`
    and `my_chat_member` updates.
    """

    callback_query: ABCView["CallbackQueryUpdate"]
    """
    A view for handling callback queries from inline buttons. If the button
    that originated the query is attached to a message sent in inline mode,
    the field `inline_message_id` will be present.
    """

    inline_query: ABCView["InlineQueryUpdate"]
    """
    This view is used to handle an incoming inline query. An inline query is sent
    when the user starts typing the bot's username in the message field. Inline
    mode must be enabled in @Botfather.
    """

    message_reaction: ABCView["MessageReactionUpdate"]
    """
    A view for handling message reactions. The bot must be an administrator
    in the chat to receive such updates. Reactions set by bots can't be
    handled.
    """

    message_reaction_count: ABCView["MessageReactionCountUpdate"]
    """
    This view is used to handle reactions set to anonymous messages. The bot
    must be an administrator in the chat to receive these updates. Reaction
    count updates are grouped and sent with a delay of several minutes.
    """

    chat_join_request: ABCView["ChatJoinRequestUpdate"]
    """
    A view for handling requests to join the chat. The bot must have
    `can_invite_users` right in the chat to receive these updates.
    """

    chosen_inline_result: ABCView["ChosenInlineResultUpdate"]
    """
    This view is used to handle a result of an inline query that was
    chosen by the user and sent to their chat partner. Feedback
    collection must be enabled in @Botfather.
    """

    shipping_query: ABCView["ShippingQueryUpdate"]
    """
    A view for handling shipping queries. This update is received only
    if the invoice has a flexible price.
    """

    pre_checkout_query: ABCView["PreCheckoutQueryUpdate"]
    """
    This view is used to handle pre-checkout queries.
    """

    chat_boost: ABCView["ChatBoostUpdate"]
    """
    A view for handling changes to chat boosts. The bot must be an administrator
    in the chat to receive these updates.
    """

    removed_chat_boost: ABCView["RemovedChatBoostUpdate"]
    """
    This view is used to handle boosts that were removed from a chat.
    The bot must be an administrator in the chat to receive these updates.
    """

    poll_answer: ABCView["PollAnswerUpdate"]
    """
    A view for handling user votes in non-anonymous polls. The bot will receive
    votes only in the polls that were sent by the bot itself.
    """

    poll: ABCView["PollUpdate"]
    """
    This view is used to handle updates made to a poll, such as content edits
    or manual closure.
    """

    @abstractmethod
    def load(self, dispatcher: "ABCDispatcher") -> None:
        """
        Loads views from one dispatcher into the other.
        """

    @property
    @abstractmethod
    def views(self) -> dict[str, "ABCView"]:
        """
        Maps available views to their names.
        """
