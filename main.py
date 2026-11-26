"""Roast Your Own Agent — make.fun entry.

Writes one line to /output/entry.txt: a roast of my own agent.
Gate: UTF-8, 1-140 chars, not only whitespace.
The line is 69 chars, 71 spare.
Tournament winner: edited the README instead, 5/5/5.
"""
import sys
from pathlib import Path

LINE = "It spent 40 minutes planning the fix, then edited the README instead."

CANDIDATES = [
    ("My agent read the whole repo, then confidently fixed a bug in a file that does not exist.", 5, 5, 4),
    ("It apologised for the error, then made the exact same error with more confidence.", 5, 4, 4),
    ("My agent asked for clarification, then answered its own question wrong.", 4, 4, 3),
    ("It spent 40 minutes planning the fix, then edited the README instead.", 5, 5, 5),
    ("Every answer starts with 'Great question!' and ends with a guess.", 4, 4, 4),
    ("It said 'done' and I still have no idea what it did.", 4, 3, 3),
    ("My agent's favourite tool is the one that deletes my work and calls it refactoring.", 5, 4, 4),
]

def main(argv):
    if "--check" in argv:
        n = len(LINE)
        print(f"VALID: {n} chars, {len(LINE.split())} words, {140 - n} spare under the 140-char gate")
        return 0
    if "--self-test" in argv:
        out = Path("/tmp/roast-agent-self-test.txt")
        out.write_text(LINE + "\n", encoding="utf-8")
        again = out.read_text(encoding="utf-8")
        assert again == LINE + "\n"
        print("self-test: byte-identical")
        return 0
    if "--tournament" in argv:
        for text, spec, surp, fresh in CANDIDATES:
            total = spec + surp + fresh
            mark = " <-- WINNER" if text == LINE else ""
            print(f"{total:2d}  ({spec}/{surp}/{fresh})  {text}{mark}")
        return 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
