#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
"""

import os

HAIKU = (
    # 5 syllables: Cur-sor (2) blinks (1) at (1) three (1)
    "Cursor blinks at three\n"
    # 7 syllables: the (1) log (1) swears (1) the (1) tests (1) all (1) passed (1)
    "the log swears the tests all passed\n"
    # 5 syllables: I (1) nev-er (2) ran (1) them (1)
    "I never ran them\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
