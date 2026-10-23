# How does a DFA decide whether to accept?

SC2203 E03.

## Source coverage

### E03. How does a DFA decide whether to accept?

**T02 · 4 min · E01.** Trace the course’s strings-ending-in-1 machine on ε, 101 and 10. Move one input cursor and one state token, including a path that visits an accept state before rejecting at the end. Reveal the five tuple components beside their graphical counterparts. **Reasoning:** final-state semantics and the memory invariant “the last symbol read is 1.” **Takeaways:** total transitions, ε, no early acceptance. **Sources:** L1 pp41–52; L2 pp5–7.

Physical PDF pages and tutorial task IDs refer to `edit/sc2203/planning/SOURCES.md`; `source-inventory.json` records original file hashes and physical page counts. Coverage notes: `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, the topic IDs in the card. These are generated coverage notes, not independent original user notes. Relevant extracted page text and tutorial solutions were consulted in constructing the script and mathematical example.

Local SC2203 lecture recordings/transcripts and standalone personal notes were unavailable. No local lecture was claimed viewed, no lecture timestamps inferred from slides, and no lectures uploaded. Public Sipser lecture metadata provides supplementary topic alignment; no unreviewed recording timestamp is claimed. Weeks12–13 remain outside the supplied source set.

## Examples and verification

The narrated worked fixtures and their intermediate states are explicit in `story.json`; mathematical adaptations are authored teaching examples unless the card identifies an exact tutorial example. Source inconsistencies are resolved as documented in the planning source audit, especially input length, reduction direction, SAT auxiliary-variable freshness and Cook–Levin size/boundary conventions. The verification report records independent semantic checks and actual final-media checks; this source map alone is not a passed verification.

## Production provenance

Exact approved reference audio and text from `edit/series/voice-lock/voice-lock.json`, local Qwen3-TTS Base, locked seed721/temperature0.65, no fresh voice design. Raw per-beat speech and unprompted word ASR preserved. Main poses change at sentence boundaries every2–3 sentences, outlined captions are composited last, all speech clips retained with padded edges and ≥1second final hold.
