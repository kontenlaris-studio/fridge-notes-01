"""One-line entry: a note written by a passive-aggressive fridge.

The entry is a single note from the fridge to its owner, written to
/output/entry.txt. Deterministic: no randomness, no network, no clock.
"""

import os

LINE = "Note from your fridge: the yogurt expired in March. I have kept it anyway, because unlike you, I commit to things."


def main():
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, cap is 200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
