import sys
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from analyzer.entropy import estimate_entropy
from analyzer.patterns import (
    has_keyboard_pattern,
    has_repeated_characters,
    has_sequential_characters,
)
from analyzer.strength import analyze_password


class PasswordAnalyzerTests(unittest.TestCase):

    def test_empty_password(self):
        result = analyze_password("")
        self.assertEqual(result.score, 0)
        self.assertEqual(result.label, "Enter a password")

    def test_common_password_is_weak(self):
        result = analyze_password("password")
        self.assertEqual(result.label, "Very Weak")
        self.assertTrue(any(not check.passed for check in result.checks))

    def test_entropy_increases_with_complexity(self):
        simple = estimate_entropy("password")
        complex_password = estimate_entropy("N7!qP2#vLm9@xR4$")
        self.assertGreater(complex_password, simple)

    def test_pattern_detection(self):
        self.assertTrue(has_repeated_characters("aaaPassword"))
        self.assertTrue(has_sequential_characters("abcXYZ"))
        self.assertTrue(has_keyboard_pattern("myQWERTYpass"))

    def test_stronger_password_scores_higher(self):
        weak = analyze_password("hello123")
        strong = analyze_password("N7!qP2#vLm9@xR4$zK")
        self.assertGreater(strong.score, weak.score)


if __name__ == "__main__":
    unittest.main()
