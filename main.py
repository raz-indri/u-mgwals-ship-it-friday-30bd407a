"""Ship It Friday entry: writes the winning one-line commit message.

The line is a git commit message from a cheerful, confident AI coding
agent, written on a Friday afternoon, moments before it breaks prod.
It won a 6-draft duel test (5/5 pairwise wins) against five other
candidates. Local test: OUTPUT_DIR=/tmp/shipit-test python3 main.py
writes exactly one line of 78 characters to entry.txt.
"""

import os

ENTRY = "feat: replace the database with vibes, deploy to prod, log off for the weekend"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate self-check: UTF-8, 1-159 chars, single line, not whitespace-only.
    assert 1 <= len(ENTRY) <= 159, "entry length out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be whitespace only"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
