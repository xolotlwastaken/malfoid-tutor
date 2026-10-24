# How do memoisation and tabulation remove repeated work?

## Sources

Dynamic Programming pp3–18; study notes 06-greedy-and-dp §§6.5–6.7.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Store a state once

How do memoisation and tabulation remove repeated work? We will compute Fibonacci six, distinguish repeated calls from distinct states, and derive both a recursive cached solution and a bottom-up table.

### b01 — Repeated subproblems

The ordinary recursive function asks for Fibonacci five and Fibonacci four to compute Fibonacci six. Fibonacci five then asks for Fibonacci four again, so two branches immediately repeat the same mathematical question.

### b02 — Calls are not states

Continuing the call tree repeats smaller inputs many more times. The uncached recursion has exponential growth, with big O of two to the n as a valid upper bound, even though its maximum call depth is only linear.

### b03 — Define the state

Dynamic programming identifies a state by the information needed to determine its answer. Here that information is just the integer index, so all calls requesting Fibonacci four can share one stored result.

### b04 — Top-down memoisation

In top-down memoisation, check the cache before solving a state again. If an answer is present, return it; otherwise obtain the smaller answers, add them, store the result and return it.

### b05 — Unknown is not zero

Zero is a valid Fibonacci answer, so it cannot double as the unknown marker. An initially unused sentinel or a separate presence flag distinguishes an unsolved state from the already computed value zero.

### b06 — The subproblem graph

Collapse the repeated call tree into a graph with one vertex for each index from zero to six. An arrow here points from a caller to a state it depends on, so the destination must be solved before that caller can finish.

### b07 — Bottom-up order

Bottom-up tabulation uses those dependencies to select an evaluation order. Set the first two cells to zero and one, then visit indices from two onward so both preceding answers already exist.

### b08 — Fill the next states

At index two, add zero and one to get one; at index three, add one and one to get two. At index four, the two preceding answers are one and two, so the result is three.

### b09 — Finish F(6)

At index five the sum is two plus three, giving five. At index six the sum is three plus five, giving eight, so the final table is zero, one, one, two, three, five, eight.

### b10 — Derive the cost

There are n plus one possible states and constant arithmetic work for each evaluated state, giving linear arithmetic time. A full table uses linear space, and the top-down version also has a linear-depth recursion stack.

### b11 — Optional storage reduction

If only the final Fibonacci value is required, bottom-up evaluation needs just the two previous values. That reduces extra storage to a constant number of machine words under the course arithmetic model; exact large-integer bit costs are a separate analysis.

### b12 — Things to take note of

Things to take note of: define the state, distinguish calls from first computations, and respect the dependency direction. Memoisation is still recursive and DP is not automatically polynomial; its cost follows the number of states and transitions, not the comforting sound of the word cache.
