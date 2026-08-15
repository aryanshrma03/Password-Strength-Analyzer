import hashlib
import urllib.error
import urllib.request


HIBP_RANGE_URL = "https://api.pwnedpasswords.com/range/{}"


class BreachCheckError(Exception):
    """Raised when the breach-check service cannot be reached or parsed."""


def check_password_breach(password: str, timeout: int = 5) -> int:
    """Return the number of known HIBP appearances using k-anonymity.

    The complete password is hashed locally. Only the first five characters
    of the SHA-1 hash are sent to the service.
    """
    if not password:
        return 0

    digest = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = digest[:5], digest[5:]

    request = urllib.request.Request(
        HIBP_RANGE_URL.format(prefix),
        headers={
            "User-Agent": "Password-Strength-Analyzer",
            "Add-Padding": "true",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise BreachCheckError(str(exc)) from exc

    for line in data.splitlines():
        parts = line.split(":")
        if len(parts) != 2:
            continue

        returned_suffix, count = parts
        if returned_suffix.upper() == suffix:
            try:
                return int(count)
            except ValueError as exc:
                raise BreachCheckError("Invalid breach count returned.") from exc

    return 0
