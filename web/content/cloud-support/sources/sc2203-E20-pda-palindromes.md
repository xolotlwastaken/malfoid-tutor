# How does a PDA guess the middle of a palindrome?

SC2203 E20.

## Source coverage

### E20. How does a PDA guess the middle of a palindrome?

**T10 · 4–5 min · E19.** Trace even 0110 and odd 010 with branches guessing different midpoints. The even branch switches without consuming; the odd branch consumes the central symbol. Then specialize to odd-length middle-0 words where paired symbols need not match. **Reasoning:** stack reversal and existential acceptance. **Takeaways:** ww^R differs from ww; wrong guesses may die; DPDA and NPDA power differs. **Sources:** L5 pp45,52; Tutorial 4 Q3(b/c). Validate both parity cases and ε.

Physical PDF pages and tutorial task IDs refer to `edit/sc2203/planning/SOURCES.md`; `source-inventory.json` records original file hashes and physical page counts. Coverage notes: `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, the topic IDs in the card. These are generated coverage notes, not independent original user notes. Relevant extracted page text and tutorial solutions were consulted in constructing the script and mathematical example.

Local SC2203 lecture recordings/transcripts and standalone personal notes were unavailable. No local lecture was claimed viewed, no lecture timestamps inferred from slides, and no lectures uploaded. Public Sipser lecture metadata provides supplementary topic alignment; no unreviewed recording timestamp is claimed. Weeks12–13 remain outside the supplied source set.

## Examples and verification

The narrated worked fixtures and their intermediate states are explicit in `story.json`; mathematical adaptations are authored teaching examples unless the card identifies an exact tutorial example. Source inconsistencies are resolved as documented in the planning source audit, especially input length, reduction direction, SAT auxiliary-variable freshness and Cook–Levin size/boundary conventions. The verification report records independent semantic checks and actual final-media checks; this source map alone is not a passed verification.

## Production provenance

Exact approved reference audio and text from `edit/series/voice-lock/voice-lock.json`, local Qwen3-TTS Base, locked seed721/temperature0.65, no fresh voice design. Raw per-beat speech and unprompted word ASR preserved. Main poses change at sentence boundaries every2–3 sentences, outlined captions are composited last, all speech clips retained with padded edges and ≥1second final hold.

Stack-label visual revision: reproduce with `edit/sc2203/batch/render_stack_revision.py E20`; its source hash is recorded in render-provenance.json. Narration is reused unchanged.
