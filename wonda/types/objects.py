from typing import NamedTuple

from .enums import *
from .helper import *


class Update(Model):
    """
    This object represents an incoming update. At most one of the optional
    parameters can be present in any given update.
    """

    update_id: int
    message: "Message | None" = None
    edited_message: "Message | None" = None
    channel_post: "Message | None" = None
    edited_channel_post: "Message | None" = None
    inline_query: "InlineQuery | None" = None
    chosen_inline_result: "ChosenInlineResult | None" = None
    callback_query: "CallbackQuery | None" = None
    shipping_query: "ShippingQuery | None" = None
    pre_checkout_query: "PreCheckoutQuery | None" = None
    poll: "Poll | None" = None
    poll_answer: "PollAnswer | None" = None
    my_chat_member: "ChatMemberUpdated | None" = None
    chat_member: "ChatMemberUpdated | None" = None
    chat_join_request: "ChatJoinRequest | None" = None


class WebhookInfo(Model):
    """
    Describes the current status of a webhook.
    """

    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: str | None = None
    last_error_date: int | None = None
    last_error_message: str | None = None
    last_synchronization_error_date: int | None = None
    max_connections: int | None = None
    allowed_updates: "list[str] | None" = None


class User(Model):
    """
    This object represents a Telegram user or bot.
    """

    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None
    is_premium: bool | None = None
    added_to_attachment_menu: bool | None = None
    can_join_groups: bool | None = None
    can_read_all_group_messages: bool | None = None
    supports_inline_queries: bool | None = None


class Chat(Model):
    """
    This object represents a chat.
    """

    id: int
    type: ChatType
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_forum: bool | None = None
    photo: "ChatPhoto | None" = None
    active_usernames: "list[str] | None" = None
    emoji_status_custom_emoji_id: str | None = None
    emoji_status_expiration_date: int | None = None
    bio: str | None = None
    has_private_forwards: bool | None = None
    has_restricted_voice_and_video_messages: bool | None = None
    join_to_send_messages: bool | None = None
    join_by_request: bool | None = None
    description: str | None = None
    invite_link: str | None = None
    pinned_message: "Message | None" = None
    permissions: "ChatPermissions | None" = None
    slow_mode_delay: int | None = None
    message_auto_delete_time: int | None = None
    has_aggressive_anti_spam_enabled: bool | None = None
    has_hidden_members: bool | None = None
    has_protected_content: bool | None = None
    sticker_set_name: str | None = None
    can_set_sticker_set: bool | None = None
    linked_chat_id: int | None = None
    location: "ChatLocation | None" = None


class Message(Model):
    """
    This object represents a message.
    """

    message_id: int
    date: int
    chat: "Chat"
    message_thread_id: int | None = None
    from_: "User | None" = None
    sender_chat: "Chat | None" = None
    forward_from: "User | None" = None
    forward_from_chat: "Chat | None" = None
    forward_from_message_id: int | None = None
    forward_signature: str | None = None
    forward_sender_name: str | None = None
    forward_date: int | None = None
    is_topic_message: bool | None = None
    is_automatic_forward: bool | None = None
    reply_to_message: "Message | None" = None
    via_bot: "User | None" = None
    edit_date: int | None = None
    has_protected_content: bool | None = None
    media_group_id: str | None = None
    author_signature: str | None = None
    text: str | None = None
    entities: "list[MessageEntity] | None" = None
    animation: "Animation | None" = None
    audio: "Audio | None" = None
    document: "Document | None" = None
    photo: "list[PhotoSize] | None" = None
    sticker: "Sticker | None" = None
    story: "Story | None" = None
    video: "Video | None" = None
    video_note: "VideoNote | None" = None
    voice: "Voice | None" = None
    caption: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    has_media_spoiler: bool | None = None
    contact: "Contact | None" = None
    dice: "Dice | None" = None
    game: "Game | None" = None
    poll: "Poll | None" = None
    venue: "Venue | None" = None
    location: "Location | None" = None
    new_chat_members: "list[User] | None" = None
    left_chat_member: "User | None" = None
    new_chat_title: str | None = None
    new_chat_photo: "list[PhotoSize] | None" = None
    delete_chat_photo: bool | None = None
    group_chat_created: bool | None = None
    supergroup_chat_created: bool | None = None
    channel_chat_created: bool | None = None
    message_auto_delete_timer_changed: "MessageAutoDeleteTimerChanged | None" = None
    migrate_to_chat_id: int | None = None
    migrate_from_chat_id: int | None = None
    pinned_message: "Message | None" = None
    invoice: "Invoice | None" = None
    successful_payment: "SuccessfulPayment | None" = None
    user_shared: "UserShared | None" = None
    chat_shared: "ChatShared | None" = None
    connected_website: str | None = None
    write_access_allowed: "WriteAccessAllowed | None" = None
    passport_data: "PassportData | None" = None
    proximity_alert_triggered: "ProximityAlertTriggered | None" = None
    forum_topic_created: "ForumTopicCreated | None" = None
    forum_topic_edited: "ForumTopicEdited | None" = None
    forum_topic_closed: "ForumTopicClosed | None" = None
    forum_topic_reopened: "ForumTopicReopened | None" = None
    general_forum_topic_hidden: "GeneralForumTopicHidden | None" = None
    general_forum_topic_unhidden: "GeneralForumTopicUnhidden | None" = None
    video_chat_scheduled: "VideoChatScheduled | None" = None
    video_chat_started: "VideoChatStarted | None" = None
    video_chat_ended: "VideoChatEnded | None" = None
    video_chat_participants_invited: "VideoChatParticipantsInvited | None" = None
    web_app_data: "WebAppData | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None


class MessageId(Model):
    """
    This object represents a unique message identifier.
    """

    message_id: int


class MessageEntity(Model):
    """
    This object represents one special entity in a text message. For
    example, hashtags, usernames, URLs, etc.
    """

    type: MessageEntityType
    offset: int
    length: int
    url: str | None = None
    user: "User | None" = None
    language: str | None = None
    custom_emoji_id: str | None = None


class PhotoSize(Model):
    """
    This object represents one size of a photo or a file / sticker
    thumbnail.
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int | None = None


class Animation(Model):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC
    video without sound).
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: "PhotoSize | None" = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None


class Audio(Model):
    """
    This object represents an audio file to be treated as music by the
    Telegram clients.
    """

    file_id: str
    file_unique_id: str
    duration: int
    performer: str | None = None
    title: str | None = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None
    thumbnail: "PhotoSize | None" = None


class Document(Model):
    """
    This object represents a general file (as opposed to photos, voice
    messages and audio files).
    """

    file_id: str
    file_unique_id: str
    thumbnail: "PhotoSize | None" = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None


class Story(Model):
    """
    This object represents a message about a forwarded story in the chat.
    Currently holds no information.
    """

    pass


class Video(Model):
    """
    This object represents a video file.
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: "PhotoSize | None" = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None


class VideoNote(Model):
    """
    This object represents a video message (available in Telegram apps as
    of v.4.0).
    """

    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumbnail: "PhotoSize | None" = None
    file_size: int | None = None


class Voice(Model):
    """
    This object represents a voice note.
    """

    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str | None = None
    file_size: int | None = None


class Contact(Model):
    """
    This object represents a phone contact.
    """

    phone_number: str
    first_name: str
    last_name: str | None = None
    user_id: int | None = None
    vcard: str | None = None


class Dice(Model):
    """
    This object represents an animated emoji that displays a random value.
    """

    emoji: str
    value: int


class PollOption(Model):
    """
    This object contains information about one answer option in a poll.
    """

    text: str
    voter_count: int


class PollAnswer(Model):
    """
    This object represents an answer of a user in a non-anonymous poll.
    """

    poll_id: str
    option_ids: "list[int]"
    voter_chat: "Chat | None" = None
    user: "User | None" = None


class Poll(Model):
    """
    This object contains information about a poll.
    """

    id: str
    question: str
    options: "list[PollOption]"
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: PollType
    allows_multiple_answers: bool
    correct_option_id: int | None = None
    explanation: str | None = None
    explanation_entities: "list[MessageEntity] | None" = None
    open_period: int | None = None
    close_date: int | None = None


class Location(Model):
    """
    This object represents a point on the map.
    """

    longitude: float
    latitude: float
    horizontal_accuracy: float | None = None
    live_period: int | None = None
    heading: int | None = None
    proximity_alert_radius: int | None = None


class Venue(Model):
    """
    This object represents a venue.
    """

    location: "Location"
    title: str
    address: str
    foursquare_id: str | None = None
    foursquare_type: str | None = None
    google_place_id: str | None = None
    google_place_type: str | None = None


class WebAppData(Model):
    """
    Describes data sent from a Web App to the bot.
    """

    data: str
    button_text: str


class ProximityAlertTriggered(Model):
    """
    This object represents the content of a service message, sent whenever
    a user in the chat triggers a proximity alert set by another user.
    """

    traveler: "User"
    watcher: "User"
    distance: int


class MessageAutoDeleteTimerChanged(Model):
    """
    This object represents a service message about a change in auto-delete
    timer settings.
    """

    message_auto_delete_time: int


class ForumTopicCreated(Model):
    """
    This object represents a service message about a new forum topic
    created in the chat.
    """

    name: str
    icon_color: int
    icon_custom_emoji_id: str | None = None


class ForumTopicClosed(Model):
    """
    This object represents a service message about a forum topic closed in
    the chat. Currently holds no information.
    """

    pass


class ForumTopicEdited(Model):
    """
    This object represents a service message about an edited forum topic.
    """

    name: str | None = None
    icon_custom_emoji_id: str | None = None


class ForumTopicReopened(Model):
    """
    This object represents a service message about a forum topic reopened
    in the chat. Currently holds no information.
    """

    pass


class GeneralForumTopicHidden(Model):
    """
    This object represents a service message about General forum topic
    hidden in the chat. Currently holds no information.
    """

    pass


class GeneralForumTopicUnhidden(Model):
    """
    This object represents a service message about General forum topic
    unhidden in the chat. Currently holds no information.
    """

    pass


class UserShared(Model):
    """
    This object contains information about the user whose identifier was
    shared with the bot using a KeyboardButtonRequestUser button.
    """

    request_id: int
    user_id: int


class ChatShared(Model):
    """
    This object contains information about the chat whose identifier was
    shared with the bot using a KeyboardButtonRequestChat button.
    """

    request_id: int
    chat_id: int


class WriteAccessAllowed(Model):
    """
    This object represents a service message about a user allowing a bot
    to write messages after adding the bot to the attachment menu or
    launching a Web App from a link.
    """

    web_app_name: str | None = None


class VideoChatScheduled(Model):
    """
    This object represents a service message about a video chat scheduled
    in the chat.
    """

    start_date: int


class VideoChatStarted(Model):
    """
    This object represents a service message about a video chat started in
    the chat. Currently holds no information.
    """

    pass


class VideoChatEnded(Model):
    """
    This object represents a service message about a video chat ended in
    the chat.
    """

    duration: int


class VideoChatParticipantsInvited(Model):
    """
    This object represents a service message about new members invited to
    a video chat.
    """

    users: "list[User]"


class UserProfilePhotos(Model):
    """
    This object represent a user's profile pictures.
    """

    total_count: int
    photos: "list[list[PhotoSize]]"


class File(Model):
    """
    This object represents a file ready to be downloaded. The file can be
    downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed
    that the link will be valid for at least 1 hour. When the link
    expires, a new one can be requested by calling getFile. The maximum
    file size to download is 20 MB
    """

    file_id: str
    file_unique_id: str
    file_size: int | None = None
    file_path: str | None = None


class WebAppInfo(Model):
    """
    Describes a Web App.
    """

    url: str


class ReplyKeyboardMarkup(Model):
    """
    This object represents a custom keyboard with reply options (see
    Introduction to bots for details and examples).
    """

    keyboard: "list[list[KeyboardButton]]"
    is_persistent: bool | None = None
    resize_keyboard: bool | None = None
    one_time_keyboard: bool | None = None
    input_field_placeholder: str | None = None
    selective: bool | None = None


class KeyboardButton(Model):
    """
    This object represents one button of the reply keyboard. For simple
    text buttons, String can be used instead of this object to specify the
    button text. The optional fields web_app, request_user, request_chat,
    request_contact, request_location, and request_poll are mutually
    exclusive.
    """

    text: str
    request_user: "KeyboardButtonRequestUser | None" = None
    request_chat: "KeyboardButtonRequestChat | None" = None
    request_contact: bool | None = None
    request_location: bool | None = None
    request_poll: "KeyboardButtonPollType | None" = None
    web_app: "WebAppInfo | None" = None


class KeyboardButtonRequestUser(Model):
    """
    This object defines the criteria used to request a suitable user. The
    identifier of the selected user will be shared with the bot when the
    corresponding button is pressed. More about requesting users »
    """

    request_id: int
    user_is_bot: bool | None = None
    user_is_premium: bool | None = None


class KeyboardButtonRequestChat(Model):
    """
    This object defines the criteria used to request a suitable chat. The
    identifier of the selected chat will be shared with the bot when the
    corresponding button is pressed. More about requesting chats »
    """

    request_id: int
    chat_is_channel: bool
    chat_is_forum: bool | None = None
    chat_has_username: bool | None = None
    chat_is_created: bool | None = None
    user_administrator_rights: "ChatAdministratorRights | None" = None
    bot_administrator_rights: "ChatAdministratorRights | None" = None
    bot_is_member: bool | None = None


class KeyboardButtonPollType(Model):
    """
    This object represents type of a poll, which is allowed to be created
    and sent when the corresponding button is pressed.
    """

    type: str | None = None


class ReplyKeyboardRemove(Model):
    """
    Upon receiving a message with this object, Telegram clients will
    remove the current custom keyboard and display the default letter-
    keyboard. By default, custom keyboards are displayed until a new
    keyboard is sent by a bot. An exception is made for one-time keyboards
    that are hidden immediately after the user presses a button (see
    ReplyKeyboardMarkup).
    """

    remove_keyboard: bool
    selective: bool | None = None


class InlineKeyboardMarkup(Model):
    """
    This object represents an inline keyboard that appears right next to
    the message it belongs to.
    """

    inline_keyboard: "list[list[InlineKeyboardButton]]"


class InlineKeyboardButton(Model):
    """
    This object represents one button of an inline keyboard. You must use
    exactly one of the optional fields.
    """

    text: str
    url: str | None = None
    callback_data: str | None = None
    web_app: "WebAppInfo | None" = None
    login_url: "LoginUrl | None" = None
    switch_inline_query: str | None = None
    switch_inline_query_current_chat: str | None = None
    switch_inline_query_chosen_chat: "SwitchInlineQueryChosenChat | None" = None
    callback_game: "CallbackGame | None" = None
    pay: bool | None = None


class LoginUrl(Model):
    """
    This object represents a parameter of the inline keyboard button used
    to automatically authorize a user. Serves as a great replacement for
    the Telegram Login Widget when the user is coming from Telegram. All
    the user needs to do is tap/click a button and confirm that they want
    to log in: Telegram apps support these buttons as of version 5.7.
    Sample bot: @discussbot
    """

    url: str
    forward_text: str | None = None
    bot_username: str | None = None
    request_write_access: bool | None = None


class SwitchInlineQueryChosenChat(Model):
    """
    This object represents an inline button that switches the current user
    to inline mode in a chosen chat, with an optional default inline
    query.
    """

    query: str | None = None
    allow_user_chats: bool | None = None
    allow_bot_chats: bool | None = None
    allow_group_chats: bool | None = None
    allow_channel_chats: bool | None = None


class CallbackQuery(Model):
    """
    This object represents an incoming callback query from a callback
    button in an inline keyboard. If the button that originated the query
    was attached to a message sent by the bot, the field message will be
    present. If the button was attached to a message sent via the bot (in
    inline mode), the field inline_message_id will be present. Exactly one
    of the fields data or game_short_name will be present.
    """

    id: str
    from_: "User"
    chat_instance: str
    message: "Message | None" = None
    inline_message_id: str | None = None
    data: str | None = None
    game_short_name: str | None = None


class ForceReply(Model):
    """
    Upon receiving a message with this object, Telegram clients will
    display a reply interface to the user (act as if the user has selected
    the bot's message and tapped 'Reply'). This can be extremely useful if
    you want to create user-friendly step-by-step interfaces without
    having to sacrifice privacy mode.
    """

    force_reply: bool
    input_field_placeholder: str | None = None
    selective: bool | None = None


class ChatPhoto(Model):
    """
    This object represents a chat photo.
    """

    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


class ChatInviteLink(Model):
    """
    Represents an invite link for a chat.
    """

    invite_link: str
    creator: "User"
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: str | None = None
    expire_date: int | None = None
    member_limit: int | None = None
    pending_join_request_count: int | None = None


class ChatAdministratorRights(Model):
    """
    Represents the rights of an administrator in a chat.
    """

    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool | None = None
    can_edit_messages: bool | None = None
    can_pin_messages: bool | None = None
    can_manage_topics: bool | None = None


class ChatMember(Model, tag_field="status"):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:
    ChatMemberOwner ChatMemberAdministrator ChatMemberMember
    ChatMemberRestricted ChatMemberLeft ChatMemberBanned
    """


class ChatMemberOwner(ChatMember, tag="creator"):
    """
    Represents a chat member that owns the chat and has all administrator
    privileges.
    """

    user: "User"
    is_anonymous: bool
    custom_title: str | None = None


class ChatMemberAdministrator(ChatMember, tag="administrator"):
    """
    Represents a chat member that has some additional privileges.
    """

    user: "User"
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool | None = None
    can_edit_messages: bool | None = None
    can_pin_messages: bool | None = None
    can_manage_topics: bool | None = None
    custom_title: str | None = None


class ChatMemberMember(ChatMember, tag="member"):
    """
    Represents a chat member that has no additional privileges or
    restrictions.
    """

    user: "User"


class ChatMemberRestricted(ChatMember, tag="restricted"):
    """
    Represents a chat member that is under certain restrictions in the
    chat. Supergroups only.
    """

    user: "User"
    is_member: bool
    can_send_messages: bool
    can_send_audios: bool
    can_send_documents: bool
    can_send_photos: bool
    can_send_videos: bool
    can_send_video_notes: bool
    can_send_voice_notes: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool
    until_date: int


class ChatMemberLeft(ChatMember, tag="left"):
    """
    Represents a chat member that isn't currently a member of the chat,
    but may join it themselves.
    """

    user: "User"


class ChatMemberBanned(ChatMember, tag="kicked"):
    """
    Represents a chat member that was banned in the chat and can't return
    to the chat or view chat messages.
    """

    user: "User"
    until_date: int


class ChatMemberUpdated(Model):
    """
    This object represents changes in the status of a chat member.
    """

    chat: "Chat"
    from_: "User"
    date: int
    old_chat_member: "ChatMember"
    new_chat_member: "ChatMember"
    invite_link: "ChatInviteLink | None" = None
    via_chat_folder_invite_link: bool | None = None


class ChatJoinRequest(Model):
    """
    Represents a join request sent to a chat.
    """

    chat: "Chat"
    from_: "User"
    user_chat_id: int
    date: int
    bio: str | None = None
    invite_link: "ChatInviteLink | None" = None


class ChatPermissions(Model):
    """
    Describes actions that a non-administrator user is allowed to take in
    a chat.
    """

    can_send_messages: bool | None = None
    can_send_audios: bool | None = None
    can_send_documents: bool | None = None
    can_send_photos: bool | None = None
    can_send_videos: bool | None = None
    can_send_video_notes: bool | None = None
    can_send_voice_notes: bool | None = None
    can_send_polls: bool | None = None
    can_send_other_messages: bool | None = None
    can_add_web_page_previews: bool | None = None
    can_change_info: bool | None = None
    can_invite_users: bool | None = None
    can_pin_messages: bool | None = None
    can_manage_topics: bool | None = None


class ChatLocation(Model):
    """
    Represents a location to which a chat is connected.
    """

    location: "Location"
    address: str


class ForumTopic(Model):
    """
    This object represents a forum topic.
    """

    message_thread_id: int
    name: str
    icon_color: int
    icon_custom_emoji_id: str | None = None


class BotCommand(Model):
    """
    This object represents a bot command.
    """

    command: str
    description: str


class BotCommandScope(Model, tag_field="type"):
    """
    This object represents the scope to which bot commands are applied.
    Currently, the following 7 scopes are supported:
    BotCommandScopeDefault BotCommandScopeAllPrivateChats
    BotCommandScopeAllGroupChats BotCommandScopeAllChatAdministrators
    BotCommandScopeChat BotCommandScopeChatAdministrators
    BotCommandScopeChatMember
    """


class BotCommandScopeDefault(BotCommandScope, tag="default"):
    """
    Represents the default scope of bot commands. Default commands are
    used if no commands with a narrower scope are specified for the user.
    """


class BotCommandScopeAllPrivateChats(BotCommandScope, tag="all_private_chats"):
    """
    Represents the scope of bot commands, covering all private chats.
    """


class BotCommandScopeAllGroupChats(BotCommandScope, tag="all_group_chats"):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chats.
    """


class BotCommandScopeAllChatAdministrators(
    BotCommandScope, tag="all_chat_administrators"
):
    """
    Represents the scope of bot commands, covering all group and
    supergroup chat administrators.
    """


class BotCommandScopeChat(BotCommandScope, tag="chat"):
    """
    Represents the scope of bot commands, covering a specific chat.
    """

    chat_id: int | str


class BotCommandScopeChatAdministrators(BotCommandScope, tag="chat_administrators"):
    """
    Represents the scope of bot commands, covering all administrators of a
    specific group or supergroup chat.
    """

    chat_id: int | str


class BotCommandScopeChatMember(BotCommandScope, tag="chat_member"):
    """
    Represents the scope of bot commands, covering a specific member of a
    group or supergroup chat.
    """

    chat_id: int | str
    user_id: int


class BotName(Model):
    """
    This object represents the bot's name.
    """

    name: str


class BotDescription(Model):
    """
    This object represents the bot's description.
    """

    description: str


class BotShortDescription(Model):
    """
    This object represents the bot's short description.
    """

    short_description: str


class MenuButton(Model, tag_field="type"):
    """
    This object describes the bot's menu button in a private chat. It
    should be one of  MenuButtonCommands MenuButtonWebApp
    MenuButtonDefault
    """


class MenuButtonCommands(MenuButton, tag="commands"):
    """
    Represents a menu button, which opens the bot's list of commands.
    """


class MenuButtonWebApp(MenuButton, tag="web_app"):
    """
    Represents a menu button, which launches a Web App.
    """

    text: str
    web_app: "WebAppInfo"


class MenuButtonDefault(MenuButton, tag="default"):
    """
    Describes that no specific value for the menu button was set.
    """


class ResponseParameters(Model):
    """
    Describes why a request was unsuccessful.
    """

    migrate_to_chat_id: int | None = None
    retry_after: int | None = None


class InputMedia(Model, tag_field="type"):
    """
    This object represents the content of a media message to be sent. It
    should be one of  InputMediaAnimation InputMediaDocument
    InputMediaAudio InputMediaPhoto InputMediaVideo
    """


class InputMediaPhoto(InputMedia, tag="photo"):
    """
    Represents a photo to be sent.
    """

    media: str
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    has_spoiler: bool | None = None


class InputMediaVideo(InputMedia, tag="video"):
    """
    Represents a video to be sent.
    """

    media: str
    thumbnail: "InputFile | str | None" = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    width: int | None = None
    height: int | None = None
    duration: int | None = None
    supports_streaming: bool | None = None
    has_spoiler: bool | None = None


class InputMediaAnimation(InputMedia, tag="animation"):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound) to be sent.
    """

    media: str
    thumbnail: "InputFile | str | None" = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    width: int | None = None
    height: int | None = None
    duration: int | None = None
    has_spoiler: bool | None = None


class InputMediaAudio(InputMedia, tag="audio"):
    """
    Represents an audio file to be treated as music to be sent.
    """

    media: str
    thumbnail: "InputFile | str | None" = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    duration: int | None = None
    performer: str | None = None
    title: str | None = None


class InputMediaDocument(InputMedia, tag="document"):
    """
    Represents a general file to be sent.
    """

    media: str
    thumbnail: "InputFile | str | None" = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    disable_content_type_detection: bool | None = None


InputFile = NamedTuple("InputFile", [("name", str), ("content", bytes)])


class Sticker(Model):
    """
    This object represents a sticker.
    """

    file_id: str
    file_unique_id: str
    type: StickerType
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumbnail: "PhotoSize | None" = None
    emoji: str | None = None
    set_name: str | None = None
    premium_animation: "File | None" = None
    mask_position: "MaskPosition | None" = None
    custom_emoji_id: str | None = None
    needs_repainting: bool | None = None
    file_size: int | None = None


class StickerSet(Model):
    """
    This object represents a sticker set.
    """

    name: str
    title: str
    sticker_type: StickerSetStickerType
    is_animated: bool
    is_video: bool
    stickers: "list[Sticker]"
    thumbnail: "PhotoSize | None" = None


class MaskPosition(Model):
    """
    This object describes the position on faces where a mask should be
    placed by default.
    """

    point: MaskPositionPoint
    x_shift: float
    y_shift: float
    scale: float


class InputSticker(Model):
    """
    This object describes a sticker to be added to a sticker set.
    """

    sticker: "InputFile | str"
    emoji_list: "list[str]"
    mask_position: "MaskPosition | None" = None
    keywords: "list[str] | None" = None


class InlineQuery(Model):
    """
    This object represents an incoming inline query. When the user sends
    an empty query, your bot could return some default or trending
    results.
    """

    id: str
    from_: "User"
    query: str
    offset: str
    chat_type: InlineQueryChatType
    location: "Location | None" = None


class InlineQueryResultsButton(Model):
    """
    This object represents a button to be shown above inline query
    results. You must use exactly one of the optional fields.
    """

    text: str
    web_app: "WebAppInfo | None" = None
    start_parameter: str | None = None


class InlineQueryResult(Model, tag_field="type"):
    """
    This object represents one result of an inline query. Telegram clients
    currently support results of the following 20 types:
    InlineQueryResultCachedAudio InlineQueryResultCachedDocument
    InlineQueryResultCachedGif InlineQueryResultCachedMpeg4Gif
    InlineQueryResultCachedPhoto InlineQueryResultCachedSticker
    InlineQueryResultCachedVideo InlineQueryResultCachedVoice
    InlineQueryResultArticle InlineQueryResultAudio
    InlineQueryResultContact InlineQueryResultGame
    InlineQueryResultDocument InlineQueryResultGif
    InlineQueryResultLocation InlineQueryResultMpeg4Gif
    InlineQueryResultPhoto InlineQueryResultVenue InlineQueryResultVideo
    InlineQueryResultVoice
    """


class InlineQueryResultArticle(InlineQueryResult, tag="article"):
    """
    Represents a link to an article or web page.
    """

    id: str
    title: str
    input_message_content: "InputMessageContent"
    reply_markup: "InlineKeyboardMarkup | None" = None
    url: str | None = None
    hide_url: bool | None = None
    description: str | None = None
    thumbnail_url: str | None = None
    thumbnail_width: int | None = None
    thumbnail_height: int | None = None


class InlineQueryResultPhoto(InlineQueryResult, tag="photo"):
    """
    Represents a link to a photo. By default, this photo will be sent by
    the user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the photo.
    """

    id: str
    photo_url: str
    thumbnail_url: str
    photo_width: int | None = None
    photo_height: int | None = None
    title: str | None = None
    description: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultGif(InlineQueryResult, tag="gif"):
    """
    Represents a link to an animated GIF file. By default, this animated
    GIF file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the animation.
    """

    thumbnail_mime_type: InlineQueryResultGifThumbnailMimeType
    id: str
    gif_url: str
    thumbnail_url: str
    gif_width: int | None = None
    gif_height: int | None = None
    gif_duration: int | None = None
    title: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultMpeg4Gif(InlineQueryResult, tag="mpeg4_gif"):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound). By default, this animated MPEG-4 file will be sent by the user
    with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the animation.
    """

    thumbnail_mime_type: InlineQueryResultMpeg4GifThumbnailMimeType
    id: str
    mpeg4_url: str
    thumbnail_url: str
    mpeg4_width: int | None = None
    mpeg4_height: int | None = None
    mpeg4_duration: int | None = None
    title: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultVideo(InlineQueryResult, tag="video"):
    """
    Represents a link to a page containing an embedded video player or a
    video file. By default, this video file will be sent by the user with
    an optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the video. If
    an InlineQueryResultVideo message contains an embedded video (e.g.,
    YouTube), you must replace its content using input_message_content.
    """

    id: str
    video_url: str
    mime_type: InlineQueryResultVideoMimeType
    thumbnail_url: str
    title: str
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    video_width: int | None = None
    video_height: int | None = None
    video_duration: int | None = None
    description: str | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultAudio(InlineQueryResult, tag="audio"):
    """
    Represents a link to an MP3 audio file. By default, this audio file
    will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the audio.
    """

    id: str
    audio_url: str
    title: str
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    performer: str | None = None
    audio_duration: int | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultVoice(InlineQueryResult, tag="voice"):
    """
    Represents a link to a voice recording in an .OGG container encoded
    with OPUS. By default, this voice recording will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the the voice message.
    """

    id: str
    voice_url: str
    title: str
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    voice_duration: int | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultDocument(InlineQueryResult, tag="document"):
    """
    Represents a link to a file. By default, this file will be sent by the
    user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the file. Currently, only .PDF and .ZIP files can be sent
    using this method.
    """

    id: str
    title: str
    document_url: str
    mime_type: InlineQueryResultDocumentMimeType
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    description: str | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None
    thumbnail_url: str | None = None
    thumbnail_width: int | None = None
    thumbnail_height: int | None = None


class InlineQueryResultLocation(InlineQueryResult, tag="location"):
    """
    Represents a location on a map. By default, the location will be sent
    by the user. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the location.
    """

    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: float | None = None
    live_period: int | None = None
    heading: int | None = None
    proximity_alert_radius: int | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None
    thumbnail_url: str | None = None
    thumbnail_width: int | None = None
    thumbnail_height: int | None = None


class InlineQueryResultVenue(InlineQueryResult, tag="venue"):
    """
    Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the venue.
    """

    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str | None = None
    foursquare_type: str | None = None
    google_place_id: str | None = None
    google_place_type: str | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None
    thumbnail_url: str | None = None
    thumbnail_width: int | None = None
    thumbnail_height: int | None = None


class InlineQueryResultContact(InlineQueryResult, tag="contact"):
    """
    Represents a contact with a phone number. By default, this contact
    will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the contact.
    """

    id: str
    phone_number: str
    first_name: str
    last_name: str | None = None
    vcard: str | None = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None
    thumbnail_url: str | None = None
    thumbnail_width: int | None = None
    thumbnail_height: int | None = None


class InlineQueryResultGame(InlineQueryResult, tag="game"):
    """
    Represents a Game.
    """

    id: str
    game_short_name: str
    reply_markup: "InlineKeyboardMarkup | None" = None


class InlineQueryResultCachedPhoto(InlineQueryResult, tag="photo"):
    """
    Represents a link to a photo stored on the Telegram servers. By
    default, this photo will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the photo.
    """

    id: str
    photo_file_id: str
    title: str | None = None
    description: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedGif(InlineQueryResult, tag="gif"):
    """
    Represents a link to an animated GIF file stored on the Telegram
    servers. By default, this animated GIF file will be sent by the user
    with an optional caption. Alternatively, you can use
    input_message_content to send a message with specified content instead
    of the animation.
    """

    id: str
    gif_file_id: str
    title: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult, tag="mpeg4_gif"):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound) stored on the Telegram servers. By default, this animated
    MPEG-4 file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the animation.
    """

    id: str
    mpeg4_file_id: str
    title: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedSticker(InlineQueryResult, tag="sticker"):
    """
    Represents a link to a sticker stored on the Telegram servers. By
    default, this sticker will be sent by the user. Alternatively, you can
    use input_message_content to send a message with the specified content
    instead of the sticker.
    """

    id: str
    sticker_file_id: str
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedDocument(InlineQueryResult, tag="document"):
    """
    Represents a link to a file stored on the Telegram servers. By
    default, this file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the file.
    """

    id: str
    title: str
    document_file_id: str
    description: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedVideo(InlineQueryResult, tag="video"):
    """
    Represents a link to a video file stored on the Telegram servers. By
    default, this video file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the video.
    """

    id: str
    video_file_id: str
    title: str
    description: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedVoice(InlineQueryResult, tag="voice"):
    """
    Represents a link to a voice message stored on the Telegram servers.
    By default, this voice message will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the voice message.
    """

    id: str
    voice_file_id: str
    title: str
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InlineQueryResultCachedAudio(InlineQueryResult, tag="audio"):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified
    content instead of the audio.
    """

    id: str
    audio_file_id: str
    caption: str | None = None
    parse_mode: str | None = None
    caption_entities: "list[MessageEntity] | None" = None
    reply_markup: "InlineKeyboardMarkup | None" = None
    input_message_content: "InputMessageContent | None" = None


class InputMessageContent(Model, tag_field="latitude"):
    """
    This object represents the content of a message to be sent as a result
    of an inline query. Telegram clients currently support the following 5
    types:  InputTextMessageContent InputLocationMessageContent
    InputVenueMessageContent InputContactMessageContent
    InputInvoiceMessageContent
    """


class InputTextMessageContent(InputMessageContent, tag="None"):
    """
    Represents the content of a text message to be sent as the result of
    an inline query.
    """

    message_text: str
    parse_mode: str | None = None
    entities: "list[MessageEntity] | None" = None
    disable_web_page_preview: bool | None = None


class InputLocationMessageContent(InputMessageContent, tag="None"):
    """
    Represents the content of a location message to be sent as the result
    of an inline query.
    """

    longitude: float
    horizontal_accuracy: float | None = None
    live_period: int | None = None
    heading: int | None = None
    proximity_alert_radius: int | None = None


class InputVenueMessageContent(InputMessageContent, tag="None"):
    """
    Represents the content of a venue message to be sent as the result of
    an inline query.
    """

    longitude: float
    title: str
    address: str
    foursquare_id: str | None = None
    foursquare_type: str | None = None
    google_place_id: str | None = None
    google_place_type: str | None = None


class InputContactMessageContent(InputMessageContent, tag="None"):
    """
    Represents the content of a contact message to be sent as the result
    of an inline query.
    """

    phone_number: str
    first_name: str
    last_name: str | None = None
    vcard: str | None = None


class InputInvoiceMessageContent(InputMessageContent, tag="None"):
    """
    Represents the content of an invoice message to be sent as the result
    of an inline query.
    """

    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: "list[LabeledPrice]"
    max_tip_amount: int | None = None
    suggested_tip_amounts: "list[int] | None" = None
    provider_data: str | None = None
    photo_url: str | None = None
    photo_size: int | None = None
    photo_width: int | None = None
    photo_height: int | None = None
    need_name: bool | None = None
    need_phone_number: bool | None = None
    need_email: bool | None = None
    need_shipping_address: bool | None = None
    send_phone_number_to_provider: bool | None = None
    send_email_to_provider: bool | None = None
    is_flexible: bool | None = None


class ChosenInlineResult(Model):
    """
    Represents a result of an inline query that was chosen by the user and
    sent to their chat partner.
    """

    result_id: str
    from_: "User"
    query: str
    location: "Location | None" = None
    inline_message_id: str | None = None


class SentWebAppMessage(Model):
    """
    Describes an inline message sent by a Web App on behalf of a user.
    """

    inline_message_id: str | None = None


class LabeledPrice(Model):
    """
    This object represents a portion of the price for goods or services.
    """

    label: str
    amount: int


class Invoice(Model):
    """
    This object contains basic information about an invoice.
    """

    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


class ShippingAddress(Model):
    """
    This object represents a shipping address.
    """

    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


class OrderInfo(Model):
    """
    This object represents information about an order.
    """

    name: str | None = None
    phone_number: str | None = None
    email: str | None = None
    shipping_address: "ShippingAddress | None" = None


class ShippingOption(Model):
    """
    This object represents one shipping option.
    """

    id: str
    title: str
    prices: "list[LabeledPrice]"


class SuccessfulPayment(Model):
    """
    This object contains basic information about a successful payment.
    """

    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    shipping_option_id: str | None = None
    order_info: "OrderInfo | None" = None


class ShippingQuery(Model):
    """
    This object contains information about an incoming shipping query.
    """

    id: str
    from_: "User"
    invoice_payload: str
    shipping_address: "ShippingAddress"


class PreCheckoutQuery(Model):
    """
    This object contains information about an incoming pre-checkout query.
    """

    id: str
    from_: "User"
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str | None = None
    order_info: "OrderInfo | None" = None


class PassportData(Model):
    """
    Describes Telegram Passport data shared with the bot by the user.
    """

    data: "list[EncryptedPassportElement]"
    credentials: "EncryptedCredentials"


class PassportFile(Model):
    """
    This object represents a file uploaded to Telegram Passport. Currently
    all Telegram Passport files are in JPEG format when decrypted and
    don't exceed 10MB.
    """

    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


class EncryptedPassportElement(Model):
    """
    Describes documents or other Telegram Passport elements shared with
    the bot by the user.
    """

    type: EncryptedPassportElementType
    hash: str
    data: str | None = None
    phone_number: str | None = None
    email: str | None = None
    files: "list[PassportFile] | None" = None
    front_side: "PassportFile | None" = None
    reverse_side: "PassportFile | None" = None
    selfie: "PassportFile | None" = None
    translation: "list[PassportFile] | None" = None


class EncryptedCredentials(Model):
    """
    Describes data required for decrypting and authenticating
    EncryptedPassportElement. See the Telegram Passport Documentation for
    a complete description of the data decryption and authentication
    processes.
    """

    data: str
    hash: str
    secret: str


class PassportElementError(Model, tag_field="source"):
    """
    This object represents an error in the Telegram Passport element which
    was submitted that should be resolved by the user. It should be one
    of:  PassportElementErrorDataField PassportElementErrorFrontSide
    PassportElementErrorReverseSide PassportElementErrorSelfie
    PassportElementErrorFile PassportElementErrorFiles
    PassportElementErrorTranslationFile
    PassportElementErrorTranslationFiles PassportElementErrorUnspecified
    """


class PassportElementErrorDataField(PassportElementError, tag="data"):
    """
    Represents an issue in one of the data fields that was provided by the
    user. The error is considered resolved when the field's value changes.
    """

    type: PassportElementErrorDataFieldType
    field_name: str
    data_hash: str
    message: str


class PassportElementErrorFrontSide(PassportElementError, tag="front_side"):
    """
    Represents an issue with the front side of a document. The error is
    considered resolved when the file with the front side of the document
    changes.
    """

    type: PassportElementErrorFrontSideType
    file_hash: str
    message: str


class PassportElementErrorReverseSide(PassportElementError, tag="reverse_side"):
    """
    Represents an issue with the reverse side of a document. The error is
    considered resolved when the file with reverse side of the document
    changes.
    """

    type: PassportElementErrorReverseSideType
    file_hash: str
    message: str


class PassportElementErrorSelfie(PassportElementError, tag="selfie"):
    """
    Represents an issue with the selfie with a document. The error is
    considered resolved when the file with the selfie changes.
    """

    type: PassportElementErrorSelfieType
    file_hash: str
    message: str


class PassportElementErrorFile(PassportElementError, tag="file"):
    """
    Represents an issue with a document scan. The error is considered
    resolved when the file with the document scan changes.
    """

    type: PassportElementErrorFileType
    file_hash: str
    message: str


class PassportElementErrorFiles(PassportElementError, tag="files"):
    """
    Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.
    """

    type: PassportElementErrorFilesType
    file_hashes: "list[str]"
    message: str


class PassportElementErrorTranslationFile(PassportElementError, tag="translation_file"):
    """
    Represents an issue with one of the files that constitute the
    translation of a document. The error is considered resolved when the
    file changes.
    """

    type: PassportElementErrorTranslationFileType
    file_hash: str
    message: str


class PassportElementErrorTranslationFiles(
    PassportElementError, tag="translation_files"
):
    """
    Represents an issue with the translated version of a document. The
    error is considered resolved when a file with the document translation
    change.
    """

    type: PassportElementErrorTranslationFilesType
    file_hashes: "list[str]"
    message: str


class PassportElementErrorUnspecified(PassportElementError, tag="unspecified"):
    """
    Represents an issue in an unspecified place. The error is considered
    resolved when new data is added.
    """

    type: str
    element_hash: str
    message: str


class Game(Model):
    """
    This object represents a game. Use BotFather to create and edit games,
    their short names will act as unique identifiers.
    """

    title: str
    description: str
    photo: "list[PhotoSize]"
    text: str | None = None
    text_entities: "list[MessageEntity] | None" = None
    animation: "Animation | None" = None


class CallbackGame(Model):
    """
    A placeholder, currently holds no information. Use BotFather to set up
    your game.
    """

    pass


class GameHighScore(Model):
    """
    This object represents one row of the high scores table for a game.
    """

    position: int
    user: "User"
    score: int


ChatMember = (
    ChatMemberOwner
    | ChatMemberAdministrator
    | ChatMemberMember
    | ChatMemberRestricted
    | ChatMemberLeft
    | ChatMemberBanned
)


BotCommandScope = (
    BotCommandScopeDefault
    | BotCommandScopeAllPrivateChats
    | BotCommandScopeAllGroupChats
    | BotCommandScopeAllChatAdministrators
    | BotCommandScopeChat
    | BotCommandScopeChatAdministrators
    | BotCommandScopeChatMember
)


MenuButton = MenuButtonCommands | MenuButtonWebApp | MenuButtonDefault


InputMedia = (
    InputMediaAnimation
    | InputMediaDocument
    | InputMediaAudio
    | InputMediaPhoto
    | InputMediaVideo
)


InlineQueryResult = (
    InlineQueryResultCachedAudio
    | InlineQueryResultCachedDocument
    | InlineQueryResultCachedGif
    | InlineQueryResultCachedMpeg4Gif
    | InlineQueryResultCachedPhoto
    | InlineQueryResultCachedSticker
    | InlineQueryResultCachedVideo
    | InlineQueryResultCachedVoice
    | InlineQueryResultArticle
    | InlineQueryResultAudio
    | InlineQueryResultContact
    | InlineQueryResultGame
    | InlineQueryResultDocument
    | InlineQueryResultGif
    | InlineQueryResultLocation
    | InlineQueryResultMpeg4Gif
    | InlineQueryResultPhoto
    | InlineQueryResultVenue
    | InlineQueryResultVideo
    | InlineQueryResultVoice
)


InputMessageContent = (
    InputTextMessageContent
    | InputLocationMessageContent
    | InputVenueMessageContent
    | InputContactMessageContent
    | InputInvoiceMessageContent
)


PassportElementError = (
    PassportElementErrorDataField
    | PassportElementErrorFrontSide
    | PassportElementErrorReverseSide
    | PassportElementErrorSelfie
    | PassportElementErrorFile
    | PassportElementErrorFiles
    | PassportElementErrorTranslationFile
    | PassportElementErrorTranslationFiles
    | PassportElementErrorUnspecified
)
