from pathlib import Path

from wonda.errors.internal import EmptyDirectoryError, InvalidPathError
from wonda.tools.localization.abc import ABCLocalizator
from wonda.tools.localization.types import Locale, Translation, FileContent


class TranslationLoader:
    """
    Handles loading and processing of translation files.
    """

    def __init__(self, base_directory: Path):
        self.base_directory = base_directory

    def construct_key(self, file_path: Path) -> str:
        """
        Constructs translation key from file path.
        """
        return "/".join(
            file_path.relative_to(self.base_directory).parts[:-1] + (file_path.stem,)
        )

    def load_translations(self) -> list[Translation]:
        """
        Loads all translations from a directory.
        """
        translations = []

        for file_path in self.base_directory.rglob("*"):
            if file_path.is_file():
                file_content = FileContent.from_file(file_path)
                key = self.construct_key(file_path)
                translations.append(Translation(key, file_content.content))

        return translations


class DefaultLocalizator(ABCLocalizator):
    """
    Default implementation of the localization system.
    """

    def __init__(self, path: Path | str, default_language: str = "en") -> None:
        self.locales = {}
        self.default_language = default_language
        self.path = Path(path) if isinstance(path, str) else path

        self._initialize_locales()

    def _initialize_locales(self) -> None:
        """
        Initialize locales from directory structure.
        """
        
        if not self.path.is_dir():
            raise InvalidPathError("Localization path must be a directory")

        directories = [d for d in self.path.iterdir() if d.is_dir()]
        if not directories:
            raise EmptyDirectoryError("No language directories found")

        for directory in directories:
            if not any(directory.iterdir()):
                raise EmptyDirectoryError(
                    f"Language directory {directory.name!r} is empty"
                )

            loader = TranslationLoader(directory)
            self.locales[directory.name] = Locale(
                directory.name, loader.load_translations()
            )

    def get_locale(self, language_code: str) -> Locale:
        return self.locales.get(language_code, self.locales[self.default_language])
