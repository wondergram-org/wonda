class FrameworkError(Exception):
    """
    A base exception for all framework-related errors.
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
    the user does not comply to Telegram's spec.
    """

    pass
