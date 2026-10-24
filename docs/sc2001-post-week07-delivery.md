# SC2001 Weeks 8–13 delivery

Status: published and live-verified on24 October2026.

Website:https://malfoid-study.vercel.app/#/course/sc2001

Content release:`4daa38ece4dfcc919b4d5c88e289147afe029b6e` on GitHub main. Vercel deployment:`su6Mc21uPmhNxsW2HH6mhK938hLk`.

The user approved the detailed plan and the subsequent video → questions → website → GitHub stages. The approved source basis is supplied slides and study notes; matching later recordings were unavailable. Every new lesson source map records that limitation.

## Delivered content

- 31 complete lessons: A1–A7, G1–G3, D1–D7, S1–S6, N1–N8.
- 101.85 minutes of original narration, approved fixed-reference local Qwen voice, animated examples, complexity/proofs and final takeaways.
- 403 new questions: 13 per lesson, each with4 Easy,4 Medium,4 Hard,1 Baka, explicit context, one correct option, worked feedback and source references.
- SC2001 totals:49 lessons and793 questions. Existing SC2005 remains41 lessons and160 questions; local SC2203 remains48 lessons. Public deployment selects only SC2001 and SC2005.
- New topic IDs401–431 and question IDs551–953 preserve all550 old questions and their original IDs/bodies. The bank version changes to invalidate stale quiz-run layouts without deleting saved progress.

## Verification

All31 local masters passed current render provenance,1080×1920/30fps H264/AAC probing, complete decode, original PCM preservation, padded boundaries, final holds and2–3-sentence expression cadence. Encoded frames were inspected for diagrams, symbols, transitions and caption clearance, including additional rolling-hash and LCS-reversal motion samples.

Speech screening preserves unprompted local Base ASR and targeted independent Tiny ASR.41 low-score cases were explicitly reviewed for technical vocabulary, variables, digit grouping and phonetic boundaries; unclear operations were reworded and regenerated. This is not a claim of full human listening. Per-lesson raw evidence remains beside the local masters.

Mathematics checks include exhaustive LCS subsequence and knapsack subset comparisons, all9841 WOX texts of lengths0–8 for the Boyer–Moore convention, parity formulas, coin minima, fractional LP vertices, TSP traces, legal Hanoi moves and all64 four-vertex HP→TSP reduction instances.

The question-bank audit independently derives93 numerical answers and checks all64 reduction graphs, IDs, balanced counts and distinct choices. Conceptual answers/distractors were reviewed against the lesson assumptions. Rebuild and validate with:

```sh
rtk proxy python3 content/sc2001-later-authoring/build.py
rtk proxy python3 content/sc2001-later-authoring/validate.py
```

All16 website checks pass, including legacy question-body hashes and HTTP media access. The local browser verified49 SC2001 cards, LCS playback and chapter seeking, new-question feedback/locking and restoration after refresh. The390px question layout has no horizontal overflow.

The62 new720×1280 MP4/MP3 streaming files total182,265,615 bytes and were uploaded to the existing malfoid-lessons Blob store. Every remote file was read back and matched by SHA256; all31 video range checks returned206. Original masters and lecture materials remain outside Git. The build produces90 public lessons and953 questions across264 static files.

## Reusable pipeline

Installed skill: `/Users/joelloh/.codex/skills/malfoid-course-pipeline/`. A versioned copy is under `docs/skills/malfoid-course-pipeline/`. It preserves the analysis approval gate, ordered production stages, source-gap handling, media verification, stable IDs and explicit hosting/GitHub distinctions.

The repository engineering-skill setup uses the user-approved GitHub Issues tracker, default triage labels, single-context domain-document rules and root AGENTS.md.

All31 Baka items were strengthened to longer transfer/trace challenges after independent spec review; their IDs are unchanged. Both review axes have no remaining findings. See `docs/sc2001-post-week07-review.md`.

Live verification confirmed90 public lessons,953 questions and byte-for-byte matches for all263 served static resources. The production browser confirmed49 SC2001 lessons/793 questions,new hosted playback/chapter seeking,and the final longer Baka challenge.
