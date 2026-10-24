# How do we prove NP-completeness?

## Sources

Introduction to NP pp24–28; study notes 08-np-and-heuristics §§8.8–8.9. Verifier-to-circuit construction and p36 formal NP-hard extension are excluded from this lesson.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Two separate obligations

How do we prove NP-completeness? We will separate membership from reduction-based hardness, use SAT as a concrete decision example, and derive the consequence of a polynomial solver for any NP-complete problem.

### b01 — The definition

A decision problem D is NP-complete when it belongs to NP and every problem in NP has a polynomial-time reduction to D. The first condition provides efficiently checked yes-certificates, while the second makes D at least as hard as all NP problems under these reductions.

### b02 — The standard proof route

To prove a new target B NP-complete, normally start by describing a polynomial-length certificate and a polynomial verifier. Then reduce an already known NP-complete problem A to B, preserving yes exactly in both directions.

### b03 — Use transitivity

Why does one known source suffice for the second condition? Every NP problem already reduces to A, and transitivity composes that reduction with the new transformation from A to B.

### b04 — Satisfiability

For SAT, the input is a Boolean formula and the question is whether some assignment makes it true. A proposed assignment is a short certificate that can be checked by evaluating the formula's operations.

### b05 — Check one complete assignment

Consider A or B, and not A or C, with the two clauses joined by and. Set A true, B false and C true: the first clause is true from A, the second is true from C, and their conjunction is true.

### b06 — A witness answers existence

One satisfying assignment proves that this formula is a yes-instance, without needing to find the best assignment or test every possibility. An assignment failing one clause only rejects that candidate, just as in our earlier certificate examples.

### b07 — The supplied theorem chain

The course takes circuit satisfiability as a known NP-complete problem and discusses its reduction to SAT. Together with SAT membership in NP, that supplies the two obligations needed to classify SAT as NP-complete.

### b08 — Respect the theorem boundary

The full construction from an arbitrary polynomial verifier to a circuit is explicitly outside this course scope. We use the stated theorem here rather than pretending that a small hand-drawn circuit proves the theorem for all NP problems.

### b09 — Neither half replaces the other

A reduction from a known NP-complete source without a target-membership proof establishes the hardness part only. Conversely, a verifier alone establishes membership but says nothing about being as hard as every other NP problem.

### b10 — Equivalent under reductions

All NP-complete decision problems reduce to one another through polynomial transformations. This equivalence does not mean their best implementations have identical constants, polynomial exponents, or practical behaviour on typical instances.

### b11 — The consequence of a fast solver

If even one NP-complete problem has a deterministic polynomial-time algorithm, every NP problem inherits one through its reduction. Since P is already contained in NP, that would establish P equals NP, whose truth is currently unresolved in this framework.

### b12 — Things to take note of

Things to take note of: classify the decision version, show membership, choose a known NP-complete source and point the reduction toward your target. State the transformation and both correctness directions, then use transitivity; a prestigious problem name is not a substitute for either half of the proof, hmph.
