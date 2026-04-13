"""Example module demonstrating well-typed, well-documented Python code.

This module ships with the Fortress template. Replace or delete it when you
start your real project — it exists only to give the CI pipeline something to
lint, type-check, and test against.
"""

from __future__ import annotations


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The arithmetic sum of *a* and *b*.

    Examples:
        >>> add(1, 2)
        3
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


def clamp(value: float, low: float, high: float) -> float:
    """Clamp *value* to the inclusive range [*low*, *high*].

    Args:
        value: The number to clamp.
        low:   Lower bound (inclusive).
        high:  Upper bound (inclusive).

    Returns:
        *value* unchanged if it is within bounds; otherwise the nearest bound.

    Raises:
        ValueError: If *low* is greater than *high*.

    Examples:
        >>> clamp(5.0, 0.0, 10.0)
        5.0
        >>> clamp(-1.0, 0.0, 10.0)
        0.0
        >>> clamp(11.0, 0.0, 10.0)
        10.0
    """
    if low > high:
        raise ValueError(f"low ({low}) must be <= high ({high})")
    return max(low, min(value, high))


def is_palindrome(text: str) -> bool:
    """Return True if *text* reads the same forwards and backwards.

    Comparison is case-insensitive and ignores non-alphanumeric characters.

    Args:
        text: The string to test.

    Returns:
        ``True`` if *text* is a palindrome, ``False`` otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in *text*.

    Words are split on whitespace and compared case-insensitively.

    Args:
        text: Input string.

    Returns:
        A dictionary mapping each unique lowercase word to its count.

    Examples:
        >>> word_count("the cat sat on the mat")
        {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
    """
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
