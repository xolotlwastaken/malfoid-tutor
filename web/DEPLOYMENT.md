# Malfoid Study deployment

Production: https://malfoid-study.vercel.app
Dashboard: https://vercel.com/joel-0a4e/malfoid-study

Published on 23 October 2026 through the authenticated Chrome Vercel dashboard using Vercel Drop.

- Account: `joel-0a4e`
- Team: `team_XoPJgPSsrbUZRKK8Yfn1rS1S`
- Project: `prj_SD9gwT0WjKMRcnKzr51IsM5xAxJI`
- Deployment: `F4sVGPbrYRD69QsR3SYzLN1xAkdf`
- Blob store: `malfoid-lessons` (`store_gjrst1uDONedkhjT`)
- Public media origin: `https://gjrst1udonedkhjt.public.blob.vercel-storage.com`

## Published scope

The published courses are SC2001 and SC2005. The October 24 expansion adds SC2001 Weeks 8–13: 31 verified lessons and 403 questions. The resulting catalog contains 90 videos, 72 narration downloads, 90 captions/transcripts, 72 source notes and 953 interactive questions (793 SC2001,160 SC2005). The linked original SC2001 PDF remains the 90-question Weeks 1–7 edition. SC2203 remains local and is excluded through `content/hosting.json`.

The existing public Blob store contains 162 streaming files, approximately508.6 MB. The 62 new files were read back and SHA256-checked against the local streaming copies; all31 video range requests returned HTTP206. Videos use720×1280 H.264 and narration usesMP3. Original1080×1920 masters remain local.

Later SC2001 lessons use approved slides-and-notes grounding because matching Weeks8–13 recordings were unavailable. Each source map states that gap. The analysis, question audit and delivery evidence are versioned in the repository.

## GitHub automatic deployments

Repository: https://github.com/xolotlwastaken/malfoid-tutor

The existing `malfoid-study` project uses `main` as its production branch, with Root Directory `web`, Build Command `npm run build`, and Output Directory `dist`. Push commits to `main` to build and publish production through Vercel's GitHub integration. Other branches receive preview deployments.

The repository contains the website source and supporting content. Local environment files, Vercel credentials, generated bundles, media production files, and model caches are ignored. Lesson videos and narration continue to load from the existing public Blob store, so GitHub builds do not need local media masters or a Blob write token.

## Rebuild and publish manually

Run `npm run build` from this directory. The build validates `content/hosted-media.json`, selects `publishedCourseIds` from `content/hosting.json`, and stages only public files in `dist/`. Zip the contents of `dist/` without a parent folder and upload the archive through the Vercel dashboard to this project. Confirm the account and project before publishing.

The local project link now identifies the correct project. Existing CLI authentication and local environment credentials may still belong to the earlier account; authenticate to `joel-0a4e` before using a CLI deployment or media upload. Do not include environment files in the archive.

## Verification

All 100 media URLs returned HTTP 200 with the expected sizes. All 164 checked website resources returned HTTP 200. Media range requests returned HTTP 206. The live browser verified both libraries, video playback and chapter seeking, caption loading, the SC2001 quiz interface and the Malfoid home interaction. Four cloud-build tests passed after the final hosting configuration change.

Browser progress is stored per origin; localhost progress does not automatically transfer to the production domain.
