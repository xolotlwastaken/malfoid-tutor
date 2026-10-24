# How does longest common subsequence work?

## Sources

Dynamic Programming pp30–51, visually checked p44; study notes 06-greedy-and-dp §6.9. The source strings are X=ACGGA and Y=ACTG in visual order.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Longest common subsequence

How does longest common subsequence work? We will derive its two recurrence cases, fill a complete prefix table, reconstruct an actual sequence, and count both the table work and the backtracking cost.

### b01 — Subsequence, not substring

A subsequence preserves order but may skip characters, whereas a substring must be contiguous. We seek a sequence appearing in both inputs with maximum length, and more than one answer can sometimes attain that length.

### b02 — Define prefix-pair states

Let L at i and j mean the best common-subsequence length of the first i characters of X and the first j characters of Y. If either prefix is empty, its common-subsequence length is zero, giving the zero border of our table.

### b03 — Equal terminal characters

If the terminal characters match, there exists an optimum using that common terminal character. Append it to an optimum for the two shorter prefixes, so the value is one plus the diagonal predecessor.

### b04 — Unequal terminal characters

If the terminal characters differ, they cannot both be the final character of a common subsequence. Omit one or the other and take the larger value from the upper and left neighbours, covering both possibilities.

### b05 — Fill row A

Fill rows from top to bottom, and columns from left to right, so every dependency is ready. For the first X character A, the four values against Y are one, one, one, one, because the matched A remains available as the Y prefix grows.

### b06 — Fill row AC

For the next X character C, the first value stays one, and matching C raises the second value to two. The rest of this row stays two, giving one, two, two, two.

### b07 — Fill row ACG

For the first G, the row becomes one, two, two, three. The final entry uses the matching G in Y and adds one to the diagonal value two, establishing a common subsequence of length three.

### b08 — Fill the remaining rows

The second G does not produce a fourth common character, because the Y prefix contains only one G at its end. Its row is one, two, two, three again, and the final A row has those same values, leaving the optimum at three.

### b09 — Begin backtracking

To reconstruct, begin at the bottom-right cell, and choose the upper neighbour when an unequal-character tie occurs. From the final A we move up; at the second G we move diagonally, emit G, and continue at the shorter prefixes.

### b10 — Finish backtracking

Continue upward past the unused first G, then left past T, reaching the matching C. Emit C diagonally, then emit the matching A, and stop when an empty-prefix border is reached.

### b11 — Reverse the emitted sequence

The emitted characters are reversed because we travelled from the end toward the start. Reverse G, C, A to obtain A, C, G, which appears in order in both original strings and has the optimal length three.

### b12 — Derive time and space

There are n times m interior states with constant work per state, so filling costs Theta of n m and the full table occupies big O of n m space. Each backtracking step decreases at least one index, giving big O of n plus m reconstruction time.

### b13 — Memoisation is also DP

Memoised top-down recursion also avoids repeated states, so it can achieve the same polynomial state bound. The slide warning about inefficient recursion concerns the uncached version; optional rolling rows save length-only storage but complicate this simple reconstruction.

### b14 — Things to take note of

Things to take note of: define prefix lengths, initialise both borders, distinguish equal and unequal terminal cases, and state your tie rule. Recover a sequence as well as its length when asked, and reverse backtracked characters instead of proudly submitting the answer backwards, how charming.
