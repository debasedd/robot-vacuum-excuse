#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — writes one line to /output/entry.txt.

The line is the excuse a robot vacuum gives for missing a spot, spoken by
the vacuum itself in its own world: it mapped the crumb and approached
with confidence, and then its bumper signed a peace treaty with the chair
leg instead of cleaning.
"""

import os

LINE = "I mapped the crumb, approached with confidence, then my bumper signed a peace treaty with the chair leg instead."

# The gate allows 1 to 140 characters; keep the line inside it by construction.
MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-140 character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
