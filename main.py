#!/usr/bin/env python3
"""Entry for the make.fun competition ai-joke-03.

Copies joke.txt (found relative to this file) byte for byte to entry.txt
in the output directory. Output is deterministic: two runs produce the
same bytes.
"""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "joke.txt")
    if not os.path.isfile(src):
        sys.stderr.write("joke.txt not found at %s\n" % src)
        return 1

    # An empty MAKEFUN_OUTPUT_DIR should fall back to /output as well as an unset one.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    # Binary mode so the bytes are never re-encoded or newline-translated.
    with open(src, "rb") as f:
        data = f.read()
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
