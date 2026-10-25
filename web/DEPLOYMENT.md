# Malfoid Study deployment

Production: https://malfoid-study.vercel.app
Dashboard: https://vercel.com/joel-0a4e/malfoid-study

Updated on 25 October 2026 through the existing GitHub main integration. The initial manual Vercel Drop deployment was 23 October 2026.

- Account: `joel-0a4e`
- Team: `team_XoPJgPSsrbUZRKK8Yfn1rS1S`
- Project: `prj_SD9gwT0WjKMRcnKzr51IsM5xAxJI`
- SC2001 content release: `4daa38e`, deployment `su6Mc21uPmhNxsW2HH6mhK938hLk`
- Initial manual deployment: `F4sVGPbrYRD69QsR3SYzLN1xAkdf`
- Blob store: `malfoid-lessons` (`store_gjrst1uDONedkhjT`)
- Public media origin: `https://gjrst1udonedkhjt.public.blob.vercel-storage.com`

## Published scope

The published courses are SC2001, SC2005 and SC2203. The October 25 release adds all 48 existing SC2203 Automata lessons through Week 11, narration, captions/transcripts, source notes and the existing exam-bank download. The resulting catalog contains 138 videos, 120 narration downloads, 138 captions/transcripts, 120 source notes and the existing 953 interactive questions (793 SC2001, 160 SC2005). SC2203 has an exam-style bank with 176 MCQs and 44 open-ended questions, but no scored interactive bank. The linked original SC2001 PDF remains the 90-question Weeks 1–7 edition. `content/hosting.json` includes all three courses.

The existing public Blob store contains 258 streaming files, approximately 798.3 MB. The 96 SC2203 files (289,702,837 bytes) were read back and SHA256-checked against the local streaming copies; all 48 SC2203 video range requests returned HTTP 206. Videos use 720×1280 H.264 and narration uses MP3. Original 1080×1920 masters remain local.

Later SC2001 lessons use approved slides-and-notes grounding because matching Weeks 8–13 recordings were unavailable. Each source map states that gap. The analysis, question audit and delivery evidence are versioned in the repository.

## GitHub automatic deployments

Repository: https://github.com/xolotlwastaken/malfoid-tutor

The existing `malfoid-study` project uses `main` as its production branch, with Root Directory `web`, Build Command `npm run build`, and Output Directory `dist`. Push commits to `main` to build and publish production through Vercel's GitHub integration. Other branches receive preview deployments.

The repository contains the website source and supporting content. Local environment files, Vercel credentials, generated bundles, media production files, and model caches are ignored. Lesson videos and narration continue to load from the existing public Blob store, so GitHub builds do not need local media masters or a Blob write token.

## Rebuild and publish manually

Run `npm run build` from this directory. The build validates `content/hosted-media.json`, selects `publishedCourseIds` from `content/hosting.json`, and stages only public files in `dist/`. Zip the contents of `dist/` without a parent folder and upload the archive through the Vercel dashboard to this project. Confirm the account and project before publishing.

The local project link now identifies the correct project. Existing CLI authentication and local environment credentials may still belong to the earlier account; authenticate to `joel-0a4e` before using a CLI deployment or media upload. Do not include environment files in the archive.

## Verification

The SC2203 upload verification covers all 96 remote file hashes, content lengths and all 48 video range responses. Evidence is saved locally in `.hosting-media/sc2203-upload-verification.json`. All 16 website checks pass, including a regression check that the build includes the repository-root SC2203 exam-bank file at `/sc2203-exam-question-bank.md`. The production build includes 138 lessons and 953 interactive questions.

The earlier SC2001 release verified all 62 new media files, all 31 video range responses, the 90-lesson live catalog and all 263 static resources. Its production browser checks covered hosted playback, chapter seeking and the Baka challenge; local browser checks also covered answer locking, worked feedback, refresh restoration and 390px layout.

Browser progress is stored per origin; localhost progress does not automatically transfer to the production domain.
