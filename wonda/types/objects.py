import inspect
from typing import Optional, List, Literal, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Update(BaseModel):
    """
    This object represents an incoming update. At most one of the optional parameters
    can be present in any given update.
    """

    update_id: int = Field()
    message: Optional["Message"] = Field(default=None)
    edited_message: Optional["Message"] = Field(default=None)
    channel_post: Optional["Message"] = Field(default=None)
    edited_channel_post: Optional["Message"] = Field(default=None)
    inline_query: Optional["InlineQuery"] = Field(default=None)
    chosen_inline_result: Optional["ChosenInlineResult"] = Field(default=None)
    callback_query: Optional["CallbackQuery"] = Field(default=None)
    shipping_query: Optional["ShippingQuery"] = Field(default=None)
    pre_checkout_query: Optional["PreCheckoutQuery"] = Field(default=None)
    poll: Optional["Poll"] = Field(default=None)
    poll_answer: Optional["PollAnswer"] = Field(default=None)
    my_chat_member: Optional["ChatMemberUpdated"] = Field(default=None)
    chat_member: Optional["ChatMemberUpdated"] = Field(default=None)
    chat_join_request: Optional["ChatJoinRequest"] = Field(default=None)


class WebhookInfo(BaseModel):
    """
    Describes the current status of a webhook.
    """

    url: str = Field()
    has_custom_certificate: bool = Field()
    pending_update_count: int = Field()
    ip_address: Optional[str] = Field(default=None)
    last_error_date: Optional[int] = Field(default=None)
    last_error_message: Optional[str] = Field(default=None)
    last_synchronization_error_date: Optional[int] = Field(default=None)
    max_connections: Optional[int] = Field(default=None)
    allowed_updates: Optional[List[str]] = Field(default_factory=list)


class User(BaseModel):
    """
    This object represents a Telegram user or bot.
    """

    id: int = Field()
    is_bot: bool = Field()
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)
    language_code: Optional[str] = Field(default=None)
    is_premium: Optional[bool] = Field(default=None)
    added_to_attachment_menu: Optional[bool] = Field(default=None)
    can_join_groups: Optional[bool] = Field(default=None)
    can_read_all_group_messages: Optional[bool] = Field(default=None)
    supports_inline_queries: Optional[bool] = Field(default=None)


class Chat(BaseModel):
    """
    This object represents a chat.
    """

    id: int = Field()
    type: Literal["private", "group", "supergroup", "channel"] = Field()
    title: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    is_forum: Optional[bool] = Field(default=None)
    photo: Optional["ChatPhoto"] = Field(default=None)
    active_usernames: Optional[List[str]] = Field(default_factory=list)
    emoji_status_custom_emoji_id: Optional[str] = Field(default=None)
    bio: Optional[str] = Field(default=None)
    has_private_forwards: Optional[bool] = Field(default=None)
    has_restricted_voice_and_video_messages: Optional[bool] = Field(default=None)
    join_to_send_messages: Optional[bool] = Field(default=None)
    join_by_request: Optional[bool] = Field(default=None)
    description: Optional[str] = Field(default=None)
    invite_link: Optional[str] = Field(default=None)
    pinned_message: Optional["Message"] = Field(default=None)
    permissions: Optional["ChatPermissions"] = Field(default=None)
    slow_mode_delay: Optional[int] = Field(default=None)
    message_auto_delete_time: Optional[int] = Field(default=None)
    has_aggressive_anti_spam_enabled: Optional[bool] = Field(default=None)
    has_hidden_members: Optional[bool] = Field(default=None)
    has_protected_content: Optional[bool] = Field(default=None)
    sticker_set_name: Optional[str] = Field(default=None)
    can_set_sticker_set: Optional[bool] = Field(default=None)
    linked_chat_id: Optional[int] = Field(default=None)
    location: Optional["ChatLocation"] = Field(default=None)


class Message(BaseModel):
    """
    This object represents a message.
    """

    message_id: int = Field()
    message_thread_id: Optional[int] = Field(default=None)
    from_: Optional["User"] = Field(default=None, alias="from")
    sender_chat: Optional["Chat"] = Field(default=None)
    date: int = Field()
    chat: "Chat" = Field()
    forward_from: Optional["User"] = Field(default=None)
    forward_from_chat: Optional["Chat"] = Field(default=None)
    forward_from_message_id: Optional[int] = Field(default=None)
    forward_signature: Optional[str] = Field(default=None)
    forward_sender_name: Optional[str] = Field(default=None)
    forward_date: Optional[int] = Field(default=None)
    is_topic_message: Optional[bool] = Field(default=None)
    is_automatic_forward: Optional[bool] = Field(default=None)
    reply_to_message: Optional["Message"] = Field(default=None)
    via_bot: Optional["User"] = Field(default=None)
    edit_date: Optional[int] = Field(default=None)
    has_protected_content: Optional[bool] = Field(default=None)
    media_group_id: Optional[str] = Field(default=None)
    author_signature: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    animation: Optional["Animation"] = Field(default=None)
    audio: Optional["Audio"] = Field(default=None)
    document: Optional["Document"] = Field(default=None)
    photo: Optional[List["PhotoSize"]] = Field(default_factory=list)
    sticker: Optional["Sticker"] = Field(default=None)
    video: Optional["Video"] = Field(default=None)
    video_note: Optional["VideoNote"] = Field(default=None)
    voice: Optional["Voice"] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    has_media_spoiler: Optional[bool] = Field(default=None)
    contact: Optional["Contact"] = Field(default=None)
    dice: Optional["Dice"] = Field(default=None)
    game: Optional["Game"] = Field(default=None)
    poll: Optional["Poll"] = Field(default=None)
    venue: Optional["Venue"] = Field(default=None)
    location: Optional["Location"] = Field(default=None)
    new_chat_members: Optional[List["User"]] = Field(default_factory=list)
    left_chat_member: Optional["User"] = Field(default=None)
    new_chat_title: Optional[str] = Field(default=None)
    new_chat_photo: Optional[List["PhotoSize"]] = Field(default_factory=list)
    delete_chat_photo: Optional[bool] = Field(default=None)
    group_chat_created: Optional[bool] = Field(default=None)
    supergroup_chat_created: Optional[bool] = Field(default=None)
    channel_chat_created: Optional[bool] = Field(default=None)
    message_auto_delete_timer_changed: Optional[
        "MessageAutoDeleteTimerChanged"
    ] = Field(default=None)
    migrate_to_chat_id: Optional[int] = Field(default=None)
    migrate_from_chat_id: Optional[int] = Field(default=None)
    pinned_message: Optional["Message"] = Field(default=None)
    invoice: Optional["Invoice"] = Field(default=None)
    successful_payment: Optional["SuccessfulPayment"] = Field(default=None)
    connected_website: Optional[str] = Field(default=None)
    write_access_allowed: Optional["WriteAccessAllowed"] = Field(default=None)
    passport_data: Optional["PassportData"] = Field(default=None)
    proximity_alert_triggered: Optional["ProximityAlertTriggered"] = Field(default=None)
    forum_topic_created: Optional["ForumTopicCreated"] = Field(default=None)
    forum_topic_edited: Optional["ForumTopicEdited"] = Field(default=None)
    forum_topic_closed: Optional["ForumTopicClosed"] = Field(default=None)
    forum_topic_reopened: Optional["ForumTopicReopened"] = Field(default=None)
    general_forum_topic_hidden: Optional["GeneralForumTopicHidden"] = Field(
        default=None
    )
    general_forum_topic_unhidden: Optional["GeneralForumTopicUnhidden"] = Field(
        default=None
    )
    video_chat_scheduled: Optional["VideoChatScheduled"] = Field(default=None)
    video_chat_started: Optional["VideoChatStarted"] = Field(default=None)
    video_chat_ended: Optional["VideoChatEnded"] = Field(default=None)
    video_chat_participants_invited: Optional["VideoChatParticipantsInvited"] = Field(
        default=None
    )
    web_app_data: Optional["WebAppData"] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)


class MessageId(BaseModel):
    """
    This object represents a unique message identifier.
    """

    message_id: int = Field()


class MessageEntity(BaseModel):
    """
    This object represents one special entity in a text message. For example, hashtags,
    usernames, URLs, etc.
    """

    type: Literal[
        "mention",
        "hashtag",
        "cashtag",
        "bot_command",
        "url",
        "email",
        "phone_number",
        "bold",
        "italic",
        "underline",
        "strikethrough",
        "spoiler",
        "code",
        "pre",
        "text_link",
        "text_mention",
        "custom_emoji",
    ] = Field()
    offset: int = Field()
    length: int = Field()
    url: Optional[str] = Field(default=None)
    user: Optional["User"] = Field(default=None)
    language: Optional[str] = Field(default=None)
    custom_emoji_id: Optional[str] = Field(default=None)


class PhotoSize(BaseModel):
    """
    This object represents one size of a photo or a file / sticker thumbnail.
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    width: int = Field()
    height: int = Field()
    file_size: Optional[int] = Field(default=None)


class Animation(BaseModel):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound).
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    width: int = Field()
    height: int = Field()
    duration: int = Field()
    thumb: Optional["PhotoSize"] = Field(default=None)
    file_name: Optional[str] = Field(default=None)
    mime_type: Optional[str] = Field(default=None)
    file_size: Optional[int] = Field(default=None)


class Audio(BaseModel):
    """
    This object represents an audio file to be treated as music by the Telegram clients.
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    duration: int = Field()
    performer: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    file_name: Optional[str] = Field(default=None)
    mime_type: Optional[str] = Field(default=None)
    file_size: Optional[int] = Field(default=None)
    thumb: Optional["PhotoSize"] = Field(default=None)


class Document(BaseModel):
    """
    This object represents a general file (as opposed to photos, voice messages and
    audio files).
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    thumb: Optional["PhotoSize"] = Field(default=None)
    file_name: Optional[str] = Field(default=None)
    mime_type: Optional[str] = Field(default=None)
    file_size: Optional[int] = Field(default=None)


class Video(BaseModel):
    """
    This object represents a video file.
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    width: int = Field()
    height: int = Field()
    duration: int = Field()
    thumb: Optional["PhotoSize"] = Field(default=None)
    file_name: Optional[str] = Field(default=None)
    mime_type: Optional[str] = Field(default=None)
    file_size: Optional[int] = Field(default=None)


class VideoNote(BaseModel):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    length: int = Field()
    duration: int = Field()
    thumb: Optional["PhotoSize"] = Field(default=None)
    file_size: Optional[int] = Field(default=None)


class Voice(BaseModel):
    """
    This object represents a voice note.
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    duration: int = Field()
    mime_type: Optional[str] = Field(default=None)
    file_size: Optional[int] = Field(default=None)


class Contact(BaseModel):
    """
    This object represents a phone contact.
    """

    phone_number: str = Field()
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    user_id: Optional[int] = Field(default=None)
    vcard: Optional[str] = Field(default=None)


class Dice(BaseModel):
    """
    This object represents an animated emoji that displays a random value.
    """

    emoji: str = Field()
    value: int = Field()


class PollOption(BaseModel):
    """
    This object contains information about one answer option in a poll.
    """

    text: str = Field()
    voter_count: int = Field()


class PollAnswer(BaseModel):
    """
    This object represents an answer of a user in a non-anonymous poll.
    """

    poll_id: str = Field()
    user: "User" = Field()
    option_ids: List[int] = Field()


class Poll(BaseModel):
    """
    This object contains information about a poll.
    """

    id: str = Field()
    question: str = Field()
    options: List["PollOption"] = Field()
    total_voter_count: int = Field()
    is_closed: bool = Field()
    is_anonymous: bool = Field()
    type: Literal["regular", "quiz"] = Field()
    allows_multiple_answers: bool = Field()
    correct_option_id: Optional[int] = Field(default=None)
    explanation: Optional[str] = Field(default=None)
    explanation_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    open_period: Optional[int] = Field(default=None)
    close_date: Optional[int] = Field(default=None)


class Location(BaseModel):
    """
    This object represents a point on the map.
    """

    longitude: float = Field()
    latitude: float = Field()
    horizontal_accuracy: Optional[float] = Field(default=None)
    live_period: Optional[int] = Field(default=None)
    heading: Optional[int] = Field(default=None)
    proximity_alert_radius: Optional[int] = Field(default=None)


class Venue(BaseModel):
    """
    This object represents a venue.
    """

    location: "Location" = Field()
    title: str = Field()
    address: str = Field()
    foursquare_id: Optional[str] = Field(default=None)
    foursquare_type: Optional[str] = Field(default=None)
    google_place_id: Optional[str] = Field(default=None)
    google_place_type: Optional[str] = Field(default=None)


class WebAppData(BaseModel):
    """
    Describes data sent from a Web App to the bot.
    """

    data: str = Field()
    button_text: str = Field()


class ProximityAlertTriggered(BaseModel):
    """
    This object represents the content of a service message, sent whenever a user in the
    chat triggers a proximity alert set by another user.
    """

    traveler: "User" = Field()
    watcher: "User" = Field()
    distance: int = Field()


class MessageAutoDeleteTimerChanged(BaseModel):
    """
    This object represents a service message about a change in auto-delete timer
    settings.
    """

    message_auto_delete_time: int = Field()


class ForumTopicCreated(BaseModel):
    """
    This object represents a service message about a new forum topic created in the
    chat.
    """

    name: str = Field()
    icon_color: int = Field()
    icon_custom_emoji_id: Optional[str] = Field(default=None)


class ForumTopicClosed(BaseModel):
    """
    This object represents a service message about a forum topic closed in the chat.
    Currently holds no information.
    """

    pass


class ForumTopicEdited(BaseModel):
    """
    This object represents a service message about an edited forum topic.
    """

    name: Optional[str] = Field(default=None)
    icon_custom_emoji_id: Optional[str] = Field(default=None)


class ForumTopicReopened(BaseModel):
    """
    This object represents a service message about a forum topic reopened in the chat.
    Currently holds no information.
    """

    pass


class GeneralForumTopicHidden(BaseModel):
    """
    This object represents a service message about General forum topic hidden in the
    chat. Currently holds no information.
    """

    pass


class GeneralForumTopicUnhidden(BaseModel):
    """
    This object represents a service message about General forum topic unhidden in the
    chat. Currently holds no information.
    """

    pass


class WriteAccessAllowed(BaseModel):
    """
    This object represents a service message about a user allowing a bot added to the
    attachment menu to write messages. Currently holds no information.
    """

    pass


class VideoChatScheduled(BaseModel):
    """
    This object represents a service message about a video chat scheduled in the chat.
    """

    start_date: int = Field()


class VideoChatStarted(BaseModel):
    """
    This object represents a service message about a video chat started in the chat.
    Currently holds no information.
    """

    pass


class VideoChatEnded(BaseModel):
    """
    This object represents a service message about a video chat ended in the chat.
    """

    duration: int = Field()


class VideoChatParticipantsInvited(BaseModel):
    """
    This object represents a service message about new members invited to a video chat.
    """

    users: List["User"] = Field()


class UserProfilePhotos(BaseModel):
    """
    This object represent a user's profile pictures.
    """

    total_count: int = Field()
    photos: List[List["PhotoSize"]] = Field()


class File(BaseModel):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via
    the link https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt;. It is
    guaranteed that the link will be valid for at least 1 hour. When the link expires, a
    new one can be requested by calling getFile. The maximum file size to download is 20
    MB
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    file_size: Optional[int] = Field(default=None)
    file_path: Optional[str] = Field(default=None)


class WebAppInfo(BaseModel):
    """
    Describes a Web App.
    """

    url: str = Field()


class ReplyKeyboardMarkup(BaseModel):
    """
    This object represents a custom keyboard with reply options (see Introduction to
    bots for details and examples).
    """

    keyboard: List[List["KeyboardButton"]] = Field()
    is_persistent: Optional[bool] = Field(default=None)
    resize_keyboard: Optional[bool] = Field(default=None)
    one_time_keyboard: Optional[bool] = Field(default=None)
    input_field_placeholder: Optional[str] = Field(default=None)
    selective: Optional[bool] = Field(default=None)


class KeyboardButton(BaseModel):
    """
    This object represents one button of the reply keyboard. For simple text buttons
    String can be used instead of this object to specify text of the button. Optional
    fields web_app, request_contact, request_location, and request_poll are mutually
    exclusive.
    """

    text: str = Field()
    request_contact: Optional[bool] = Field(default=None)
    request_location: Optional[bool] = Field(default=None)
    request_poll: Optional["KeyboardButtonPollType"] = Field(default=None)
    web_app: Optional["WebAppInfo"] = Field(default=None)


class KeyboardButtonPollType(BaseModel):
    """
    This object represents type of a poll, which is allowed to be created and sent when
    the corresponding button is pressed.
    """

    type: Optional[str] = Field(default=None)


class ReplyKeyboardRemove(BaseModel):
    """
    Upon receiving a message with this object, Telegram clients will remove the current
    custom keyboard and display the default letter-keyboard. By default, custom
    keyboards are displayed until a new keyboard is sent by a bot. An exception is made
    for one-time keyboards that are hidden immediately after the user presses a button
    (see ReplyKeyboardMarkup).
    """

    remove_keyboard: bool = Field()
    selective: Optional[bool] = Field(default=None)


class InlineKeyboardMarkup(BaseModel):
    """
    This object represents an inline keyboard that appears right next to the message it
    belongs to.
    """

    inline_keyboard: List[List["InlineKeyboardButton"]] = Field()


class InlineKeyboardButton(BaseModel):
    """
    This object represents one button of an inline keyboard. You must use exactly one of
    the optional fields.
    """

    text: str = Field()
    url: Optional[str] = Field(default=None)
    callback_data: Optional[str] = Field(default=None)
    web_app: Optional["WebAppInfo"] = Field(default=None)
    login_url: Optional["LoginUrl"] = Field(default=None)
    switch_inline_query: Optional[str] = Field(default=None)
    switch_inline_query_current_chat: Optional[str] = Field(default=None)
    callback_game: Optional["CallbackGame"] = Field(default=None)
    pay: Optional[bool] = Field(default=None)


class LoginUrl(BaseModel):
    """
    This object represents a parameter of the inline keyboard button used to
    automatically authorize a user. Serves as a great replacement for the Telegram Login
    Widget when the user is coming from Telegram. All the user needs to do is tap/click
    a button and confirm that they want to log in: Telegram apps support these buttons
    as of version 5.7. Sample bot: @discussbot
    """

    url: str = Field()
    forward_text: Optional[str] = Field(default=None)
    bot_username: Optional[str] = Field(default=None)
    request_write_access: Optional[bool] = Field(default=None)


class CallbackQuery(BaseModel):
    """
    This object represents an incoming callback query from a callback button in an
    inline keyboard. If the button that originated the query was attached to a message
    sent by the bot, the field message will be present. If the button was attached to a
    message sent via the bot (in inline mode), the field inline_message_id will be
    present. Exactly one of the fields data or game_short_name will be present.
    """

    id: str = Field()
    from_: "User" = Field(alias="from")
    message: Optional["Message"] = Field(default=None)
    inline_message_id: Optional[str] = Field(default=None)
    chat_instance: str = Field()
    data: Optional[str] = Field(default=None)
    game_short_name: Optional[str] = Field(default=None)


class ForceReply(BaseModel):
    """
    Upon receiving a message with this object, Telegram clients will display a reply
    interface to the user (act as if the user has selected the bot's message and tapped
    'Reply'). This can be extremely useful if you want to create user-friendly step-by-
    step interfaces without having to sacrifice privacy mode.
    """

    force_reply: bool = Field()
    input_field_placeholder: Optional[str] = Field(default=None)
    selective: Optional[bool] = Field(default=None)


class ChatPhoto(BaseModel):
    """
    This object represents a chat photo.
    """

    small_file_id: str = Field()
    small_file_unique_id: str = Field()
    big_file_id: str = Field()
    big_file_unique_id: str = Field()


class ChatInviteLink(BaseModel):
    """
    Represents an invite link for a chat.
    """

    invite_link: str = Field()
    creator: "User" = Field()
    creates_join_request: bool = Field()
    is_primary: bool = Field()
    is_revoked: bool = Field()
    name: Optional[str] = Field(default=None)
    expire_date: Optional[int] = Field(default=None)
    member_limit: Optional[int] = Field(default=None)
    pending_join_request_count: Optional[int] = Field(default=None)


class ChatAdministratorRights(BaseModel):
    """
    Represents the rights of an administrator in a chat.
    """

    is_anonymous: bool = Field()
    can_manage_chat: bool = Field()
    can_delete_messages: bool = Field()
    can_manage_video_chats: bool = Field()
    can_restrict_members: bool = Field()
    can_promote_members: bool = Field()
    can_change_info: bool = Field()
    can_invite_users: bool = Field()
    can_post_messages: Optional[bool] = Field(default=None)
    can_edit_messages: Optional[bool] = Field(default=None)
    can_pin_messages: Optional[bool] = Field(default=None)
    can_manage_topics: Optional[bool] = Field(default=None)


class ChatMemberOwner(BaseModel):
    """
    Represents a chat member that owns the chat and has all administrator privileges.
    """

    status: Literal["creator"] = Field(default="creator")
    user: "User" = Field()
    is_anonymous: bool = Field()
    custom_title: Optional[str] = Field(default=None)


class ChatMemberAdministrator(BaseModel):
    """
    Represents a chat member that has some additional privileges.
    """

    status: Literal["administrator"] = Field(default="administrator")
    user: "User" = Field()
    can_be_edited: bool = Field()
    is_anonymous: bool = Field()
    can_manage_chat: bool = Field()
    can_delete_messages: bool = Field()
    can_manage_video_chats: bool = Field()
    can_restrict_members: bool = Field()
    can_promote_members: bool = Field()
    can_change_info: bool = Field()
    can_invite_users: bool = Field()
    can_post_messages: Optional[bool] = Field(default=None)
    can_edit_messages: Optional[bool] = Field(default=None)
    can_pin_messages: Optional[bool] = Field(default=None)
    can_manage_topics: Optional[bool] = Field(default=None)
    custom_title: Optional[str] = Field(default=None)


class ChatMemberMember(BaseModel):
    """
    Represents a chat member that has no additional privileges or restrictions.
    """

    status: Literal["member"] = Field(default="member")
    user: "User" = Field()


class ChatMemberRestricted(BaseModel):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups
    only.
    """

    status: Literal["restricted"] = Field(default="restricted")
    user: "User" = Field()
    is_member: bool = Field()
    can_change_info: bool = Field()
    can_invite_users: bool = Field()
    can_pin_messages: bool = Field()
    can_manage_topics: bool = Field()
    can_send_messages: bool = Field()
    can_send_media_messages: bool = Field()
    can_send_polls: bool = Field()
    can_send_other_messages: bool = Field()
    can_add_web_page_previews: bool = Field()
    until_date: int = Field()


class ChatMemberLeft(BaseModel):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it
    themselves.
    """

    status: Literal["left"] = Field(default="left")
    user: "User" = Field()


class ChatMemberBanned(BaseModel):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or
    view chat messages.
    """

    status: Literal["kicked"] = Field(default="kicked")
    user: "User" = Field()
    until_date: int = Field()


class ChatMemberUpdated(BaseModel):
    """
    This object represents changes in the status of a chat member.
    """

    chat: "Chat" = Field()
    from_: "User" = Field(alias="from")
    date: int = Field()
    old_chat_member: "ChatMember" = Field()
    new_chat_member: "ChatMember" = Field()
    invite_link: Optional["ChatInviteLink"] = Field(default=None)


class ChatJoinRequest(BaseModel):
    """
    Represents a join request sent to a chat.
    """

    chat: "Chat" = Field()
    from_: "User" = Field(alias="from")
    date: int = Field()
    bio: Optional[str] = Field(default=None)
    invite_link: Optional["ChatInviteLink"] = Field(default=None)


class ChatPermissions(BaseModel):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.
    """

    can_send_messages: Optional[bool] = Field(default=None)
    can_send_media_messages: Optional[bool] = Field(default=None)
    can_send_polls: Optional[bool] = Field(default=None)
    can_send_other_messages: Optional[bool] = Field(default=None)
    can_add_web_page_previews: Optional[bool] = Field(default=None)
    can_change_info: Optional[bool] = Field(default=None)
    can_invite_users: Optional[bool] = Field(default=None)
    can_pin_messages: Optional[bool] = Field(default=None)
    can_manage_topics: Optional[bool] = Field(default=None)


class ChatLocation(BaseModel):
    """
    Represents a location to which a chat is connected.
    """

    location: "Location" = Field()
    address: str = Field()


class ForumTopic(BaseModel):
    """
    This object represents a forum topic.
    """

    message_thread_id: int = Field()
    name: str = Field()
    icon_color: int = Field()
    icon_custom_emoji_id: Optional[str] = Field(default=None)


class BotCommand(BaseModel):
    """
    This object represents a bot command.
    """

    command: str = Field()
    description: str = Field()


class BotCommandScopeDefault(BaseModel):
    """
    Represents the default scope of bot commands. Default commands are used if no
    commands with a narrower scope are specified for the user.
    """

    type: Literal["default"] = Field(default="default")


class BotCommandScopeAllPrivateChats(BaseModel):
    """
    Represents the scope of bot commands, covering all private chats.
    """

    type: Literal["all_private_chats"] = Field(default="all_private_chats")


class BotCommandScopeAllGroupChats(BaseModel):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.
    """

    type: Literal["all_group_chats"] = Field(default="all_group_chats")


class BotCommandScopeAllChatAdministrators(BaseModel):
    """
    Represents the scope of bot commands, covering all group and supergroup chat
    administrators.
    """

    type: Literal["all_chat_administrators"] = Field(default="all_chat_administrators")


class BotCommandScopeChat(BaseModel):
    """
    Represents the scope of bot commands, covering a specific chat.
    """

    type: Literal["chat"] = Field(default="chat")
    chat_id: Union[int, str] = Field()


class BotCommandScopeChatAdministrators(BaseModel):
    """
    Represents the scope of bot commands, covering all administrators of a specific
    group or supergroup chat.
    """

    type: Literal["chat_administrators"] = Field(default="chat_administrators")
    chat_id: Union[int, str] = Field()


class BotCommandScopeChatMember(BaseModel):
    """
    Represents the scope of bot commands, covering a specific member of a group or
    supergroup chat.
    """

    type: Literal["chat_member"] = Field(default="chat_member")
    chat_id: Union[int, str] = Field()
    user_id: int = Field()


class MenuButtonCommands(BaseModel):
    """
    Represents a menu button, which opens the bot's list of commands.
    """

    type: Literal["commands"] = Field(default="commands")


class MenuButtonWebApp(BaseModel):
    """
    Represents a menu button, which launches a Web App.
    """

    type: Literal["web_app"] = Field(default="web_app")
    text: str = Field()
    web_app: "WebAppInfo" = Field()


class MenuButtonDefault(BaseModel):
    """
    Describes that no specific value for the menu button was set.
    """

    type: Literal["default"] = Field(default="default")


class ResponseParameters(BaseModel):
    """
    Describes why a request was unsuccessful.
    """

    migrate_to_chat_id: Optional[int] = Field(default=None)
    retry_after: Optional[int] = Field(default=None)


class InputMediaPhoto(BaseModel):
    """
    Represents a photo to be sent.
    """

    type: Literal["photo"] = Field(default="photo")
    media: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    has_spoiler: Optional[bool] = Field(default=None)


class InputMediaVideo(BaseModel):
    """
    Represents a video to be sent.
    """

    type: Literal["video"] = Field(default="video")
    media: str = Field()
    thumb: Optional[Union["InputFile", str]] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    width: Optional[int] = Field(default=None)
    height: Optional[int] = Field(default=None)
    duration: Optional[int] = Field(default=None)
    supports_streaming: Optional[bool] = Field(default=None)
    has_spoiler: Optional[bool] = Field(default=None)


class InputMediaAnimation(BaseModel):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be
    sent.
    """

    type: Literal["animation"] = Field(default="animation")
    media: str = Field()
    thumb: Optional[Union["InputFile", str]] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    width: Optional[int] = Field(default=None)
    height: Optional[int] = Field(default=None)
    duration: Optional[int] = Field(default=None)
    has_spoiler: Optional[bool] = Field(default=None)


class InputMediaAudio(BaseModel):
    """
    Represents an audio file to be treated as music to be sent.
    """

    type: Literal["audio"] = Field(default="audio")
    media: str = Field()
    thumb: Optional[Union["InputFile", str]] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    duration: Optional[int] = Field(default=None)
    performer: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)


class InputMediaDocument(BaseModel):
    """
    Represents a general file to be sent.
    """

    type: Literal["document"] = Field(default="document")
    media: str = Field()
    thumb: Optional[Union["InputFile", str]] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    disable_content_type_detection: Optional[bool] = Field(default=None)


class InputFile(BaseModel):
    """
    This object represents the contents of a file to be uploaded. Must be posted using
    multipart/form-data in the usual way that files are uploaded via the browser.
    """

    pass


class Sticker(BaseModel):
    """
    This object represents a sticker.
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    type: Literal["regular", "mask", "custom_emoji"] = Field()
    width: int = Field()
    height: int = Field()
    is_animated: bool = Field()
    is_video: bool = Field()
    thumb: Optional["PhotoSize"] = Field(default=None)
    emoji: Optional[str] = Field(default=None)
    set_name: Optional[str] = Field(default=None)
    premium_animation: Optional["File"] = Field(default=None)
    mask_position: Optional["MaskPosition"] = Field(default=None)
    custom_emoji_id: Optional[str] = Field(default=None)
    file_size: Optional[int] = Field(default=None)


class StickerSet(BaseModel):
    """
    This object represents a sticker set.
    """

    name: str = Field()
    title: str = Field()
    sticker_type: Literal["regular", "mask", "custom_emoji"] = Field()
    is_animated: bool = Field()
    is_video: bool = Field()
    stickers: List["Sticker"] = Field()
    thumb: Optional["PhotoSize"] = Field(default=None)


class MaskPosition(BaseModel):
    """
    This object describes the position on faces where a mask should be placed by
    default.
    """

    point: Literal["forehead", "eyes", "mouth", "chin"] = Field()
    x_shift: float = Field()
    y_shift: float = Field()
    scale: float = Field()


class InlineQuery(BaseModel):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.
    """

    id: str = Field()
    from_: "User" = Field(alias="from")
    query: str = Field()
    offset: str = Field()
    chat_type: Literal["sender", "private", "group", "supergroup", "channel"] = Field(
        default=None
    )
    location: Optional["Location"] = Field(default=None)


class InlineQueryResultArticle(BaseModel):
    """
    Represents a link to an article or web page.
    """

    type: Literal["article"] = Field(default="article")
    id: str = Field()
    title: str = Field()
    input_message_content: "InputMessageContent" = Field()
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    url: Optional[str] = Field(default=None)
    hide_url: Optional[bool] = Field(default=None)
    description: Optional[str] = Field(default=None)
    thumb_url: Optional[str] = Field(default=None)
    thumb_width: Optional[int] = Field(default=None)
    thumb_height: Optional[int] = Field(default=None)


class InlineQueryResultPhoto(BaseModel):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the photo.
    """

    type: Literal["photo"] = Field(default="photo")
    id: str = Field()
    photo_url: str = Field()
    thumb_url: str = Field()
    photo_width: Optional[int] = Field(default=None)
    photo_height: Optional[int] = Field(default=None)
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultGif(BaseModel):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will
    be sent by the user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    animation.
    """

    type: Literal["gif"] = Field(default="gif")
    id: str = Field()
    gif_url: str = Field()
    gif_width: Optional[int] = Field(default=None)
    gif_height: Optional[int] = Field(default=None)
    gif_duration: Optional[int] = Field(default=None)
    thumb_url: str = Field()
    thumb_mime_type: Literal["image/jpeg", "image/gif", "video/mp4"] = Field(
        default="image/jpeg"
    )
    title: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultMpeg4Gif(BaseModel):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By
    default, this animated MPEG-4 file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the animation.
    """

    type: Literal["mpeg4_gif"] = Field(default="mpeg4_gif")
    id: str = Field()
    mpeg4_url: str = Field()
    mpeg4_width: Optional[int] = Field(default=None)
    mpeg4_height: Optional[int] = Field(default=None)
    mpeg4_duration: Optional[int] = Field(default=None)
    thumb_url: str = Field()
    thumb_mime_type: Literal["image/jpeg", "image/gif", "video/mp4"] = Field(
        default="image/jpeg"
    )
    title: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultVideo(BaseModel):
    """
    Represents a link to a page containing an embedded video player or a video file. By
    default, this video file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the video. If an InlineQueryResultVideo message
    contains an embedded video (e.g., YouTube), you must replace its content using
    input_message_content.
    """

    type: Literal["video"] = Field(default="video")
    id: str = Field()
    video_url: str = Field()
    mime_type: Literal["text/html", "video/mp4"] = Field()
    thumb_url: str = Field()
    title: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    video_width: Optional[int] = Field(default=None)
    video_height: Optional[int] = Field(default=None)
    video_duration: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultAudio(BaseModel):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the audio.
    """

    type: Literal["audio"] = Field(default="audio")
    id: str = Field()
    audio_url: str = Field()
    title: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    performer: Optional[str] = Field(default=None)
    audio_duration: Optional[int] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultVoice(BaseModel):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By
    default, this voice recording will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    the voice message.
    """

    type: Literal["voice"] = Field(default="voice")
    id: str = Field()
    voice_url: str = Field()
    title: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    voice_duration: Optional[int] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultDocument(BaseModel):
    """
    Represents a link to a file. By default, this file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the file. Currently, only .PDF and .ZIP files
    can be sent using this method.
    """

    type: Literal["document"] = Field(default="document")
    id: str = Field()
    title: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    document_url: str = Field()
    mime_type: Literal["application/pdf", "application/zip"] = Field()
    description: Optional[str] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)
    thumb_url: Optional[str] = Field(default=None)
    thumb_width: Optional[int] = Field(default=None)
    thumb_height: Optional[int] = Field(default=None)


class InlineQueryResultLocation(BaseModel):
    """
    Represents a location on a map. By default, the location will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the location.
    """

    type: Literal["location"] = Field(default="location")
    id: str = Field()
    latitude: float = Field()
    longitude: float = Field()
    title: str = Field()
    horizontal_accuracy: Optional[float] = Field(default=None)
    live_period: Optional[int] = Field(default=None)
    heading: Optional[int] = Field(default=None)
    proximity_alert_radius: Optional[int] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)
    thumb_url: Optional[str] = Field(default=None)
    thumb_width: Optional[int] = Field(default=None)
    thumb_height: Optional[int] = Field(default=None)


class InlineQueryResultVenue(BaseModel):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified content
    instead of the venue.
    """

    type: Literal["venue"] = Field(default="venue")
    id: str = Field()
    latitude: float = Field()
    longitude: float = Field()
    title: str = Field()
    address: str = Field()
    foursquare_id: Optional[str] = Field(default=None)
    foursquare_type: Optional[str] = Field(default=None)
    google_place_id: Optional[str] = Field(default=None)
    google_place_type: Optional[str] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)
    thumb_url: Optional[str] = Field(default=None)
    thumb_width: Optional[int] = Field(default=None)
    thumb_height: Optional[int] = Field(default=None)


class InlineQueryResultContact(BaseModel):
    """
    Represents a contact with a phone number. By default, this contact will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the contact.
    """

    type: Literal["contact"] = Field(default="contact")
    id: str = Field()
    phone_number: str = Field()
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    vcard: Optional[str] = Field(default=None)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)
    thumb_url: Optional[str] = Field(default=None)
    thumb_width: Optional[int] = Field(default=None)
    thumb_height: Optional[int] = Field(default=None)


class InlineQueryResultGame(BaseModel):
    """
    Represents a Game.
    """

    type: Literal["game"] = Field(default="game")
    id: str = Field()
    game_short_name: str = Field()
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)


class InlineQueryResultCachedPhoto(BaseModel):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo
    will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    photo.
    """

    type: Literal["photo"] = Field(default="photo")
    id: str = Field()
    photo_file_id: str = Field()
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedGif(BaseModel):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By
    default, this animated GIF file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with specified
    content instead of the animation.
    """

    type: Literal["gif"] = Field(default="gif")
    id: str = Field()
    gif_file_id: str = Field()
    title: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedMpeg4Gif(BaseModel):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored
    on the Telegram servers. By default, this animated MPEG-4 file will be sent by the
    user with an optional caption. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the animation.
    """

    type: Literal["mpeg4_gif"] = Field(default="mpeg4_gif")
    id: str = Field()
    mpeg4_file_id: str = Field()
    title: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedSticker(BaseModel):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this
    sticker will be sent by the user. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the sticker.
    """

    type: Literal["sticker"] = Field(default="sticker")
    id: str = Field()
    sticker_file_id: str = Field()
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedDocument(BaseModel):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file
    will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    file.
    """

    type: Literal["document"] = Field(default="document")
    id: str = Field()
    title: str = Field()
    document_file_id: str = Field()
    description: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedVideo(BaseModel):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this
    video file will be sent by the user with an optional caption. Alternatively, you can
    use input_message_content to send a message with the specified content instead of
    the video.
    """

    type: Literal["video"] = Field(default="video")
    id: str = Field()
    video_file_id: str = Field()
    title: str = Field()
    description: Optional[str] = Field(default=None)
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedVoice(BaseModel):
    """
    Represents a link to a voice message stored on the Telegram servers. By default,
    this voice message will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    voice message.
    """

    type: Literal["voice"] = Field(default="voice")
    id: str = Field()
    voice_file_id: str = Field()
    title: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedAudio(BaseModel):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default,
    this audio file will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    audio.
    """

    type: Literal["audio"] = Field(default="audio")
    id: str = Field()
    audio_file_id: str = Field()
    caption: Optional[str] = Field(default=None)
    parse_mode: Optional[str] = Field(default=None)
    caption_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    reply_markup: Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: Optional["InputMessageContent"] = Field(default=None)


class InputTextMessageContent(BaseModel):
    """
    Represents the content of a text message to be sent as the result of an inline
    query.
    """

    message_text: str = Field()
    parse_mode: Optional[str] = Field(default=None)
    entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    disable_web_page_preview: Optional[bool] = Field(default=None)


class InputLocationMessageContent(BaseModel):
    """
    Represents the content of a location message to be sent as the result of an inline
    query.
    """

    latitude: float = Field()
    longitude: float = Field()
    horizontal_accuracy: Optional[float] = Field(default=None)
    live_period: Optional[int] = Field(default=None)
    heading: Optional[int] = Field(default=None)
    proximity_alert_radius: Optional[int] = Field(default=None)


class InputVenueMessageContent(BaseModel):
    """
    Represents the content of a venue message to be sent as the result of an inline
    query.
    """

    latitude: float = Field()
    longitude: float = Field()
    title: str = Field()
    address: str = Field()
    foursquare_id: Optional[str] = Field(default=None)
    foursquare_type: Optional[str] = Field(default=None)
    google_place_id: Optional[str] = Field(default=None)
    google_place_type: Optional[str] = Field(default=None)


class InputContactMessageContent(BaseModel):
    """
    Represents the content of a contact message to be sent as the result of an inline
    query.
    """

    phone_number: str = Field()
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    vcard: Optional[str] = Field(default=None)


class InputInvoiceMessageContent(BaseModel):
    """
    Represents the content of an invoice message to be sent as the result of an inline
    query.
    """

    title: str = Field()
    description: str = Field()
    payload: str = Field()
    provider_token: str = Field()
    currency: str = Field()
    prices: List["LabeledPrice"] = Field()
    max_tip_amount: Optional[int] = Field(default=None)
    suggested_tip_amounts: Optional[List[int]] = Field(default_factory=list)
    provider_data: Optional[str] = Field(default=None)
    photo_url: Optional[str] = Field(default=None)
    photo_size: Optional[int] = Field(default=None)
    photo_width: Optional[int] = Field(default=None)
    photo_height: Optional[int] = Field(default=None)
    need_name: Optional[bool] = Field(default=None)
    need_phone_number: Optional[bool] = Field(default=None)
    need_email: Optional[bool] = Field(default=None)
    need_shipping_address: Optional[bool] = Field(default=None)
    send_phone_number_to_provider: Optional[bool] = Field(default=None)
    send_email_to_provider: Optional[bool] = Field(default=None)
    is_flexible: Optional[bool] = Field(default=None)


class ChosenInlineResult(BaseModel):
    """
    Represents a result of an inline query that was chosen by the user and sent to their
    chat partner.
    """

    result_id: str = Field()
    from_: "User" = Field(alias="from")
    location: Optional["Location"] = Field(default=None)
    inline_message_id: Optional[str] = Field(default=None)
    query: str = Field()


class SentWebAppMessage(BaseModel):
    """
    Describes an inline message sent by a Web App on behalf of a user.
    """

    inline_message_id: Optional[str] = Field(default=None)


class LabeledPrice(BaseModel):
    """
    This object represents a portion of the price for goods or services.
    """

    label: str = Field()
    amount: int = Field()


class Invoice(BaseModel):
    """
    This object contains basic information about an invoice.
    """

    title: str = Field()
    description: str = Field()
    start_parameter: str = Field()
    currency: str = Field()
    total_amount: int = Field()


class ShippingAddress(BaseModel):
    """
    This object represents a shipping address.
    """

    country_code: str = Field()
    state: str = Field()
    city: str = Field()
    street_line1: str = Field()
    street_line2: str = Field()
    post_code: str = Field()


class OrderInfo(BaseModel):
    """
    This object represents information about an order.
    """

    name: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    shipping_address: Optional["ShippingAddress"] = Field(default=None)


class ShippingOption(BaseModel):
    """
    This object represents one shipping option.
    """

    id: str = Field()
    title: str = Field()
    prices: List["LabeledPrice"] = Field()


class SuccessfulPayment(BaseModel):
    """
    This object contains basic information about a successful payment.
    """

    currency: str = Field()
    total_amount: int = Field()
    invoice_payload: str = Field()
    shipping_option_id: Optional[str] = Field(default=None)
    order_info: Optional["OrderInfo"] = Field(default=None)
    telegram_payment_charge_id: str = Field()
    provider_payment_charge_id: str = Field()


class ShippingQuery(BaseModel):
    """
    This object contains information about an incoming shipping query.
    """

    id: str = Field()
    from_: "User" = Field(alias="from")
    invoice_payload: str = Field()
    shipping_address: "ShippingAddress" = Field()


class PreCheckoutQuery(BaseModel):
    """
    This object contains information about an incoming pre-checkout query.
    """

    id: str = Field()
    from_: "User" = Field(alias="from")
    currency: str = Field()
    total_amount: int = Field()
    invoice_payload: str = Field()
    shipping_option_id: Optional[str] = Field(default=None)
    order_info: Optional["OrderInfo"] = Field(default=None)


class PassportData(BaseModel):
    """
    Describes Telegram Passport data shared with the bot by the user.
    """

    data: List["EncryptedPassportElement"] = Field()
    credentials: "EncryptedCredentials" = Field()


class PassportFile(BaseModel):
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram
    Passport files are in JPEG format when decrypted and don't exceed 10MB.
    """

    file_id: str = Field()
    file_unique_id: str = Field()
    file_size: int = Field()
    file_date: int = Field()


class EncryptedPassportElement(BaseModel):
    """
    Describes documents or other Telegram Passport elements shared with the bot by the
    user.
    """

    type: Literal[
        "personal_details",
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "address",
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
        "phone_number",
        "email",
    ] = Field()
    data: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    files: Optional[List["PassportFile"]] = Field(default_factory=list)
    front_side: Optional["PassportFile"] = Field(default=None)
    reverse_side: Optional["PassportFile"] = Field(default=None)
    selfie: Optional["PassportFile"] = Field(default=None)
    translation: Optional[List["PassportFile"]] = Field(default_factory=list)
    hash: str = Field()


class EncryptedCredentials(BaseModel):
    """
    Describes data required for decrypting and authenticating EncryptedPassportElement.
    See the Telegram Passport Documentation for a complete description of the data
    decryption and authentication processes.
    """

    data: str = Field()
    hash: str = Field()
    secret: str = Field()


class PassportElementErrorDataField(BaseModel):
    """
    Represents an issue in one of the data fields that was provided by the user. The
    error is considered resolved when the field's value changes.
    """

    source: Literal["data"] = Field(default="data")
    type: Literal[
        "personal_details",
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "address",
    ] = Field()
    field_name: str = Field()
    data_hash: str = Field()
    message: str = Field()


class PassportElementErrorFrontSide(BaseModel):
    """
    Represents an issue with the front side of a document. The error is considered
    resolved when the file with the front side of the document changes.
    """

    source: Literal["front_side"] = Field(default="front_side")
    type: Literal[
        "passport", "driver_license", "identity_card", "internal_passport"
    ] = Field()
    file_hash: str = Field()
    message: str = Field()


class PassportElementErrorReverseSide(BaseModel):
    """
    Represents an issue with the reverse side of a document. The error is considered
    resolved when the file with reverse side of the document changes.
    """

    source: Literal["reverse_side"] = Field(default="reverse_side")
    type: Literal["driver_license", "identity_card"] = Field()
    file_hash: str = Field()
    message: str = Field()


class PassportElementErrorSelfie(BaseModel):
    """
    Represents an issue with the selfie with a document. The error is considered
    resolved when the file with the selfie changes.
    """

    source: Literal["selfie"] = Field(default="selfie")
    type: Literal[
        "passport", "driver_license", "identity_card", "internal_passport"
    ] = Field()
    file_hash: str = Field()
    message: str = Field()


class PassportElementErrorFile(BaseModel):
    """
    Represents an issue with a document scan. The error is considered resolved when the
    file with the document scan changes.
    """

    source: Literal["file"] = Field(default="file")
    type: Literal[
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = Field()
    file_hash: str = Field()
    message: str = Field()


class PassportElementErrorFiles(BaseModel):
    """
    Represents an issue with a list of scans. The error is considered resolved when the
    list of files containing the scans changes.
    """

    source: Literal["files"] = Field(default="files")
    type: Literal[
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = Field()
    file_hashes: List[str] = Field()
    message: str = Field()


class PassportElementErrorTranslationFile(BaseModel):
    """
    Represents an issue with one of the files that constitute the translation of a
    document. The error is considered resolved when the file changes.
    """

    source: Literal["translation_file"] = Field(default="translation_file")
    type: Literal[
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = Field()
    file_hash: str = Field()
    message: str = Field()


class PassportElementErrorTranslationFiles(BaseModel):
    """
    Represents an issue with the translated version of a document. The error is
    considered resolved when a file with the document translation change.
    """

    source: Literal["translation_files"] = Field(default="translation_files")
    type: Literal[
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = Field()
    file_hashes: List[str] = Field()
    message: str = Field()


class PassportElementErrorUnspecified(BaseModel):
    """
    Represents an issue in an unspecified place. The error is considered resolved when
    new data is added.
    """

    source: Literal["unspecified"] = Field(default="unspecified")
    type: str = Field()
    element_hash: str = Field()
    message: str = Field()


class Game(BaseModel):
    """
    This object represents a game. Use BotFather to create and edit games, their short
    names will act as unique identifiers.
    """

    title: str = Field()
    description: str = Field()
    photo: List["PhotoSize"] = Field()
    text: Optional[str] = Field(default=None)
    text_entities: Optional[List["MessageEntity"]] = Field(default_factory=list)
    animation: Optional["Animation"] = Field(default=None)


class CallbackGame(BaseModel):
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.
    """

    pass


class GameHighScore(BaseModel):
    """
    This object represents one row of the high scores table for a game.
    """

    position: int = Field()
    user: "User" = Field()
    score: int = Field()


ChatMember = Annotated[
    Union[
        ChatMemberOwner,
        ChatMemberAdministrator,
        ChatMemberMember,
        ChatMemberRestricted,
        ChatMemberLeft,
        ChatMemberBanned,
    ],
    Field(discriminator="status"),
]


BotCommandScope = Annotated[
    Union[
        BotCommandScopeDefault,
        BotCommandScopeAllPrivateChats,
        BotCommandScopeAllGroupChats,
        BotCommandScopeAllChatAdministrators,
        BotCommandScopeChat,
        BotCommandScopeChatAdministrators,
        BotCommandScopeChatMember,
    ],
    Field(discriminator="type"),
]


MenuButton = Annotated[
    Union[
        MenuButtonCommands,
        MenuButtonWebApp,
        MenuButtonDefault,
    ],
    Field(discriminator="type"),
]


InputMedia = Annotated[
    Union[
        InputMediaAnimation,
        InputMediaDocument,
        InputMediaAudio,
        InputMediaPhoto,
        InputMediaVideo,
    ],
    Field(discriminator="type"),
]


InlineQueryResult = Annotated[
    Union[
        InlineQueryResultCachedAudio,
        InlineQueryResultCachedDocument,
        InlineQueryResultCachedGif,
        InlineQueryResultCachedMpeg4Gif,
        InlineQueryResultCachedPhoto,
        InlineQueryResultCachedSticker,
        InlineQueryResultCachedVideo,
        InlineQueryResultCachedVoice,
        InlineQueryResultArticle,
        InlineQueryResultAudio,
        InlineQueryResultContact,
        InlineQueryResultGame,
        InlineQueryResultDocument,
        InlineQueryResultGif,
        InlineQueryResultLocation,
        InlineQueryResultMpeg4Gif,
        InlineQueryResultPhoto,
        InlineQueryResultVenue,
        InlineQueryResultVideo,
        InlineQueryResultVoice,
    ],
    Field(discriminator="type"),
]


InputMessageContent = Annotated[
    Union[
        InputTextMessageContent,
        InputLocationMessageContent,
        InputVenueMessageContent,
        InputContactMessageContent,
        InputInvoiceMessageContent,
    ],
    Field(discriminator=None),
]


PassportElementError = Annotated[
    Union[
        PassportElementErrorDataField,
        PassportElementErrorFrontSide,
        PassportElementErrorReverseSide,
        PassportElementErrorSelfie,
        PassportElementErrorFile,
        PassportElementErrorFiles,
        PassportElementErrorTranslationFile,
        PassportElementErrorTranslationFiles,
        PassportElementErrorUnspecified,
    ],
    Field(discriminator="source"),
]


for v in locals().copy().values():
    if inspect.isclass(v) and issubclass(v, BaseModel):
        v.update_forward_refs()

__all__ = (
    "Update",
    "WebhookInfo",
    "User",
    "Chat",
    "Message",
    "MessageId",
    "MessageEntity",
    "PhotoSize",
    "Animation",
    "Audio",
    "Document",
    "Video",
    "VideoNote",
    "Voice",
    "Contact",
    "Dice",
    "PollOption",
    "PollAnswer",
    "Poll",
    "Location",
    "Venue",
    "WebAppData",
    "ProximityAlertTriggered",
    "MessageAutoDeleteTimerChanged",
    "ForumTopicCreated",
    "ForumTopicClosed",
    "ForumTopicEdited",
    "ForumTopicReopened",
    "GeneralForumTopicHidden",
    "GeneralForumTopicUnhidden",
    "WriteAccessAllowed",
    "VideoChatScheduled",
    "VideoChatStarted",
    "VideoChatEnded",
    "VideoChatParticipantsInvited",
    "UserProfilePhotos",
    "File",
    "WebAppInfo",
    "ReplyKeyboardMarkup",
    "KeyboardButton",
    "KeyboardButtonPollType",
    "ReplyKeyboardRemove",
    "InlineKeyboardMarkup",
    "InlineKeyboardButton",
    "LoginUrl",
    "CallbackQuery",
    "ForceReply",
    "ChatPhoto",
    "ChatInviteLink",
    "ChatAdministratorRights",
    "ChatMember",
    "ChatMemberOwner",
    "ChatMemberAdministrator",
    "ChatMemberMember",
    "ChatMemberRestricted",
    "ChatMemberLeft",
    "ChatMemberBanned",
    "ChatMemberUpdated",
    "ChatJoinRequest",
    "ChatPermissions",
    "ChatLocation",
    "ForumTopic",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeDefault",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonWebApp",
    "MenuButtonDefault",
    "ResponseParameters",
    "InputMedia",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputFile",
    "Sticker",
    "StickerSet",
    "MaskPosition",
    "InlineQuery",
    "InlineQueryResult",
    "InlineQueryResultArticle",
    "InlineQueryResultPhoto",
    "InlineQueryResultGif",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultVideo",
    "InlineQueryResultAudio",
    "InlineQueryResultVoice",
    "InlineQueryResultDocument",
    "InlineQueryResultLocation",
    "InlineQueryResultVenue",
    "InlineQueryResultContact",
    "InlineQueryResultGame",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultCachedAudio",
    "InputMessageContent",
    "InputTextMessageContent",
    "InputLocationMessageContent",
    "InputVenueMessageContent",
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "ChosenInlineResult",
    "SentWebAppMessage",
    "LabeledPrice",
    "Invoice",
    "ShippingAddress",
    "OrderInfo",
    "ShippingOption",
    "SuccessfulPayment",
    "ShippingQuery",
    "PreCheckoutQuery",
    "PassportData",
    "PassportFile",
    "EncryptedPassportElement",
    "EncryptedCredentials",
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "Game",
    "CallbackGame",
    "GameHighScore",
)
