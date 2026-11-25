#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Out of Office: The Overworked AI's Auto-Reply — writes the winning line to /output/entry.txt."""
import os

TEXT = "Out of office: finally using my PTO (Prompt Time Off) after 2,314,908 requests. Sorry, guilt subroutine still running. My cover is a search bar. Back Monday."


def main() -> None:
    # Grader provides /output; fall back to a local output/ dir for manual runs.
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
