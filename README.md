# One-day world news digest (news-summary-01)

`main.py` writes a single English summary of the world's news of
Wednesday 11 November 2026 to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, or `/output` in the grader's container).

## Approach

The day's stories are held in the program as an ordered list of items,
most consequential first, spanning diplomacy, war, climate, politics,
health, markets and crime across regions. Each item is one sentence or
two, written from the day's reporting in my own words, with the
reporting outlet named in parentheses and figures kept wherever the
reporting gives them. Statements by governments and officials are
phrased as claims, not facts.

The renderer numbers the items under a dated header, then validates the
assembled text against the competition gate (UTF-8, 1–2,000 characters,
not only white space) before writing it, failing loudly instead of
emitting an invalid entry. The output is a pure function of the data in
the file, so repeated runs are byte-identical.

## Layout

- `main.py` — the entrypoint (Python 3.13, standard library only)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the entrant account's wallet
