from dataclasses import dataclass

from analyzer.entropy import estimate_crack_seconds, estimate_entropy, format_crack_time
from analyzer.patterns import (
    character_classes,
    has_keyboard_pattern,
    has_repeated_characters,
    has_sequential_characters,
)


DEFAULT_COMMON_PASSWORDS = {
    "123456", "123456789", "password", "password1", "qwerty",
    "qwerty123", "12345678", "12345", "111111", "123123",
    "admin", "admin123", "letmein", "welcome", "monkey", "dragon",
    "football", "iloveyou", "abc123", "000000", "passw0rd",
    "login", "root", "test",
}


@dataclass
class CheckResult:
    name: str
    passed: bool


@dataclass
class AnalysisResult:
    score: int
    label: str
    entropy: float
    crack_time: str
    checks: list[CheckResult]
    recommendations: list[str]


def analyze_password(password: str, common_passwords=None) -> AnalysisResult:
    if not password:
        return AnalysisResult(
            score=0,
            label="Enter a password",
            entropy=0.0,
            crack_time="—",
            checks=[],
            recommendations=["Enter a password to begin the analysis."],
        )

    common_passwords = common_passwords or DEFAULT_COMMON_PASSWORDS
    normalized = password.lower()

    score = 0
    recommendations = []

    if len(password) >= 16:
        score += 30
    elif len(password) >= 12:
        score += 22
    elif len(password) >= 8:
        score += 12
        recommendations.append("Use at least 12 characters; 16+ is better.")
    else:
        recommendations.append("Use at least 12 characters, preferably 16+.")

    classes = character_classes(password)
    for present in classes.values():
        if present:
            score += 8

    if not classes["Lowercase"]:
        recommendations.append("Add lowercase letters.")
    if not classes["Uppercase"]:
        recommendations.append("Add uppercase letters.")
    if not classes["Numbers"]:
        recommendations.append("Add numbers.")
    if not classes["Symbols"]:
        recommendations.append("Add symbols such as !, @, # or $.")

    common = normalized in common_passwords
    repeated = has_repeated_characters(password)
    sequential = has_sequential_characters(password)
    keyboard = has_keyboard_pattern(password)

    checks = [
        CheckResult("Length ≥ 12", len(password) >= 12),
        CheckResult("Lowercase", classes["Lowercase"]),
        CheckResult("Uppercase", classes["Uppercase"]),
        CheckResult("Numbers", classes["Numbers"]),
        CheckResult("Symbols", classes["Symbols"]),
        CheckResult("Not a common password", not common),
        CheckResult("No repeated characters", not repeated),
        CheckResult("No obvious sequences", not sequential),
        CheckResult("No keyboard pattern", not keyboard),
    ]

    if common:
        score = min(score, 20)
        recommendations.append("This is a commonly used password. Choose something unique.")

    if repeated:
        score -= 8
        recommendations.append("Avoid repeated characters such as aaa or 111.")

    if sequential:
        score -= 8
        recommendations.append("Avoid sequences such as abc, 123 or 987.")

    if keyboard:
        score -= 8
        recommendations.append("Avoid keyboard patterns such as qwerty or asdfgh.")

    score = max(0, min(100, score))

    if common or score < 30:
        label = "Very Weak"
    elif score < 50:
        label = "Weak"
    elif score < 70:
        label = "Fair"
    elif score < 85:
        label = "Strong"
    else:
        label = "Very Strong"

    if not recommendations:
        recommendations.append("Good job. Use a unique password and never reuse it.")

    entropy = estimate_entropy(password)
    crack_time = format_crack_time(estimate_crack_seconds(entropy))

    return AnalysisResult(
        score=score,
        label=label,
        entropy=entropy,
        crack_time=crack_time,
        checks=checks,
        recommendations=recommendations,
    )
