import re
import random
import string
import hashlib
import requests


# Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    # Minimum Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(
            "Password should be at least 8 characters long."
        )

    # Uppercase Letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append(
            "Password must contain at least one uppercase letter."
        )

    # Lowercase Letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(
            "Password must contain at least one lowercase letter."
        )

    # Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append(
            "Password must contain at least one number."
        )

    # Special Character Check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append(
            "Password must contain at least one special character."
        )

    # Repeating Characters
    if re.search(r"(.)\1\1", password):
        feedback.append(
            "Avoid repeating the same character multiple times."
        )
    else:
        score += 1

    # Strength Levels
    if score <= 2:
        strength = "Weak"
        color = "red"

    elif score <= 4:
        strength = "Medium"
        color = "orange"

    else:
        strength = "Strong"
        color = "green"

    return strength, color, feedback


# Secure Password Generator
def generate_secure_password(length=14):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


# Data Breach Checker
def check_data_breach(password):
    sha1_password = hashlib.sha1(
        password.encode()
    ).hexdigest().upper()

    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)

    if response.status_code != 200:
        return False

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(':')

        if hash_suffix == suffix:
            return int(count)

    return 0