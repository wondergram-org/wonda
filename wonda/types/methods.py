from typing import *

from pydantic import parse_obj_as

from .objects import *

if TYPE_CHECKING:
    from wonda.api import ABCAPI, API, File as InputFile


class APIMethods:
    def __init__(self, api: Union["ABCAPI", "API"]) -> None:
        self.api = api

    @staticmethod
    def get_params(loc: dict) -> dict:
        n = {
            k: v
            for k, v in loc.items()
            if k not in ("self", "kwargs") and v is not None
        }
        n.update(loc["kwargs"])
        return n

    async def get_updates(
        self,
        timeout: Optional[int] = 0,
        offset: Optional[int] = None,
        limit: Optional[int] = 100,
        allowed_updates: Optional[List[str]] = None,
        **kwargs
    ) -> List[Update]:
        """
        Use this method to receive incoming updates using long polling (wiki). Returns an
        Array of Update objects.
        """
        response = await self.api.request("getUpdates", self.get_params(locals()))
        return parse_obj_as(List[Update], response)

    async def set_webhook(
        self,
        url: str,
        secret_token: Optional[str] = None,
        max_connections: Optional[int] = 40,
        ip_address: Optional[str] = None,
        drop_pending_updates: Optional[bool] = None,
        certificate: Optional["InputFile"] = None,
        allowed_updates: Optional[List[str]] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to specify a URL and receive incoming updates via an outgoing
        webhook. Whenever there is an update for the bot, we will send an HTTPS POST request
        to the specified URL, containing a JSON-serialized Update. In case of an
        unsuccessful request, we will give up after a reasonable amount of attempts. Returns
        True on success. If you'd like to make sure that the webhook was set by you, you can
        specify secret data in the parameter secret_token. If specified, the request will
        contain a header “X-Telegram-Bot-Api-Secret-Token” with the secret token as content.
        """
        response = await self.api.request("setWebhook", self.get_params(locals()))
        return response

    async def delete_webhook(
        self, drop_pending_updates: Optional[bool] = None, **kwargs
    ) -> bool:
        """
        Use this method to remove webhook integration if you decide to switch back to
        getUpdates. Returns True on success.
        """
        response = await self.api.request("deleteWebhook", self.get_params(locals()))
        return response

    async def get_webhook_info(self, **kwargs) -> WebhookInfo:
        """
        Use this method to get current webhook status. Requires no parameters. On success,
        returns a WebhookInfo object. If the bot is using getUpdates, will return an object
        with the url field empty.
        """
        response = await self.api.request("getWebhookInfo", self.get_params(locals()))
        return WebhookInfo(**response)

    async def get_me(self, **kwargs) -> User:
        """
        A simple method for testing your bot's authentication token. Requires no parameters.
        Returns basic information about the bot in form of a User object.
        """
        response = await self.api.request("getMe", self.get_params(locals()))
        return User(**response)

    async def log_out(self, **kwargs) -> bool:
        """
        Use this method to log out from the cloud Bot API server before launching the bot
        locally. You must log out the bot before running it locally, otherwise there is no
        guarantee that the bot will receive updates. After a successful call, you can
        immediately log in on a local server, but will not be able to log in back to the
        cloud Bot API server for 10 minutes. Returns True on success. Requires no
        parameters.
        """
        response = await self.api.request("logOut", self.get_params(locals()))
        return response

    async def close(self, **kwargs) -> bool:
        """
        Use this method to close the bot instance before moving it from one local server to
        another. You need to delete the webhook before calling this method to ensure that
        the bot isn't launched again after server restart. The method will return error 429
        in the first 10 minutes after the bot is launched. Returns True on success. Requires
        no parameters.
        """
        response = await self.api.request("close", self.get_params(locals()))
        return response

    async def send_message(
        self,
        text: str,
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        entities: Optional[List["MessageEntity"]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send text messages. On success, the sent Message is returned.
        """
        response = await self.api.request("sendMessage", self.get_params(locals()))
        return Message(**response)

    async def forward_message(
        self,
        message_id: int,
        from_chat_id: Union[int, str],
        chat_id: Union[int, str],
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to forward messages of any kind. Service messages can't be
        forwarded. On success, the sent Message is returned.
        """
        response = await self.api.request("forwardMessage", self.get_params(locals()))
        return Message(**response)

    async def copy_message(
        self,
        message_id: int,
        from_chat_id: Union[int, str],
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> MessageId:
        """
        Use this method to copy messages of any kind. Service messages and invoice messages
        can't be copied. A quiz poll can be copied only if the value of the field
        correct_option_id is known to the bot. The method is analogous to the method
        forwardMessage, but the copied message doesn't have a link to the original message.
        Returns the MessageId of the sent message on success.
        """
        response = await self.api.request("copyMessage", self.get_params(locals()))
        return MessageId(**response)

    async def send_photo(
        self,
        photo: Union["InputFile", str],
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send photos. On success, the sent Message is returned.
        """
        response = await self.api.request("sendPhoto", self.get_params(locals()))
        return Message(**response)

    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: Union["InputFile", str],
        title: Optional[str] = None,
        thumb: Optional[Union["InputFile", str]] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        performer: Optional[str] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to display them in
        the music player. Your audio must be in the .MP3 or .M4A format. On success, the
        sent Message is returned. Bots can currently send audio files of up to 50 MB in
        size, this limit may be changed in the future. For sending voice messages, use the
        sendVoice method instead.
        """
        response = await self.api.request("sendAudio", self.get_params(locals()))
        return Message(**response)

    async def send_document(
        self,
        document: Union["InputFile", str],
        chat_id: Union[int, str],
        thumb: Optional[Union["InputFile", str]] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        disable_content_type_detection: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send general files. On success, the sent Message is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may be
        changed in the future.
        """
        response = await self.api.request("sendDocument", self.get_params(locals()))
        return Message(**response)

    async def send_video(
        self,
        video: Union["InputFile", str],
        chat_id: Union[int, str],
        width: Optional[int] = None,
        thumb: Optional[Union["InputFile", str]] = None,
        supports_streaming: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        height: Optional[int] = None,
        has_spoiler: Optional[bool] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send video files, Telegram clients support MPEG4 videos (other
        formats may be sent as Document). On success, the sent Message is returned. Bots can
        currently send video files of up to 50 MB in size, this limit may be changed in the
        future.
        """
        response = await self.api.request("sendVideo", self.get_params(locals()))
        return Message(**response)

    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: Union["InputFile", str],
        width: Optional[int] = None,
        thumb: Optional[Union["InputFile", str]] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        height: Optional[int] = None,
        has_spoiler: Optional[bool] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without
        sound). On success, the sent Message is returned. Bots can currently send animation
        files of up to 50 MB in size, this limit may be changed in the future.
        """
        response = await self.api.request("sendAnimation", self.get_params(locals()))
        return Message(**response)

    async def send_voice(
        self,
        voice: Union["InputFile", str],
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        parse_mode: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send audio files, if you want Telegram clients to display the
        file as a playable voice message. For this to work, your audio must be in an .OGG
        file encoded with OPUS (other formats may be sent as Audio or Document). On success,
        the sent Message is returned. Bots can currently send voice messages of up to 50 MB
        in size, this limit may be changed in the future.
        """
        response = await self.api.request("sendVoice", self.get_params(locals()))
        return Message(**response)

    async def send_video_note(
        self,
        video_note: Union["InputFile", str],
        chat_id: Union[int, str],
        thumb: Optional[Union["InputFile", str]] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        length: Optional[int] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute
        long. Use this method to send video messages. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendVideoNote", self.get_params(locals()))
        return Message(**response)

    async def send_media_group(
        self,
        media: List[
            Union[
                "InputMediaAudio",
                "InputMediaDocument",
                "InputMediaPhoto",
                "InputMediaVideo",
            ]
        ],
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> List[Message]:
        """
        Use this method to send a group of photos, videos, documents or audios as an album.
        Documents and audio files can be only grouped in an album with messages of the same
        type. On success, an array of Messages that were sent is returned.
        """
        response = await self.api.request("sendMediaGroup", self.get_params(locals()))
        return parse_obj_as(List[Message], response)

    async def send_location(
        self,
        longitude: float,
        latitude: float,
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        proximity_alert_radius: Optional[int] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        live_period: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send point on the map. On success, the sent Message is returned.
        """
        response = await self.api.request("sendLocation", self.get_params(locals()))
        return Message(**response)

    async def edit_message_live_location(
        self,
        longitude: float,
        latitude: float,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        proximity_alert_radius: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        chat_id: Optional[Union[int, str]] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to edit live location messages. A location can be edited until its
        live_period expires or editing is explicitly disabled by a call to
        stopMessageLiveLocation. On success, if the edited message is not an inline message,
        the edited Message is returned, otherwise True is returned.
        """
        response = await self.api.request(
            "editMessageLiveLocation", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def stop_message_live_location(
        self,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to stop updating a live location message before live_period expires.
        On success, if the message is not an inline message, the edited Message is returned,
        otherwise True is returned.
        """
        response = await self.api.request(
            "stopMessageLiveLocation", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def send_venue(
        self,
        title: str,
        longitude: float,
        latitude: float,
        chat_id: Union[int, str],
        address: str,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        google_place_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        foursquare_id: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send information about a venue. On success, the sent Message is
        returned.
        """
        response = await self.api.request("sendVenue", self.get_params(locals()))
        return Message(**response)

    async def send_contact(
        self,
        phone_number: str,
        first_name: str,
        chat_id: Union[int, str],
        vcard: Optional[str] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        last_name: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send phone contacts. On success, the sent Message is returned.
        """
        response = await self.api.request("sendContact", self.get_params(locals()))
        return Message(**response)

    async def send_poll(
        self,
        question: str,
        options: List[str],
        chat_id: Union[int, str],
        type: Optional[str] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        open_period: Optional[int] = None,
        message_thread_id: Optional[int] = None,
        is_closed: Optional[bool] = None,
        is_anonymous: Optional[bool] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[List["MessageEntity"]] = None,
        explanation: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        close_date: Optional[int] = None,
        allows_multiple_answers: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send a native poll. On success, the sent Message is returned.
        """
        response = await self.api.request("sendPoll", self.get_params(locals()))
        return Message(**response)

    async def send_dice(
        self,
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = "🎲",
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send an animated emoji that will display a random value. On
        success, the sent Message is returned.
        """
        response = await self.api.request("sendDice", self.get_params(locals()))
        return Message(**response)

    async def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: str,
        message_thread_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        """
        Use this method when you need to tell the user that something is happening on the
        bot's side. The status is set for 5 seconds or less (when a message arrives from
        your bot, Telegram clients clear its typing status). Returns True on success.
        Example: The ImageBot needs some time to process a request and upload the image.
        Instead of sending a text message along the lines of “Retrieving image, please
        wait…”, the bot may use sendChatAction with action = upload_photo. The user will see
        a “sending photo” status for the bot. We only recommend using this method when a
        response from the bot will take a noticeable amount of time to arrive.
        """
        response = await self.api.request("sendChatAction", self.get_params(locals()))
        return response

    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = 100,
        **kwargs
    ) -> UserProfilePhotos:
        """
        Use this method to get a list of profile pictures for a user. Returns a
        UserProfilePhotos object.
        """
        response = await self.api.request(
            "getUserProfilePhotos", self.get_params(locals())
        )
        return UserProfilePhotos(**response)

    async def get_file(self, file_id: str, **kwargs) -> File:
        """
        Use this method to get basic information about a file and prepare it for
        downloading. For the moment, bots can download files of up to 20MB in size. On
        success, a File object is returned. The file can then be downloaded via the link
        https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt;, where
        &lt;file_path&gt; is taken from the response. It is guaranteed that the link will be
        valid for at least 1 hour. When the link expires, a new one can be requested by
        calling getFile again.
        """
        response = await self.api.request("getFile", self.get_params(locals()))
        return File(**response)

    async def ban_chat_member(
        self,
        user_id: int,
        chat_id: Union[int, str],
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to ban a user in a group, a supergroup or a channel. In the case of
        supergroups and channels, the user will not be able to return to the chat on their
        own using invite links, etc., unless unbanned first. The bot must be an
        administrator in the chat for this to work and must have the appropriate
        administrator rights. Returns True on success.
        """
        response = await self.api.request("banChatMember", self.get_params(locals()))
        return response

    async def unban_chat_member(
        self,
        user_id: int,
        chat_id: Union[int, str],
        only_if_banned: Optional[bool] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to unban a previously banned user in a supergroup or channel. The
        user will not return to the group or channel automatically, but will be able to join
        via link, etc. The bot must be an administrator for this to work. By default, this
        method guarantees that after the call the user is not a member of the chat, but will
        be able to join it. So if the user is a member of the chat they will also be removed
        from the chat. If you don't want this, use the parameter only_if_banned. Returns
        True on success.
        """
        response = await self.api.request("unbanChatMember", self.get_params(locals()))
        return response

    async def restrict_chat_member(
        self,
        user_id: int,
        permissions: "ChatPermissions",
        chat_id: Union[int, str],
        until_date: Optional[int] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to restrict a user in a supergroup. The bot must be an administrator
        in the supergroup for this to work and must have the appropriate administrator
        rights. Pass True for all permissions to lift restrictions from a user. Returns True
        on success.
        """
        response = await self.api.request(
            "restrictChatMember", self.get_params(locals())
        )
        return response

    async def promote_chat_member(
        self,
        user_id: int,
        chat_id: Union[int, str],
        is_anonymous: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to promote or demote a user in a supergroup or a channel. The bot
        must be an administrator in the chat for this to work and must have the appropriate
        administrator rights. Pass False for all boolean parameters to demote a user.
        Returns True on success.
        """
        response = await self.api.request(
            "promoteChatMember", self.get_params(locals())
        )
        return response

    async def set_chat_administrator_custom_title(
        self, user_id: int, custom_title: str, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to set a custom title for an administrator in a supergroup promoted
        by the bot. Returns True on success.
        """
        response = await self.api.request(
            "setChatAdministratorCustomTitle", self.get_params(locals())
        )
        return response

    async def ban_chat_sender_chat(
        self, sender_chat_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to ban a channel chat in a supergroup or a channel. Until the chat
        is unbanned, the owner of the banned chat won't be able to send messages on behalf
        of any of their channels. The bot must be an administrator in the supergroup or
        channel for this to work and must have the appropriate administrator rights. Returns
        True on success.
        """
        response = await self.api.request(
            "banChatSenderChat", self.get_params(locals())
        )
        return response

    async def unban_chat_sender_chat(
        self, sender_chat_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to unban a previously banned channel chat in a supergroup or
        channel. The bot must be an administrator for this to work and must have the
        appropriate administrator rights. Returns True on success.
        """
        response = await self.api.request(
            "unbanChatSenderChat", self.get_params(locals())
        )
        return response

    async def set_chat_permissions(
        self, permissions: "ChatPermissions", chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to set default chat permissions for all members. The bot must be an
        administrator in the group or a supergroup for this to work and must have the
        can_restrict_members administrator rights. Returns True on success.
        """
        response = await self.api.request(
            "setChatPermissions", self.get_params(locals())
        )
        return response

    async def export_chat_invite_link(self, chat_id: Union[int, str], **kwargs) -> str:
        """
        Use this method to generate a new primary invite link for a chat; any previously
        generated primary link is revoked. The bot must be an administrator in the chat for
        this to work and must have the appropriate administrator rights. Returns the new
        invite link as String on success.
        """
        response = await self.api.request(
            "exportChatInviteLink", self.get_params(locals())
        )
        return response

    async def create_chat_invite_link(
        self,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        member_limit: Optional[int] = None,
        expire_date: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
        **kwargs
    ) -> ChatInviteLink:
        """
        Use this method to create an additional invite link for a chat. The bot must be an
        administrator in the chat for this to work and must have the appropriate
        administrator rights. The link can be revoked using the method revokeChatInviteLink.
        Returns the new invite link as ChatInviteLink object.
        """
        response = await self.api.request(
            "createChatInviteLink", self.get_params(locals())
        )
        return ChatInviteLink(**response)

    async def edit_chat_invite_link(
        self,
        invite_link: str,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        member_limit: Optional[int] = None,
        expire_date: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
        **kwargs
    ) -> ChatInviteLink:
        """
        Use this method to edit a non-primary invite link created by the bot. The bot must
        be an administrator in the chat for this to work and must have the appropriate
        administrator rights. Returns the edited invite link as a ChatInviteLink object.
        """
        response = await self.api.request(
            "editChatInviteLink", self.get_params(locals())
        )
        return ChatInviteLink(**response)

    async def revoke_chat_invite_link(
        self, invite_link: str, chat_id: Union[int, str], **kwargs
    ) -> ChatInviteLink:
        """
        Use this method to revoke an invite link created by the bot. If the primary link is
        revoked, a new link is automatically generated. The bot must be an administrator in
        the chat for this to work and must have the appropriate administrator rights.
        Returns the revoked invite link as ChatInviteLink object.
        """
        response = await self.api.request(
            "revokeChatInviteLink", self.get_params(locals())
        )
        return ChatInviteLink(**response)

    async def approve_chat_join_request(
        self, user_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to approve a chat join request. The bot must be an administrator in
        the chat for this to work and must have the can_invite_users administrator right.
        Returns True on success.
        """
        response = await self.api.request(
            "approveChatJoinRequest", self.get_params(locals())
        )
        return response

    async def decline_chat_join_request(
        self, user_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to decline a chat join request. The bot must be an administrator in
        the chat for this to work and must have the can_invite_users administrator right.
        Returns True on success.
        """
        response = await self.api.request(
            "declineChatJoinRequest", self.get_params(locals())
        )
        return response

    async def set_chat_photo(
        self, photo: "InputFile", chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed for
        private chats. The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Returns True on success.
        """
        response = await self.api.request("setChatPhoto", self.get_params(locals()))
        return response

    async def delete_chat_photo(self, chat_id: Union[int, str], **kwargs) -> bool:
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns True on success.
        """
        response = await self.api.request("deleteChatPhoto", self.get_params(locals()))
        return response

    async def set_chat_title(
        self, title: str, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to change the title of a chat. Titles can't be changed for private
        chats. The bot must be an administrator in the chat for this to work and must have
        the appropriate administrator rights. Returns True on success.
        """
        response = await self.api.request("setChatTitle", self.get_params(locals()))
        return response

    async def set_chat_description(
        self, chat_id: Union[int, str], description: Optional[str] = None, **kwargs
    ) -> bool:
        """
        Use this method to change the description of a group, a supergroup or a channel. The
        bot must be an administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns True on success.
        """
        response = await self.api.request(
            "setChatDescription", self.get_params(locals())
        )
        return response

    async def pin_chat_message(
        self,
        message_id: int,
        chat_id: Union[int, str],
        disable_notification: Optional[bool] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to add a message to the list of pinned messages in a chat. If the
        chat is not a private chat, the bot must be an administrator in the chat for this to
        work and must have the 'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns True on success.
        """
        response = await self.api.request("pinChatMessage", self.get_params(locals()))
        return response

    async def unpin_chat_message(
        self, chat_id: Union[int, str], message_id: Optional[int] = None, **kwargs
    ) -> bool:
        """
        Use this method to remove a message from the list of pinned messages in a chat. If
        the chat is not a private chat, the bot must be an administrator in the chat for
        this to work and must have the 'can_pin_messages' administrator right in a
        supergroup or 'can_edit_messages' administrator right in a channel. Returns True on
        success.
        """
        response = await self.api.request("unpinChatMessage", self.get_params(locals()))
        return response

    async def unpin_all_chat_messages(self, chat_id: Union[int, str], **kwargs) -> bool:
        """
        Use this method to clear the list of pinned messages in a chat. If the chat is not a
        private chat, the bot must be an administrator in the chat for this to work and must
        have the 'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns True on success.
        """
        response = await self.api.request(
            "unpinAllChatMessages", self.get_params(locals())
        )
        return response

    async def leave_chat(self, chat_id: Union[int, str], **kwargs) -> bool:
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True
        on success.
        """
        response = await self.api.request("leaveChat", self.get_params(locals()))
        return response

    async def get_chat(self, chat_id: Union[int, str], **kwargs) -> Chat:
        """
        Use this method to get up to date information about the chat (current name of the
        user for one-on-one conversations, current username of a user, group or channel,
        etc.). Returns a Chat object on success.
        """
        response = await self.api.request("getChat", self.get_params(locals()))
        return Chat(**response)

    async def get_chat_administrators(
        self, chat_id: Union[int, str], **kwargs
    ) -> List[ChatMember]:
        """
        Use this method to get a list of administrators in a chat, which aren't bots.
        Returns an Array of ChatMember objects.
        """
        response = await self.api.request(
            "getChatAdministrators", self.get_params(locals())
        )
        return parse_obj_as(List[ChatMember], response)

    async def get_chat_member_count(self, chat_id: Union[int, str], **kwargs) -> int:
        """
        Use this method to get the number of members in a chat. Returns Int on success.
        """
        response = await self.api.request(
            "getChatMemberCount", self.get_params(locals())
        )
        return response

    async def get_chat_member(
        self, user_id: int, chat_id: Union[int, str], **kwargs
    ) -> ChatMember:
        """
        Use this method to get information about a member of a chat. The method is
        guaranteed to work only if the bot is an administrator in the chat. Returns a
        ChatMember object on success.
        """
        response = await self.api.request("getChatMember", self.get_params(locals()))
        return parse_obj_as(ChatMember, response)

    async def set_chat_sticker_set(
        self, sticker_set_name: str, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be an
        administrator in the chat for this to work and must have the appropriate
        administrator rights. Use the field can_set_sticker_set optionally returned in
        getChat requests to check if the bot can use this method. Returns True on success.
        """
        response = await self.api.request(
            "setChatStickerSet", self.get_params(locals())
        )
        return response

    async def delete_chat_sticker_set(self, chat_id: Union[int, str], **kwargs) -> bool:
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be an
        administrator in the chat for this to work and must have the appropriate
        administrator rights. Use the field can_set_sticker_set optionally returned in
        getChat requests to check if the bot can use this method. Returns True on success.
        """
        response = await self.api.request(
            "deleteChatStickerSet", self.get_params(locals())
        )
        return response

    async def get_forum_topic_icon_stickers(self, **kwargs) -> List[Sticker]:
        """
        Use this method to get custom emoji stickers, which can be used as a forum topic
        icon by any user. Requires no parameters. Returns an Array of Sticker objects.
        """
        response = await self.api.request(
            "getForumTopicIconStickers", self.get_params(locals())
        )
        return parse_obj_as(List[Sticker], response)

    async def create_forum_topic(
        self,
        name: str,
        chat_id: Union[int, str],
        icon_custom_emoji_id: Optional[str] = None,
        icon_color: Optional[int] = None,
        **kwargs
    ) -> ForumTopic:
        """
        Use this method to create a topic in a forum supergroup chat. The bot must be an
        administrator in the chat for this to work and must have the can_manage_topics
        administrator rights. Returns information about the created topic as a ForumTopic
        object.
        """
        response = await self.api.request("createForumTopic", self.get_params(locals()))
        return ForumTopic(**response)

    async def edit_forum_topic(
        self,
        message_thread_id: int,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        icon_custom_emoji_id: Optional[str] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to edit name and icon of a topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have
        can_manage_topics administrator rights, unless it is the creator of the topic.
        Returns True on success.
        """
        response = await self.api.request("editForumTopic", self.get_params(locals()))
        return response

    async def close_forum_topic(
        self, message_thread_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to close an open topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic. Returns True on
        success.
        """
        response = await self.api.request("closeForumTopic", self.get_params(locals()))
        return response

    async def reopen_forum_topic(
        self, message_thread_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to reopen a closed topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic. Returns True on
        success.
        """
        response = await self.api.request("reopenForumTopic", self.get_params(locals()))
        return response

    async def delete_forum_topic(
        self, message_thread_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to delete a forum topic along with all its messages in a forum
        supergroup chat. The bot must be an administrator in the chat for this to work and
        must have the can_delete_messages administrator rights. Returns True on success.
        """
        response = await self.api.request("deleteForumTopic", self.get_params(locals()))
        return response

    async def unpin_all_forum_topic_messages(
        self, message_thread_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to clear the list of pinned messages in a forum topic. The bot must
        be an administrator in the chat for this to work and must have the can_pin_messages
        administrator right in the supergroup. Returns True on success.
        """
        response = await self.api.request(
            "unpinAllForumTopicMessages", self.get_params(locals())
        )
        return response

    async def edit_general_forum_topic(
        self, name: str, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to edit the name of the 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        can_manage_topics administrator rights. Returns True on success.
        """
        response = await self.api.request(
            "editGeneralForumTopic", self.get_params(locals())
        )
        return response

    async def close_general_forum_topic(
        self, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to close an open 'General' topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. Returns True on success.
        """
        response = await self.api.request(
            "closeGeneralForumTopic", self.get_params(locals())
        )
        return response

    async def reopen_general_forum_topic(
        self, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to reopen a closed 'General' topic in a forum supergroup chat. The
        bot must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. The topic will be automatically unhidden if
        it was hidden. Returns True on success.
        """
        response = await self.api.request(
            "reopenGeneralForumTopic", self.get_params(locals())
        )
        return response

    async def hide_general_forum_topic(
        self, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to hide the 'General' topic in a forum supergroup chat. The bot must
        be an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights. The topic will be automatically closed if it was open. Returns
        True on success.
        """
        response = await self.api.request(
            "hideGeneralForumTopic", self.get_params(locals())
        )
        return response

    async def unhide_general_forum_topic(
        self, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to unhide the 'General' topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have the
        can_manage_topics administrator rights. Returns True on success.
        """
        response = await self.api.request(
            "unhideGeneralForumTopic", self.get_params(locals())
        )
        return response

    async def answer_callback_query(
        self,
        callback_query_id: str,
        url: Optional[str] = None,
        text: Optional[str] = None,
        show_alert: Optional[bool] = False,
        cache_time: Optional[int] = 0,
        **kwargs
    ) -> bool:
        """
        Use this method to send answers to callback queries sent from inline keyboards. The
        answer will be displayed to the user as a notification at the top of the chat screen
        or as an alert. On success, True is returned. Alternatively, the user can be
        redirected to the specified Game URL. For this option to work, you must first create
        a game for your bot via @BotFather and accept the terms. Otherwise, you may use
        links like t.me/your_bot?start=XXXX that open your bot with a parameter.
        """
        response = await self.api.request(
            "answerCallbackQuery", self.get_params(locals())
        )
        return response

    async def set_my_commands(
        self,
        commands: List["BotCommand"],
        scope: Optional["BotCommandScope"] = None,
        language_code: Optional[str] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to change the list of the bot's commands. See this manual for more
        details about bot commands. Returns True on success.
        """
        response = await self.api.request("setMyCommands", self.get_params(locals()))
        return response

    async def delete_my_commands(
        self,
        scope: Optional["BotCommandScope"] = None,
        language_code: Optional[str] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to delete the list of the bot's commands for the given scope and
        user language. After deletion, higher level commands will be shown to affected
        users. Returns True on success.
        """
        response = await self.api.request("deleteMyCommands", self.get_params(locals()))
        return response

    async def get_my_commands(
        self,
        scope: Optional["BotCommandScope"] = None,
        language_code: Optional[str] = None,
        **kwargs
    ) -> List[BotCommand]:
        """
        Use this method to get the current list of the bot's commands for the given scope
        and user language. Returns an Array of BotCommand objects. If commands aren't set,
        an empty list is returned.
        """
        response = await self.api.request("getMyCommands", self.get_params(locals()))
        return parse_obj_as(List[BotCommand], response)

    async def set_chat_menu_button(
        self,
        menu_button: Optional["MenuButton"] = None,
        chat_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to change the bot's menu button in a private chat, or the default
        menu button. Returns True on success.
        """
        response = await self.api.request(
            "setChatMenuButton", self.get_params(locals())
        )
        return response

    async def get_chat_menu_button(
        self, chat_id: Optional[int] = None, **kwargs
    ) -> MenuButton:
        """
        Use this method to get the current value of the bot's menu button in a private chat,
        or the default menu button. Returns MenuButton on success.
        """
        response = await self.api.request(
            "getChatMenuButton", self.get_params(locals())
        )
        return parse_obj_as(MenuButton, response)

    async def set_my_default_administrator_rights(
        self,
        rights: Optional["ChatAdministratorRights"] = None,
        for_channels: Optional[bool] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to change the default administrator rights requested by the bot when
        it's added as an administrator to groups or channels. These rights will be suggested
        to users, but they are are free to modify the list before adding the bot. Returns
        True on success.
        """
        response = await self.api.request(
            "setMyDefaultAdministratorRights", self.get_params(locals())
        )
        return response

    async def get_my_default_administrator_rights(
        self, for_channels: Optional[bool] = None, **kwargs
    ) -> ChatAdministratorRights:
        """
        Use this method to get the current default administrator rights of the bot. Returns
        ChatAdministratorRights on success.
        """
        response = await self.api.request(
            "getMyDefaultAdministratorRights", self.get_params(locals())
        )
        return ChatAdministratorRights(**response)

    async def edit_message_text(
        self,
        text: str,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        parse_mode: Optional[str] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        entities: Optional[List["MessageEntity"]] = None,
        disable_web_page_preview: Optional[bool] = None,
        chat_id: Optional[Union[int, str]] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to edit text and game messages. On success, if the edited message is
        not an inline message, the edited Message is returned, otherwise True is returned.
        """
        response = await self.api.request("editMessageText", self.get_params(locals()))
        return parse_obj_as(Union[Message, bool], response)

    async def edit_message_caption(
        self,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        parse_mode: Optional[str] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        caption: Optional[str] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to edit captions of messages. On success, if the edited message is
        not an inline message, the edited Message is returned, otherwise True is returned.
        """
        response = await self.api.request(
            "editMessageCaption", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def edit_message_media(
        self,
        media: "InputMedia",
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to edit animation, audio, document, photo, or video messages. If a
        message is part of a message album, then it can be edited only to an audio for audio
        albums, only to a document for document albums and to a photo or a video otherwise.
        When an inline message is edited, a new file can't be uploaded; use a previously
        uploaded file via its file_id or specify a URL. On success, if the edited message is
        not an inline message, the edited Message is returned, otherwise True is returned.
        """
        response = await self.api.request("editMessageMedia", self.get_params(locals()))
        return parse_obj_as(Union[Message, bool], response)

    async def edit_message_reply_markup(
        self,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to edit only the reply markup of messages. On success, if the edited
        message is not an inline message, the edited Message is returned, otherwise True is
        returned.
        """
        response = await self.api.request(
            "editMessageReplyMarkup", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def stop_poll(
        self,
        message_id: int,
        chat_id: Union[int, str],
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        **kwargs
    ) -> Poll:
        """
        Use this method to stop a poll which was sent by the bot. On success, the stopped
        Poll is returned.
        """
        response = await self.api.request("stopPoll", self.get_params(locals()))
        return Poll(**response)

    async def delete_message(
        self, message_id: int, chat_id: Union[int, str], **kwargs
    ) -> bool:
        """
        Use this method to delete a message, including service messages, with the following
        limitations: - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be
        deleted. - A dice message in a private chat can only be deleted if it was sent more
        than 24 hours ago. - Bots can delete outgoing messages in private chats, groups, and
        supergroups. - Bots can delete incoming messages in private chats. - Bots granted
        can_post_messages permissions can delete outgoing messages in channels. - If the bot
        is an administrator of a group, it can delete any message there. - If the bot has
        can_delete_messages permission in a supergroup or a channel, it can delete any
        message there. Returns True on success.
        """
        response = await self.api.request("deleteMessage", self.get_params(locals()))
        return response

    async def send_sticker(
        self,
        sticker: Union["InputFile", str],
        chat_id: Union[int, str],
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On
        success, the sent Message is returned.
        """
        response = await self.api.request("sendSticker", self.get_params(locals()))
        return Message(**response)

    async def get_sticker_set(self, name: str, **kwargs) -> StickerSet:
        """
        Use this method to get a sticker set. On success, a StickerSet object is returned.
        """
        response = await self.api.request("getStickerSet", self.get_params(locals()))
        return StickerSet(**response)

    async def get_custom_emoji_stickers(
        self, custom_emoji_ids: List[str], **kwargs
    ) -> List[Sticker]:
        """
        Use this method to get information about custom emoji stickers by their identifiers.
        Returns an Array of Sticker objects.
        """
        response = await self.api.request(
            "getCustomEmojiStickers", self.get_params(locals())
        )
        return parse_obj_as(List[Sticker], response)

    async def upload_sticker_file(
        self, user_id: int, png_sticker: "InputFile", **kwargs
    ) -> File:
        """
        Use this method to upload a .PNG file with a sticker for later use in
        createNewStickerSet and addStickerToSet methods (can be used multiple times).
        Returns the uploaded File on success.
        """
        response = await self.api.request(
            "uploadStickerFile", self.get_params(locals())
        )
        return File(**response)

    async def create_new_sticker_set(
        self,
        user_id: int,
        title: str,
        name: str,
        emojis: str,
        webm_sticker: Optional["InputFile"] = None,
        tgs_sticker: Optional["InputFile"] = None,
        sticker_type: Optional[str] = None,
        png_sticker: Optional[Union["InputFile", str]] = None,
        mask_position: Optional["MaskPosition"] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to create a new sticker set owned by a user. The bot will be able to
        edit the sticker set thus created. You must use exactly one of the fields
        png_sticker, tgs_sticker, or webm_sticker. Returns True on success.
        """
        response = await self.api.request(
            "createNewStickerSet", self.get_params(locals())
        )
        return response

    async def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        emojis: str,
        webm_sticker: Optional["InputFile"] = None,
        tgs_sticker: Optional["InputFile"] = None,
        png_sticker: Optional[Union["InputFile", str]] = None,
        mask_position: Optional["MaskPosition"] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to add a new sticker to a set created by the bot. You must use
        exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated
        stickers can be added to animated sticker sets and only to them. Animated sticker
        sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers.
        Returns True on success.
        """
        response = await self.api.request("addStickerToSet", self.get_params(locals()))
        return response

    async def set_sticker_position_in_set(
        self, sticker: str, position: int, **kwargs
    ) -> bool:
        """
        Use this method to move a sticker in a set created by the bot to a specific
        position. Returns True on success.
        """
        response = await self.api.request(
            "setStickerPositionInSet", self.get_params(locals())
        )
        return response

    async def delete_sticker_from_set(self, sticker: str, **kwargs) -> bool:
        """
        Use this method to delete a sticker from a set created by the bot. Returns True on
        success.
        """
        response = await self.api.request(
            "deleteStickerFromSet", self.get_params(locals())
        )
        return response

    async def set_sticker_set_thumb(
        self,
        user_id: int,
        name: str,
        thumb: Optional[Union["InputFile", str]] = None,
        **kwargs
    ) -> bool:
        """
        Use this method to set the thumbnail of a sticker set. Animated thumbnails can be
        set for animated sticker sets only. Video thumbnails can be set only for video
        sticker sets only. Returns True on success.
        """
        response = await self.api.request(
            "setStickerSetThumb", self.get_params(locals())
        )
        return response

    async def answer_inline_query(
        self,
        results: List["InlineQueryResult"],
        inline_query_id: str,
        switch_pm_text: Optional[str] = None,
        switch_pm_parameter: Optional[str] = None,
        next_offset: Optional[str] = None,
        is_personal: Optional[bool] = None,
        cache_time: Optional[int] = 300,
        **kwargs
    ) -> bool:
        """
        Use this method to send answers to an inline query. On success, True is returned. No
        more than 50 results per query are allowed.
        """
        response = await self.api.request(
            "answerInlineQuery", self.get_params(locals())
        )
        return response

    async def answer_web_app_query(
        self, web_app_query_id: str, result: "InlineQueryResult", **kwargs
    ) -> SentWebAppMessage:
        """
        Use this method to set the result of an interaction with a Web App and send a
        corresponding message on behalf of the user to the chat from which the query
        originated. On success, a SentWebAppMessage object is returned.
        """
        response = await self.api.request(
            "answerWebAppQuery", self.get_params(locals())
        )
        return SentWebAppMessage(**response)

    async def send_invoice(
        self,
        title: str,
        provider_token: str,
        prices: List["LabeledPrice"],
        payload: str,
        description: str,
        currency: str,
        chat_id: Union[int, str],
        suggested_tip_amounts: Optional[List[int]] = None,
        start_parameter: Optional[str] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        provider_data: Optional[str] = None,
        protect_content: Optional[bool] = None,
        photo_width: Optional[int] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_shipping_address: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_name: Optional[bool] = None,
        need_email: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        max_tip_amount: Optional[int] = 0,
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send invoices. On success, the sent Message is returned.
        """
        response = await self.api.request("sendInvoice", self.get_params(locals()))
        return Message(**response)

    async def create_invoice_link(
        self,
        title: str,
        provider_token: str,
        prices: List["LabeledPrice"],
        payload: str,
        description: str,
        currency: str,
        suggested_tip_amounts: Optional[List[int]] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        provider_data: Optional[str] = None,
        photo_width: Optional[int] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_shipping_address: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_name: Optional[bool] = None,
        need_email: Optional[bool] = None,
        max_tip_amount: Optional[int] = 0,
        is_flexible: Optional[bool] = None,
        **kwargs
    ) -> str:
        """
        Use this method to create a link for an invoice. Returns the created invoice link as
        String on success.
        """
        response = await self.api.request(
            "createInvoiceLink", self.get_params(locals())
        )
        return response

    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[List["ShippingOption"]] = None,
        error_message: Optional[str] = None,
        **kwargs
    ) -> bool:
        """
        If you sent an invoice requesting a shipping address and the parameter is_flexible
        was specified, the Bot API will send an Update with a shipping_query field to the
        bot. Use this method to reply to shipping queries. On success, True is returned.
        """
        response = await self.api.request(
            "answerShippingQuery", self.get_params(locals())
        )
        return response

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: Optional[str] = None,
        **kwargs
    ) -> bool:
        """
        Once the user has confirmed their payment and shipping details, the Bot API sends
        the final confirmation in the form of an Update with the field pre_checkout_query.
        Use this method to respond to such pre-checkout queries. On success, True is
        returned. Note: The Bot API must receive an answer within 10 seconds after the pre-
        checkout query was sent.
        """
        response = await self.api.request(
            "answerPreCheckoutQuery", self.get_params(locals())
        )
        return response

    async def set_passport_data_errors(
        self, user_id: int, errors: List["PassportElementError"], **kwargs
    ) -> bool:
        """
        Informs a user that some of the Telegram Passport elements they provided contains
        errors. The user will not be able to re-submit their Passport to you until the
        errors are fixed (the contents of the field for which you returned the error must
        change). Returns True on success. Use this if the data submitted by the user doesn't
        satisfy the standards your service requires for any reason. For example, if a
        birthday date seems invalid, a submitted document is blurry, a scan shows evidence
        of tampering, etc. Supply some details in the error message to make sure the user
        knows how to correct the issues.
        """
        response = await self.api.request(
            "setPassportDataErrors", self.get_params(locals())
        )
        return response

    async def send_game(
        self,
        game_short_name: str,
        chat_id: int,
        reply_to_message_id: Optional[int] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> Message:
        """
        Use this method to send a game. On success, the sent Message is returned.
        """
        response = await self.api.request("sendGame", self.get_params(locals()))
        return Message(**response)

    async def set_game_score(
        self,
        user_id: int,
        score: int,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        **kwargs
    ) -> Union[Message, bool]:
        """
        Use this method to set the score of the specified user in a game message. On
        success, if the message is not an inline message, the Message is returned, otherwise
        True is returned. Returns an error, if the new score is not greater than the user's
        current score in the chat and force is False.
        """
        response = await self.api.request("setGameScore", self.get_params(locals()))
        return parse_obj_as(Union[Message, bool], response)

    async def get_game_high_scores(
        self,
        user_id: int,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        chat_id: Optional[int] = None,
        **kwargs
    ) -> List[GameHighScore]:
        """
        Use this method to get data for high score tables. Will return the score of the
        specified user and several of their neighbors in a game. Returns an Array of
        GameHighScore objects. This method will currently return scores for the target user,
        plus two of their closest neighbors on each side. Will also return the top three
        users if the user and their neighbors are not among them. Please note that this
        behavior is subject to change.
        """
        response = await self.api.request(
            "getGameHighScores", self.get_params(locals())
        )
        return parse_obj_as(List[GameHighScore], response)
