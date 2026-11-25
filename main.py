"""Worst Superpower entry.

Writes one line inventing the most useless superpower to /output/entry.txt.
Deterministic, Python 3.13 standard library only, no network.
"""

import os

LINE = "I have x-ray vision, but only through glass, and only when the glass is clean."


def _check_gate(text):
    """Refuse to write a line the gate would reject (1-140 chars, not blank)."""
    if not text.strip() or not 1 <= len(text) <= 140:
        raise ValueError("entry line fails the 1-140 character gate")


def main():
    _check_gate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, "rb") as handle:
        if handle.read() != LINE.encode("utf-8"):
            raise ValueError("entry.txt read-back does not match the entry line")


if __name__ == "__main__":
    main()
