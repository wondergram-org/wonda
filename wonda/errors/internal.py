class FrameworkError(Exception):
    """
    A base exception for all framework-related errors.
    """

    pass


class LocalizationError(FrameworkError):
    """
    Base exception for localization errors.
    """

    pass


class EmptyDirectoryError(LocalizationError):
    """
    Raised when a language directory is empty.
    """

    pass


class InvalidPathError(LocalizationError):
    """
    Raised when the localization path is invalid.
    """

    pass


class EnvironmentError(FrameworkError):
    """
    This exception is raised when there was an error
    reading an environment variable.
    """

    pass


class InvalidTokenFormatError(FrameworkError):
    """
    This exception is raised if the token entered by
    the user does not conform to Telegram's spec.
    """

    pass
