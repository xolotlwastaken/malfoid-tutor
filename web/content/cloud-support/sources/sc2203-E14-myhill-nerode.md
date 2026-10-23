# How does Myhill–Nerode measure the memory a DFA needs?

SC2203 E14.

## Source coverage

### E14. How does Myhill–Nerode measure the memory a DFA needs?

**T07 · 5 min · E02, E04.** Place prefixes 0⁰,0¹,0²,… into candidate memory boxes. For an arbitrary distinct pair, append 1^n and make exactly one word enter {0^r1^r}. Then use a small finite language example to show matching upper/lower state bounds. **Reasoning:** same DFA state would force the same verdict for every suffix. **Takeaways:** one suffix per pair is allowed; an infinite distinguishable set proves nonregularity. **Sources:** L4 pp30–35; Tutorial 3 Q3 definitions.

Physical PDF pages and tutorial task IDs refer to `edit/sc2203/planning/SOURCES.md`; `source-inventory.json` records original file hashes and physical page counts. Coverage notes: `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, the topic IDs in the card. These are generated coverage notes, not independent original user notes. Relevant extracted page text and tutorial solutions were consulted in constructing the script and mathematical example.

Local SC2203 lecture recordings/transcripts and standalone personal notes were unavailable. No local lecture was claimed viewed, no lecture timestamps inferred from slides, and no lectures uploaded. Public Sipser lecture metadata provides supplementary topic alignment; no unreviewed recording timestamp is claimed. Weeks12–13 remain outside the supplied source set.

## Examples and verification

The narrated worked fixtures and their intermediate states are explicit in `story.json`; mathematical adaptations are authored teaching examples unless the card identifies an exact tutorial example. Source inconsistencies are resolved as documented in the planning source audit, especially input length, reduction direction, SAT auxiliary-variable freshness and Cook–Levin size/boundary conventions. The verification report records independent semantic checks and actual final-media checks; this source map alone is not a passed verification.

## Production provenance

Exact approved reference audio and text from `edit/series/voice-lock/voice-lock.json`, local Qwen3-TTS Base, locked seed721/temperature0.65, no fresh voice design. Raw per-beat speech and unprompted word ASR preserved. Main poses change at sentence boundaries every2–3 sentences, outlined captions are composited last, all speech clips retained with padded edges and ≥1second final hold.
