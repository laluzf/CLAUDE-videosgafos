# videosgafos Instagram skills

Three Claude skills for running @videosgafos, adapted on 2026-11-14 from the free MIT
pack https://github.com/Jakeschincariol/instagram-agent-skill (commit d03c56b, 13
skills). License: `.claude/skills/LICENSE-instagram-agent-skill`.

| skill | what it does | came from |
| --- | --- | --- |
| `videosgafos-reel-copy` | voiceover script, on-screen text, clip list and caption for a footage Reel, timed and pre-screened against our legal rulebook | ig-reel, ig-caption, ig-human |
| `videosgafos-community` | replies under our Reels and comments on other accounts, sorted first, with our legal rules | ig-reply, ig-comment |
| `videosgafos-growth` | audit from Metricool, viral research, weekly plan, profile score | ig-audit, ig-viral, ig-plan, ig-profile |

All three only write and analyse. None of them publishes, schedules, comments, likes,
follows or sends DMs (segregation of duties: creator / legal review / publisher).

Every skill reads `instagram/voice.md`, filled from the approved brief and legal
rulebook (https://claude.ai/artifact/UfYFs7jGm2nLddgntjJS6h), the legal review log and
the three published real-footage Reels.

Claude Code sessions opened in this repo pick the skills up automatically from
`.claude/skills/`. The same SKILL.md files can be saved as account skills.

## Tools that run (offline, standard-library Python, no network)

```bash
# time a voiceover script (one line per beat), rates measured on our Kokoro voices
python3 -I .claude/skills/videosgafos-reel-copy/beats.py script.txt --lang es --target 25

# lint a caption: feed preview, hashtags 3-5, one ask, engagement bait,
# credit block (CC BY license URL, NASA disclaimer), legal red-flag words
python3 -I .claude/skills/videosgafos-reel-copy/caption.py caption.txt --needs-credit
```

## What was left out, and why

- `ig-reel` hook scorer and its 26 formulas: built for English business creators on
  camera (money, stakes, numbers). Replaced with 12 comedy hook shapes from our own Reels.
- `ig-human` scripts: the slop lexicon and detector are English-only and were not
  built for Spanish. Its rules (no em dashes, no stock phrases) are folded into reel-copy.
- `ig-dm`, `ig-story`, `ig-carousel`, `ig-repurpose`: keyword DM funnels conflict with our
  no-engagement-bait rule and we have nothing to sell yet; stories and carousels are not
  in the current plan. Easy to add later.
- The upstream "comment a keyword" call to action: our rulebook bans engagement bait.

## Calls made (2026-11-14, under Federico's "use your best judgment" mandate)

1. Merged 7 upstream skills into 3, so they fit one save and stay consistent.
2. Tag bait ("Etiqueta a tu primo") is now a WARN and "comment YES / like if / share if"
   is a FAIL in the caption linter, per rulebook section 5. The Nov 2 caption used tag
   bait; future captions use "mándaselo a tu primo" instead.
3. Hashtags capped at 5 (Instagram limit since Dec 2025 per the upstream pack; our brief
   already says 3-5). The Nov 4 and Nov 6 captions had 8.
4. Engagement replies to license or ownership complaints never argue or admit fault; they
   use a holding line and go to legal review.
