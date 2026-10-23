# What does an operating system actually do?

SC2005 episode01. New complete lesson; older introductory drafts are preserved.

## Source map

- Slides: `Part1 (Intro and Background).pdf`, physical PDF pp2–6 (goals, roles, layers/kernel); pp10–13 (batch, multiprogramming, time sharing); p19 (multiprocessor systems). The local extracted cache in `edit/sc2005/planning/sources/Part1 (Intro and Background).txt` records physical-page boundaries. Pages23/26 support CPU/device overlap, but the exact numerical workload below is authored, not a claimed lecture trace.
- Tutorial: `tut1.pdf`, physical p1, question3: distinguish multiprogramming from multiprocessing and explain motivations.
- Coverage notes: `edit/sc2005/planning/SC2005-exam-topic-guide.md`, §1 and introductory §2; these are newly generated coverage notes, not pre-existing independent student notes.
- Lecture recordings/transcripts: none found in the supplied SC2005 inventory. This gap remains explicit. No recording was claimed reviewed and no timestamp was invented.
- User lecture photographs: later scheduling photos support general event-ledger discipline, but no claim that their numeric workload is this episode’s example is made.

Original source folder: `NTU/Y2S1/SC2005`.

## Authored worked example and verified assumptions

Both jobs submitted at0; one processor; A selected first. A needs CPU2, then I/O4, then CPU2. B needs CPU4. Ignore context-switch, admission and transfer overhead. A’s I/O uses a separate device that can overlap CPU work.

One-job-at-a-time comparison: A CPU[0,2), I/O[2,6), CPU[6,8); B is admitted after A completes and CPU[8,12). CPU busy8, elapsed12, utilization2/3≈66.7%. B is submitted but not a ready in-memory job while A alone occupies the batch model’s user memory.

Multiprogrammed: A CPU[0,2), I/O[2,6), CPU[6,8); B CPU[2,6). CPU busy8, elapsed8, utilization100% in this ideal fixture. At2 A becomes blocked; at6 its I/O completes, it becomes ready, then dispatches. A single CPU never runs both at once. A remains resident while blocked. Finishing B and completing A’s I/O at6 is an explicit simultaneous event, without switching overhead.

Separate parallelism illustration: C and D each need4 CPU units. One core: C[0,4),D[4,8), completion8. Two cores: C[0,4) on core1,D[0,4) on core2, completion4. Total CPU work8 in both cases; elapsed completion changes. This is a distinct workload, not a claim that a second core must halve the first example’s8-unit completion time.

## Corrections to older draft wording

Do not claim CPU never idles, maximizing utilization is the sole OS goal, multiprogramming requires a one-core machine, or extra cores automatically guarantee fault tolerance. Interrupt/context-switch protection and real-time scheduling have their own later lessons. Time sharing emphasizes responsive turns; concurrency can be interleaved on a single core and can also be parallel on multiple cores.

## Production and verification

Use approved exact reference and transcript in `edit/series/voice-lock/voice-lock.json` with cached local Qwen3-TTS Base. No lecture uploads, ElevenLabs or new speaker design. Reuse the seven clean main poses; expression changes every2–3 spoken sentences. Full speech clips preserved,100ms handles,30ms boundary fades, final hold≥1second. Original word ASR retained separately from authored captions. Timeline, character cues, state fixtures, verifier and final media are kept beside this file.

Final delivery requires independent workload/CPU-exclusive checks, raw ASR review, voice-reference hash/provenance,1080×1920/30fps H.264/AAC MP4 checks, full decode, and encoded-frame inspection during movement/transitions. See `verification.json` for actual completed checks; this source map alone is not proof they passed.
