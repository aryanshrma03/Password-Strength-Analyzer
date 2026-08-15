import math
import re


def character_pool_size(password: str) -> int:
    """Return an estimated character pool based on character classes used."""
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"\d", password):
        pool += 10
    if re.search(r"[^A-Za-z0-9]", password):
        pool += 33

    return pool


def estimate_entropy(password: str) -> float:
    """Estimate entropy in bits using length and character pool size."""
    if not password:
        return 0.0

    pool = character_pool_size(password)
    if pool == 0:
        return 0.0

    return len(password) * math.log2(pool)


def estimate_crack_seconds(entropy: float, guesses_per_second: float = 10_000_000_000) -> float:
    """Estimate theoretical offline guessing time.

    This is an educational estimate, not a real password-cracking benchmark.
    """
    if entropy <= 0:
        return 0.0

    guesses = 2 ** min(entropy, 80)
    return guesses / guesses_per_second


def format_crack_time(seconds: float) -> str:
    if seconds < 1:
        return "Instantly"

    units = (
        ("year", 365.25 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1),
    )

    for name, size in units:
        if seconds >= size:
            value = seconds / size
            suffix = "" if value == 1 else "s"
            return f"{value:,.1f} {name}{suffix}"

    return "< 1 second"
