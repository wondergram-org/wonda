from wonda.bot.dispatch.middleware.abc import ABCMiddleware
from wonda.bot.updates.types import MessageUpdate
from wonda.tools.localization import ABCLocalizator, DefaultLocalizator


class InternationalizationMiddleware(ABCMiddleware[MessageUpdate]):
    """
    Provides foreign language capabilities for your bot.
    """

    def __init__(
        self,
        localizator: ABCLocalizator | None = None,
        default_language_code: str = "en",
    ) -> None:
        self.default_language_code = default_language_code
        self.localizator = localizator or DefaultLocalizator("loc/")

    async def pre(self, m: MessageUpdate, ctx: dict) -> bool:
        ctx["locale"] = self.localizator.get_locale(await self.get_language_code(m))
        return True

    async def get_language_code(self, m: MessageUpdate) -> str:
        return m.from_.language_code or self.default_language_code  # type: ignore
