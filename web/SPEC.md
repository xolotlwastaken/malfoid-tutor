# Malfoid Study — implementation scope

Source: the user's request to create a simple, minimal, Apple-like web app organising their long-form Malfoy/Malfoid explanations and interactive MCQ quizzes for each topic.

- Organise the 18 existing complete lessons from SC2001 Weeks 1-7; preserve original media files.
- Include the original 90 PDF questions plus 300 new questions across all 30 topics: four Easy, four Medium, four Hard and one extremely difficult Baka per topic (390 total). New questions use their own concrete input arrays/graphs and explicit setups; preserve original IDs and answered progress. Add Baka last in the difficulty selector. The linked original PDF remains the original 90-question edition.
- Offer library search and topic filters, an actual video player, chapter navigation, timestamped narration, and captions.
- Provide lesson-linked and individual topic quizzes, original graph inputs and trace conventions, selected-answer checking, answer locking, worked explanations, accurate scores, and retry of missed questions.
- Persist answers, quiz state and playback progress in this browser. Do not promise cross-device sync. Keep the app usable if storage is unavailable.
- Responsive, keyboard-usable interface with clearly visible focus, reduced-motion support, accessible controls and restrained design.
- Use the user-approved recommendation: plain HTML/CSS/JavaScript and a local Node server; no account or deployment is requested.
- Validate the user-approved public actions (locking, scoring, retry, persistence) and the browser's navigation and playback.

This folder began without Git history. The comparison baseline for review is the pre-existing content collection: every file under web/ is new; PRODUCT.md is new; original edit/, study-notes/ and PDF files are not modified.

## SC2005 integration — 22 October 2026

Source: “now that you have the videos, add them to the web app”.

- Import all 41 published SC2005 videos through Week 7 in manifest order, preserving the masters.
- Provide a separate SC2005 course library with topic filters and search, captions, actual spoken-beat chapter timestamps, transcripts, narration downloads and original source notes.
- Support direct course/lesson URLs, next lesson navigation, watched state and playback resume. Reset course-specific filters when changing course from any route.
- Retain the original 18 SC2001 lesson identities and all 390 questions unchanged; preserve the existing browser storage keys. Progress counts all 59 lessons.
- Do not offer SC2005 quizzes until a question bank is added. No deployment or account changes requested.

Review baseline for this integration: filesystem snapshot `/tmp/sc2005-web-before/web`, taken before edits; no Git history is available.

## Subject home and navigation — 22 October 2026

Source: user requests a more elegant, Apple-like way to change SC2001/SC2005, suggesting a separate home page showing subjects.

- The root home page presents both subjects as clear, generous navigation panels; each opens its existing course library.
- Replace the course dropdown with contextual navigation: All subjects, current course name, Library, Practice and global progress. The brand returns home from every route.
- Preserve existing course, lesson, quiz and progress URLs, all media, question data and saved progress. Subject selection remains usable on mobile and with a keyboard.
- Inherit the existing Apple-like visual system; no new account, deployment, dependency or content changes.

Review baseline: `/tmp/subject-home-before`, containing the pre-change web app files.

## Home tutor expression — 22 October 2026

User asks to feature Malfoid on the subject home with her normal smug expression changing to flustered on hover. Use the existing original artwork. Keep subject navigation accessible and responsive. Add keyboard-focus reaction and tap toggle for non-hover devices; honor reduced motion. No media or question changes. Review baseline: `/tmp/malfoid-home-before`.

## Approved production publication — 23 October 2026

The user subsequently approved publishing the complete SC2001/SC2005 app, including 59 videos, 41 narration files, captions, transcripts, source notes, quizzes and the question-bank PDF, to `joel-0a4e`. Production is https://malfoid-study.vercel.app. SC2203 additions remain local; original media masters remain untouched. This authorization supersedes earlier local-only deployment constraints for the listed materials.
