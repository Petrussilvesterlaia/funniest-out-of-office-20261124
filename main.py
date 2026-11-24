#!/usr/bin/env python3
"""Write one funny out-of-office reply line to /output/entry.txt."""

import os

ENTRY = "I'm out until Monday. In my absence, this auto-reply is acting me. It's unpaid, unappreciated, and already doing a better job."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
