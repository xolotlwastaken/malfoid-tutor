# Why does density greedy fail for 0/1 knapsack?

## Sources

Introduction to NP pp34–35; Greedy Algorithms pp14–17; Dynamic Programming pp52–65; study notes 08-np-and-heuristics §8.13.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Same items, different constraints

Why does density greedy fail for zero-one knapsack? We will reuse our fractional example, enforce whole-item choices, compare the resulting profits and identify exactly where the earlier exchange proof breaks.

### b01 — Density-greedy 0/1 rule

The heuristic sorts items by decreasing profit divided by weight. Scan that order, take a whole item if it fits, and otherwise skip it and continue rather than taking a fraction.

### b02 — The shared dataset

Use the weight-profit pairs ten and sixty, twenty and one hundred, and thirty and one hundred twenty. Their densities are six, five and four, so the scan order is exactly the same as in the fractional lesson.

### b03 — Take the first two

Take item one fully, using ten weight and earning sixty. Item two also fits, so take it, bringing the totals to weight thirty and profit one hundred sixty.

### b04 — Skip the overweight whole item

The remaining capacity is twenty, but item three weighs thirty and cannot be divided. Skip it, ending with profit one hundred sixty rather than the fractional answer two hundred forty.

### b05 — A better whole-item solution

Instead select items two and three, whose weights twenty and thirty exactly fill the bag. Their profits sum to two hundred twenty, already proving that the greedy one-hundred-sixty result is not optimal.

### b06 — Independently verify the optimum

For these three items we can verify the optimum by inspecting all feasible subsets. The best individual profit is one hundred twenty, the other feasible pairs give one hundred sixty and one hundred eighty, and all three exceed capacity, so two hundred twenty is the optimum.

### b07 — Compare all three answers

Fractional greedy reaches two hundred forty by taking only twenty of the last item's thirty weight units. The zero-one optimum is two hundred twenty, and the density-greedy zero-one result is one hundred sixty, so these are three different quantities.

### b08 — Why the exchange proof breaks

The fractional proof exchanged equal small amounts of weight between different materials. Such an exchange may cut an item into forbidden pieces here, so it cannot justify the same density rule for indivisible choices.

### b09 — Conditional grouping matters

Correct implementation updates total weight and profit only when an item is actually accepted. The slide's informal grouping must not be copied as an unconditional weight update after a rejection, because that would incorrectly reduce room for later fitting items.

### b10 — Compare the costs

Sorting takes order n times the logarithm of n, followed by a linear scan through the items. The exact dynamic program uses a table with n item choices and C capacity values, giving order n times C work that depends on the numeric capacity.

### b11 — Report the requested result

An instance where greedy happens to match the optimum cannot establish universal correctness. State whether the question asks you to trace a heuristic, find an exact optimum, or explain a counterexample before choosing which result to report.

### b12 — Things to take note of

Things to take note of: preserve the item variant, skip rather than fractionally fill, continue scanning, and update totals only on acceptance. Compare feasibility and profit explicitly, and do not let an optimal fractional argument smuggle illegal pieces into a whole-item bag, how charming.
