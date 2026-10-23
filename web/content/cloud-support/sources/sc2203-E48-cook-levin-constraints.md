# How do Cook–Levin constraints prevent a fake computation?

SC2203 E48.

## Source coverage

### E48. How do Cook–Levin constraints prevent a fake computation?

**T22 · 6–8 min · E47.** Take a valid two-row tableau and introduce errors: two heads, wrong start, remote cell changing, invalid instruction, never accepting. Add the clause group ruling each out. Show exactly-one expansion and derive a safe polynomial size bound for the actual pairwise encoding. **Reasoning:** all eight groups, time 0…T vs steps 0…T−1, boundary and halt padding, reconstruction in both directions. **Takeaways:** preserve overbars; pairwise head clauses can be Θ(T³), so do not repeat the deck’s unqualified O(T²) claim. **Sources:** W11-CL pp8–21; source audit corrections. E47 is a complete overview; this is a complete detailed encoding lesson.

Physical PDF pages and tutorial task IDs refer to `edit/sc2203/planning/SOURCES.md`; `source-inventory.json` records original file hashes and physical page counts. Coverage notes: `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, the topic IDs in the card. These are generated coverage notes, not independent original user notes. Relevant extracted page text and tutorial solutions were consulted in constructing the script and mathematical example.

Local SC2203 lecture recordings/transcripts and standalone personal notes were unavailable. No local lecture was claimed viewed, no lecture timestamps inferred from slides, and no lectures uploaded. Public Sipser lecture metadata provides supplementary topic alignment; no unreviewed recording timestamp is claimed. Weeks12–13 remain outside the supplied source set.

## Examples and verification

The narrated worked fixtures and their intermediate states are explicit in `story.json`; mathematical adaptations are authored teaching examples unless the card identifies an exact tutorial example. Source inconsistencies are resolved as documented in the planning source audit, especially input length, reduction direction, SAT auxiliary-variable freshness and Cook–Levin size/boundary conventions. The verification report records independent semantic checks and actual final-media checks; this source map alone is not a passed verification.

## Production provenance

Exact approved reference audio and text from `edit/series/voice-lock/voice-lock.json`, local Qwen3-TTS Base, locked seed721/temperature0.65, no fresh voice design. Raw per-beat speech and unprompted word ASR preserved. Main poses change at sentence boundaries every2–3 sentences, outlined captions are composited last, all speech clips retained with padded edges and ≥1second final hold.
