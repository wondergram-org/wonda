from typing import TYPE_CHECKING

from .objects import (
    Update,
    WebhookInfo,
    User,
    ChatFullInfo,
    Message,
    MessageId,
    MessageEntity,
    ReplyParameters,
    InputPollOption,
    Poll,
    LinkPreviewOptions,
    UserProfilePhotos,
    File,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    ForceReply,
    ChatInviteLink,
    ChatAdministratorRights,
    ChatMember,
    ChatPermissions,
    ReactionType,
    ForumTopic,
    BotCommand,
    BotCommandScope,
    BotName,
    BotDescription,
    BotShortDescription,
    MenuButton,
    UserChatBoosts,
    BusinessConnection,
    InputMedia,
    InputMediaPhoto,
    InputMediaVideo,
    InputMediaAudio,
    InputMediaDocument,
    InputFile,
    InputPaidMedia,
    Sticker,
    StickerSet,
    MaskPosition,
    InputSticker,
    InlineQueryResultsButton,
    InlineQueryResult,
    SentWebAppMessage,
    LabeledPrice,
    ShippingOption,
    StarTransactions,
    PassportElementError,
    GameHighScore,
)
from .helper import get_params, from_json

if TYPE_CHECKING:
    from wonda.api.abc import ABCAPI


class APIMethods:
    def __init__(self, api: "ABCAPI") -> None:
        self.api = api

    async def get_updates(
        self,
        timeout: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
        allowed_updates: list[str] | None = None,
        **kwargs,
    ) -> list[Update]:
        """
        Use this method to receive incoming updates using long polling (wiki).
        Returns an Array of Update objects.
        """
        response = await self.api.request("getUpdates", get_params(locals()))
        return from_json(response, type=list[Update])

    async def set_webhook(
        self,
        url: str,
        secret_token: str | None = None,
        max_connections: int | None = None,
        ip_address: str | None = None,
        drop_pending_updates: bool | None = None,
        certificate: InputFile | None = None,
        allowed_updates: list[str] | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to specify a URL and receive incoming updates via an
        outgoing webhook. Whenever there is an update for the bot, we will
        send an HTTPS POST request to the specified URL, containing a JSON-
        serialized Update. In case of an unsuccessful request, we will give up
        after a reasonable amount of attempts. Returns True on success. If
        you'd like to make sure that the webhook was set by you, you can
        specify secret data in the parameter secret_token. If specified, the
        request will contain a header "X-Telegram-Bot-Api-Secret-Token" with
        the secret token as content.
        """
        response = await self.api.request("setWebhook", get_params(locals()))
        return from_json(response, type=bool)

    async def delete_webhook(
        self, drop_pending_updates: bool | None = None, **kwargs
    ) -> bool:
        """
        Use this method to remove webhook integration if you decide to switch
        back to getUpdates. Returns True on success.
        """
        response = await self.api.request("deleteWebhook", get_params(locals()))
        return from_json(response, type=bool)

    async def get_webhook_info(self, **kwargs) -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no parameters.
        On success, returns a WebhookInfo object. If the bot is using
        getUpdates, will return an object with the url field empty.
        """
        response = await self.api.request("getWebhookInfo", get_params(locals()))
        return from_json(response, type=WebhookInfo)

    async def get_me(self, **kwargs) -> User:
        """
        A simple method for testing your bot's authentication token. Requires
        no parameters. Returns basic information about the bot in form of a
        User object.
        """
        response = await self.api.request("getMe", get_params(locals()))
        return from_json(response, type=User)

    async def log_out(self, **kwargs) -> bool:
        """
        Use this method to log out from the cloud Bot API server before
        launching the bot locally. You must log out the bot before running it
        locally, otherwise there is no guarantee that the bot will receive
        updates. After a successful call, you can immediately log in on a
        local server, but will not be able to log in back to the cloud Bot API
        server for 10 minutes. Returns True on success. Requires no
        parameters.
        """
        response = await self.api.request("logOut", get_params(locals()))
        return from_json(response, type=bool)

    async def close(self, **kwargs) -> bool:
        """
        Use this method to close the bot instance before moving it from one
        local server to another. You need to delete the webhook before calling
        this method to ensure that the bot isn't launched again after server
        restart. The method will return error 429 in the first 10 minutes
        after the bot is launched. Returns True on success. Requires no
        parameters.
        """
        response = await self.api.request("close", get_params(locals()))
        return from_json(response, type=bool)

    async def send_message(
        self,
        text: str,
        chat_id: int | str,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
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
        """
        Use this method to send text messages. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendMessage", get_params(locals()))
        return from_json(response, type=Message)

    async def forward_message(
        self,
        message_id: int,
        from_chat_id: int | str,
        chat_id: int | str,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to forward messages of any kind. Service messages and
        messages with protected content can't be forwarded. On success, the
        sent Message is returned.
        """
        response = await self.api.request("forwardMessage", get_params(locals()))
        return from_json(response, type=Message)

    async def forward_messages(
        self,
        message_ids: list[int],
        from_chat_id: int | str,
        chat_id: int | str,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        **kwargs,
    ) -> list[MessageId]:
        """
        Use this method to forward multiple messages of any kind. If some of
        the specified messages can't be found or forwarded, they are skipped.
        Service messages and messages with protected content can't be
        forwarded. Album grouping is kept for forwarded messages. On success,
        an array of MessageId of the sent messages is returned.
        """
        response = await self.api.request("forwardMessages", get_params(locals()))
        return from_json(response, type=list[MessageId])

    async def copy_message(
        self,
        message_id: int,
        from_chat_id: int | str,
        chat_id: int | str,
        show_caption_above_media: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        **kwargs,
    ) -> MessageId:
        """
        Use this method to copy messages of any kind. Service messages, paid
        media messages, giveaway messages, giveaway winners messages, and
        invoice messages can't be copied. A quiz poll can be copied only if
        the value of the field correct_option_id is known to the bot. The
        method is analogous to the method forwardMessage, but the copied
        message doesn't have a link to the original message. Returns the
        MessageId of the sent message on success.
        """
        response = await self.api.request("copyMessage", get_params(locals()))
        return from_json(response, type=MessageId)

    async def copy_messages(
        self,
        message_ids: list[int],
        from_chat_id: int | str,
        chat_id: int | str,
        remove_caption: bool | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        **kwargs,
    ) -> list[MessageId]:
        """
        Use this method to copy messages of any kind. If some of the specified
        messages can't be found or copied, they are skipped. Service messages,
        paid media messages, giveaway messages, giveaway winners messages, and
        invoice messages can't be copied. A quiz poll can be copied only if
        the value of the field correct_option_id is known to the bot. The
        method is analogous to the method forwardMessages, but the copied
        messages don't have a link to the original message. Album grouping is
        kept for copied messages. On success, an array of MessageId of the
        sent messages is returned.
        """
        response = await self.api.request("copyMessages", get_params(locals()))
        return from_json(response, type=list[MessageId])

    async def send_photo(
        self,
        photo: InputFile | str,
        chat_id: int | str,
        show_caption_above_media: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send photos. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendPhoto", get_params(locals()))
        return from_json(response, type=Message)

    async def send_audio(
        self,
        chat_id: int | str,
        audio: InputFile | str,
        title: str | None = None,
        thumbnail: InputFile | str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        performer: str | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to
        display them in the music player. Your audio must be in the .MP3 or
        .M4A format. On success, the sent Message is returned. Bots can
        currently send audio files of up to 50 MB in size, this limit may be
        changed in the future. For sending voice messages, use the sendVoice
        method instead.
        """
        response = await self.api.request("sendAudio", get_params(locals()))
        return from_json(response, type=Message)

    async def send_document(
        self,
        document: InputFile | str,
        chat_id: int | str,
        thumbnail: InputFile | str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        disable_notification: bool | None = None,
        disable_content_type_detection: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send general files. On success, the sent Message is
        returned. Bots can currently send files of any type of up to 50 MB in
        size, this limit may be changed in the future.
        """
        response = await self.api.request("sendDocument", get_params(locals()))
        return from_json(response, type=Message)

    async def send_video(
        self,
        video: InputFile | str,
        chat_id: int | str,
        width: int | None = None,
        thumbnail: InputFile | str | None = None,
        supports_streaming: bool | None = None,
        show_caption_above_media: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        height: int | None = None,
        has_spoiler: bool | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send video files, Telegram clients support MPEG4
        videos (other formats may be sent as Document). On success, the sent
        Message is returned. Bots can currently send video files of up to 50
        MB in size, this limit may be changed in the future.
        """
        response = await self.api.request("sendVideo", get_params(locals()))
        return from_json(response, type=Message)

    async def send_animation(
        self,
        chat_id: int | str,
        animation: InputFile | str,
        width: int | None = None,
        thumbnail: InputFile | str | None = None,
        show_caption_above_media: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        height: int | None = None,
        has_spoiler: bool | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video
        without sound). On success, the sent Message is returned. Bots can
        currently send animation files of up to 50 MB in size, this limit may
        be changed in the future.
        """
        response = await self.api.request("sendAnimation", get_params(locals()))
        return from_json(response, type=Message)

    async def send_voice(
        self,
        voice: InputFile | str,
        chat_id: int | str,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to
        display the file as a playable voice message. For this to work, your
        audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or
        in .M4A format (other formats may be sent as Audio or Document). On
        success, the sent Message is returned. Bots can currently send voice
        messages of up to 50 MB in size, this limit may be changed in the
        future.
        """
        response = await self.api.request("sendVoice", get_params(locals()))
        return from_json(response, type=Message)

    async def send_video_note(
        self,
        video_note: InputFile | str,
        chat_id: int | str,
        thumbnail: InputFile | str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        length: int | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        As of v.4.0, Telegram clients support rounded square MPEG4 videos of
        up to 1 minute long. Use this method to send video messages. On
        success, the sent Message is returned.
        """
        response = await self.api.request("sendVideoNote", get_params(locals()))
        return from_json(response, type=Message)

    async def send_paid_media(
        self,
        star_count: int,
        media: list[InputPaidMedia],
        chat_id: int | str,
        show_caption_above_media: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        parse_mode: str | None = None,
        disable_notification: bool | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send paid media to channel chats. On success, the
        sent Message is returned.
        """
        response = await self.api.request("sendPaidMedia", get_params(locals()))
        return from_json(response, type=Message)

    async def send_media_group(
        self,
        media: list[
            InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo
        ],
        chat_id: int | str,
        reply_parameters: ReplyParameters | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> list[Message]:
        """
        Use this method to send a group of photos, videos, documents or audios
        as an album. Documents and audio files can be only grouped in an album
        with messages of the same type. On success, an array of Messages that
        were sent is returned.
        """
        response = await self.api.request("sendMediaGroup", get_params(locals()))
        return from_json(response, type=list[Message])

    async def send_location(
        self,
        longitude: float,
        latitude: float,
        chat_id: int | str,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        proximity_alert_radius: int | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        live_period: int | None = None,
        horizontal_accuracy: float | None = None,
        heading: int | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send point on the map. On success, the sent Message
        is returned.
        """
        response = await self.api.request("sendLocation", get_params(locals()))
        return from_json(response, type=Message)

    async def send_venue(
        self,
        title: str,
        longitude: float,
        latitude: float,
        chat_id: int | str,
        address: str,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        google_place_type: str | None = None,
        google_place_id: str | None = None,
        foursquare_type: str | None = None,
        foursquare_id: str | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send information about a venue. On success, the
        sent Message is returned.
        """
        response = await self.api.request("sendVenue", get_params(locals()))
        return from_json(response, type=Message)

    async def send_contact(
        self,
        phone_number: str,
        first_name: str,
        chat_id: int | str,
        vcard: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        last_name: str | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send phone contacts. On success, the sent Message
        is returned.
        """
        response = await self.api.request("sendContact", get_params(locals()))
        return from_json(response, type=Message)

    async def send_poll(
        self,
        question: str,
        options: list[InputPollOption],
        chat_id: int | str,
        type: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        question_parse_mode: str | None = None,
        question_entities: list[MessageEntity] | None = None,
        protect_content: bool | None = None,
        open_period: int | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        is_closed: bool | None = None,
        is_anonymous: bool | None = None,
        explanation_parse_mode: str | None = None,
        explanation_entities: list[MessageEntity] | None = None,
        explanation: str | None = None,
        disable_notification: bool | None = None,
        correct_option_id: int | None = None,
        close_date: int | None = None,
        business_connection_id: str | None = None,
        allows_multiple_answers: bool | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send a native poll. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendPoll", get_params(locals()))
        return from_json(response, type=Message)

    async def send_dice(
        self,
        chat_id: int | str,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send an animated emoji that will display a random
        value. On success, the sent Message is returned.
        """
        response = await self.api.request("sendDice", get_params(locals()))
        return from_json(response, type=Message)

    async def send_chat_action(
        self,
        chat_id: int | str,
        action: str,
        message_thread_id: int | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method when you need to tell the user that something is
        happening on the bot's side. The status is set for 5 seconds or less
        (when a message arrives from your bot, Telegram clients clear its
        typing status). Returns True on success. Example: The ImageBot needs
        some time to process a request and upload the image. Instead of
        sending a text message along the lines of "Retrieving image, please
        wait...", the bot may use sendChatAction with action = upload_photo.
        The user will see a "sending photo" status for the bot. We only
        recommend using this method when a response from the bot will take a
        noticeable amount of time to arrive.
        """
        response = await self.api.request("sendChatAction", get_params(locals()))
        return from_json(response, type=bool)

    async def set_message_reaction(
        self,
        message_id: int,
        chat_id: int | str,
        reaction: list[ReactionType] | None = None,
        is_big: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to change the chosen reactions on a message. Service
        messages can't be reacted to. Automatically forwarded messages from a
        channel to its discussion group have the same available reactions as
        messages in the channel. Returns True on success.
        """
        response = await self.api.request("setMessageReaction", get_params(locals()))
        return from_json(response, type=bool)

    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: int | None = None,
        limit: int | None = None,
        **kwargs,
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a user. Returns
        a UserProfilePhotos object.
        """
        response = await self.api.request("getUserProfilePhotos", get_params(locals()))
        return from_json(response, type=UserProfilePhotos)

    async def get_file(self, file_id: str, **kwargs) -> File:
        """
        Use this method to get basic information about a file and prepare it
        for downloading. For the moment, bots can download files of up to 20MB
        in size. On success, a File object is returned. The file can then be
        downloaded via the link
        https://api.telegram.org/file/bot<token>/<file_path>, where
        <file_path> is taken from the response. It is guaranteed that the link
        will be valid for at least 1 hour. When the link expires, a new one
        can be requested by calling getFile again.
        """
        response = await self.api.request("getFile", get_params(locals()))
        return from_json(response, type=File)

    async def ban_chat_member(
        self,
        user_id: int,
        chat_id: int | str,
        until_date: int | None = None,
        revoke_messages: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup or a channel.
        In the case of supergroups and channels, the user will not be able to
        return to the chat on their own using invite links, etc., unless
        unbanned first. The bot must be an administrator in the chat for this
        to work and must have the appropriate administrator rights. Returns
        True on success.
        """
        response = await self.api.request("banChatMember", get_params(locals()))
        return from_json(response, type=bool)

    async def unban_chat_member(
        self,
        user_id: int,
        chat_id: int | str,
        only_if_banned: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to unban a previously banned user in a supergroup or
        channel. The user will not return to the group or channel
        automatically, but will be able to join via link, etc. The bot must be
        an administrator for this to work. By default, this method guarantees
        that after the call the user is not a member of the chat, but will be
        able to join it. So if the user is a member of the chat they will also
        be removed from the chat. If you don't want this, use the parameter
        only_if_banned. Returns True on success.
        """
        response = await self.api.request("unbanChatMember", get_params(locals()))
        return from_json(response, type=bool)

    async def restrict_chat_member(
        self,
        user_id: int,
        permissions: ChatPermissions,
        chat_id: int | str,
        use_independent_chat_permissions: bool | None = None,
        until_date: int | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup. The bot must be an
        administrator in the supergroup for this to work and must have the
        appropriate administrator rights. Pass True for all permissions to
        lift restrictions from a user. Returns True on success.
        """
        response = await self.api.request("restrictChatMember", get_params(locals()))
        return from_json(response, type=bool)

    async def promote_chat_member(
        self,
        user_id: int,
        chat_id: int | str,
        is_anonymous: bool | None = None,
        can_restrict_members: bool | None = None,
        can_promote_members: bool | None = None,
        can_post_stories: bool | None = None,
        can_post_messages: bool | None = None,
        can_pin_messages: bool | None = None,
        can_manage_video_chats: bool | None = None,
        can_manage_topics: bool | None = None,
        can_manage_chat: bool | None = None,
        can_invite_users: bool | None = None,
        can_edit_stories: bool | None = None,
        can_edit_messages: bool | None = None,
        can_delete_stories: bool | None = None,
        can_delete_messages: bool | None = None,
        can_change_info: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup or a
        channel. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Pass False for all
        boolean parameters to demote a user. Returns True on success.
        """
        response = await self.api.request("promoteChatMember", get_params(locals()))
        return from_json(response, type=bool)

    async def set_chat_administrator_custom_title(
        self, user_id: int, custom_title: str, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to set a custom title for an administrator in a
        supergroup promoted by the bot. Returns True on success.
        """
        response = await self.api.request(
            "setChatAdministratorCustomTitle", get_params(locals())
        )
        return from_json(response, type=bool)

    async def ban_chat_sender_chat(
        self, sender_chat_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to ban a channel chat in a supergroup or a channel.
        Until the chat is unbanned, the owner of the banned chat won't be able
        to send messages on behalf of any of their channels. The bot must be
        an administrator in the supergroup or channel for this to work and
        must have the appropriate administrator rights. Returns True on
        success.
        """
        response = await self.api.request("banChatSenderChat", get_params(locals()))
        return from_json(response, type=bool)

    async def unban_chat_sender_chat(
        self, sender_chat_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in a
        supergroup or channel. The bot must be an administrator for this to
        work and must have the appropriate administrator rights. Returns True
        on success.
        """
        response = await self.api.request("unbanChatSenderChat", get_params(locals()))
        return from_json(response, type=bool)

    async def set_chat_permissions(
        self,
        permissions: ChatPermissions,
        chat_id: int | str,
        use_independent_chat_permissions: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to set default chat permissions for all members. The
        bot must be an administrator in the group or a supergroup for this to
        work and must have the can_restrict_members administrator rights.
        Returns True on success.
        """
        response = await self.api.request("setChatPermissions", get_params(locals()))
        return from_json(response, type=bool)

    async def export_chat_invite_link(self, chat_id: int | str, **kwargs) -> str:
        """
        Use this method to generate a new primary invite link for a chat; any
        previously generated primary link is revoked. The bot must be an
        administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns the new invite link as
        String on success.
        """
        response = await self.api.request("exportChatInviteLink", get_params(locals()))
        return from_json(response, type=str)

    async def create_chat_invite_link(
        self,
        chat_id: int | str,
        name: str | None = None,
        member_limit: int | None = None,
        expire_date: int | None = None,
        creates_join_request: bool | None = None,
        **kwargs,
    ) -> ChatInviteLink:
        """
        Use this method to create an additional invite link for a chat. The
        bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. The link can be revoked
        using the method revokeChatInviteLink. Returns the new invite link as
        ChatInviteLink object.
        """
        response = await self.api.request("createChatInviteLink", get_params(locals()))
        return from_json(response, type=ChatInviteLink)

    async def edit_chat_invite_link(
        self,
        invite_link: str,
        chat_id: int | str,
        name: str | None = None,
        member_limit: int | None = None,
        expire_date: int | None = None,
        creates_join_request: bool | None = None,
        **kwargs,
    ) -> ChatInviteLink:
        """
        Use this method to edit a non-primary invite link created by the bot.
        The bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Returns the edited invite
        link as a ChatInviteLink object.
        """
        response = await self.api.request("editChatInviteLink", get_params(locals()))
        return from_json(response, type=ChatInviteLink)

    async def revoke_chat_invite_link(
        self, invite_link: str, chat_id: int | str, **kwargs
    ) -> ChatInviteLink:
        """
        Use this method to revoke an invite link created by the bot. If the
        primary link is revoked, a new link is automatically generated. The
        bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Returns the revoked invite
        link as ChatInviteLink object.
        """
        response = await self.api.request("revokeChatInviteLink", get_params(locals()))
        return from_json(response, type=ChatInviteLink)

    async def approve_chat_join_request(
        self, user_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to approve a chat join request. The bot must be an
        administrator in the chat for this to work and must have the
        can_invite_users administrator right. Returns True on success.
        """
        response = await self.api.request(
            "approveChatJoinRequest", get_params(locals())
        )
        return from_json(response, type=bool)

    async def decline_chat_join_request(
        self, user_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to decline a chat join request. The bot must be an
        administrator in the chat for this to work and must have the
        can_invite_users administrator right. Returns True on success.
        """
        response = await self.api.request(
            "declineChatJoinRequest", get_params(locals())
        )
        return from_json(response, type=bool)

    async def set_chat_photo(
        self, photo: InputFile, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to set a new profile photo for the chat. Photos can't
        be changed for private chats. The bot must be an administrator in the
        chat for this to work and must have the appropriate administrator
        rights. Returns True on success.
        """
        response = await self.api.request("setChatPhoto", get_params(locals()))
        return from_json(response, type=bool)

    async def delete_chat_photo(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to delete a chat photo. Photos can't be changed for
        private chats. The bot must be an administrator in the chat for this
        to work and must have the appropriate administrator rights. Returns
        True on success.
        """
        response = await self.api.request("deleteChatPhoto", get_params(locals()))
        return from_json(response, type=bool)

    async def set_chat_title(self, title: str, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to change the title of a chat. Titles can't be changed
        for private chats. The bot must be an administrator in the chat for
        this to work and must have the appropriate administrator rights.
        Returns True on success.
        """
        response = await self.api.request("setChatTitle", get_params(locals()))
        return from_json(response, type=bool)

    async def set_chat_description(
        self, chat_id: int | str, description: str | None = None, **kwargs
    ) -> bool:
        """
        Use this method to change the description of a group, a supergroup or
        a channel. The bot must be an administrator in the chat for this to
        work and must have the appropriate administrator rights. Returns True
        on success.
        """
        response = await self.api.request("setChatDescription", get_params(locals()))
        return from_json(response, type=bool)

    async def pin_chat_message(
        self,
        message_id: int,
        chat_id: int | str,
        disable_notification: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to add a message to the list of pinned messages in a
        chat. If the chat is not a private chat, the bot must be an
        administrator in the chat for this to work and must have the
        'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns True on
        success.
        """
        response = await self.api.request("pinChatMessage", get_params(locals()))
        return from_json(response, type=bool)

    async def unpin_chat_message(
        self, chat_id: int | str, message_id: int | None = None, **kwargs
    ) -> bool:
        """
        Use this method to remove a message from the list of pinned messages
        in a chat. If the chat is not a private chat, the bot must be an
        administrator in the chat for this to work and must have the
        'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns True on
        success.
        """
        response = await self.api.request("unpinChatMessage", get_params(locals()))
        return from_json(response, type=bool)

    async def unpin_all_chat_messages(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to clear the list of pinned messages in a chat. If the
        chat is not a private chat, the bot must be an administrator in the
        chat for this to work and must have the 'can_pin_messages'
        administrator right in a supergroup or 'can_edit_messages'
        administrator right in a channel. Returns True on success.
        """
        response = await self.api.request("unpinAllChatMessages", get_params(locals()))
        return from_json(response, type=bool)

    async def leave_chat(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method for your bot to leave a group, supergroup or channel.
        Returns True on success.
        """
        response = await self.api.request("leaveChat", get_params(locals()))
        return from_json(response, type=bool)

    async def get_chat(self, chat_id: int | str, **kwargs) -> ChatFullInfo:
        """
        Use this method to get up-to-date information about the chat. Returns
        a ChatFullInfo object on success.
        """
        response = await self.api.request("getChat", get_params(locals()))
        return from_json(response, type=ChatFullInfo)

    async def get_chat_administrators(
        self, chat_id: int | str, **kwargs
    ) -> list[ChatMember]:
        """
        Use this method to get a list of administrators in a chat, which
        aren't bots. Returns an Array of ChatMember objects.
        """
        response = await self.api.request("getChatAdministrators", get_params(locals()))
        return from_json(response, type=list[ChatMember])

    async def get_chat_member_count(self, chat_id: int | str, **kwargs) -> int:
        """
        Use this method to get the number of members in a chat. Returns Int on
        success.
        """
        response = await self.api.request("getChatMemberCount", get_params(locals()))
        return from_json(response, type=int)

    async def get_chat_member(
        self, user_id: int, chat_id: int | str, **kwargs
    ) -> ChatMember:
        """
        Use this method to get information about a member of a chat. The
        method is only guaranteed to work for other users if the bot is an
        administrator in the chat. Returns a ChatMember object on success.
        """
        response = await self.api.request("getChatMember", get_params(locals()))
        return from_json(response, type=ChatMember)  # type: ignore

    async def set_chat_sticker_set(
        self, sticker_set_name: str, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to set a new group sticker set for a supergroup. The
        bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Use the field
        can_set_sticker_set optionally returned in getChat requests to check
        if the bot can use this method. Returns True on success.
        """
        response = await self.api.request("setChatStickerSet", get_params(locals()))
        return from_json(response, type=bool)

    async def delete_chat_sticker_set(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to delete a group sticker set from a supergroup. The
        bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Use the field
        can_set_sticker_set optionally returned in getChat requests to check
        if the bot can use this method. Returns True on success.
        """
        response = await self.api.request("deleteChatStickerSet", get_params(locals()))
        return from_json(response, type=bool)

    async def get_forum_topic_icon_stickers(self, **kwargs) -> list[Sticker]:
        """
        Use this method to get custom emoji stickers, which can be used as a
        forum topic icon by any user. Requires no parameters. Returns an Array
        of Sticker objects.
        """
        response = await self.api.request(
            "getForumTopicIconStickers", get_params(locals())
        )
        return from_json(response, type=list[Sticker])

    async def create_forum_topic(
        self,
        name: str,
        chat_id: int | str,
        icon_custom_emoji_id: str | None = None,
        icon_color: int | None = None,
        **kwargs,
    ) -> ForumTopic:
        """
        Use this method to create a topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights. Returns information about
        the created topic as a ForumTopic object.
        """
        response = await self.api.request("createForumTopic", get_params(locals()))
        return from_json(response, type=ForumTopic)

    async def edit_forum_topic(
        self,
        message_thread_id: int,
        chat_id: int | str,
        name: str | None = None,
        icon_custom_emoji_id: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to edit name and icon of a topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work
        and must have can_manage_topics administrator rights, unless it is the
        creator of the topic. Returns True on success.
        """
        response = await self.api.request("editForumTopic", get_params(locals()))
        return from_json(response, type=bool)

    async def close_forum_topic(
        self, message_thread_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to close an open topic in a forum supergroup chat. The
        bot must be an administrator in the chat for this to work and must
        have the can_manage_topics administrator rights, unless it is the
        creator of the topic. Returns True on success.
        """
        response = await self.api.request("closeForumTopic", get_params(locals()))
        return from_json(response, type=bool)

    async def reopen_forum_topic(
        self, message_thread_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to reopen a closed topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must
        have the can_manage_topics administrator rights, unless it is the
        creator of the topic. Returns True on success.
        """
        response = await self.api.request("reopenForumTopic", get_params(locals()))
        return from_json(response, type=bool)

    async def delete_forum_topic(
        self, message_thread_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to delete a forum topic along with all its messages in
        a forum supergroup chat. The bot must be an administrator in the chat
        for this to work and must have the can_delete_messages administrator
        rights. Returns True on success.
        """
        response = await self.api.request("deleteForumTopic", get_params(locals()))
        return from_json(response, type=bool)

    async def unpin_all_forum_topic_messages(
        self, message_thread_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a forum topic.
        The bot must be an administrator in the chat for this to work and must
        have the can_pin_messages administrator right in the supergroup.
        Returns True on success.
        """
        response = await self.api.request(
            "unpinAllForumTopicMessages", get_params(locals())
        )
        return from_json(response, type=bool)

    async def edit_general_forum_topic(
        self, name: str, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to edit the name of the 'General' topic in a forum
        supergroup chat. The bot must be an administrator in the chat for this
        to work and must have can_manage_topics administrator rights. Returns
        True on success.
        """
        response = await self.api.request("editGeneralForumTopic", get_params(locals()))
        return from_json(response, type=bool)

    async def close_general_forum_topic(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to close an open 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work
        and must have the can_manage_topics administrator rights. Returns True
        on success.
        """
        response = await self.api.request(
            "closeGeneralForumTopic", get_params(locals())
        )
        return from_json(response, type=bool)

    async def reopen_general_forum_topic(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to reopen a closed 'General' topic in a forum
        supergroup chat. The bot must be an administrator in the chat for this
        to work and must have the can_manage_topics administrator rights. The
        topic will be automatically unhidden if it was hidden. Returns True on
        success.
        """
        response = await self.api.request(
            "reopenGeneralForumTopic", get_params(locals())
        )
        return from_json(response, type=bool)

    async def hide_general_forum_topic(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to hide the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work
        and must have the can_manage_topics administrator rights. The topic
        will be automatically closed if it was open. Returns True on success.
        """
        response = await self.api.request("hideGeneralForumTopic", get_params(locals()))
        return from_json(response, type=bool)

    async def unhide_general_forum_topic(self, chat_id: int | str, **kwargs) -> bool:
        """
        Use this method to unhide the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work
        and must have the can_manage_topics administrator rights. Returns True
        on success.
        """
        response = await self.api.request(
            "unhideGeneralForumTopic", get_params(locals())
        )
        return from_json(response, type=bool)

    async def unpin_all_general_forum_topic_messages(
        self, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a General
        forum topic. The bot must be an administrator in the chat for this to
        work and must have the can_pin_messages administrator right in the
        supergroup. Returns True on success.
        """
        response = await self.api.request(
            "unpinAllGeneralForumTopicMessages", get_params(locals())
        )
        return from_json(response, type=bool)

    async def answer_callback_query(
        self,
        callback_query_id: str,
        url: str | None = None,
        text: str | None = None,
        show_alert: bool | None = None,
        cache_time: int | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from inline
        keyboards. The answer will be displayed to the user as a notification
        at the top of the chat screen or as an alert. On success, True is
        returned. Alternatively, the user can be redirected to the specified
        Game URL. For this option to work, you must first create a game for
        your bot via @BotFather and accept the terms. Otherwise, you may use
        links like t.me/your_bot?start=XXXX that open your bot with a
        parameter.
        """
        response = await self.api.request("answerCallbackQuery", get_params(locals()))
        return from_json(response, type=bool)

    async def get_user_chat_boosts(
        self, user_id: int, chat_id: int | str, **kwargs
    ) -> UserChatBoosts:
        """
        Use this method to get the list of boosts added to a chat by a user.
        Requires administrator rights in the chat. Returns a UserChatBoosts
        object.
        """
        response = await self.api.request("getUserChatBoosts", get_params(locals()))
        return from_json(response, type=UserChatBoosts)

    async def get_business_connection(
        self, business_connection_id: str, **kwargs
    ) -> BusinessConnection:
        """
        Use this method to get information about the connection of the bot
        with a business account. Returns a BusinessConnection object on
        success.
        """
        response = await self.api.request("getBusinessConnection", get_params(locals()))
        return from_json(response, type=BusinessConnection)

    async def set_my_commands(
        self,
        commands: list[BotCommand],
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to change the list of the bot's commands. See this
        manual for more details about bot commands. Returns True on success.
        """
        response = await self.api.request("setMyCommands", get_params(locals()))
        return from_json(response, type=bool)

    async def delete_my_commands(
        self,
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given
        scope and user language. After deletion, higher level commands will be
        shown to affected users. Returns True on success.
        """
        response = await self.api.request("deleteMyCommands", get_params(locals()))
        return from_json(response, type=bool)

    async def get_my_commands(
        self,
        scope: BotCommandScope | None = None,
        language_code: str | None = None,
        **kwargs,
    ) -> list[BotCommand]:
        """
        Use this method to get the current list of the bot's commands for the
        given scope and user language. Returns an Array of BotCommand objects.
        If commands aren't set, an empty list is returned.
        """
        response = await self.api.request("getMyCommands", get_params(locals()))
        return from_json(response, type=list[BotCommand])

    async def set_my_name(
        self, name: str | None = None, language_code: str | None = None, **kwargs
    ) -> bool:
        """
        Use this method to change the bot's name. Returns True on success.
        """
        response = await self.api.request("setMyName", get_params(locals()))
        return from_json(response, type=bool)

    async def get_my_name(self, language_code: str | None = None, **kwargs) -> BotName:
        """
        Use this method to get the current bot name for the given user
        language. Returns BotName on success.
        """
        response = await self.api.request("getMyName", get_params(locals()))
        return from_json(response, type=BotName)

    async def set_my_description(
        self, language_code: str | None = None, description: str | None = None, **kwargs
    ) -> bool:
        """
        Use this method to change the bot's description, which is shown in the
        chat with the bot if the chat is empty. Returns True on success.
        """
        response = await self.api.request("setMyDescription", get_params(locals()))
        return from_json(response, type=bool)

    async def get_my_description(
        self, language_code: str | None = None, **kwargs
    ) -> BotDescription:
        """
        Use this method to get the current bot description for the given user
        language. Returns BotDescription on success.
        """
        response = await self.api.request("getMyDescription", get_params(locals()))
        return from_json(response, type=BotDescription)

    async def set_my_short_description(
        self,
        short_description: str | None = None,
        language_code: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to change the bot's short description, which is shown
        on the bot's profile page and is sent together with the link when
        users share the bot. Returns True on success.
        """
        response = await self.api.request("setMyShortDescription", get_params(locals()))
        return from_json(response, type=bool)

    async def get_my_short_description(
        self, language_code: str | None = None, **kwargs
    ) -> BotShortDescription:
        """
        Use this method to get the current bot short description for the given
        user language. Returns BotShortDescription on success.
        """
        response = await self.api.request("getMyShortDescription", get_params(locals()))
        return from_json(response, type=BotShortDescription)

    async def set_chat_menu_button(
        self,
        menu_button: MenuButton | None = None,
        chat_id: int | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to change the bot's menu button in a private chat, or
        the default menu button. Returns True on success.
        """
        response = await self.api.request("setChatMenuButton", get_params(locals()))
        return from_json(response, type=bool)

    async def get_chat_menu_button(
        self, chat_id: int | None = None, **kwargs
    ) -> MenuButton:
        """
        Use this method to get the current value of the bot's menu button in a
        private chat, or the default menu button. Returns MenuButton on
        success.
        """
        response = await self.api.request("getChatMenuButton", get_params(locals()))
        return from_json(response, type=MenuButton)  # type: ignore

    async def set_my_default_administrator_rights(
        self,
        rights: ChatAdministratorRights | None = None,
        for_channels: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to change the default administrator rights requested
        by the bot when it's added as an administrator to groups or channels.
        These rights will be suggested to users, but they are free to modify
        the list before adding the bot. Returns True on success.
        """
        response = await self.api.request(
            "setMyDefaultAdministratorRights", get_params(locals())
        )
        return from_json(response, type=bool)

    async def get_my_default_administrator_rights(
        self, for_channels: bool | None = None, **kwargs
    ) -> ChatAdministratorRights:
        """
        Use this method to get the current default administrator rights of the
        bot. Returns ChatAdministratorRights on success.
        """
        response = await self.api.request(
            "getMyDefaultAdministratorRights", get_params(locals())
        )
        return from_json(response, type=ChatAdministratorRights)

    async def edit_message_text(
        self,
        text: str,
        reply_markup: InlineKeyboardMarkup | None = None,
        parse_mode: str | None = None,
        message_id: int | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        inline_message_id: str | None = None,
        entities: list[MessageEntity] | None = None,
        chat_id: int | str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to edit text and game messages. On success, if the
        edited message is not an inline message, the edited Message is
        returned, otherwise True is returned. Note that business messages that
        were not sent by the bot and do not contain an inline keyboard can
        only be edited within 48 hours from the time they were sent.
        """
        response = await self.api.request("editMessageText", get_params(locals()))
        return from_json(response, type=Message | bool)  # type: ignore

    async def edit_message_caption(
        self,
        show_caption_above_media: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
        parse_mode: str | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        chat_id: int | str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        caption: str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to edit captions of messages. On success, if the
        edited message is not an inline message, the edited Message is
        returned, otherwise True is returned. Note that business messages that
        were not sent by the bot and do not contain an inline keyboard can
        only be edited within 48 hours from the time they were sent.
        """
        response = await self.api.request("editMessageCaption", get_params(locals()))
        return from_json(response, type=Message | bool)  # type: ignore

    async def edit_message_media(
        self,
        media: InputMedia,
        reply_markup: InlineKeyboardMarkup | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        chat_id: int | str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to edit animation, audio, document, photo, or video
        messages. If a message is part of a message album, then it can be
        edited only to an audio for audio albums, only to a document for
        document albums and to a photo or a video otherwise. When an inline
        message is edited, a new file can't be uploaded; use a previously
        uploaded file via its file_id or specify a URL. On success, if the
        edited message is not an inline message, the edited Message is
        returned, otherwise True is returned. Note that business messages that
        were not sent by the bot and do not contain an inline keyboard can
        only be edited within 48 hours from the time they were sent.
        """
        response = await self.api.request("editMessageMedia", get_params(locals()))
        return from_json(response, type=Message | bool)  # type: ignore

    async def edit_message_live_location(
        self,
        longitude: float,
        latitude: float,
        reply_markup: InlineKeyboardMarkup | None = None,
        proximity_alert_radius: int | None = None,
        message_id: int | None = None,
        live_period: int | None = None,
        inline_message_id: str | None = None,
        horizontal_accuracy: float | None = None,
        heading: int | None = None,
        chat_id: int | str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to edit live location messages. A location can be
        edited until its live_period expires or editing is explicitly disabled
        by a call to stopMessageLiveLocation. On success, if the edited
        message is not an inline message, the edited Message is returned,
        otherwise True is returned.
        """
        response = await self.api.request(
            "editMessageLiveLocation", get_params(locals())
        )
        return from_json(response, type=Message | bool)  # type: ignore

    async def stop_message_live_location(
        self,
        reply_markup: InlineKeyboardMarkup | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        chat_id: int | str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to stop updating a live location message before
        live_period expires. On success, if the message is not an inline
        message, the edited Message is returned, otherwise True is returned.
        """
        response = await self.api.request(
            "stopMessageLiveLocation", get_params(locals())
        )
        return from_json(response, type=Message | bool)  # type: ignore

    async def edit_message_reply_markup(
        self,
        reply_markup: InlineKeyboardMarkup | None = None,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        chat_id: int | str | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to edit only the reply markup of messages. On success,
        if the edited message is not an inline message, the edited Message is
        returned, otherwise True is returned. Note that business messages that
        were not sent by the bot and do not contain an inline keyboard can
        only be edited within 48 hours from the time they were sent.
        """
        response = await self.api.request(
            "editMessageReplyMarkup", get_params(locals())
        )
        return from_json(response, type=Message | bool)  # type: ignore

    async def stop_poll(
        self,
        message_id: int,
        chat_id: int | str,
        reply_markup: InlineKeyboardMarkup | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Poll:
        """
        Use this method to stop a poll which was sent by the bot. On success,
        the stopped Poll is returned.
        """
        response = await self.api.request("stopPoll", get_params(locals()))
        return from_json(response, type=Poll)

    async def delete_message(
        self, message_id: int, chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to delete a message, including service messages, with
        the following limitations: - A message can only be deleted if it was
        sent less than 48 hours ago. - Service messages about a supergroup,
        channel, or forum topic creation can't be deleted. - A dice message in
        a private chat can only be deleted if it was sent more than 24 hours
        ago. - Bots can delete outgoing messages in private chats, groups, and
        supergroups. - Bots can delete incoming messages in private chats. -
        Bots granted can_post_messages permissions can delete outgoing
        messages in channels. - If the bot is an administrator of a group, it
        can delete any message there. - If the bot has can_delete_messages
        permission in a supergroup or a channel, it can delete any message
        there. Returns True on success.
        """
        response = await self.api.request("deleteMessage", get_params(locals()))
        return from_json(response, type=bool)

    async def delete_messages(
        self, message_ids: list[int], chat_id: int | str, **kwargs
    ) -> bool:
        """
        Use this method to delete multiple messages simultaneously. If some of
        the specified messages can't be found, they are skipped. Returns True
        on success.
        """
        response = await self.api.request("deleteMessages", get_params(locals()))
        return from_json(response, type=bool)

    async def send_sticker(
        self,
        sticker: InputFile | str,
        chat_id: int | str,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send static .WEBP, animated .TGS, or video .WEBM
        stickers. On success, the sent Message is returned.
        """
        response = await self.api.request("sendSticker", get_params(locals()))
        return from_json(response, type=Message)

    async def get_sticker_set(self, name: str, **kwargs) -> StickerSet:
        """
        Use this method to get a sticker set. On success, a StickerSet object
        is returned.
        """
        response = await self.api.request("getStickerSet", get_params(locals()))
        return from_json(response, type=StickerSet)

    async def get_custom_emoji_stickers(
        self, custom_emoji_ids: list[str], **kwargs
    ) -> list[Sticker]:
        """
        Use this method to get information about custom emoji stickers by
        their identifiers. Returns an Array of Sticker objects.
        """
        response = await self.api.request(
            "getCustomEmojiStickers", get_params(locals())
        )
        return from_json(response, type=list[Sticker])

    async def upload_sticker_file(
        self, user_id: int, sticker_format: str, sticker: InputFile, **kwargs
    ) -> File:
        """
        Use this method to upload a file with a sticker for later use in the
        createNewStickerSet, addStickerToSet, or replaceStickerInSet methods
        (the file can be used multiple times). Returns the uploaded File on
        success.
        """
        response = await self.api.request("uploadStickerFile", get_params(locals()))
        return from_json(response, type=File)

    async def create_new_sticker_set(
        self,
        user_id: int,
        title: str,
        stickers: list[InputSticker],
        name: str,
        sticker_type: str | None = None,
        needs_repainting: bool | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to create a new sticker set owned by a user. The bot
        will be able to edit the sticker set thus created. Returns True on
        success.
        """
        response = await self.api.request("createNewStickerSet", get_params(locals()))
        return from_json(response, type=bool)

    async def add_sticker_to_set(
        self, user_id: int, sticker: InputSticker, name: str, **kwargs
    ) -> bool:
        """
        Use this method to add a new sticker to a set created by the bot.
        Emoji sticker sets can have up to 200 stickers. Other sticker sets can
        have up to 120 stickers. Returns True on success.
        """
        response = await self.api.request("addStickerToSet", get_params(locals()))
        return from_json(response, type=bool)

    async def set_sticker_position_in_set(
        self, sticker: str, position: int, **kwargs
    ) -> bool:
        """
        Use this method to move a sticker in a set created by the bot to a
        specific position. Returns True on success.
        """
        response = await self.api.request(
            "setStickerPositionInSet", get_params(locals())
        )
        return from_json(response, type=bool)

    async def delete_sticker_from_set(self, sticker: str, **kwargs) -> bool:
        """
        Use this method to delete a sticker from a set created by the bot.
        Returns True on success.
        """
        response = await self.api.request("deleteStickerFromSet", get_params(locals()))
        return from_json(response, type=bool)

    async def replace_sticker_in_set(
        self, user_id: int, sticker: InputSticker, old_sticker: str, name: str, **kwargs
    ) -> bool:
        """
        Use this method to replace an existing sticker in a sticker set with a
        new one. The method is equivalent to calling deleteStickerFromSet,
        then addStickerToSet, then setStickerPositionInSet. Returns True on
        success.
        """
        response = await self.api.request("replaceStickerInSet", get_params(locals()))
        return from_json(response, type=bool)

    async def set_sticker_emoji_list(
        self, sticker: str, emoji_list: list[str], **kwargs
    ) -> bool:
        """
        Use this method to change the list of emoji assigned to a regular or
        custom emoji sticker. The sticker must belong to a sticker set created
        by the bot. Returns True on success.
        """
        response = await self.api.request("setStickerEmojiList", get_params(locals()))
        return from_json(response, type=bool)

    async def set_sticker_keywords(
        self, sticker: str, keywords: list[str] | None = None, **kwargs
    ) -> bool:
        """
        Use this method to change search keywords assigned to a regular or
        custom emoji sticker. The sticker must belong to a sticker set created
        by the bot. Returns True on success.
        """
        response = await self.api.request("setStickerKeywords", get_params(locals()))
        return from_json(response, type=bool)

    async def set_sticker_mask_position(
        self, sticker: str, mask_position: MaskPosition | None = None, **kwargs
    ) -> bool:
        """
        Use this method to change the mask position of a mask sticker. The
        sticker must belong to a sticker set that was created by the bot.
        Returns True on success.
        """
        response = await self.api.request(
            "setStickerMaskPosition", get_params(locals())
        )
        return from_json(response, type=bool)

    async def set_sticker_set_title(self, title: str, name: str, **kwargs) -> bool:
        """
        Use this method to set the title of a created sticker set. Returns
        True on success.
        """
        response = await self.api.request("setStickerSetTitle", get_params(locals()))
        return from_json(response, type=bool)

    async def set_sticker_set_thumbnail(
        self,
        user_id: int,
        name: str,
        format: str,
        thumbnail: InputFile | str | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to set the thumbnail of a regular or mask sticker set.
        The format of the thumbnail file must match the format of the stickers
        in the set. Returns True on success.
        """
        response = await self.api.request(
            "setStickerSetThumbnail", get_params(locals())
        )
        return from_json(response, type=bool)

    async def set_custom_emoji_sticker_set_thumbnail(
        self, name: str, custom_emoji_id: str | None = None, **kwargs
    ) -> bool:
        """
        Use this method to set the thumbnail of a custom emoji sticker set.
        Returns True on success.
        """
        response = await self.api.request(
            "setCustomEmojiStickerSetThumbnail", get_params(locals())
        )
        return from_json(response, type=bool)

    async def delete_sticker_set(self, name: str, **kwargs) -> bool:
        """
        Use this method to delete a sticker set that was created by the bot.
        Returns True on success.
        """
        response = await self.api.request("deleteStickerSet", get_params(locals()))
        return from_json(response, type=bool)

    async def answer_inline_query(
        self,
        results: list[InlineQueryResult],
        inline_query_id: str,
        next_offset: str | None = None,
        is_personal: bool | None = None,
        cache_time: int | None = None,
        button: InlineQueryResultsButton | None = None,
        **kwargs,
    ) -> bool:
        """
        Use this method to send answers to an inline query. On success, True
        is returned. No more than 50 results per query are allowed.
        """
        response = await self.api.request("answerInlineQuery", get_params(locals()))
        return from_json(response, type=bool)

    async def answer_web_app_query(
        self, web_app_query_id: str, result: InlineQueryResult, **kwargs
    ) -> SentWebAppMessage:
        """
        Use this method to set the result of an interaction with a Web App and
        send a corresponding message on behalf of the user to the chat from
        which the query originated. On success, a SentWebAppMessage object is
        returned.
        """
        response = await self.api.request("answerWebAppQuery", get_params(locals()))
        return from_json(response, type=SentWebAppMessage)

    async def send_invoice(
        self,
        title: str,
        prices: list[LabeledPrice],
        payload: str,
        description: str,
        currency: str,
        chat_id: int | str,
        suggested_tip_amounts: list[int] | None = None,
        start_parameter: str | None = None,
        send_phone_number_to_provider: bool | None = None,
        send_email_to_provider: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
        provider_token: str | None = None,
        provider_data: str | None = None,
        protect_content: bool | None = None,
        photo_width: int | None = None,
        photo_url: str | None = None,
        photo_size: int | None = None,
        photo_height: int | None = None,
        need_shipping_address: bool | None = None,
        need_phone_number: bool | None = None,
        need_name: bool | None = None,
        need_email: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        max_tip_amount: int | None = None,
        is_flexible: bool | None = None,
        disable_notification: bool | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send invoices. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendInvoice", get_params(locals()))
        return from_json(response, type=Message)

    async def create_invoice_link(
        self,
        title: str,
        prices: list[LabeledPrice],
        payload: str,
        description: str,
        currency: str,
        suggested_tip_amounts: list[int] | None = None,
        send_phone_number_to_provider: bool | None = None,
        send_email_to_provider: bool | None = None,
        provider_token: str | None = None,
        provider_data: str | None = None,
        photo_width: int | None = None,
        photo_url: str | None = None,
        photo_size: int | None = None,
        photo_height: int | None = None,
        need_shipping_address: bool | None = None,
        need_phone_number: bool | None = None,
        need_name: bool | None = None,
        need_email: bool | None = None,
        max_tip_amount: int | None = None,
        is_flexible: bool | None = None,
        **kwargs,
    ) -> str:
        """
        Use this method to create a link for an invoice. Returns the created
        invoice link as String on success.
        """
        response = await self.api.request("createInvoiceLink", get_params(locals()))
        return from_json(response, type=str)

    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: list[ShippingOption] | None = None,
        error_message: str | None = None,
        **kwargs,
    ) -> bool:
        """
        If you sent an invoice requesting a shipping address and the parameter
        is_flexible was specified, the Bot API will send an Update with a
        shipping_query field to the bot. Use this method to reply to shipping
        queries. On success, True is returned.
        """
        response = await self.api.request("answerShippingQuery", get_params(locals()))
        return from_json(response, type=bool)

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Once the user has confirmed their payment and shipping details, the
        Bot API sends the final confirmation in the form of an Update with the
        field pre_checkout_query. Use this method to respond to such pre-
        checkout queries. On success, True is returned. Note: The Bot API must
        receive an answer within 10 seconds after the pre-checkout query was
        sent.
        """
        response = await self.api.request(
            "answerPreCheckoutQuery", get_params(locals())
        )
        return from_json(response, type=bool)

    async def get_star_transactions(
        self, offset: int | None = None, limit: int | None = None, **kwargs
    ) -> StarTransactions:
        """
        Returns the bot's Telegram Star transactions in chronological order.
        On success, returns a StarTransactions object.
        """
        response = await self.api.request("getStarTransactions", get_params(locals()))
        return from_json(response, type=StarTransactions)

    async def refund_star_payment(
        self, user_id: int, telegram_payment_charge_id: str, **kwargs
    ) -> bool:
        """
        Refunds a successful payment in Telegram Stars. Returns True on
        success.
        """
        response = await self.api.request("refundStarPayment", get_params(locals()))
        return from_json(response, type=bool)

    async def set_passport_data_errors(
        self, user_id: int, errors: list[PassportElementError], **kwargs
    ) -> bool:
        """
        Informs a user that some of the Telegram Passport elements they
        provided contains errors. The user will not be able to re-submit their
        Passport to you until the errors are fixed (the contents of the field
        for which you returned the error must change). Returns True on
        success. Use this if the data submitted by the user doesn't satisfy
        the standards your service requires for any reason. For example, if a
        birthday date seems invalid, a submitted document is blurry, a scan
        shows evidence of tampering, etc. Supply some details in the error
        message to make sure the user knows how to correct the issues.
        """
        response = await self.api.request("setPassportDataErrors", get_params(locals()))
        return from_json(response, type=bool)

    async def send_game(
        self,
        game_short_name: str,
        chat_id: int,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
        protect_content: bool | None = None,
        message_thread_id: int | None = None,
        message_effect_id: str | None = None,
        disable_notification: bool | None = None,
        business_connection_id: str | None = None,
        **kwargs,
    ) -> Message:
        """
        Use this method to send a game. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendGame", get_params(locals()))
        return from_json(response, type=Message)

    async def set_game_score(
        self,
        user_id: int,
        score: int,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        force: bool | None = None,
        disable_edit_message: bool | None = None,
        chat_id: int | None = None,
        **kwargs,
    ) -> Message | bool:
        """
        Use this method to set the score of the specified user in a game
        message. On success, if the message is not an inline message, the
        Message is returned, otherwise True is returned. Returns an error, if
        the new score is not greater than the user's current score in the chat
        and force is False.
        """
        response = await self.api.request("setGameScore", get_params(locals()))
        return from_json(response, type=Message | bool)  # type: ignore

    async def get_game_high_scores(
        self,
        user_id: int,
        message_id: int | None = None,
        inline_message_id: str | None = None,
        chat_id: int | None = None,
        **kwargs,
    ) -> list[GameHighScore]:
        """
        Use this method to get data for high score tables. Will return the
        score of the specified user and several of their neighbors in a game.
        Returns an Array of GameHighScore objects. This method will currently
        return scores for the target user, plus two of their closest neighbors
        on each side. Will also return the top three users if the user and
        their neighbors are not among them. Please note that this behavior is
        subject to change.
        """
        response = await self.api.request("getGameHighScores", get_params(locals()))
        return from_json(response, type=list[GameHighScore])
