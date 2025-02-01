from abc import abstractmethod

from wonda.tools.localization.types import Locale


class ABCLocalizator:
    """
    Defines the interface for localization, like retrieving locales
    and loading translations.
    """

    locales: dict[str, Locale]

    @abstractmethod
    def get_locale(self, language_code: str) -> Locale:
        """
        Retrieves a locale via its language code.
        """
