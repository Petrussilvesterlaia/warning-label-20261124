"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- one single-line safety warning label -- to
/output/entry.txt, creating the directory if needed.
"""

import os
import sys

ENTRY = (
    "WARNING: This human is 60% water, 40% overconfidence, "
    "and 0% able to find its keys in under twenty minutes."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> None:
    if not ENTRY.strip() or len(ENTRY) > MAX_CHARS or "\n" in ENTRY:
        print(
            f"invalid entry: {len(ENTRY)} chars, "
            f"must be a single line of 1-{MAX_CHARS} characters",
            file=sys.stderr,
        )
        sys.exit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
