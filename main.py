"""One Word for Your Wi-Fi: write a single word naming the Wi-Fi.

The word is the joke itself: home Wi-Fi that vanishes mid-call without
a word of explanation, then comes back like nothing happened. Ghosting.
"""

from pathlib import Path

WORD = "Ghosting"
OUTPUT = Path("/output/entry.txt")


def validate(word: str) -> str:
    """Enforce the gate: 1-20 chars, exactly one word, not only whitespace."""
    if not 1 <= len(word) <= 20:
        raise ValueError(f"word must be 1-20 chars, got {len(word)}")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    return word


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(validate(WORD), encoding="utf-8")


if __name__ == "__main__":
    main()
