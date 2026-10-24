# How do we choose a correct state and strategy?

## Sources

Dynamic Programming pp20–21,28–29,66–67; Greedy Algorithms p18; study notes 06-greedy-and-dp §§6.5,6.12.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Choose by problem structure

How do we choose a correct state and algorithmic strategy? We will compare divide and conquer, greedy and dynamic programming, then use a path example to test whether a proposed state remembers enough information.

### b01 — Two familiar strategies

Divide and conquer solves smaller versions and combines their answers, as merge sort solves two halves and merges them. Greedy instead commits to one locally best feasible choice, and needs a proof that this choice can safely agree with an optimum.

### b02 — What DP adds

Dynamic programming compares relevant alternatives while reusing stored answers for overlapping states. It may be recursive or iterative, and it does not need to try every numerical split unless that problem's recurrence actually demands it.

### b03 — A sufficient state

Start by defining a state in a sentence rather than writing a table shape. The state must contain everything needed to determine the best future answer independently of the particular history that reached it.

### b04 — Why dimensions differ

For minimum coin change with unlimited coins, the remaining amount is enough. For zero-one knapsack it is not enough, because the available item set changes; the standard prefix formulation therefore also records how many initial items remain eligible.

### b05 — Replacement reasoning

Optimal substructure can be justified by replacement: if an optimum used a nonoptimal subsolution, a better legal replacement would improve the whole answer. The word legal matters, because a replacement that violates the original constraints proves nothing.

### b06 — Shortest-path substructure

Consider a shortest path split into a prefix and suffix under conditions where the shortest route is well-defined. Replacing a subpath by a cheaper route cannot improve on a true optimum, which motivates the familiar shortest-path property.

### b07 — Longest simple paths need history

Now consider longest simple paths, where no vertex may repeat. A state naming only the current endpoint forgets which vertices have already been used, even though those choices decide which continuations are legal.

### b08 — A state-collision problem

Suppose two partial paths reach the same vertex, but one has already used a vertex required by a later extension. Merging those histories into one endpoint-only answer can keep a numerically attractive path whose future extension is forbidden.

### b09 — Correct state can still be large

Adding a visited set can restore the missing information in a longest-simple-path formulation. However, n vertices have two to the n possible subsets, so a sufficient state does not automatically produce a polynomial-size dynamic program.

### b10 — Choose the proof for the problem

The same discipline explains our greedy examples. Fractional density ordering has a legal equal-weight exchange, while indivisible knapsack and arbitrary coin denominations can defeat a local choice, so each requires its own proof or counterexample.

### b11 — A complete DP design answer

After deriving the state and recurrence, give an evaluation order that respects dependencies. Then multiply the number of distinct states by transition work, and add initialisation, reconstruction and stack costs where they matter.

### b12 — Things to take note of

Things to take note of: an algorithmic label is not a correctness proof, and optimal substructure alone does not guarantee a small table. Keep every relevant constraint in the state, distinguish reachable states from repeated calls, and let the actual dependencies choose your implementation, obviously.
