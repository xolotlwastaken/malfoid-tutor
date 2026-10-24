# How do we prove a recurrence bound by substitution?

## Sources

Analysis Techniques pp35–42,46; Review Week 8 pp14–16; Review Week 9 pp2–3; study notes 01-analysis §1.7.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Guess, then prove

How do we prove a recurrence bound by substitution? We will guess a concrete inequality, verify its base case, and carry it through an induction step without assuming the conclusion.

### b01 — The recurrence

Our example has T of one equal to zero and T of n equal to T of n minus one plus n minus one. Expanding a few terms suggests quadratic growth, but we must still justify that quadratic guess.

### b02 — Choose a concrete claim

We choose the concrete upper bound T of n at most n squared. This fixes the multiplicative constant at one; if that attempt failed, we would need a different constant or a stronger candidate inequality.

### b03 — Check the basis

Begin at n equal to one, where the actual recurrence gives zero. Since zero is at most one squared, the base case holds.

### b04 — State the hypothesis

Now assume the bound holds at k, namely T of k at most k squared. This is our induction hypothesis about the smaller input, not an assumption that the desired bound already holds at k plus one.

### b05 — Substitute into the recurrence

Apply the recurrence first: T of k plus one equals T of k plus k. Substituting the hypothesis gives at most k squared plus k, which is at most k squared plus two k plus one.

### b06 — What has been proved?

That closes the step, and induction proves the claimed upper bound for all positive integer n. Therefore the function is big O of n squared, but this proof alone has not supplied a matching lower bound.

### b07 — Add the missing lower bound

To make the result tight, expand the recurrence completely. It sums one through n minus one, giving n times n minus one over two and therefore Theta of n squared.

### b08 — Induct on the right domain

For a divide-by-two recurrence, it can be easier to induct over powers of two. Assume the statement for input two to the k and use it to prove the statement for input two to the k plus one.

### b09 — A failed base case

Consider T of n equals two T of n over two plus n minus one, with T of one equal to one. The tempting inequality T of n at most c n log base two of n fails at n equal to one, because its right side is zero.

### b10 — Repair and verify the proof

We can instead start the power-of-two induction at n equal to two, where T of two equals three. Choosing c at least two makes the base hold, and substituting the hypothesis yields c n log n minus c n plus n minus one, which stays below c n log n.

### b11 — A repair still needs proof

A different valid repair is to strengthen the candidate bound by adding a linear term. Whatever repair you choose, it must be checked against the recurrence and the actual domain rather than being waved away as a small-input detail.

### b12 — Things to take note of

Things to take note of: distinguish the guess from its proof, fix your constants, and substitute only a hypothesis established for smaller inputs. Check the base and state whether you proved O or Theta; the missing half of a tight-bound argument will not prove itself, obviously.
