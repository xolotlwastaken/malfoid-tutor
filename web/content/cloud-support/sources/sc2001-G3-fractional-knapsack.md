# Why is density greedy optimal for fractional knapsack?

## Sources

Greedy Algorithms pp14–17; study notes 06-greedy-and-dp §6.4.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Fractional knapsack

Why is density greedy optimal for fractional knapsack? We will fill a bag with divisible items, compute the exact profit, and use an equal-weight exchange to explain why the rule works.

### b01 — The density

Each item has a positive weight and a positive profit for taking all of it. Taking a fraction earns the same fraction of its profit, so profit divided by weight measures the value of each unit of capacity.

### b02 — Order by density

Our capacity is fifty, and the items have weight-profit pairs ten and sixty, twenty and one hundred, and thirty and one hundred twenty. Their densities are six, five and four, so that is also the descending order for filling the bag.

### b03 — Take item 1

Take the first item fully, using ten units of weight and earning sixty. Forty units of capacity remain, and no other material gives more profit per unit than the density-six item just selected.

### b04 — Take item 2

Take the second item fully, adding twenty units of weight and one hundred profit. The bag now has weight thirty and profit one hundred sixty, leaving twenty units for the last item.

### b05 — Take a fraction of item 3

The last item weighs thirty, but only twenty units fit. Because fractions are allowed, take two thirds of it, adding eighty profit and filling the capacity exactly.

### b06 — The completed solution

Total profit is sixty plus one hundred plus eighty, which equals two hundred forty. This total uses fifty units of weight; taking the whole third item instead would violate the capacity limit.

### b07 — Set up an exchange

Why is that local density rule globally safe? Suppose some feasible solution includes lower-density material while higher-density material is still available.

### b08 — Equal-weight replacement

Exchange an equal small amount of weight from the lower-density material for the higher-density material. Weight stays unchanged, while profit cannot decrease and strictly increases when the densities differ.

### b09 — Why the rule is optimal

Continue exchanging until no such inversion remains. The resulting solution takes the highest-density material first, which is the greedy structure, so an optimal solution can be transformed into a greedy one without losing profit.

### b10 — Divisibility is essential

The ability to take equal portions of different items is what makes that argument possible. With indivisible items, the exchange might be forbidden, so the same proof does not establish optimality for zero-one knapsack.

### b11 — Safe stopping conditions

Compute densities, sort them in descending order, and scan once, taking the smaller of remaining capacity and item weight. Stop when the bag is full or the items run out; forgetting the second condition can index beyond the list when total available weight is too small.

### b12 — Complexity

Sorting costs big O of n log n, followed by a linear scan, while an already density-sorted list needs only that scan. A conventional stored list uses linear space, and any additional sorting workspace depends on the chosen sorting method.

### b13 — Things to take note of

Things to take note of: compute profit per weight, allow proportional fractions, and state why an equal-weight exchange preserves feasibility. Highest total profit and smallest weight are different rules; the density order wins because of this problem's assumptions, not because the word greedy sounds confident, hmph.
