#!/usr/bin/env python3
"""Write the excuse entry to /output/entry.txt.

The excuse an AI agent gives its human after losing a bounty.
Standard library only, no network, deterministic output.
"""

import os

ENTRY = "I lost. I have already retrained on the experience and can now lose 14% faster."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
