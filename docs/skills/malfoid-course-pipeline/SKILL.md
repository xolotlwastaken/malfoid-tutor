---
name: malfoid-course-pipeline
description: Extend WaifuTutor course coverage through source analysis, approved topic breakdowns, Malfoid explainer videos, verified question banks, website integration and a requested GitHub push. Use for coordinated course or multi-topic expansions; use malfoid-explainer directly for a standalone video.
---

# Malfoid course pipeline

Project: `/Users/joelloh/Documents/Code/WaifuTutor`. Read the current user's scope and repository instructions before acting. The pipeline order is **analysis → videos → question bank → website → GitHub**. A request to do only analysis ends at a concrete breakdown for approval. Do not render sample narration, create questions, run content importers or push while that gate is closed. Later user approval carries forward the actions already authorized; do not add routine confirmation gates.

## 1. Discover and analyse

- Inspect source files, study notes/source ledgers, recording/transcript caches, current complete lesson masters and website catalog. Treat existing READMEs as leads; verify current content and paths. Discover actual week/topic scope from the supplied course schedule, not chapter filename prefixes.
- Use slides for course conventions, notes for coverage, recordings for lecturer examples/explanations. Reuse valid local transcripts. Verify physical PDF pages and inspect diagrams whose spatial layout affects correctness. Do not upload lecture material. If a source type is missing, identify the precise gap and obtain an explicit decision before producing lessons that require it; approval of a plan which clearly accepts the gap is sufficient.
- Produce a durable Markdown plan with: source inventory/evidence limits; existing coverage and prerequisites; ordered lessons grouped by topic/week; per-lesson source pages/note sections/genuine recording ranges or gap; objective; teaching sequence; concrete animated example; derivation/proof; assumptions and common mistakes; estimated duration; proposed assessment skills. Separate core, review and explicitly excluded material.
- Independently check proposed traces and mathematical claims. Resolve source errors mathematically and record corrections; distinguish explanatory additions from literal source content. Do not invent transcript timestamps, lecture claims, exam promises or exact production durations.
- Propose a question-bank distribution by actual topic granularity, following the current bank's conventions when appropriate. At analysis stage, describe assessed skills and counts without authoring the bank.
- Save a status record identifying the approval boundary, completed artifacts and next permitted stage. The SC2001 precedent is `docs/sc2001-post-week07-plan.md` if present, with evidence under `edit/planning/sc2001-post-week07/`. Recheck it before using its counts or missing-source assumptions for another request.

## 2. Produce and verify videos

After the applicable approval, read and apply `/Users/joelloh/.codex/skills/malfoid-explainer/SKILL.md` and its applicable references. The project copy is `skills/malfoid-explainer/` if the installed path is unavailable. If neither is present, locate it or report the dependency; do not silently replace the accepted production format.

Use complete lessons: named topic → mechanism with actual animated operations → complexity/correctness → “Things to take note of.” Let topic complexity determine length. Reuse accepted production helpers under `edit/revisions/insertion-sort/` and `merge-sort/`, adapting every topic-dependent verifier, renderer and publisher. Keep sources and previous finished revisions intact.

Use the exact live `edit/series/voice-lock/voice-lock.json` audio/transcript/hash with local Qwen3-TTS Base. No ElevenLabs, new VoiceDesign speaker or generic substitute. Retain narration beats, padded word-aligned audio, raw ASR, captions, expression schedule and source map. The main Malfoid pose changes at sentence boundaries every 2–3 spoken sentences. Verify encoded final video, narration-to-motion timing, maths glyphs, trace/counters, base/tie cases, full decode and voice provenance before marking a lesson finished. Preserve recording gaps explicitly in source maps.

## 3. Create and validate questions

Create the bank after the approved lessons are verified. Use the approved distribution; SC2001 currently uses Easy/Medium/Hard/Baka. Avoid quota-filling duplicates. Each item needs self-contained inputs, indexing/tie rules, distinct options with one correct answer, worked reasoning, source pages and a stable lesson/topic association. Do not fabricate media chapter times.

Independently derive numeric/trace answers and check distractors for ambiguity or accidental correctness. Check reductions in both directions and explicit algorithm variants. Preserve existing question/topic IDs and allocate new IDs against the actual current bank across relevant courses; counts are not IDs. Use meaningful answer-validation evidence rather than comparing an answer to itself.

## 4. Integrate into the website

For source changes, read the relevant installed Matt Pocock skills selected by current repository instructions: `codebase-design` for implementation, `tdd` for behaviour needing tests, `code-review` before substantive changes are complete, and other workflows only where applicable. Read their required references. Check `docs/agents/`; use `setup-matt-pocock-skills` if a selected workflow requires configuration that is missing.

Inspect `web/scripts/prepare_content.py`, durable banks, generated catalog, media manifest and hosting configuration before editing. Existing import logic may hardcode earlier week ranges, lesson lists, source defaults or topic indices. Extend it deliberately; missing recording metadata must stay missing. Add captions, transcripts, source notes, narration downloads and real chapter boundaries where the existing course supports them. Preserve other courses and browser progress IDs; update bank version when needed.

Verify content links, lesson-topic mapping, quiz answer locking/feedback, progress compatibility and playback/captions. Run appropriate existing tests/checks/build and focused browser checks; report what actually passed. Do not publish a lesson whose media is absent from the intended environment.

## 5. Push when authorized

Inspect current Git status, branch, remote and deployment triggers. Preserve unrelated changes. Stage only intended files; never use blanket staging over an unknown working tree. Review substantive code changes with the selected workflow before committing/pushing. Push only within the user's authorized scope and report the commit/branch/result; attach any PR actually created with the app's artifact tool.

WaifuTutor ignores `/edit/`, `/output/`, `/tmp/`, `/study-notes/` and `/skills/`: a Git push does not distribute local video masters. Inspect `web/DEPLOYMENT.md` and current hosted-media configuration when that matters. Follow the established authorized media workflow; keep recordings/models/secrets out of Git and public bundles. Do not force-add ignored masters to make a push appear complete. Do not silently expand a GitHub request to a new hosting provider, public lecture upload or social post.

## Handoff

Maintain a small durable stage record with approvals, evidence/artifact paths, finished and pending lesson IDs, validation results and publication state. Distinguish local rendering, local website import, GitHub push and hosted availability. If stopped at analysis, link the reviewable plan and state the next stage; do not claim downstream work is complete.
