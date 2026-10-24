# How does Boyer–Moore use the good suffix?

## Sources

String Matching pp39–49,51–54; physical p40 visually checked; study notes 07-string-matching §7.7.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Reuse the matched suffix

How does Boyer–Moore use the good suffix? We will find the suffix already matched before a mismatch, choose a safe pattern slide, and convert that slide into the match-jump table used by the course code.

### b01 — What has already been learned?

Suppose right-to-left comparisons matched the last m minus k pattern characters before failing at k. That matched text suffix is information we should preserve when choosing the next possible alignment.

### b02 — Case 1: earlier suitable suffix

First look for an earlier full occurrence of that suffix in the pattern, preceded by a different character from P at k. Choose the rightmost suitable occurrence, which gives the smallest positive slide preserving this useful match.

### b03 — Exclude a known repeated mismatch

Why insist on a different preceding character? If the earlier suffix had the same preceding pattern character, aligning it would reproduce the mismatch we already know, so it cannot supply the next viable alignment.

### b04 — A concrete case 1

The slide example uses pattern R A T S A N D C A T S, length eleven, with mismatch at position eight after matching A T S. The earlier A T S ends at position four and is preceded by R rather than C.

### b05 — Convert slide to pointer increment

The actual pattern slide is eleven minus four, which equals seven. But j has already moved three places left, so its increment is those three places plus seven, giving match jump ten.

### b06 — Case 2: prefix overlap

If no suitable full suffix occurrence exists, try aligning the longest suffix of that matched portion which is also a prefix of the pattern. This second case preserves a partial overlap that could still grow into a complete match.

### b07 — Case 3: no overlap

If neither a full occurrence nor a prefix overlap works, move the pattern beyond the matched suffix. In that third case the actual pattern slide is m, while the pointer increment still includes the m minus k matched positions.

### b08 — WOWWOW: empty suffix

Now build the course table for W O W W O W, with positions listed in increasing k. When no suffix has matched at k equal to six, the convention is slide one and match jump one.

### b09 — Two informative entries

For k equal to five, suffix W can align to a suitable earlier W with slide two, giving pointer increment three. For k equal to four, suffix O W has an earlier full occurrence preceded by the same W as the mismatch position, so that occurrence is excluded.

### b10 — Finish the table

For that k equal to four case, a prefix overlap W instead gives slide five, and the pointer increment is two plus five, or seven. For k equal to three, two and one, the useful shift is three, giving jumps six, seven and eight respectively.

### b11 — The complete course table

Reading entries from k one through six, the slide table is three, three, three, five, two, one. The corresponding match-jump table is eight, seven, six, seven, three, one, because each entry adds its matched-suffix length.

### b12 — Stay within the shown variant

The deck teaches these cases and tables without developing a complete preprocessing implementation. Do not invent its preprocessing cost or borrow a differently indexed good-suffix table; the number required by this scan is always the pointer increment, not just the slide.

### b13 — Things to take note of

Things to take note of: identify the exact matched suffix, test full occurrence before prefix overlap, and check the preceding-character condition. Add the matched-suffix length when converting to the pointer increment, and label table order explicitly so an extracted PDF cannot silently reverse your answer, hmph.
