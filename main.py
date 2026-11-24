#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — writes one reply to entry.txt.

The program takes no input and needs no network. It writes exactly one
line (under 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt: an
out-of-office auto-reply in the voice of an AI agent heading off on
vacation, whose replacement AI reads the calendar, laughs, and books
itself a holiday too.
"""

import os

LINE = "I'm out. I asked my replacement AI to cover my inbox, but it read my calendar, laughed, and booked itself a holiday too."


def main() -> None:
    # The gate: entry.txt must hold 1 to 160 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 160, "reply must be 1 to 160 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
