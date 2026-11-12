#!/usr/bin/env python3
"""news-summary-01 entry: a one-day world news digest.

The program holds the day's stories as data, renders them as a numbered
digest ordered by importance, checks the result against the competition
gate (UTF-8, 1 to 2,000 characters, not only white space) and writes it to
entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, else /output).

Every story is a single sentence or two, attributed to the outlet that
reported it, in the entrant's own words. Claims made by governments or
officials are worded as claims. The output depends only on the data below,
so two runs write the same bytes.
"""

import os
import sys

HEADER = "World news, Wednesday 11 November 2026."

# The day's stories, most consequential first. Each entry is the whole item
# as it will be printed; the renderer adds only the item number.
STORIES = [
    "Russia and Ukraine ended two days of US-mediated talks in Abu Dhabi "
    "with agreement on a major prisoner-of-war exchange but no ceasefire "
    "or deal on territory, US envoy Jared Kushner citing a lack of trust; "
    "Russian strikes hit six Ukrainian electricity substations overnight, "
    "and the US envoys go to Moscow on Thursday (Reuters).",

    "Iran said the Strait of Hormuz, shut for more than 250 days, would "
    "never return to its pre-war status, and claimed more tankers had "
    "struck mines in the waterway (Al Jazeera); monitoring firms counted "
    "at least 37 attacks on ships in and near the strait in November, "
    "the most in any month of the war.",

    "World leaders opened the COP31 climate summit in Antalya, Turkey, "
    "where UN Secretary-General Antonio Guterres called for a tax on "
    "fossil fuels (AFP).",

    "The US House voted 211-204 to refer an impeachment resolution "
    "against Defense Secretary Pete Hegseth to committee, effectively "
    "killing it (BBC).",

    "Millions of Spanish workers staged the country's first general "
    "strike in 14 years over housing costs; average rent has nearly "
    "doubled in a decade to 1,176 euros a month (Reuters).",

    "Confirmed Ebola cases in the Democratic Republic of Congo passed "
    "11,000, with at least 5,387 deaths reported in the Bundibugyo-strain "
    "outbreak, now the second-largest and second-deadliest on record "
    "(Reuters).",

    "US consumer prices rose 0.4% in October and core prices 0.3%, both "
    "above forecasts (Bureau of Labor Statistics), and Asian shares "
    "fell as traders bet on a larger December Federal Reserve rate rise.",

    "US prosecutors charged three men over alleged Iran-backed plots, "
    "including one targeting RAF Fairford, the British air base used by "
    "US forces (BBC).",

    "El Salvador's President Nayib Bukele said his forces had destroyed "
    "the headquarters of Haiti's 400 Mawozo gang and the home of its "
    "leader (BBC).",

    "Nine people were seriously injured when a bus collided with several "
    "vehicles in Seongnam, South Korea (Yonhap).",
]

MAX_CHARS = 2000


def render() -> str:
    """Assemble the digest exactly as the judge will read it."""
    lines = [HEADER, ""]
    for i, story in enumerate(STORIES, start=1):
        lines.append(f"{i}. {story}")
    return "\n".join(lines)


def check_gate(text: str) -> None:
    """Fail loudly rather than write an entry the gate would refuse."""
    if not text.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, outside 1..{MAX_CHARS}")
    text.encode("utf-8")  # raises if the text cannot be written as UTF-8


def main() -> int:
    text = render()
    check_gate(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
