# How does Boyer–Moore use the bad character?

## Sources

String Matching pp26–38; study notes 07-string-matching §§7.5–7.6.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Right-to-left comparisons

How does Boyer–Moore use the bad character? We will compare from right to left, build the course's character-jump table, and distinguish moving a text pointer from sliding the pattern alignment.

### b01 — Two directions

The pattern still moves overall to the right across the text, but comparisons within one alignment run from the pattern's end toward its beginning. Set both j and k to the pattern length m.

### b02 — Build charJump

For every alphabet character, start its character jump at m, representing absence from the pattern. Then scan the pattern from one to m and set each present character's entry to m minus its position, leaving the rightmost occurrence.

### b03 — The example table

Take pattern A B C A of length four. Its rightmost A is at position four, so the A entry is zero; B is two from the end, C is one from the end, and an absent X receives four.

### b04 — Match a suffix

Align this pattern with the start of text A X C A B C A. At text position four, A matches A; at position three, C matches C, leaving a matched suffix C A.

### b05 — Mismatch after a suffix

At j equal to two and k equal to two, text X disagrees with pattern B. The character table suggests increment four, while the fallback m minus k plus one is three, so the simplified scan takes their maximum, four.

### b06 — Pointer advance versus slide

Increment j from two to six and reset k to four. The old alignment ended at text position four and the new one ends at six, so the pattern itself slid only two positions even though the text pointer advanced four.

### b07 — Why the numbers differ

The difference comes from the two successful comparisons that moved j left before the mismatch. A jump measured from the mismatch pointer must account for that matched suffix, so it cannot be treated as an alignment slide without conversion.

### b08 — Advance once more

At the new endpoint six, text C disagrees with pattern A. Character jump one and fallback one advance j to seven; reset k and the pattern now aligns with A B C A at text positions four through seven.

### b09 — Return the first match

All four comparisons then match from right to left, reducing k to zero. Under this one-based course convention the successful start is j plus one, which is four for our example.

### b10 — Why the fallback exists

The fallback m minus k plus one is essential because character jumps alone can suggest a nonprogressing or backward alignment when the rightmost occurrence lies beyond the mismatch position. The extra term restores the old endpoint and forces at least one position of alignment progress.

### b11 — Cost and limits

Initialising the alphabet table and scanning the pattern costs big O of alphabet size plus m, with corresponding table storage. The simplified scan still has a general big O of n m bound; skipping many comparisons on some inputs is not a sublinear worst-case guarantee.

### b12 — Things to take note of

Things to take note of: preserve one-based indices, keep the rightmost occurrence, reset k after jumping, and distinguish a zero table entry from a safe zero alignment shift. Track j from its actual mismatch location; borrowing a table from a different pointer convention can produce a beautifully wrong trace.
