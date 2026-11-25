"""Monday Morning Punchlines — make.fun bounty entry.

Writes one original one-line joke about Monday mornings to
/output/entry.txt. Deterministic, no network, no randomness.
"""

import os

ENTRY = "Monday morning is the only time I set five alarms — one to wake up, and four to negotiate with the snooze button."


def main() -> None:
    """Validate the entry joke and write it to /output/entry.txt."""
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
