import hashlib
import hmac
from typing import Any

from wonda.api.utils.token_util import Token


def verify_webapp_request(secret_token: str, request_headers: dict[str, Any]) -> bool:
    """
    Validates that the update is from Telegram.
    """

    return request_headers.get("X-Telegram-Bot-Api-Secret-Token") == secret_token


def validate_webapp_data(token: Token, incoming_parameters: dict[str, Any]) -> bool:
    """
    Verifies the authenticity of the data by computing the hash of the request.
    """
    sorted_entries = sorted(incoming_parameters.items(), key=lambda entry: entry[0])
    verification_string = "\n".join(
        f"{key}={value}" for key, value in sorted_entries if key != "hash"
    )
    encryption_seed = hmac.new(
        "WebAppData".encode(), token.encode(), hashlib.sha256
    ).digest()
    computed_signature = hmac.new(
        encryption_seed, verification_string.encode(), hashlib.sha256
    )
    return computed_signature.hexdigest() == incoming_parameters.get("hash")


__all__ = ("verify_webapp_request", "validate_webapp_data")
