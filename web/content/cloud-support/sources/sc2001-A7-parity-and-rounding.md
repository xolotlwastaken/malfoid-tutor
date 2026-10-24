# How do parity and rounding affect recurrences?

## Sources

Review Week 8 pp10–12; Analysis Techniques pp43–45; study notes 01-analysis §§1.5,1.7.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Exact details and growth

How do parity and rounding affect recurrence solutions? We will expand a recurrence that decreases by two, handle its two base cases, and then explain when rounding can safely be suppressed in an asymptotic analysis.

### b01 — The stipulated count

The review analyses a particular median-of-three quicksort comparison count using T of n equals T of n minus two plus n. It sets T of one to zero and T of two to one, so odd and even inputs finish at different bases.

### b02 — Name what is counted

The local n in this review comes from three pivot-selection comparisons and n minus three partition comparisons. It is a convention for the shown algorithm, not a universal exact comparison count for every median-of-three implementation.

### b03 — Even trace

Take an even input size of eight and expand the recurrence. We obtain eight plus six plus four plus the base value one, for nineteen comparisons under this model.

### b04 — Even formula

Write a general even input as two k. The terms are four through two k in steps of two, together with T of two equal to one, so their sum is k times k plus one minus one.

### b05 — Odd trace

For an odd input of seven, expansion instead gives seven plus five plus three plus zero. The result is fifteen, because the recurrence reaches T of one rather than T of two.

### b06 — Odd formula

For a general odd input two k plus one, sum the k odd terms from three through two k plus one. Their arithmetic-series sum is k times k plus two, again quadratic in n.

### b07 — Same order, different totals

Both the even and odd cases therefore have Theta of n squared growth despite different exact totals. Median-of-three can improve pivot selection, but this example shows it does not guarantee balanced splits in the worst case.

### b08 — Beyond exact powers

Now consider recurrences that divide input sizes by two and therefore need floors or ceilings. Solving on exact powers of two is convenient, but extending that result to arbitrary n requires a justification.

### b09 — The smoothness idea

The slides call a nonnegative function smooth when its value at two n is Theta of its value at n. A polynomial n to the c qualifies, since doubling n multiplies it by the fixed constant two to the c.

### b10 — Check examples

The function n log n is also smooth for sufficiently large n, while two to the n is not. Doubling the input in that exponential changes its ratio by another factor two to the n, which cannot be bounded by a fixed constant.

### b11 — Why sandwiching works

For an ordinary monotone running-time function, sandwich n between the adjacent powers of two. Bounds at those endpoints and a smooth comparison function then control the in-between values, which explains the usual rounding shortcut for standard algorithmic recurrences.

### b12 — Things to take note of

Things to take note of: expand until the correct base, keep parity when exact counts matter, and distinguish exact formulas from their common growth class. Ignore rounding only when the algorithm and comparison bounds justify it, not because floors happen to look untidy, hmph.
