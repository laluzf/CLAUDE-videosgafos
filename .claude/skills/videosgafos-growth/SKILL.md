---
name: videosgafos-growth
description: Growth work for videosgafos: audit past Reels from Metricool, research what is going viral in our niche, plan the posting week, and score the Instagram profile. Analyses and writes only, never publishes.
---

# videosgafos-growth

Four modes that turn evidence into next week's Reels. Pick the one asked for; on a
weekly review run them in this order: **audit, research (monthly), plan**. Run profile
once a month or when follows per reach is low.

Adapted from `ig-audit`, `ig-viral`, `ig-plan` and `ig-profile` in
github.com/Jakeschincariol/instagram-agent-skill (MIT, (c) Jake Schincariol), rebuilt
for a faceless bilingual comedy page made from free footage, with Metricool as the data
source.

**This skill reads and writes plans. It never publishes, schedules, comments, likes,
follows or sends DMs.** Scheduling belongs to the publisher thread, and only for items
with a legal pass.

Read `instagram/voice.md` (laluzf/claude-videosgafos repo, or
`/mnt/project-files/instagram/voice.md`) and the flagged-posts log in project memory
first.

The goal is a **profitable page**. Judge every Reel by **sends (shares), saves and
follows per reach**, not likes or raw views. A Reel with 900 views and 40 sends beat one
with 9,000 views and 2.

---

## Mode 1: audit (what already worked)

**Data.** Metricool, brand **videosgafos, id 7719378 only** (never rentalnumbersmedia or
Miami Desde Mi Ventana). Call `getAnalyticsDataByMetrics` with:

| field | metric |
| --- | --- |
| IGRE01 | date |
| IGRE03 | caption |
| IGRE06 | Reel URL |
| IGRE23 | views |
| IGRE11 | reach |
| IGRE21 | shares (sends) |
| IGRE12 | saves |
| IGRE07, IGRE10 | comments, likes |
| IGRE24 | average watch time (s) |
| IGRE27 | retention (% of video watched) |
| IGRE30 | skip rate (left in the first 3 s) |
| IGRE28 | 3-second view rate |

Follower growth: `getAnalyticsAvailableMetrics` with network `instagram`, connector
`evolution`, to find the follower field. YouTube Shorts: network `youtube`. If a field
is reported deprecated, use the suggested alternative.

**Compute and show the working:**

| metric | how | tells you |
| --- | --- | --- |
| outlier multiple | views / our median views | a real hit or a normal day |
| hold at 3 s | 100 - skip rate | **the hook's grade** |
| watch share | avg watch time / Reel length | whether the middle worked |
| sends per 1k reach | shares / reach x 1000 | the strongest signal; people put their name on it |
| saves per 1k reach | saves / reach x 1000 | rewatch value |
| follows per 1k reach | follows / reach x 1000 | whether the profile converts |

Reel length is in the post-sheet (`reels/<folder>/post-sheet.md`).

**Then find the pattern,** top vs bottom, in this order: hold at 3 s, hook shape (from
the reel-copy skill's hook table), language (EN/ES), topic (family, Miami, bilingual,
current event), footage type (animals, rockets, objects), length, whether we replied to
comments in the first hour. **Day and time last**; it is almost never the cause.

**The split that saves months:** no views = hook problem (fix the first 2 s and the
first frame). Views but no follows = profile problem (go to Mode 4). Views but no sends =
the joke is not relatable or specific enough to forward.

**Be honest about sample size.** With 3 Reels you cannot see a pattern, say so, and
give the one or two things the numbers do show.

```
AUDIT  ·  3 Reels  ·  Nov 2-14  ·  median 155 views
         views reach sends saves hold@3s watch  sends/1k
familia    159   150     0     1    45%   6.0s/24s   0
NASA       153   131     0     0    49%   6.1s/28s   0
frente     155   128     0     0    51%   6.6s/23s   0

WHAT THE DATA SAYS (n=3, low confidence)
1. Half the viewers leave in the first 3 s. The hook is the job.
2. People watch about a quarter of each Reel. Shorter, faster beats.
3. Zero sends. Nothing yet is "I have to send this to my tía".
```

---

## Mode 2: research (what is going viral in our niche)

Run monthly. Formats last a season.

**Raw views are not evidence.** Rank on the **outlier multiple**: a Reel's views divided
by that account's own median of its last 12 Reels. Above 3x is a signal; under 1.5x is a
normal day. Prefer accounts within about 10x of our size.

**Pick 8 to 12 accounts** and write them down with why:

- 4 direct: Latino family humor, Venezuelan humor, bilingual comedy.
- 4 adjacent: funny animals, Miami life, "explained by" edits, faceless meme pages built
  on footage.
- 2 to 4 big ones, for format only.

**How to look:** whatever browser tool the session has, or YouTube Shorts (public view
counts, no login). Rules that are not negotiable:

- **Never log in to Instagram on anyone's behalf and never ask for a password.**
- **Read, do not scrape.** A dozen Reels per account at human speed. No crawler, no
  scraping service, nothing running in the background.
- **Copy the formula, never the video.** Hook shape, structure, length, cut rhythm.
  Never their script, jokes, characters, catchphrases, footage or audio. Attribute each
  row to its account.
- **Never study a real person to imitate them.** A creator's face, voice or persona is
  off limits.

Capture per Reel: account, followers, median, views, first line (spoken or on screen,
verbatim), first frame, length, footage type, ask at the end.

**Report three things only:** which hook shapes over-index in the top third (with
counts), what the top third share structurally (hook length, first-frame motion, payoff
position, length), and hooks that fit no known shape (read those by hand; new formats
live there). State sample size and confidence. Forty Reels across six accounts supports
a claim; twelve does not.

**Then write our version** of the top three shapes: a hook line in our voice, on a topic
from our audience, ready for the reel-copy skill. Never "make one like this".

Save the swipe file to `instagram/swipe.md` in the repo (or
`/mnt/project-files/instagram/swipe.md`).

---

## Mode 3: plan (the posting week)

Read `swipe.md`, the last audit, the flagged-posts log, and the Reels of the last two
weeks (no repeated topic or footage within a fortnight).

**Rhythm:** 3 Reels a week, Mon / Wed / Fri, America/New_York, alternating EN and ES,
about 40% of topics Venezuelan-oriented. Raise the count only when the audit shows
sends and follows growing. Cross-post each legally passed Reel as a YouTube Short.

| slot | default | week A | week B |
| --- | --- | --- | --- |
| Mon 7-9 pm | character or family bit | ES, Venezuelan | EN |
| Wed 12-1 pm | POV / relatable | EN | ES, Venezuelan |
| Fri 7-9 pm | current-event or bilingual bit | ES, US Latino | EN/ES bilingual |

Use `getBestTimeToPostByNetwork` (brand 7719378, instagram) once there is enough data,
but say it plainly: **the first 2 seconds matter far more than the hour.**

For each slot give: language, angle (not a topic: "Miami at 65°F as a national
emergency", not "weather"), hook shape number, footage idea and likely source, and a
current-event check (no fresh tragedy, no politics, weather advisory check on the day).

**Daily engagement round** (20 minutes, a person does it): 5 big accounts in our niche to
comment on early, 3 peers our size, 2 Latino businesses in Miami (future sponsors:
comment for weeks, never pitch). Hand the list to the community skill.

```
WEEK OF NOV 16  (week B)
MON 8pm   REEL  EN   #2 small thing / huge thing   "Thanksgiving leftovers, explained by NASA cargo loading"
WED 12:30 REEL  ES   #5 Cuando...                  "Cuando tu mamá dice 'ahorita vengo'" (sloth footage)
FRI 8pm   REEL  EN/ES #6 literal translation        Mr. Literal vs "me estás tomando el pelo"
ENGAGE    5 reach / 3 peers / 2 Miami businesses
NEXT      creator thread writes Mon; legal; publisher schedules after a pass
```

Write it to `instagram/plan.md`. Nothing is scheduled by this skill.

---

## Mode 4: profile score (out of 100)

The profile is a decision screen reached from one Reel: in three seconds, is there more
of that here, and is it for me. Get the profile from a screenshot or from Federico; do
not log in.

| item | pts | full marks for videosgafos |
| --- | --- | --- |
| name field (30 chars) | 12 | searchable words, both languages: "Videos Gafos \| humor latino" or "Videos Gafos \| funny videos" |
| bio line 1 | 12 | who it is for and the promise: "Videos gafos para reír en español e inglés 😂" |
| bio rest | 8 | posting rhythm or a hook ("Nuevo video lun/mié/vie"), no keyword soup |
| pinned three | 10 | three jobs: best laugh in ES, best in EN, the one that explains the page |
| link | 6 | none until there is something to send people to (YouTube channel is fine) |
| highlights | 6 | 0 is fine early; later "Familia", "Miami", "Bilingual", "Personajes" |
| grid covers | 10 | readable at thumbnail size, 3 to 4 words each, consistent style |
| avatar | 6 | the VG mark, readable at 40 px, same as YouTube |
| handle | 6 | @videosgafos everywhere |
| category and contact | 6 | Creator or Media account, category Comedian or Entertainment, working email |
| recent activity | 12 | a Reel in the last 7 days and replies on the latest post |
| stories | 6 | a story on posting days (repost the Reel with a poll sticker) |

Score honestly (most first passes land in the 30s and 40s), show the table, then rewrite
in order of points lost, three options for the name field and bio, each copy-ready.
Re-score and show the real delta. Nothing is changed on Instagram by this skill; Federico
edits the fields.

---

## Hand-offs

- Audit and research conclusions go to the plan.
- Plan slots go to the creator thread (reel-copy skill), then legal review, then the
  publisher thread.
- Profile rewrites go to Federico (only he can edit the profile).
- Revenue milestones (5k, 10k, 50k followers; YouTube 1,000 subs) go in the weekly
  review with the next revenue step from voice.md. Paid tools and sponsor deals go to
  Federico first.
