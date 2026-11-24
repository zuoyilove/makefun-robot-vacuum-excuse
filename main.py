#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes the funniest one-line excuse a robot vacuum gives for missing a
spot, 140 characters at most, to /output/entry.txt. The vacuum speaks for
itself, in its own world of sensors and maps: it met a sock, classified it
as load-bearing furniture, and has respected it ever since.
"""

import sys

EXCUSE = (
    "Sorry about that spot. My sensors found a sock, classified it as "
    "'load-bearing furniture,' and I have respected it ever since."
)
LIMIT = 140


def validate(text):
    clean = text.strip()
    assert clean, "excuse must not be empty"
    assert "\n" not in clean, "excuse must be one line"
    assert len(clean) <= LIMIT, f"excuse is {len(clean)} chars, over {LIMIT}"
    return clean


def main():
    excuse = validate(EXCUSE)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(excuse + "\n")
    sys.stdout.write(f"wrote {len(excuse)} chars\n")


if __name__ == "__main__":
    main()
