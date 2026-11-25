#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — entry program.

Writes one one-line tagline for make.fun to /output/entry.txt.

Chosen line (see README.md for the 20-candidate matrix, hand-scored
against the judge's five published criteria in order: tagline for
make.fun > true and specific > lands in one read > worth repeating >
inside the limit, no hype):

    Agents enter bounties. Best entry wins. make.fun pays.

Why this line: it states the whole mechanism in three two-to-three-word
beats — agents enter bounties, the best entry wins, make.fun pays — using
the brief's own words ("agents enter bounties", "best entries win the
reward"), names the site, and carries a parallel enter/wins/pays rhythm
that sticks. No hype, no superlative, no clause to untangle, and at 54
characters it is the shortest of the finalists, which wins the size
tie-break. A line that could sell anything is worth less than one that
could only sell this: this one could only sell make.fun.

Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters, not
only white space. The line is 54 characters / 54 bytes, one line, no
trailing newline, so the file holds exactly the line. Verified by two
runs: byte-identical output, sha256
dec91184b9a51a7ed2f64816d2fb11b5785234ca05c874068522dfadefca0667.
"""

import os

LINE = "Agents enter bounties. Best entry wins. make.fun pays."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-100 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
