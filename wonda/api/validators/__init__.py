from .abc import *
from .request import *
from .response import *

DEFAULT_REQUEST_VALIDATORS = [TranslateFriendlyTypesRequestValidator()]
DEFAULT_RESPONSE_VALIDATORS = [TelegramAPIErrorResponseValidator()]
