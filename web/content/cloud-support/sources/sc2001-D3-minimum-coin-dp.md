# How does DP find the minimum number of coins?

## Sources

Dynamic Programming pp19–27; study notes 06-greedy-and-dp §§6.5,6.8.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Minimum coins for an exact amount

How does dynamic programming find the minimum number of coins? We will define an exact-amount state, compare every possible final coin, fill a small table and reconstruct an optimal answer that greedy misses.

### b01 — Define the state

Define the entry at amount a as the minimum coin count making that exact amount. The empty amount needs zero coins, while an unreachable positive amount must have an infinity marker rather than a misleading count of zero.

### b02 — Derive the recurrence

In any nonempty solution, remove its last coin of value d. The remaining coins must make amount a minus d, so trying every affordable denomination gives one plus the best stored count for that remainder.

### b03 — Optimal substructure

Why may we use an optimal remainder solution? If that remainder used more coins than necessary, replacing it by a better solution and restoring the last coin would improve the supposed optimum, a contradiction.

### b04 — A small complete table

Use denominations one, three and four, and target amount six. Start from C of zero equal to zero and fill increasing amounts, because every positive denomination points to a smaller amount.

### b05 — Amounts 1 and 2

For amount one, only the one-coin fits, so the answer is one. For amount two, that same denomination extends C of one, giving two coins.

### b06 — Amounts 3 and 4

For amount three, compare three ones with the single three-coin, so the minimum is one. For amount four, the single four-coin beats both ways of extending earlier amounts, so the minimum is again one.

### b07 — Amounts 5 and 6

Amount five has candidates two, three and two, so its optimum is two coins. At amount six, the candidates are three using a final one, two using a final three, and three using a final four, so choose two.

### b08 — Reconstruct an actual solution

To reconstruct six, select a coin of value three and reduce the remaining amount to three. Select another three-coin, reach zero, and recover two coins of value three.

### b09 — Compare with greedy

The largest-first rule would take four and then two ones, for three coins instead of two. The dynamic program succeeds because it compares alternatives rather than permanently committing to the largest denomination.

### b10 — Derive the complexity

For a target A and k denominations, there are A positive amounts and at most k candidates per amount. This gives big O of k A time and big O of A table storage, with reconstruction adding work proportional to the number of coins output.

### b11 — Unreachable amounts

If coin one is absent, some amounts may be unreachable; with denominations three and four, amount two is one example. Keep those entries at infinity and report impossibility, rather than following a nonexistent reconstruction choice.

### b12 — Things to take note of

Things to take note of: the state means exactly an amount, and its objective is minimum count, not the number of combinations. Derive cost from actual states and choices, avoid the slide's unsupported blanket factorial claim, and remember that dependence on the numeric amount will matter when we discuss input bits.
