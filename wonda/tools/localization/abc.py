from abc import abstractmethod
from pathlib import Path

from wonda.tools.localization.types import Locale, Translation


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

    @abstractmethod
    def load_translations(self, path: Path) -> list[Translation]:
        """
        Loads translations from a specified path. Controls how translations
        are loaded from a given directory.
        """