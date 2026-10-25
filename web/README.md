# Malfoid Study

A quiet home for SC2001 through Week 13, SC2005 through Week 7, SC2203 Automata through Week 11, and interactive practice.

## Run

Requires Node.js 20 or newer. From this directory:

```sh
npm start
```

Open http://localhost:4173. No package installation is needed. To use another port, run `PORT=4174 npm start`.

## Included

- 138 complete video lessons: 49 for SC2001, 41 for SC2005 and 48 for SC2203, with a subject home page, contextual course navigation, search and topic filters.
- SC2005 includes the 34 core explanations, three worked clinics and four lab companions, with narration downloads and source notes. Open `http://localhost:4173/#/course/sc2005` directly.
- SC2203 includes all 48 reviewed Automata episodes, grouped by topic, with the original chapter timestamps, captions, transcripts, narration downloads and source notes. Open `http://localhost:4173/#/course/sc2203` directly. Coverage follows the supplied Weeks 1–11 materials; Weeks 12–13 materials were not supplied.
- SC2005 includes 160 interactive questions. SC2203 provides the existing exam-style bank with 176 MCQs and 44 open-ended questions; it has no scored interactive bank yet.
- Chapter seeking, full timestamped narration and English captions.
- 953 interactive questions: 793 for SC2001 and 160 for SC2005. The original 90 questions and IDs are retained.
- Per-topic and per-lesson quizzes with difficulty filters, answer feedback, scoring and missed-question retries.
- Playback resume, watched lessons and question progress saved in browser local storage.
- Question-specific input arrays/graphs, explicit trace conventions, worked feedback and course references. Baka combines longer traces and interacting operations.

Use the same browser and port to retain progress. Private browsing, blocked storage, clearing site data, or switching browsers can discard or separate it. The app indicates when storage is unavailable. Videos remain in their original workspace locations; this is a local app, not a portable video bundle. The server binds only to the local computer.

## Source layout

`public/app.mjs` owns routes and views. `public/quiz.mjs` owns quiz state, answer locking and scoring. `public/progress.mjs` owns browser-local progress and storage recovery. `public/data/catalog.json` is a generated content snapshot, not fetched from the temporary PDF authoring directory at runtime. `media-manifest.json` maps only the approved lesson videos, SC2005/SC2203 narration and source notes; the server does not expose the workspace as a directory.

`server.mjs` supports HTTP range requests so video seeking works. The public directory, listed videos, narration, source notes and the question-bank PDF are the only served files.

## Validation

```sh
npm test
npm run check
```

The HTTP checks open an ephemeral localhost port. `tests/browser.mjs` runs additional end-to-end scenarios and captures desktop/mobile screenshots. It currently uses the Codex bundled Playwright runtime and locally installed Chrome; adjust that import if running elsewhere.

Content regeneration (only needed when source lessons/questions change):

```sh
python3 scripts/prepare_content.py
```

The importer uses Pillow and FFmpeg/FFprobe, finds the latest complete local lesson masters, produces WebP previews and VTT captions, and imports the durable question bank from `content/question-bank.json`. The PDF link remains the original 90-question edition. Existing video/audio masters are never rewritten. Content import is separate from normal app startup.

`python3 scripts/expand_questions.py` reproduces the 300 added questions from frozen deterministic inputs, preserving the original 90 in `content/catalog-before-expansion.json`. It also writes calculation evidence to `content/answer-audit.json`. Review generated content before changing the published bank; retain IDs for progress compatibility. Quiz sessions are versioned so old three-question runs do not hide new questions.

## Vercel deployment

Production is [Malfoid Study](https://malfoid-study.vercel.app), in the `joel-0a4e` account. The published catalog includes SC2001, SC2005 and SC2203: 138 lessons and 953 interactive questions, plus the SC2203 exam-bank download. Open [SC2203 Automata](https://malfoid-study.vercel.app/#/course/sc2203) directly.

Vercel serves the static `dist/` build; videos and narration use the public `malfoid-lessons` Blob store. `content/hosting.json` selects the published courses and Blob origin. `npm run build` validates all media URLs and includes staged source notes and the question-bank PDF from `content/cloud-support/`. Environment files and credentials are excluded from the public output.

See [DEPLOYMENT.md](DEPLOYMENT.md) for the verified project IDs, publication scope and browser upload workflow. Browser progress remains local to each origin.
