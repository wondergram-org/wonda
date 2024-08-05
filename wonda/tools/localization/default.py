from pathlib import Path

from wonda.tools.localization.abc import ABCLocalizator
from wonda.tools.localization.types import Locale, Translation


def construct_key(source_directory: Path, file_path: Path) -> str:
    return "/".join(
        file_path.relative_to(source_directory).parts[:-1] + (file_path.stem,)
    )


def read_file_content(path: Path) -> str | bytes:
    return (
        path.read_text()
        if path.suffix in (".txt", ".html", ".md")
        else path.read_bytes()
    )


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

    def load_translations(self, directory: Path) -> list[Translation]:
        translations = []

        for f in directory.rglob("*"):
            if f.is_file():
                translations.append(
                    Translation(construct_key(directory, f), read_file_content(f))
                )

        return translations

    def get_locale(self, language_code: str) -> Locale:
        return self.locales.get(language_code, self.locales[self.default_language])
