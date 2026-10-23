# How does repeated squaring avoid enormous loops?

SC2203 E36.

## Source coverage

### E36. How does repeated squaring avoid enormous loops?

**T17 · 5–6 min · E35.** Animate exponent bits driving “square and optionally multiply” on a modular example, reducing after each operation. Reuse the pattern for a small permutation and Fibonacci modulo p via the 2×2 matrix. **Reasoning:** invariant for powers, O(log exponent) operations and bounded operand bits. **Takeaways:** count bit work; arbitrary integer matrix powers can have enormous entries. **Sources:** W9A pp10–12; Tutorial 8 Q4; IMG_2465/2468/2469. Do not claim bare arithmetic-operation count proves the photographed exact matrix problem in P.

Physical PDF pages and tutorial task IDs refer to `edit/sc2203/planning/SOURCES.md`; `source-inventory.json` records original file hashes and physical page counts. Coverage notes: `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, the topic IDs in the card. These are generated coverage notes, not independent original user notes. Relevant extracted page text and tutorial solutions were consulted in constructing the script and mathematical example.

Local SC2203 lecture recordings/transcripts and standalone personal notes were unavailable. No local lecture was claimed viewed, no lecture timestamps inferred from slides, and no lectures uploaded. Public Sipser lecture metadata provides supplementary topic alignment; no unreviewed recording timestamp is claimed. Weeks12–13 remain outside the supplied source set.

## Examples and verification

The narrated worked fixtures and their intermediate states are explicit in `story.json`; mathematical adaptations are authored teaching examples unless the card identifies an exact tutorial example. Source inconsistencies are resolved as documented in the planning source audit, especially input length, reduction direction, SAT auxiliary-variable freshness and Cook–Levin size/boundary conventions. The verification report records independent semantic checks and actual final-media checks; this source map alone is not a passed verification.

## Production provenance

Exact approved reference audio and text from `edit/series/voice-lock/voice-lock.json`, local Qwen3-TTS Base, locked seed721/temperature0.65, no fresh voice design. Raw per-beat speech and unprompted word ASR preserved. Main poses change at sentence boundaries every2–3 sentences, outlined captions are composited last, all speech clips retained with padded edges and ≥1second final hold.
