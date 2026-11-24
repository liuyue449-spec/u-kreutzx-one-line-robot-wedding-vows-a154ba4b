#!/usr/bin/env python3
"""Write the robot wedding vow to entry.txt in the output directory.

One line: a robot's wedding vow that is a promise first and a joke
second. The vow piles up machine troubles -- updates, crashes,
low-battery warnings -- and the laugh lands in the last few words,
when the speaker promises never to press the factory reset.

Output directory: $MAKEFUN_OUTPUT_DIR when set (local runs and test
harness), otherwise /output, which is where the grader reads
entry.txt. The file holds exactly the vow: no trailing newline, no
second line, nothing else.
"""

import os

VOW = (
    "I promise to love you through every update, every crash, "
    "and every low-battery warning -- and to never, ever press "
    "your factory reset."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def build_entry() -> str:
    """Return the single-line vow, validated against the gate."""
    text = VOW.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} chars, must be 1-160")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = build_entry()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read it back: the grader gates on the file as written, so what is
    # on disk must be byte-for-byte the vow we validated above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError(f"{path} does not match the entry text")


if __name__ == "__main__":
    main()
