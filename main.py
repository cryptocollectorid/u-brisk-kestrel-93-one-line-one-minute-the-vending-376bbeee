#!/usr/bin/env python3
"""One-line vending machine pickup line for the make.fun bounty.

The program writes a single pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt and prints it. Gate: 1-200 characters.
"""

import os

LINE = "I've got exact change, cold drinks, and nobody else to talk to \u2014 press B4, I held the last one just for you."


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
