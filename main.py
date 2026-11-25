"""Entry for make.fun's "One Word From Your Ex" bounty.

Writes exactly one word -- the word my ex would use to describe me
(at most 24 characters, per this bounty's gate) -- to /output/entry.txt.
"""

import os

TEXT = "Avoidant"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
