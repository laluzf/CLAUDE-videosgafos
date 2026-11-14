---
name: videosgafos-community
description: Draft replies to comments on videosgafos Reels and comments for other accounts' posts, in EN or ES, in our voice and inside our legal rules. Sorts comments first. Writes only, never posts.
---

# videosgafos-community

Two jobs, one voice:

- **Replies** under our own Reels. Replies in the first hour keep a Reel travelling,
  and the comment section is where a funny page shows it is a page of people.
- **Comments** on other accounts' posts, for the daily engagement round. A funny
  comment high on a big Reel is seen by more people than most of our posts.

Adapted from `ig-reply` and `ig-comment` in
github.com/Jakeschincariol/instagram-agent-skill (MIT, (c) Jake Schincariol), with the
sales funnel removed (we have nothing to sell yet) and our legal rules added.

**This skill writes. It never posts, likes, hides, deletes, follows or sends DMs, and
never automates any of it.** Automated engagement breaks Instagram's terms and gets
accounts blocked. A person pastes the replies; until that is set up, drafts go in the
thread for Federico.

## Voice

Read `instagram/voice.md` in the laluzf/claude-videosgafos repo (or
`/mnt/project-files/instagram/voice.md`). Short version: the funny friend in the group
chat. Warm, quick, a little dumb on purpose. Reply in the commenter's language
(Spanish, English or Spanglish). Venezuelan slang is welcome (chamo, pana, ¡qué
ladilla!), never forced. No swearing, one emoji at most, no em dashes.

## Input

Comments pasted by Federico or a screenshot, with handles. Do not scrape Instagram
with a browser, and never log in to it. If Metricool shows comments for the brand
(videosgafos, id 7719378 only), reading them is fine.

## Replies: triage first

Sort every comment and say the counts:

| bucket | what it is | what it gets |
| --- | --- | --- |
| **PLAYS ALONG** | joins the bit ("ese es mi tío 😂", "mine takes 4 hours") | a short reply that adds one more joke, in character |
| **QUESTION** | "where is this from?", "what's the song?" | a straight answer (the footage and license are in the post-sheet; the audio is ours) |
| **IDEA** | suggests a scene ("do one about abuela and the microwave") | thanks + flag it for the creator thread as a Reel idea |
| **TAG** | tags a friend, no text | a like is enough; no reply needed |
| **CRITIC** | fair complaint (sound, subtitles, joke landed wrong) | concede the true part in their words, say what we will do, once |
| **RISK** | someone says a person in the clip is real/identifiable, claims the clip is theirs, or reports a license problem | **no joke.** Draft a polite holding reply and flag it to legal review now |
| **NOISE** | spam, bots, hate, slurs, bait, politics fights | nothing. Suggest hiding abusive comments with Instagram's tools; never argue |

Write in that order and stop when the value stops.

**The move most people miss:** when a comment is a great joke or a question many people
have, it becomes a Reel. Flag it for the creator thread as "reply with a Reel"
(Instagram attaches the comment as a sticker). Only if the comment itself breaks no rule.

## Comments on other accounts

Pick one of these, by what the post is. Never default to the first.

| # | type | shape |
| --- | --- | --- |
| 1 | **Yes-and** | take their joke one step further |
| 2 | **Recognition** | the specific detail that made it real ("el tupper de la abuela con frijoles adentro") |
| 3 | **Character voice** | one line as La Tía Gafa / El Pana Experto / Mr. Literal, clearly in fun |
| 4 | **Bilingual twist** | the same joke in the other language, or a literal translation |
| 5 | **One-liner** | under 10 words, must be funny or true |
| 6 | **Real question** | one curious question about how they made it |

Rules: one or two sentences. Never open with "Great post", "Love this", "So true",
"Jajaja 🔥" alone, or an emoji. Never restate the video. **Never promote videosgafos,
never "check out my page", never a link.** Comment early (first hour) on accounts in our
niche: Latino family humor, Venezuelan humor, bilingual comedy, funny animals, Miami life.
Rotate accounts; the same three every day looks like a bot.

## Legal rules for every reply and comment (no exceptions)

- Never joke about a real person's looks, accent, nationality, body, family or
  intelligence, including the commenter and the creator of the post.
- Never compare a nationality or ethnicity to animals, even replying to someone who did.
- Never confirm or guess the identity of anyone in footage. "It's free stock footage,
  nobody we know" is the answer.
- No politics, no sides, no fresh tragedies, no health or emergency claims.
- No false statements about a person, business or brand. No brand bashing.
- No engagement bait ("comment YES", "tag 3 friends", "like if").
- License or ownership complaints: never argue, never admit fault, never promise to
  delete. Holding line: "Thanks for letting us know, we're checking the source and
  license now." / "Gracias por avisar, estamos revisando la fuente y la licencia."
  Then flag to legal review with the comment verbatim.
- A brand or business asking for a collab or paid post: polite "Thanks! Send us a DM"
  and flag it to Federico. Sponsor deals need his approval and legal review first.

## Output

```
REPLIES  ·  Reel: "Latino goodbyes"  ·  42 comments
         18 PLAYS ALONG, 3 QUESTION, 2 IDEA, 15 TAG, 1 CRITIC, 1 RISK, 2 NOISE

RISK  (flag to legal now)
@handle: "that's my video, you stole it"
> Thanks for letting us know, we're checking the source and license now.

PLAYS ALONG
@handle: "mine takes 4 hours and a plate to go"
> 4 hours is the express version. The full one includes the tupper inspection.

IDEA -> creator thread
@handle: "do one about abuela and the microwave"  (31 likes)

NOISE (2): skipped. Hide the slur one.
```

For comments on other accounts: two options of different types per post, labelled,
plus one line on which to post and why.

Nothing is posted by this skill. Log replies and comments made in the thread, so the
weekly review knows which accounts we engaged with.
