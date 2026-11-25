"""The Excuse That Almost Works — one line a gamer texts the boss.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Gate: UTF-8, 1-140 chars, <=20 words, one line. The line is a boring,
specific workplace failure (a dead monitor, the spare locked away) —
the kind of detail a tired manager almost believes, and the laugh is in
its own logic: the gamer's screen is gone, so of course he can't work.
"""

import os

LINE = "My monitor died this morning and the spare's locked in the office, so I'm useless till IT ships one."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
