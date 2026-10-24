# How does naive string matching scan the text?

## Sources

String Matching pp2–10; study notes 07-string-matching §§7.1–7.2.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Find the first occurrence

How does naive string matching scan the text? We will align a pattern, compare characters, reset after mismatches, and derive the scan bound from the number of legal alignments.

### b01 — Fix the convention

Our output is the first starting index where every pattern character matches a consecutive text window. We will use zero-based indices here, with text A B A B A B A C and pattern A B A C.

### b02 — Legal windows

A legal starting index i ranges from zero through n minus m inclusive. If the pattern is longer than the text, there is no complete window, so return no match without reading past the text.

### b03 — Alignment at start 0

At start zero, compare A with A, B with B, and A with A successfully. The fourth comparison checks pattern C against text B and fails, so that window is not a match.

### b04 — Reset at start 1

Move the entire pattern one position right and restart at its first character. At start one, pattern A immediately disagrees with text B, so reject after one comparison rather than continuing from the previous mismatch.

### b05 — Alignment at start 2

At start two, the first three characters again match A, B and A. Pattern C then disagrees with text B, using four comparisons for this alignment.

### b06 — Finish the scan

At start three, A immediately disagrees with B, so reject with one comparison. At start four, all four characters A, B, A, C match, so return index four as the first occurrence.

### b07 — Count the example

The trace used four plus one plus four plus one plus four comparisons, for fourteen in total. Count actual character checks separately from loop-control tests when that is the question's chosen operation.

### b08 — A repeated near-match family

For the worst-case pattern, place many A characters before a final C and search an all-A text. Each legal alignment matches almost the whole pattern before failing on its last character.

### b09 — Derive the scan bound

There are n minus m plus one complete windows, and each can require m character comparisons. That gives a scan upper bound of m times n minus m plus one, with the near-match family attaining that order.

### b10 — Space and boundaries

The straightforward implementation uses a constant number of indices beyond the input strings. A full specification should also state an empty-pattern convention; returning zero is common, but blindly reading pattern position zero when the pattern is empty is invalid.

### b11 — Things to take note of

Things to take note of: keep the alignment start distinct from the current character pointers and reset the pattern after a mismatch. Stop at the last complete window, return the first successful start, and do not confuse a subsequence with the consecutive substring we are searching for, hmph.
