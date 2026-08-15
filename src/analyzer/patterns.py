import re


KEYBOARD_PATTERNS = (
    "qwerty",
    "qwertyuiop",
    "asdfgh",
    "asdfghjkl",
    "zxcvbn",
    "1234567890",
    "0987654321",
)


def has_repeated_characters(password: str) -> bool:
    return bool(re.search(r"(.)\1{2,}", password))


def has_sequential_characters(password: str) -> bool:
    """Detect simple ascending or descending 3-character sequences."""
    if len(password) < 3:
        return False

    lowered = password.lower()

    for index in range(len(lowered) - 2):
        chunk = lowered[index:index + 3]
        values = [ord(char) for char in chunk]

        ascending = values[1] == values[0] + 1 and values[2] == values[1] + 1
        descending = values[1] == values[0] - 1 and values[2] == values[1] - 1

        if ascending or descending:
            return True

    return False


def has_keyboard_pattern(password: str) -> bool:
    lowered = password.lower()
    return any(pattern in lowered for pattern in KEYBOARD_PATTERNS)


def character_classes(password: str) -> dict:
    return {
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Numbers": bool(re.search(r"\d", password)),
        "Symbols": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
