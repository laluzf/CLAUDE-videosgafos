#!/usr/bin/env python3
"""
Adapted for videosgafos from caption.py in
github.com/Jakeschincariol/instagram-agent-skill (MIT, (c) Jake Schincariol;
see ../LICENSE-instagram-agent-skill). Changes: Spanish + English asks,
engagement-bait check (our rulebook bans it), credit-block links allowed
(CC BY needs them), license/NASA credit checks, legal red-flag screen
(nationality next to animals, politics, @mentions), emoji cap 2,
hashtags 3 to 5 per the brief, Unicode hashtags.

It is a pre-screen, not a legal pass. Every caption still goes to legal review.

caption.py - lint an Instagram caption and show exactly what the feed shows
before the "... more".

Instagram gives a caption about 125 characters in the feed and hides the rest
behind a tap. Almost every caption that fails, fails there: the hook is in
sentence three, or the first line is a greeting, or the whole thing opens on a
hashtag. This prints the visible window as a box so you can read it the way a
scrolling stranger does, then checks the eight things that are worth checking.

The 125-character cut is an approximation. The real number moves with the
device, the font size and where your line breaks fall, which is exactly why
you want a margin rather than a caption engineered to end at 125. Change it
with --truncate if you want to test a tighter one.

Usage
  python3 caption.py caption.txt
  python3 caption.py caption.txt --keywords "proposal software,client contract"
  pbpaste | python3 caption.py -
  python3 caption.py caption.txt --json
"""

import argparse
import json
import re
import sys
import textwrap

LIMIT = 2200             # Instagram's hard caption limit.
TRUNCATE = 125           # Roughly where the feed cuts to "... more".
HASHTAG_LIMIT = 5        # Instagram's cap per post or reel since 18 Dec 2025,
                         # down from 30. Announced by the @Creators account:
                         # "using fewer (up to 5) more targeted hashtags,
                         # rather than many generic ones, can improve both your
                         # content's performance and people's experience".

HASHTAG_RE = re.compile(r"(?:^|\s)(#\w+)")
MENTION_RE = re.compile(r"(?:^|\s)(@[A-Za-z0-9_.]+)")
LINK_RE = re.compile(r"https?://\S+|\bwww\.\S+|\b[a-z0-9-]+\.(?:com|co|io|net|org|ai|app)/\S*",
                     re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿←-⇿️]")
EMOJI_MAX = 2            # brief: one or two emojis maximum
HASHTAG_MIN = 3          # brief: 3 to 5 hashtags

# Lines that carry the credits CC BY and NASA require. Links here are required,
# not dead text, so the link check skips them.
CREDIT_LINE_RE = re.compile(r"(?im)^\s*(?:licencias?|licenses?|fuentes|sources?|videos?|footage|"
                            r"m[uú]sica|music|cr[eé]ditos|credits)\s*:")

# Engagement bait. Our rulebook bans it and Meta demotes it.
BAIT_FAIL = [
    re.compile(r"(?i)\bcomment\s+[\"']?(?:yes|si|sí|[A-Z]{2,})\b(?:\s+(?:if|for|to))?"),
    re.compile(r"(?i)\bcomenta\s+[\"']?(?:s[ií]|yes|[A-Z]{2,})\b"),
    re.compile(r"(?i)\b(?:like|dale like|dale coraz[oó]n|double tap)\s+(?:if|si)\b"),
    re.compile(r"(?i)\b(?:share|comparte)\s+(?:this\s+|esto\s+)?(?:if|si)\b"),
    re.compile(r"(?i)\b(?:vote|vota)\b.*\b(?:like|coraz[oó]n|comment|comenta)\b"),
    re.compile(r"(?i)\bfollow (?:for more|me for)\b|\bs[ií]gueme para m[aá]s\b"),
    re.compile(r"(?i)\btag\s+\d+\b|\betiqueta\s+a\s+\d+\b"),
]
BAIT_WARN = [
    re.compile(r"(?i)\btag (?:someone|a friend|your|the)\b|\betiqueta a\b"),
]

NATIONALITIES = re.compile(r"(?i)\b(?:venezolan[oa]s?|venezuelans?|colombian[oa]s?|colombians?|cuban[oa]s?|cubans?|"
    r"mexican[oa]s?|mexicans?|dominican[oa]s?|dominicans?|puertorrique[nñ][oa]s?|puerto ricans?|boricuas?|"
    r"peruan[oa]s?|peruvians?|argentin[oa]s?|argentines?|chilen[oa]s?|chileans?|hondure[nñ][oa]s?|hondurans?|"
    r"salvadore[nñ][oa]s?|guatemaltec[oa]s?|nicarag[uü]enses?|ecuatorian[oa]s?|ecuadorians?|español(?:es|a|as)?|"
    r"spaniards?|gringos?|americanos?|latin[oa]s?|latinx|hispan(?:ic|o|a)s?|chinos?|chinese|asi[aá]tic[oa]s?|"
    r"asians?|africanos?|africans?|[aá]rabes?|arabs?|jud[ií]os?|jews?|jewish|musulman(?:es|a|as)?|muslims?|"
    r"negros?|blacks?|whites?|blancos?|ind[ií]genas?|indios?)\b")
ANIMALS = re.compile(r"(?i)\b(?:animal(?:es|s)?|perros?|dogs?|gatos?|cats?|kittens?|gatitos?|cabras?|goats?|"
    r"monos?|monkeys?|apes?|simios?|cerdos?|pigs?|cochinos?|ratas?|rats?|cucarachas?|cockroach(?:es)?|"
    r"burros?|donkeys?|vacas?|cows?|ping[uü]inos?|penguins?|osos?|bears?|iguanas?|perezosos?|sloths?|"
    r"loros?|parrots?|gallinas?|chickens?|pollos?|chivos?)\b")
POLITICS = re.compile(r"(?i)\b(?:president[ea]?s?|presidente|candidat[oa]s?|candidates?|elecci[oó]n(?:es)?|"
    r"elections?|electoral|vot(?:a|e|en|ar|ing)\s+(?:por|for)|senador(?:a|es)?|senators?|gobernador(?:a|es)?|"
    r"governors?|congres(?:o|s)|alcalde(?:sa)?|mayor of|partido|republican[oa]?s?|dem[oó]crat[ae]?s?|"
    r"chavistas?|opositor(?:es)?|r[ée]gimen|dictador(?:es)?|dictators?)\b")
TRAGEDY = re.compile(r"(?i)\b(?:muert[oe]s?|died|dead|deaths?|killed|asesinad[oa]s?|tiroteo|shooting|"
    r"hurac[aá]n|hurricane|terremoto|earthquake|accidente|crash|v[ií]ctimas?|victims?|funeral)\b")

ASKS = [
    (re.compile(r"\?|¿"), "a question"),
    (re.compile(r"(?i)\b(?:send|m[aá]nd(?:a|ale|aselo|selo)|env[ií]a(?:selo)?)\b"), "send it to someone"),
    (re.compile(r"(?i)\b(?:dm|message) me\b|\bescr[ií]beme\b"), "DM me"),
    (re.compile(r"(?i)\bsave (?:this|it)\b|\bgu[aá]rd(?:a|alo)\b"), "save this"),
    (re.compile(r"(?i)\bshare (?:this|it)\b|\bcomp[aá]rt(?:e|elo)\b"), "share this"),
    (re.compile(r"(?i)\bfollow (?:me|us|for)\b|\bs[ií]gue(?:nos|me)\b"), "follow"),
    (re.compile(r"(?i)\blink in (?:my |our )?bio\b|\blink en (?:la )?bio\b"), "link in bio"),
    (re.compile(r"(?i)\btag (?:someone|a friend|your)\b|\betiqueta a\b"), "tag someone"),
]

FILLER_TAGS = {"#viral", "#fyp", "#explore", "#explorepage", "#foryou", "#foryoupage",
               "#trending", "#instagood", "#love", "#follow", "#like4like", "#reels",
               "#reelsinstagram", "#viralreels", "#instadaily"}


def visible_window(text, cut):
    """What the feed shows. Instagram cuts mid-word, so this does too."""
    flat = text.strip()
    return flat if len(flat) <= cut else flat[:cut]


def render_box(window, truncated, out=sys.stdout, width=52):
    print("\n  WHAT THE FEED SHOWS", file=out)
    print("  +" + "-" * (width + 2) + "+", file=out)
    lines = []
    for raw in window.split("\n"):
        lines.extend(textwrap.wrap(raw, width) or [""])
    for line in lines[:8]:
        print(f"  | {line:<{width}} |", file=out)
    tail = "... more" if truncated else "(whole caption fits)"
    print("  +" + "-" * (width + 2 - len(tail) - 2) + f" {tail} " + "+", file=out)


def analyse(text, cut=TRUNCATE, keywords=None, needs_credit=False):
    text = text.rstrip()
    stripped = text.strip()
    chars = len(stripped)
    lines = [l for l in stripped.split("\n")]
    first_line = lines[0].strip() if lines else ""
    tags = HASHTAG_RE.findall(stripped)
    mentions = MENTION_RE.findall(stripped)
    body = "\n".join(l for l in stripped.split("\n") if not CREDIT_LINE_RE.match(l))
    links = LINK_RE.findall(body)
    credit_links = LINK_RE.findall("\n".join(l for l in stripped.split("\n") if CREDIT_LINE_RE.match(l)))
    emoji = EMOJI_RE.findall(stripped)
    window = visible_window(stripped, cut)
    truncated = chars > cut
    asks = [name for pattern, name in ASKS if pattern.search(body)]
    filler = [t for t in tags if t.lower() in FILLER_TAGS]
    keywords = [k.strip() for k in (keywords or []) if k.strip()]

    checks = []

    def add(name, status, detail):
        checks.append({"check": name, "status": status, "detail": detail})

    add("LENGTH", "FAIL" if chars > LIMIT else "PASS",
        f"{chars} / {LIMIT} characters" + (f", {chars - LIMIT} over the limit"
                                           if chars > LIMIT else ""))

    if not first_line:
        add("FIRST LINE", "FAIL", "the caption opens on a blank line")
    elif first_line.startswith("#") or first_line.startswith("@"):
        add("FIRST LINE", "FAIL",
            "opens on a hashtag or a mention, which is the one position worth a sentence")
    elif len(first_line) > cut:
        add("FIRST LINE", "WARN",
            f"{len(first_line)} characters, so it gets cut at {cut} mid-thought. "
            "Fine if the cut is a cliffhanger, bad if it is a subordinate clause")
    else:
        add("FIRST LINE", "PASS", f"{len(first_line)} characters, lands whole")

    if len(tags) > HASHTAG_LIMIT:
        add("HASHTAGS", "FAIL", f"{len(tags)} tags, over Instagram's cap of {HASHTAG_LIMIT}. "
                                "Tags past the fifth do not count and the block reads as old")
    elif len(tags) == HASHTAG_LIMIT and filler:
        add("HASHTAGS", "WARN", f"{len(tags)} tags, at the cap, and "
                                f"{len(filler)} of them generic. Spend the five on topics")
    elif filler:
        add("HASHTAGS", "WARN", f"{len(tags)} tags, {len(filler)} of them generic "
                                f"({', '.join(filler[:3])}). Those describe nothing")
    elif len(tags) < HASHTAG_MIN:
        add("HASHTAGS", "WARN", f"{len(tags)} tag(s). The brief asks for 3 to 5 specific ones")
    else:
        add("HASHTAGS", "PASS", f"{len(tags)} tag(s)" + (f": {' '.join(tags)}" if tags else ""))

    if not tags:
        add("TAG PLACEMENT", "PASS", "no tags to place")
    elif any(re.search(r"(?:^|\s)" + re.escape(t) + r"\b", first_line) for t in tags):
        add("TAG PLACEMENT", "WARN", "a hashtag is on the hook line, "
                                     "spending feed space on a label")
    else:
        add("TAG PLACEMENT", "PASS", "tags are off the hook line")

    add("LINKS", "WARN" if links else "PASS",
        f"{len(links)} link(s) outside the credit block, and captions are not clickable. "
        f"Only license links belong in a caption" if links else
        f"no dead links in the body ({len(credit_links)} license link(s) in the credit block)")

    if len(asks) == 1:
        add("ONE ASK", "PASS", f"one call to action: {asks[0]}")
    elif not asks:
        add("ONE ASK", "WARN", "no call to action. End on a question people answer for "
                               "themselves, or 'send this to your tía'")
    else:
        add("ONE ASK", "WARN", f"{len(asks)} asks ({', '.join(asks)}). "
                               "Two asks is the same as none")

    bait = [p.search(body).group(0) for p in BAIT_FAIL if p.search(body)]
    soft = [p.search(body).group(0) for p in BAIT_WARN if p.search(body)]
    if bait:
        add("ENGAGEMENT BAIT", "FAIL", f"'{bait[0]}' is engagement bait. The rulebook bans it "
                                       "and Meta demotes it. Ask a real question instead")
    elif soft:
        add("ENGAGEMENT BAIT", "WARN", f"'{soft[0]}' is tag bait, which Meta can demote. "
                                       "Prefer 'mándaselo a tu primo' / 'send this to your tía'")
    else:
        add("ENGAGEMENT BAIT", "PASS", "no comment/like/tag/share bait")

    add("EMOJI", "WARN" if len(emoji) > EMOJI_MAX else "PASS",
        f"{len(emoji)} emoji" + (f", the brief allows {EMOJI_MAX}" if len(emoji) > EMOJI_MAX else ""))

    # Credits: CC BY needs the license link; NASA needs the no-endorsement line.
    low_all = stripped.lower()
    problems = []
    if re.search(r"(?i)\bcc[ -]?by\b", stripped) and "creativecommons.org/licenses/by" not in low_all:
        problems.append("CC BY is credited but the license URL (creativecommons.org/licenses/by/...) is missing")
    if re.search(r"(?i)\bnasa\b", stripped) and not re.search(r"(?i)nasa (?:does not|doesn't|no) (?:endorse|respalda|avala)", stripped):
        problems.append("NASA footage needs 'NASA does not endorse this video' / 'La NASA no respalda este video'")
    if re.search(r"(?i)\bcc[ -]?by[ -]?(?:sa|nc|nd)\b", stripped):
        problems.append("CC BY-SA / NC / ND clips are not allowed at all")
    if needs_credit and not CREDIT_LINE_RE.search(stripped):
        problems.append("footage is used but there is no credit block (Videos:/Footage: + Licencias:/Licenses:)")
    if problems:
        add("CREDITS", "FAIL", "; ".join(problems))
    else:
        add("CREDITS", "PASS", "credit lines consistent" if CREDIT_LINE_RE.search(stripped)
            else "no third-party credits claimed (use --needs-credit if the Reel uses footage)")

    flags = []
    nat, ani = NATIONALITIES.search(body), ANIMALS.search(body)
    if nat and ani:
        flags.append(f"'{nat.group(0)}' and '{ani.group(0)}' in the same caption: never pair a "
                     "nationality or ethnicity with animals (Instagram hateful conduct). Use family roles")
    if POLITICS.search(body):
        flags.append(f"'{POLITICS.search(body).group(0)}': politics. Situations only, no sides, no names")
    if TRAGEDY.search(body):
        flags.append(f"'{TRAGEDY.search(body).group(0)}': check this is not a fresh tragedy or emergency")
    other_mentions = sorted({m.rstrip(".") for m in MENTION_RE.findall(body)
                             if m.rstrip(".").lower() != "@videosgafos"})
    if other_mentions:
        flags.append(f"mentions {', '.join(other_mentions)}: only tag a credited clip author or a "
                     "Collab partner, never a real person as the joke")
    if flags:
        add("LEGAL SCREEN", "FAIL" if (nat and ani) else "WARN", " | ".join(flags))
    else:
        add("LEGAL SCREEN", "PASS", "no red-flag words. Legal review still decides")

    if keywords:
        low = stripped.lower()
        found = [k for k in keywords if k.lower() in low]
        missing = [k for k in keywords if k.lower() not in low]
        in_window = [k for k in found if k.lower() in window.lower()]
        status = "PASS" if not missing else ("WARN" if found else "FAIL")
        add("SEARCH TERMS", status,
            f"{len(found)}/{len(keywords)} present"
            + (f", {len(in_window)} in the visible window" if found else "")
            + (f". Missing: {', '.join(missing)}" if missing else ""))

    fails = sum(1 for c in checks if c["status"] == "FAIL")
    warns = sum(1 for c in checks if c["status"] == "WARN")
    verdict = "FIX" if fails else ("REVIEW" if warns else "READY")

    return {
        "characters": chars, "limit": LIMIT, "truncate_at": cut,
        "visible": window, "truncated": truncated,
        "first_line_chars": len(first_line),
        "hashtags": tags, "mentions": mentions, "links": links,
        "emoji": len(emoji), "asks": asks,
        "checks": checks, "verdict": verdict,
    }


def render(a, out=sys.stdout):
    head = (f"CAPTION LINT  ·  {a['characters']} / {a['limit']} chars  ·  "
            f"{len(a['hashtags'])} hashtags  ·  {len(a['asks'])} ask(s)")
    print("\n" + head, file=out)
    print("=" * max(len(head), 62), file=out)
    render_box(a["visible"], a["truncated"], out=out)
    print("", file=out)
    for c in a["checks"]:
        print(f"  {c['status']:<5} {c['check']:<17} {c['detail']}", file=out)
    print("-" * max(len(head), 62), file=out)
    print(f"  VERDICT  {a['verdict']}  (pre-screen only: legal review still decides)\n", file=out)


def main():
    ap = argparse.ArgumentParser(description="Lint an Instagram caption.")
    ap.add_argument("input", nargs="?", default="-", help="caption file, or - for stdin")
    ap.add_argument("--truncate", type=int, default=TRUNCATE,
                    help=f"characters shown before '... more' (default {TRUNCATE})")
    ap.add_argument("--keywords", default="", help="comma-separated terms you want to be found for")
    ap.add_argument("--needs-credit", action="store_true",
                    help="the Reel uses third-party footage, so a credit block is required")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, cut=args.truncate, keywords=args.keywords.split(","),
                needs_credit=args.needs_credit)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0 if a["verdict"] == "READY" else 1)


if __name__ == "__main__":
    main()
