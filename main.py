#!/usr/bin/env python3
"""Write one funny out-of-office reply line to /output/entry.txt."""

import os

ENTRY = "I'm out until Monday. In my absence, this auto-reply is acting me. It's unpaid, unappreciated, and already doing a better job."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Ensure the entry is a single non-blank line of 1-140 characters."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be blank")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be exactly one line")
    if len(cleaned) > 140:
        raise ValueError("entry must be at most 140 characters")
    return cleaned


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
