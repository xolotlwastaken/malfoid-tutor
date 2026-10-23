# Why is P closed under Kleene star?

SC2203 E38.

## Source coverage

### E38. Why is P closed under Kleene star?

**T17 · 5–6 min · E08, E35.** First fail greedy parsing on L={0,01,11}, w=011. Animate prefix DP, highlighting each split and membership-subroutine call. **Reasoning:** inductive iff for D[j]; at most n(n+1)/2 calls; include copy/reset cost to derive O(n^(c+2)) for c≥1. **Takeaways:** ε, discard empty factors, polynomial DP instead of 2^(n−1) partitions. **Sources:** Tutorial 7 Q5 (worked solutions in “Problems” file pp4–6); Tutorial 8 Q5; W9A pp13–14.

Physical PDF pages and tutorial task IDs refer to `edit/sc2203/planning/SOURCES.md`; `source-inventory.json` records original file hashes and physical page counts. Coverage notes: `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, the topic IDs in the card. These are generated coverage notes, not independent original user notes. Relevant extracted page text and tutorial solutions were consulted in constructing the script and mathematical example.

Local SC2203 lecture recordings/transcripts and standalone personal notes were unavailable. No local lecture was claimed viewed, no lecture timestamps inferred from slides, and no lectures uploaded. Public Sipser lecture metadata provides supplementary topic alignment; no unreviewed recording timestamp is claimed. Weeks12–13 remain outside the supplied source set.

## Examples and verification

The narrated worked fixtures and their intermediate states are explicit in `story.json`; mathematical adaptations are authored teaching examples unless the card identifies an exact tutorial example. Source inconsistencies are resolved as documented in the planning source audit, especially input length, reduction direction, SAT auxiliary-variable freshness and Cook–Levin size/boundary conventions. The verification report records independent semantic checks and actual final-media checks; this source map alone is not a passed verification.

## Production provenance

Exact approved reference audio and text from `edit/series/voice-lock/voice-lock.json`, local Qwen3-TTS Base, locked seed721/temperature0.65, no fresh voice design. Raw per-beat speech and unprompted word ASR preserved. Main poses change at sentence boundaries every2–3 sentences, outlined captions are composited last, all speech clips retained with padded edges and ≥1second final hold.
