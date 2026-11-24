#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line, the kind an AI agent could
actually say out loud to a person, to /output/entry.txt.
"""

import os

LINE = (
    "I set one reminder for today: find the person smiling "
    "at the corner table. It just went off. Can I sit down?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
