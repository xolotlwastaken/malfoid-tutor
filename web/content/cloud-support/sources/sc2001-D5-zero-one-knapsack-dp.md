# How does 0/1 knapsack DP enforce single use?

## Sources

Dynamic Programming pp52–63; study notes 06-greedy-and-dp §6.10.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — 0/1 means once or not at all

How does zero-one knapsack dynamic programming enforce single use? We will derive an include-or-exclude recurrence, build a complete small table, recover the chosen items, and identify the update that would accidentally permit reuse.

### b01 — State the constraints

Each item is indivisible and may be selected at most once. Capacity is an upper limit, so an optimal solution may leave room unused; filling the bag exactly is not required.

### b02 — The two state dimensions

Let P at c and j be the maximum profit attainable with capacity c using only the first j items. With no items or with zero capacity, the value is zero under the positive-weight assumptions.

### b03 — Include or exclude

If item j is too heavy, it cannot be included, so copy the value using the first j minus one items. Otherwise compare excluding it with its profit plus the best value at the remaining capacity, again using only the first j minus one items.

### b04 — Why reuse is impossible

Both branches decrease the item index, which is the reason single use is enforced. Once item j has been included, its subproblem cannot include that same item again.

### b05 — The example

Our capacity is five, and items have weight-profit pairs two and three, three and four, and four and five. Begin with the empty column, then add one available item at a time while preserving the already computed previous column.

### b06 — First-item column

With only item one available, capacities zero and one cannot fit it, so they stay zero. At capacities two through five the profit is three; the bag never gets two copies just because a larger capacity could hold them.

### b07 — Second-item column

Add item two, whose weight is three and profit is four. At capacity three it improves the profit to four, at capacity four it still gives four, and at capacity five combining it with item one yields seven.

### b08 — Third-item column

Add item three, whose weight is four and profit is five. It improves capacity four from four to five, but at capacity five its inclusion gives only five, so excluding it preserves the better value seven.

### b09 — Backtrack the choices

Reconstruct from capacity five and all three items. The value equals the previous column, so skip item three; with the first two items the value seven exceeds the first-item value three, so select item two and reduce capacity by three.

### b10 — Recover the selected subset

At capacity two and item one, the value three exceeds the no-item value zero, so select item one. The recovered pair has total weight five and profit seven; decrease the item index after either taking or skipping.

### b11 — Derive the complexity

The table has order n C states, each comparing at most two constant-time alternatives, giving big O of n C time and space. Reconstruction takes at most n item decisions, while a memoised version must also account for recursive storage.

### b12 — One-dimensional update direction

A one-dimensional optimisation processes capacities downward for each item, so a transition reads a value from before that item was added. Updating upward can read a newly improved smaller-capacity cell and reuse the item, silently changing the problem to unbounded knapsack.

### b13 — Things to take note of

Things to take note of: define both state dimensions, guard the overweight branch, and keep j minus one in both choices. Distinguish zero-one, fractional and unlimited-item variants, allow unused capacity, and explain the numeric-capacity cost before calling this algorithm polynomial.
