# What do O, Omega and Theta actually mean?

## Sources

Analysis Techniques pp5–12; Review Week 8 pp2–3; study notes 01-analysis §§1.1–1.2.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Bounds describe growth

What do big O, big Omega, and big Theta actually mean? We will build their definitions around one running-cost function, prove its bounds, and finish with the mistakes that make an otherwise sensible answer wrong.

### b01 — Name the quantity

First say what n measures and what operation you count. For a sorting problem, n might be the number of records, while the cost counts key comparisons; copies and swaps would be different counters.

### b02 — One concrete function

Suppose our chosen cost is three n squared plus seven n plus four. The whole expression matters for exact work, but its quadratic term will control its asymptotic growth.

### b03 — O: an eventual ceiling

Big O gives an eventual upper bound, allowing a positive constant multiplier. There must be one constant c and one threshold n zero such that every input size beyond that threshold satisfies f of n at most c times g of n.

### b04 — Prove the upper bound

For every n at least one, seven n is at most seven n squared, and four is at most four n squared. Adding these inequalities puts our whole function at most fourteen n squared, so c equals fourteen is a valid upper-bound witness.

### b05 — Ω: an eventual floor

Big Omega reverses the inequality and supplies an eventual lower bound. Here the positive extra terms cannot reduce the quadratic term, so our function is at least three n squared for every positive n.

### b06 — Θ: prove both sides

Big Theta requires both sides with positive constants. We have already trapped the function between three n squared and fourteen n squared, which proves a tight quadratic bound.

### b07 — Tight does not mean equal

A tight asymptotic bound does not mean exact equality: the function need not equal n squared, and the two bounding constants may differ. Theta groups functions whose growth differs by at most constant factors after a suitable threshold.

### b08 — A correct but loose bound

Our function is also big O of n cubed, because n squared is at most n cubed once n reaches one. That upper bound is true but loose, so use Theta when you have actually established a tight order.

### b09 — Ratio shortcut

A ratio limit can provide a convenient shortcut when it exists. Dividing our function by n squared gives three plus seven over n plus four over n squared, whose limit is the positive constant three.

### b10 — Limits are useful tests

A ratio approaching zero supplies an upper bound, while a ratio growing without limit supplies a lower bound. These are sufficient tests under the usual positivity assumptions; an oscillating ratio can lack a limit even when asymptotic bounds exist.

### b11 — Case and bound are different

Now separate the notation from the input case being analysed. Big O does not mean worst case, and big Omega does not mean best case; either can describe a best-case, worst-case, or suitably defined expected-cost function.

### b12 — State the assumptions

For example, a worst-case function may have both a quadratic upper bound and a quadratic lower bound. An average-case statement additionally needs a distribution on inputs, so do not hide that assumption behind a symbol.

### b13 — Things to take note of

Things to take note of: name the input size and counted operation, keep the constants fixed, and make the inequality hold eventually for every size. Prove both sides for Theta, distinguish a tight bound from a merely valid one, and stop making the letters do the job of a case definition, hmph.
