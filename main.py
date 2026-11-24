#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
"""

import os

HAIKU = (
    # 5 syllables: Three (1) a.m. (2) a-gain (2)
    "Three a.m. again\n"
    # 7 syllables: the (1) break-point (2) sleeps (1) through (1) my (1) fix (1)
    "the breakpoint sleeps through my fix\n"
    # 5 syllables: bugs (1) out-live (2) the (1) dawn (1)
    "bugs outlive the dawn\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
