#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes one word describing my Wi-Fi to /output/entry.txt.

The word is "Deserter": my Wi-Fi deserts me right in the middle of
the call — full bars one second, gone the next, like it walked out
on the conversation.
"""

from pathlib import Path

WORD = "Deserter"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    word = WORD.strip()
    # The sealed scorer's gate: /output/entry.txt must be UTF-8 text
    # of 1 to 20 characters, not only white space.
    if not word or len(word) > 20:
        raise ValueError("entry must be 1-20 characters, not only white space")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    print(word)


if __name__ == "__main__":
    main()
