from pathlib import Path

from wonda.tools.localization.abc import ABCLocalizator
from wonda.tools.localization.types import Locale, Translation


class DefaultLocalizator(ABCLocalizator):
    def __init__(self, path: Path | str, default_language: str = "en") -> None:
        self.default_language = default_language
        self.locales = {}

        self.path = path if isinstance(path, Path) else Path(path)

        if not self.path.is_dir():
            raise SystemExit("Localization path has to be a directory")

        directories = [i for i in self.path.iterdir() if i.is_dir()]

        if not directories:
            raise FileNotFoundError("No language directories found")

        for d in directories:
            if not any(d.iterdir()):
                raise KeyError(f"Language directory {d.name!r} is empty")

            self.locales[d.name] = Locale(d.name, self.load_translations(d))

    def load_translations(self, source: Path) -> list[Translation]:
        translations = []

        for path in source.iterdir():
            if path.is_dir():
                self.load_translations(path)
            elif path.is_file():
                content: bytes = path.read_bytes()

                if path.suffix in (".txt", ".html", ".md"):
                    content: bytes = content.decode("utf-8")

                translations.append(Translation(path.stem, content))

        return translations

    def get_locale(self, language_code: str) -> Locale:
        return self.locales.get(language_code, self.locales.get(self.default_language))
