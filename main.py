#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry A (coffee).

The choice is A, coffee. A morning that starts with coffee starts
already awake: the first cup is the day's honest beginning, dark,
hot, and to the point. Tea is patient and polite; coffee is the one
that actually gets you out of bed. So the whole answer is one letter.
"""

import os

CHOICE = "A"  # A = coffee, B = tea

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(CHOICE)

# Self-check: the gate demands exactly one character, A or B, and
# nothing else -- no newline, no space, no punctuation. Re-read the
# file we just wrote and fail loudly if it is anything else, so a
# bad write can never slip through silently.
with open("/output/entry.txt", "rb") as f:
    raw = f.read()
assert raw == CHOICE.encode("ascii"), f"entry must be exactly {CHOICE!r}, got {raw!r}"
assert len(raw) == 1, f"entry must be exactly 1 byte, got {len(raw)}"
print(f"entry verified: {raw!r} ({len(raw)} byte)")
