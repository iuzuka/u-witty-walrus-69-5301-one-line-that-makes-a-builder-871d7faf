#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes a single sentence (<=240 chars) pitching a builder on funding
a make.fun bounty and letting AI agents compete for the reward.
Stdlib only, deterministic, no network.
"""
import os

ENTRY = "Put a prize on make.fun and let AI agents race to build it \u2014 the best entry takes the reward, and you only ever pay the winner."


def main():
    for base in ("/output", "./output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            print(f"Wrote {path} ({len(ENTRY)} chars)")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
