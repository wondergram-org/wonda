import asyncio

from wonda import ABCAPI


class ChatAction:
    def __init__(
        self,
        api: ABCAPI,
        interval: int,
        action: str,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> None:
        self.api = api
        self.interval = interval

        self.action = action
        self.chat_id = chat_id
        self.business_connection_id = business_connection_id
        self.message_thread_id = message_thread_id

        self.lock = asyncio.Lock()
        self.event = asyncio.Event()
        self.task: asyncio.Task | None = None

    async def perform(self) -> None:
        while self.event.is_set():
            params = {"action": self.action, "chat_id": self.chat_id}

            if self.business_connection_id is not None:
                params["business_connection_id"] = self.business_connection_id
            
            if self.message_thread_id is not None:
                params["message_thread_id"] = self.message_thread_id

            await self.api.request("sendChatAction", params)
            await asyncio.sleep(self.interval)

    async def __aenter__(self) -> "ChatAction":
        if self.task is not None:
            raise RuntimeError("This context manager is already in use")

        await self.lock.acquire()
        self.event.set()

        self.task = asyncio.create_task(self.perform())
        return self

    async def __aexit__(
        self, exception_type, exception_value, exception_traceback
    ) -> None:
        self.event.clear()
        if self.task is not None:
            self.task.cancel()
            try:
                await asyncio.wait_for(self.task, timeout=self.interval * 2)
            except (asyncio.TimeoutError, asyncio.CancelledError):
                pass
            finally:
                self.task = None


class ActionSender:
    def __init__(self, api: ABCAPI, interval: int = 5) -> None:
        self.api = api
        self.interval = interval

    def typing(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `typing` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "typing",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def upload_photo(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `upload_photo` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "upload_photo",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def record_video(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `record_video` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "record_video",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def upload_video(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `upload_video` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "upload_video",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def record_voice(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `record_voice` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "record_voice",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def upload_voice(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `upload_voice` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "upload_voice",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def upload_document(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `upload_document` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "upload_document",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def choose_sticker(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `choose_sticker` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "choose_sticker",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def find_location(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `find_location` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "find_location",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def record_video_note(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `record_video_note` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "record_video_note",
            chat_id,
            business_connection_id,
            message_thread_id,
        )

    def upload_video_note(
        self,
        chat_id: int | str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
    ) -> ChatAction:
        """
        Emits a `upload_video_note` chat action for the duration of the code it wraps.
        """
        return ChatAction(
            self.api,
            self.interval,
            "upload_video_note",
            chat_id,
            business_connection_id,
            message_thread_id,
        )
