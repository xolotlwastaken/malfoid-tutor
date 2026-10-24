# How do we turn a new recurrence into a DP?

## Sources

Review Week 9 pp8–13; Dynamic Programming pp15–18; study notes 06-greedy-and-dp §§6.6–6.7.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Transfer the method

How do we turn a new recurrence into a dynamic program? We will use the review's Virahanka definition, build its state graph and table, and derive memoised and bottom-up solutions from the same dependencies.

### b01 — Read the given definition

Use the definition actually supplied in this course: both base values are one. For a larger index, add the value at the previous index to the value at the floor of half the index; do not replace this recurrence with a familiar Fibonacci formula.

### b02 — State and evaluation order

Let the state V of j mean exactly the value of that recurrence at index j. Both dependencies are smaller than j when j exceeds one, which permits an increasing-index table order.

### b03 — Initialise safely

Begin the table with one at zero and one at one. For a request at zero, return its base value before attempting to write index one in an array that may contain only a single slot.

### b04 — Compute V(2)

At index two, the dependencies are index one and floor of two over two, which is also one. Add the stored one twice, giving two; repeated dependence on a state does not require computing that state twice.

### b05 — Compute V(3) and V(4)

At index three, the dependencies are index two and index one, giving two plus one equal to three. At index four, use index three and index two, giving three plus two equal to five.

### b06 — Finish V(6)

At index five, use V of four plus V of two to get seven. At index six, use V of five plus V of three to get ten, completing the table one, one, two, three, five, seven, ten.

### b07 — Bottom-up algorithm

In a bottom-up implementation, loop j from two to n inclusive. Each iteration reads the two required earlier cells and stores their sum in V at j, then the function returns V at n.

### b08 — Memoised algorithm

A top-down implementation instead checks whether V at the requested index is already cached. If not, it recursively obtains those same two smaller states, adds them and stores the result before returning.

### b09 — Derive complexity

There are n plus one state positions, and each costs a constant number of arithmetic and cache operations. Both implementations therefore take linear arithmetic time and linear table space; the recursive version additionally counts its possible linear stack depth.

### b10 — Why two values are insufficient

Two rolling values are not sufficient here, because a future state may need an older half-index entry. The dependency pattern decides what memory can be discarded, so a Fibonacci optimisation cannot be copied just because both definitions contain two terms.

### b11 — Things to take note of

Things to take note of: preserve the supplied bases and floor operation, justify the fill order, and distinguish repeated use from repeated computation. The method is state, dependencies, order and cost; remembering someone else's loop without those meanings is a rather fragile sort of confidence.
