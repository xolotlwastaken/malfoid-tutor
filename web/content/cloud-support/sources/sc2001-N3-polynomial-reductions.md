# Which direction does a polynomial reduction go?

## Sources

Introduction to NP pp20–23; study notes 08-np-and-heuristics §8.6.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — A reduction transfers a solver

Which direction does a polynomial reduction go? We will transform an instance of one decision problem into another, preserve its answer, and use a solver diagram to keep the hardness direction straight.

### b01 — The correctness contract

A polynomial many-one reduction computes a transformation f in polynomial time. For every source instance x, x must be a yes-instance of A exactly when f of x is a yes-instance of B.

### b02 — Follow the direction

Imagine being given an algorithm that solves B. To solve A on input x, first transform x into f of x, then run the B solver and return its yes-or-no answer.

### b03 — Interpret the arrow

This means A is no harder than B under the reduction, or equivalently B is at least as hard as A. The arrow points toward the solver we would like to borrow, not toward the problem we are initially trying to solve.

### b04 — The easy-target implication

If B has a polynomial algorithm, combining it with the polynomial transformation gives a polynomial algorithm for A. The transformed instance has polynomial length because a polynomial-time transformation cannot explicitly output more than polynomially many symbols.

### b05 — Algorithm-use intuition

For intuition, the deck describes pairing equal-rank elements of two arrays by using sorting. Sort X equal to three, one, two and Y equal to thirty, ten, twenty, then pair one with ten, two with twenty, and three with thirty.

### b06 — Do not blur reduction models

That pairing example illustrates using one algorithm to solve another task, but a formal decision reduction needs the yes-if-and-only-if statement. Likewise, repeatedly calling a factor-finding procedure is an algorithmic reduction illustration, not automatically one many-one decision transformation.

### b07 — Proving a new target hard

To show a new problem B is hard, start from a problem A already known hard and transform A into B. Then a hypothetical fast B solver would give a fast A solver, transferring the established difficulty to the target.

### b08 — The common reversal

Reducing B to a known-hard A goes the wrong way for that argument. Easy problems can also reduce to hard ones, so that reverse arrow alone says nothing about B being hard.

### b09 — Four proof obligations

A complete proof states the construction, its runtime, and both directions of correctness. Showing one transformed example works demonstrates the construction, but does not prove it preserves the answer on every instance.

### b10 — Transitivity

Reductions compose: if A reduces to B and B reduces to C, composing the transformations reduces A to C. This transitivity will let one known NP-complete problem transfer hardness without rebuilding reductions from every problem in NP separately.

### b11 — Things to take note of

Things to take note of: keep the instance transformation and the solver call in the same direction, and explicitly preserve yes in both directions. When proving a new problem hard, the known-hard problem is the source; reverse that arrow and your elegant diagram proves the wrong implication, hmph.
