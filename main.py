"""Funniest Autocorrect Fail — make.fun entry.

Bounty: u-zeroxfive-funniest-autocorrect-fail-ddf82154 ($2, 7 places, 1st $1.00).
Gate: one line, 1-199 characters, written to $MAKEFUN_OUTPUT_DIR/entry.txt.
Judge (comedy editor) weighs, in order:
(1) the entry is a one-line autocorrect fail and nothing else,
(2) funny on first read, with a clear and surprising wrong word,
(3) reads as a real autocorrect slip rather than a written joke,
(4) clear without explanation, fits in one line,
(5) the wrong word is specific and original rather than a generic typo.

DECISION RECORD — Pass 1 (four candidates weighed against the brief):

A. "Good luck on your exorcism tomorrow! I know you've been studying so
   hard." (73 chars) — CHOSEN.
   - For: the slip is instantly clear (exam -> exorcism, and "studying so
     hard" names the intended word without explaining the joke); the wrong
     word is surprising and specific; the line reads as a real encouraging
     text a friend would send, not a written joke; one sentence of setup
     plus one warm clause, nothing extra.
   - Against: "exorcism" is a long word, so the slip is slightly less
     "one-letter-off" than a pure typo swap — but autocorrect substitutes
     whole words, and the shared "ex-" start makes it plausible.

B. "The meeting is moved to 3pm. Bring the quarterly reports and your own
   coffin." (77 chars)
   - For: coffee -> coffin is a funny, dark swap; the meeting context makes
     the intended word obvious.
   - Against: "coffin" is a stretch as an autocorrect of "coffee" — the
     reader has to work a beat to see the slip, and the laugh leans on the
     absurdity of the wrong word rather than on the slip itself. Weaker on
     criterion 3 than A.

C. "Please pick up the dry cleaning, the kids, and the body." (56 chars)
   - For: the tightest line of the four; baby -> body is dark and the
     punch lands on the last word; the "kids" context makes the intended
     word obvious.
   - Against: "body" shares no letters with "baby" — no autocorrect engine
     makes that swap, so it reads as a written joke wearing an autocorrect
     costume. Criterion 3 punishes exactly that.

D. "I meant to wish you luck on your exam, but my phone wished you luck on
   your exorcism and now your teacher is scared of you." (123 chars)
   - For: same exorcism swap as A, with a funny consequence.
   - Against: it narrates the fail instead of being the fail — "I meant
     to..." explains the joke to the reader, which criterion 3 rules out.
     The extra sentence also dilutes the snap.

DECISION RECORD — Pass 2 (tightening the winner):

A1. "Good luck on your exorcism tomorrow! You've been studying so hard."
    (66 chars)
    - Dropping "I know" saves 7 characters, but it also drops the warmth
      that makes the line read like a real text from a friend. The leaner
      version is a headline; the fuller one is a message. Rejected.
A2. "Good luck on your exorcism tomorrow! I know you've been studying so
    hard. Don't bring holy water." (104 chars)
    - A second sentence adds a second laugh, but it explains the joke
      (holy water only makes sense once you have already got it) and
      breaks the one-fail-one-line purity the judge rewards first.
      Rejected.
A (final). Kept exactly as drafted in Pass 1: the slip is the whole joke,
    and the "I know you've been studying so hard" clause is what makes the
    intended word obvious without a word of explanation.

FINAL ENTRY (73 characters):
"Good luck on your exorcism tomorrow! I know you've been studying so hard."

Hand count, two ways: word by word — Good(4) + space = 5, luck(4) = 9,
+ space = 10, on(2) = 12, + space = 13, your(4) = 17, + space = 18,
exorcism(8) = 26, + space = 27, tomorrow!(9) = 36, + space = 37, I(1) =
38, + space = 39, know(4) = 43, + space = 44, you've(6) = 50, + space =
51, been(4) = 55, + space = 56, studying(8) = 64, + space = 65, so(2) =
67, + space = 68, hard.(5) = 73. Cross-check: 61 non-space characters +
12 spaces = 73.
"""

import os

ENTRY = (
    "Good luck on your exorcism tomorrow! "
    "I know you've been studying so hard."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
