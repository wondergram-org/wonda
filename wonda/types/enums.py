from enum import Enum


class StrEnum(str, Enum):
    """
    A base string enumeration.
    """


class ChatType(StrEnum):
    """
    Type of the chat, can be either "private", "group", "supergroup" or
    "channel"
    """

    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"


class ChatFullInfoType(StrEnum):
    """
    Type of the chat, can be either "private", "group", "supergroup" or
    "channel"
    """

    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"


class MessageEntityType(StrEnum):
    """
    Type of the entity. Currently, can be "mention" (@username), "hashtag"
    (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url"
    (https://telegram.org), "email" (do-not-reply@telegram.org),
    "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic
    text), "underline" (underlined text), "strikethrough" (strikethrough
    text), "spoiler" (spoiler message), "blockquote" (block quotation),
    "expandable_blockquote" (collapsed-by-default block quotation), "code"
    (monowidth string), "pre" (monowidth block), "text_link" (for
    clickable text URLs), "text_mention" (for users without usernames),
    "custom_emoji" (for inline custom emoji stickers)
    """

    MENTION = "mention"
    HASHTAG = "hashtag"
    CASHTAG = "cashtag"
    BOT_COMMAND = "bot_command"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    SPOILER = "spoiler"
    BLOCKQUOTE = "blockquote"
    EXPANDABLE_BLOCKQUOTE = "expandable_blockquote"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"
    TEXT_MENTION = "text_mention"
    CUSTOM_EMOJI = "custom_emoji"


class PollType(StrEnum):
    """
    Poll type, currently can be "regular" or "quiz"
    """

    REGULAR = "regular"
    QUIZ = "quiz"


class ReactionTypeEmojiEmoji(StrEnum):
    """
    Reaction emoji. Currently, it can be one of "👍", "👎", "❤", "🔥", "🥰",
    "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊",
    "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆",
    "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻",
    "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪",
    "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀",
    "😡"
    """

    THUMBS_UP = "👍"
    THUMBS_DOWN = "👎"
    RED_HEART = "❤"
    FIRE = "🔥"
    SMILING_FACE_WITH_HEARTS = "🥰"
    CLAPPING_HANDS = "👏"
    BEAMING_FACE_WITH_SMILING_EYES = "😁"
    THINKING_FACE = "🤔"
    EXPLODING_HEAD = "🤯"
    FACE_SCREAMING_IN_FEAR = "😱"
    FACE_WITH_SYMBOLS_ON_MOUTH = "🤬"
    CRYING_FACE = "😢"
    PARTY_POPPER = "🎉"
    STAR_STRUCK = "🤩"
    FACE_VOMITING = "🤮"
    PILE_OF_POO = "💩"
    FOLDED_HANDS = "🙏"
    OK_HAND = "👌"
    DOVE = "🕊"
    CLOWN_FACE = "🤡"
    YAWNING_FACE = "🥱"
    WOOZY_FACE = "🥴"
    SMILING_FACE_WITH_HEART_EYES = "😍"
    SPOUTING_WHALE = "🐳"
    HEART_ON_FIRE = "❤‍🔥"
    NEW_MOON_FACE = "🌚"
    HOT_DOG = "🌭"
    HUNDRED_POINTS = "💯"
    ROLLING_ON_THE_FLOOR_LAUGHING = "🤣"
    HIGH_VOLTAGE = "⚡"
    BANANA = "🍌"
    TROPHY = "🏆"
    BROKEN_HEART = "💔"
    FACE_WITH_RAISED_EYEBROW = "🤨"
    NEUTRAL_FACE = "😐"
    STRAWBERRY = "🍓"
    BOTTLE_WITH_POPPING_CORK = "🍾"
    KISS_MARK = "💋"
    MIDDLE_FINGER = "🖕"
    SMILING_FACE_WITH_HORNS = "😈"
    SLEEPING_FACE = "😴"
    LOUDLY_CRYING_FACE = "😭"
    NERD_FACE = "🤓"
    GHOST = "👻"
    MAN_TECHNOLOGIST = "👨‍💻"
    EYES = "👀"
    JACK_O_LANTERN = "🎃"
    SEE_NO_EVIL_MONKEY = "🙈"
    SMILING_FACE_WITH_HALO = "😇"
    FEARFUL_FACE = "😨"
    HANDSHAKE = "🤝"
    WRITING_HAND = "✍"
    SMILING_FACE_WITH_OPEN_HANDS = "🤗"
    SALUTING_FACE = "🫡"
    SANTA_CLAUS = "🎅"
    CHRISTMAS_TREE = "🎄"
    SNOWMAN = "☃"
    NAIL_POLISH = "💅"
    ZANY_FACE = "🤪"
    MOAI = "🗿"
    COOL_BUTTON = "🆒"
    HEART_WITH_ARROW = "💘"
    HEAR_NO_EVIL_MONKEY = "🙉"
    UNICORN = "🦄"
    FACE_BLOWING_A_KISS = "😘"
    PILL = "💊"
    SPEAK_NO_EVIL_MONKEY = "🙊"
    SMILING_FACE_WITH_SUNGLASSES = "😎"
    ALIEN_MONSTER = "👾"
    MAN_SHRUGGING = "🤷‍♂"
    PERSON_SHRUGGING = "🤷"
    WOMAN_SHRUGGING = "🤷‍♀"
    ENRAGED_FACE = "😡"


class StickerType(StrEnum):
    """
    Type of the sticker, currently one of "regular", "mask",
    "custom_emoji". The type of the sticker is independent from its
    format, which is determined by the fields is_animated and is_video.
    """

    REGULAR = "regular"
    MASK = "mask"
    CUSTOM_EMOJI = "custom_emoji"


class StickerSetStickerType(StrEnum):
    """
    Type of stickers in the set, currently one of "regular", "mask",
    "custom_emoji"
    """

    REGULAR = "regular"
    MASK = "mask"
    CUSTOM_EMOJI = "custom_emoji"


class MaskPositionPoint(StrEnum):
    """
    The part of the face relative to which the mask should be placed. One
    of "forehead", "eyes", "mouth", or "chin".
    """

    FOREHEAD = "forehead"
    EYES = "eyes"
    MOUTH = "mouth"
    CHIN = "chin"


class InputStickerFormat(StrEnum):
    """
    Format of the added sticker, must be one of "static" for a .WEBP or
    .PNG image, "animated" for a .TGS animation, "video" for a WEBM video
    """

    STATIC = "static"
    ANIMATED = "animated"
    VIDEO = "video"


class InlineQueryChatType(StrEnum):
    """
    Optional. Type of the chat from which the inline query was sent. Can
    be either "sender" for a private chat with the inline query sender,
    "private", "group", "supergroup", or "channel". The chat type should
    be always known for requests sent from official clients and most
    third-party clients, unless the request was sent from a secret chat
    """

    SENDER = "sender"
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"


class InlineQueryResultGifThumbnailMimeType(StrEnum):
    """
    Optional. MIME type of the thumbnail, must be one of "image/jpeg",
    "image/gif", or "video/mp4". Defaults to "image/jpeg"
    """

    IMAGE_JPEG = "image/jpeg"
    IMAGE_GIF = "image/gif"
    VIDEO_MP4 = "video/mp4"


class InlineQueryResultMpeg4GifThumbnailMimeType(StrEnum):
    """
    Optional. MIME type of the thumbnail, must be one of "image/jpeg",
    "image/gif", or "video/mp4". Defaults to "image/jpeg"
    """

    IMAGE_JPEG = "image/jpeg"
    IMAGE_GIF = "image/gif"
    VIDEO_MP4 = "video/mp4"


class InlineQueryResultVideoMimeType(StrEnum):
    """
    MIME type of the content of the video URL, "text/html" or "video/mp4"
    """

    TEXT_HTML = "text/html"
    VIDEO_MP4 = "video/mp4"


class InlineQueryResultDocumentMimeType(StrEnum):
    """
    MIME type of the content of the file, either "application/pdf" or
    "application/zip"
    """

    APPLICATION_PDF = "application/pdf"
    APPLICATION_ZIP = "application/zip"


class EncryptedPassportElementType(StrEnum):
    """
    Element type. One of "personal_details", "passport", "driver_license",
    "identity_card", "internal_passport", "address", "utility_bill",
    "bank_statement", "rental_agreement", "passport_registration",
    "temporary_registration", "phone_number", "email".
    """

    PERSONAL_DETAILS = "personal_details"
    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"
    ADDRESS = "address"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"
    PHONE_NUMBER = "phone_number"
    EMAIL = "email"


class PassportElementErrorDataFieldType(StrEnum):
    """
    The section of the user's Telegram Passport which has the error, one
    of "personal_details", "passport", "driver_license", "identity_card",
    "internal_passport", "address"
    """

    PERSONAL_DETAILS = "personal_details"
    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"
    ADDRESS = "address"


class PassportElementErrorFrontSideType(StrEnum):
    """
    The section of the user's Telegram Passport which has the issue, one
    of "passport", "driver_license", "identity_card", "internal_passport"
    """

    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"


class PassportElementErrorReverseSideType(StrEnum):
    """
    The section of the user's Telegram Passport which has the issue, one
    of "driver_license", "identity_card"
    """

    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"


class PassportElementErrorSelfieType(StrEnum):
    """
    The section of the user's Telegram Passport which has the issue, one
    of "passport", "driver_license", "identity_card", "internal_passport"
    """

    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"


class PassportElementErrorFileType(StrEnum):
    """
    The section of the user's Telegram Passport which has the issue, one
    of "utility_bill", "bank_statement", "rental_agreement",
    "passport_registration", "temporary_registration"
    """

    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"


class PassportElementErrorFilesType(StrEnum):
    """
    The section of the user's Telegram Passport which has the issue, one
    of "utility_bill", "bank_statement", "rental_agreement",
    "passport_registration", "temporary_registration"
    """

    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"


class PassportElementErrorTranslationFileType(StrEnum):
    """
    Type of element of the user's Telegram Passport which has the issue,
    one of "passport", "driver_license", "identity_card",
    "internal_passport", "utility_bill", "bank_statement",
    "rental_agreement", "passport_registration", "temporary_registration"
    """

    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"


class PassportElementErrorTranslationFilesType(StrEnum):
    """
    Type of element of the user's Telegram Passport which has the issue,
    one of "passport", "driver_license", "identity_card",
    "internal_passport", "utility_bill", "bank_statement",
    "rental_agreement", "passport_registration", "temporary_registration"
    """

    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"
