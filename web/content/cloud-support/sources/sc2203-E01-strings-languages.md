# SC2203 E01: What are strings, languages and the empty string?

Complete introductory lesson in the accepted Malfoid format. New lesson; existing videos preserved.

## Source map

Primary source folder: `/Users/joelloh/Library/CloudStorage/GoogleDrive-xolotlwastaken@gmail.com/My Drive/NTU/Y2S1/SC2203`.

| Claim / lesson beats | Source actually consulted |
|---|---|
| Finite nonempty alphabet; finite ordered string; length; epsilon has length zero | `SC2203_slides_recordings/lec1.pdf`, physical p27 |
| String concatenation; not generally commutative; epsilon identity; language is a set of strings; shortlex enumeration | `lec1.pdf`, physical p28 |
| Set order/repetition; empty set and singleton; membership vs subset | `lec1.pdf`, physical pp13–14,16 |
| Sigma star contains all strings including epsilon; regex epsilon vs empty-set languages | `lec3.pdf`, physical pp25,27,29 |
| Empty-language star is singleton epsilon | `lec3.pdf`, physical p29 |
| Coverage guide | `study-notes/sc2203/SC2203-exam-topic-breakdown.md`, T01; generated from the supplied materials, not independent pre-existing user notes |
| Planned episode | `edit/sc2203/planning/SC2203-malfoid-video-plan.md`, E01 |
| Supplementary recording captions | Michael Sipser lecture 1, https://www.youtube.com/watch?v=9syvZr-9xwk , genuine caption cues 00:24:11–00:25:51: finite strings, languages, epsilon vs empty language and singleton epsilon; cached under `edit/sc2203/planning/sources/sipser-captions/9syvZr-9xwk.en.vtt` |

Local SC2203 lecture recordings/transcripts and standalone personal notes were not found in the supplied inventory. This gap remains; the public Sipser caption passage is supplementary, not the NTU lecturer or an audiovisual playback check. No lecture was uploaded and no timestamps were invented. Revisited these source passages before the final takeaways.

## Authored examples and deductions

- Binary alphabet {0,1}; build string 101 from three symbol cards; compare epsilon with the one-symbol string 0.
- x=10,y=1: xy=101, yx=110, additive length 2+1=3; epsilon is a zero-symbol sequence, never an additional input token.
- L={01,10}: reordering or repeating set entries preserves L, while reordering symbols may change a word.
- Sigma-star shortlex prefix: epsilon,0,1,00,01,10,11,000,… . Every word is finite; the set of words is infinite.
- Distinguish epsilon (string, length 0), empty language (set, 0 members), singleton epsilon (set, 1 member). Bars around a string mean length; bars around a set mean cardinality, identified in the diagrams.
- Language concatenation with singleton epsilon preserves L; with empty language produces no pairs and hence empty language. These are direct mathematical deductions from the course definitions, added as a useful contrast, not claimed literal lecture traces.
- Empty-language star contains epsilon via zero factors; positive factor counts produce no words. This derives the slide identity rather than only naming it.
- No algorithm-complexity segment is forced onto this foundational definition lesson. Length additivity and zero-factor reasoning supply the relevant derivations.

## Voice and production

Use the exact approved reference audio/transcript and settings in `edit/series/voice-lock/voice-lock.json`. WAV hash verified before generation. Local Qwen3-TTS Base only; no ElevenLabs or new speaker design. Cached per-beat WAVs and reference provenance remain under `audio/`. Raw unprompted local word ASR is preserved separately from authored caption alignment.

20 beats with 3 sentences each; 7 clean main-pose identities available, chosen for each beat with no consecutive identical main pose. Main-pose cues are recorded in `character-direction.json`. Diagram animation timing uses heard-word cues; any missing/normalized anchors must be reviewed before delivery. Whole clips retained, 100ms handles, 30ms fades on padded edges and a 1.5-second final hold.

1080×1920,30fps,H.264/AAC with fast start; graph paper, high-contrast symbols, captions last with outline and no box. Final encoded frames and transitions must be inspected. Actual completed checks, duration, hash and raw-ASR comparison appear in `verification.json`; this README is not evidence that an unfinished render passed.

## Completed delivery checks

Final duration 324.33 seconds (5:24); 1080×1920 at 30fps, H.264/AAC, fast start, full decode passed. Independently checked the language identities and 961 finite string-length-additivity cases, retained all raw ASR and reviewed its tokenization differences, verified all 50 raw-speech motion anchors and the approved voice hash, checked 20 three-sentence main-pose segments, and visually inspected 32 encoded frames including moving states and complete mathematical takeaways. No narration retake or voice substitution was needed.
