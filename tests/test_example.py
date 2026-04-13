"""Tests for src/example.py — covers all public functions with happy-path and edge cases."""

import pytest

from src.example import add, clamp, is_palindrome, word_count


# ── add ───────────────────────────────────────────────────────────────────────

class TestAdd:
    def test_integers(self) -> None:
        assert add(2, 3) == 5

    def test_floats(self) -> None:
        assert add(1.5, 2.5) == 4.0

    def test_negative(self) -> None:
        assert add(-1, 1) == 0

    def test_zero(self) -> None:
        assert add(0, 0) == 0

    def test_mixed(self) -> None:
        assert add(1, 2.0) == 3.0


# ── clamp ─────────────────────────────────────────────────────────────────────

class TestClamp:
    def test_within_range(self) -> None:
        assert clamp(5.0, 0.0, 10.0) == 5.0

    def test_below_low(self) -> None:
        assert clamp(-1.0, 0.0, 10.0) == 0.0

    def test_above_high(self) -> None:
        assert clamp(11.0, 0.0, 10.0) == 10.0

    def test_exactly_low(self) -> None:
        assert clamp(0.0, 0.0, 10.0) == 0.0

    def test_exactly_high(self) -> None:
        assert clamp(10.0, 0.0, 10.0) == 10.0

    def test_invalid_bounds_raises(self) -> None:
        with pytest.raises(ValueError, match="must be <="):
            clamp(5.0, 10.0, 0.0)

    def test_equal_bounds(self) -> None:
        assert clamp(5.0, 5.0, 5.0) == 5.0


# ── is_palindrome ─────────────────────────────────────────────────────────────

class TestIsPalindrome:
    def test_simple_palindrome(self) -> None:
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self) -> None:
        assert is_palindrome("hello") is False

    def test_case_insensitive(self) -> None:
        assert is_palindrome("Racecar") is True

    def test_with_spaces(self) -> None:
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_empty_string(self) -> None:
        assert is_palindrome("") is True

    def test_single_char(self) -> None:
        assert is_palindrome("a") is True

    def test_numbers(self) -> None:
        assert is_palindrome("12321") is True

    def test_with_punctuation(self) -> None:
        assert is_palindrome("Was it a car or a cat I saw?") is True


# ── word_count ────────────────────────────────────────────────────────────────

class TestWordCount:
    def test_basic(self) -> None:
        result = word_count("the cat sat on the mat")
        assert result == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

    def test_case_insensitive(self) -> None:
        result = word_count("Hello hello HELLO")
        assert result == {"hello": 3}

    def test_empty_string(self) -> None:
        assert word_count("") == {}

    def test_single_word(self) -> None:
        assert word_count("python") == {"python": 1}

    def test_multiple_spaces(self) -> None:
        result = word_count("a  b   a")
        assert result == {"a": 2, "b": 1}
