---
name: videosgafos-reel-copy
description: Write a videosgafos Reel's voiceover script, on-screen text and Instagram caption (EN or ES) over free legal footage, timed and pre-screened against our legal rulebook. Writes only, never publishes.
---

# videosgafos-reel-copy

Turns one funny idea into the words of a videosgafos Reel: three hook options, the
voiceover lines for Kokoro, the on-screen text, a clip list to find footage for,
and the caption. Then it pre-screens all of it against our legal rulebook so the
legal review thread gets clean work.

Adapted from `ig-reel`, `ig-caption` and `ig-human` in
github.com/Jakeschincariol/instagram-agent-skill (MIT, (c) Jake Schincariol). Our
version drops the on-camera talking-head and keyword-funnel parts, because we are a
faceless comedy page built on footage and voiceover.

**This skill writes. It never publishes, schedules or uploads.** Creator threads use
it; the output goes to legal review; only a publisher thread schedules a Reel that
passed legal.

## Before writing

1. Read `voice.md`: `instagram/voice.md` in the laluzf/claude-videosgafos repo (or
   `/mnt/project-files/instagram/voice.md`). If neither is reachable, the essentials
   are in "Voice in one screen" below.
2. Read the flagged-posts log and legal review log in project memory, so you do not
   repeat something Federico disliked or legal sent back.
3. Check which language the slot is. Posts alternate EN and ES; about 40% of topics are
   Venezuelan-oriented.
4. If the idea touches a current event, check it is not a fresh tragedy, emergency or
   political fight. Weather jokes get a same-day check for a real advisory.

## Voice in one screen

- Faceless comedy. The joke is the gafo moment, never a real person.
- EN: deadpan, quick, meme-literate. ES: exagerado, cariñoso, de barrio, neutral Latin
  American with Venezuelan slang as a signature (gafo, chamo, pana, tupper, hallacas).
- Real free footage (PD, CC0, CC BY, NASA, commercial-use stock), light edits, Kokoro
  voices (ES `ef_dora`, `em_alex`; EN `am_michael`), in-house SFX. No cartoons.
- 10 to 30 seconds, hook in 2 seconds, burned-in subtitles.
- Caption: one hook line, one or two emoji, 3 to 5 specific hashtags, credit block.

## Hook shapes that fit us

Pick three different shapes for each idea, not three rewrites of one.

| # | shape | example |
| --- | --- | --- |
| 1 | **Family roles cast with footage** | "Mi familia llegando a la reunión." (goats, a cat, a sloth) |
| 2 | **Small thing explained by something huge** | "Latino goodbyes have their own countdown." (rocket launch) |
| 3 | **Absurd exaggeration** | "65°F en Miami = alerta roja." |
| 4 | **POV** | "POV: your tía just learned what a QR code is." |
| 5 | **Cuando...** | "Cuando tu mamá dice 'ahorita vengo'." |
| 6 | **Literal translation (Mr. Literal)** | "'Me estás tomando el pelo.' Sir, I have not touched your hair." |
| 7 | **The newcomer discovers (El Recién Llegado)** | "Day 1 in the US: why is the water free and the doctor $400?" |
| 8 | **Expert who is wrong (El Pana Experto)** | "Confía en mí, yo vi un video." over a confident fail |
| 9 | **The tía forwards it (La Tía Gafa)** | "¡Me llegó por WhatsApp!" (the video must show the claim is false) |
| 10 | **Mid-scene start** | "...y ahí fue cuando el abuelo sacó el efectivo." |
| 11 | **Head to head** | "Goodbye in the US: 4 seconds. Goodbye in my family: 3 hours." |
| 12 | **The question they answer about themselves** | "¿Cuál eres tú?" as the last line and the caption |

## The shape of a Reel

```
0:00-0:02   HOOK       spoken line + on-screen line, written separately. The first
                       frame moves. No greeting, no logo sting.
0:02-0:07   SETUP      who is who ("La tía...", "Mission control...")
0:07-...    BEATS      one joke per beat, and the clip changes every beat
LAST 3s     PAYOFF     the twist (reverse, freeze-frame, "Sí. Ese es tu primo.")
LAST LINE   THE ASK    a question people answer about themselves, echoing a word
                       from the hook so the loop lands
```

## The loop

1. **Three hooks.** Write the spoken line and the on-screen line (six words or fewer)
   for three different shapes. Say which you pick and why in one line.
2. **Script.** One voiceover line per beat, the way people actually talk, short.
   Contractions. Nothing Kokoro will mispronounce: spell out numbers ("ochenta y cinco
   grados"), avoid acronyms, put stress accents right.
3. **Time it.** Save the lines one per line and run
   `python3 -I .claude/skills/videosgafos-reel-copy/beats.py script.txt --lang es --target 25`
   (or `--lang en`). The rates are measured on our own Kokoro voiceovers (ES 185 wpm,
   EN 150). Fix every flag: hook past 3 s, a beat past 4 s, total past 30 s.
   No script runner available? Count words: ES about 3 words per second, EN about 2.5.
4. **Clip list.** For each beat, describe the footage to find ("goat staring straight
   at camera, close-up") and where to look first: Wikimedia Commons (CC0, CC BY),
   NASA Image and Video Library, Pexels, Pixabay, Mixkit. Never BY-SA, NC or ND. No
   people who could be recognized. No logos.
5. **On-screen text.** Separate list with timings. Six words or fewer per card, inside
   the safe zone (1080x1920: nothing above y=230, below y=1440, or in the right 230 px).
   Subtitles for every voiceover line. CC BY credit on screen on each shot.
6. **Caption.** See below.
7. **Humanize.** No em dashes, no "in today's video", no "stop scrolling", no
   "follow for more", no corporate words. Read every line out loud in your head.
8. **Pre-screen** with the checklist at the end, then hand everything to legal review.

## Caption

```
Line 1     the hook or the question, under 125 characters, in the video's language.
           Never a greeting, a hashtag or an emoji first.
(blank)
Hashtags   3 to 5 specific tags, never #viral #fyp #explorepage. Always #videosgafos.
(blank)
Credits    Videos: Author (CC0), Author (CC BY 3.0), via Wikimedia Commons. Editado por @videosgafos.
           Licencias: CC BY 3.0 https://creativecommons.org/licenses/by/3.0/ · CC0 https://creativecommons.org/publicdomain/zero/1.0/
           (NASA: "Footage: NASA (public domain). NASA does not endorse this video.")
```

- **One ask.** A question about themselves ("¿Cuál eres tú?", "How long does yours
  take?") or "mándaselo a tu primo / send this to your tía". Sends matter most.
- **No engagement bait:** never "comment YES", "like if", "tag 3 friends", "share if",
  "follow for more". Our rulebook bans it and Meta demotes it.
- **No links** except the license links in the credit block.
- **Search words** a person would type ("reunión familiar", "Latino goodbyes") go in
  line 1 as normal words.

Lint it:

```bash
python3 -I .claude/skills/videosgafos-reel-copy/caption.py caption.txt --needs-credit
```

It shows the 125 characters the feed shows before "... more", then checks length,
hashtags (3 to 5), one ask, engagement bait, emoji (2 max), the credit block (CC BY
license link, NASA disclaimer, no BY-SA/NC/ND) and a legal red-flag screen (nationality
next to animals, politics, tragedy words, @mentions). Fix every FAIL. Decide every WARN
out loud. A clean lint is a pre-screen, not a legal pass.

## Legal pre-screen (fill for every Reel)

- [ ] No real person named, shown, voiced or imitated. No celebrity, politician,
      creator or kid. Characters are not stand-ins for anyone real.
- [ ] No nationality or ethnicity paired with animal footage, anywhere (voice, screen,
      cover, caption, hashtags). Family roles instead.
- [ ] No punchline about race, religion, nationality, accent, disability, sexuality,
      gender identity or body. No country's accent mocked.
- [ ] Nothing that reads as a false fact about a real person, business or brand.
- [ ] No politics or sides, no fresh tragedy, no election/health/emergency
      misinformation. A tía's chain message is shown to be false.
- [ ] Every clip is PD, CC0, CC BY, NASA or commercial-use stock, with source URL and
      license logged in the post-sheet. No BY-SA, NC, ND, TV, movies, news, memes or
      other creators' clips.
- [ ] Audio: Kokoro voices, in-house SFX and music, or Meta Sound Collection. Original
      clip audio removed. No song, not even 5 seconds.
- [ ] No logos as a punchline; screens are invented designs.
- [ ] No engagement bait. AI info label ON (synthetic voice).
- [ ] Sponsored? Then "Paid partnership" + #ad/#publicidad, and Federico approved the deal.

## Output

Write to the Reel's folder `reels/rf-<date>-<slug>/post-sheet.md` (or the thread's
draft), in this order: the three hooks with the pick, the voiceover lines as JSON for
the builder (`[{"id":"a0","voice":"ef_dora","text":"...","lang":"es"}]`), the beat
sheet, the clip list, the on-screen text, the caption, the lint result, the filled
pre-screen. End with:

```
REEL COPY READY  (not legal-cleared)
language:   ES   ·  slot: Fri 8pm ET
hook:       #2 small thing explained by something huge
length:     ~24 s over 8 beats (beats.py, es 185 wpm)
caption:    lint REVIEW, 1 WARN decided (tag placement)
pre-screen: 10/10, next step: legal review thread
```

Never publish, schedule or upload. Never invent footage licenses: if a clip's license
is not confirmed from its source page, mark it `{{license?}}` and do not use it.
