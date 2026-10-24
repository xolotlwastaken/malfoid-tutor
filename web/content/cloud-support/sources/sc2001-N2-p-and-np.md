# What are P and NP, and what does verification mean?

## Sources

Introduction to NP pp9–19; study notes 08-np-and-heuristics §§8.3–8.5.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Solve versus verify

What are P and NP, and what does verification mean? We will separate finding a solution from checking a complete certificate, explain why P is contained in NP, and examine a tempting but invalid universal-tour claim.

### b01 — Define P

P contains decision problems solvable by a deterministic algorithm in polynomial worst-case time. A polynomial bound is an asymptotic classification, not a promise that every polynomial algorithm is practical for every input size.

### b02 — Define NP

NP contains decision problems whose yes-instances have polynomial-length certificates that a deterministic polynomial-time procedure can verify. The course's equivalent description uses a nondeterministic guess followed by verification, not ordinary random guessing with a guaranteed good outcome.

### b03 — A complete TSP certificate

For a TSP threshold question, a certificate can list a proposed tour. The verifier must check the vertices, all required edges, the closing return and the total cost, rather than accepting because the route merely looks plausible.

### b04 — Every condition matters

A route that repeats a vertex and omits another fails even if it is cheap. A route visiting every vertex also fails if its cost exceeds K, because the certificate must establish the entire yes-condition.

### b05 — A knapsack verifier

For knapsack, a certificate can specify the selected item indices. Check that no item is repeated, total weight is at most capacity and total profit is at least the requested threshold, with numeric operations accounted for in the representation model.

### b06 — Candidate rejection is not a no-proof

If one candidate fails verification, only that candidate has been rejected. Another candidate may succeed, so failure of a proposed certificate does not establish that the whole input is a no-instance.

### b07 — Why P ⊆ NP

Every problem in P also belongs to NP, because a polynomial verifier can simply run the polynomial solver. It does not need a useful certificate at all, which immediately disproves the idea that NP means not polynomial.

### b08 — What is and is not known

The absence of a known efficient algorithm is not part of the NP membership definition. Whether P equals NP is unresolved in the course framework, so do not draw a strict separation as an established theorem.

### b09 — Existential versus universal

Compare the question whether some tour costs at most K with the question whether every tour does. A single cheap tour witnesses the existential yes-condition, but cannot establish that every other tour is cheap.

### b10 — Do not infer an unproved separation

For the universal question, one expensive tour can instead witness a no-answer. This complementary-certificate observation does not prove that the universal problem lies outside NP or requires exponential time, despite the unsupported claims on the slide.

### b11 — Two polynomial requirements

Certificate length must be polynomial as well as verification time, and the verifier checks a yes-witness for the exact decision predicate. Guessing a whole enormous computation is not useful if merely reading the claimed certificate already exceeds the allowed bound.

### b12 — Things to take note of

Things to take note of: define the decision question, give a complete witness and explain every verification check. Keep solving separate from checking, remember P is inside NP, and never turn a failed witness into a proof of nonexistence, how charming.
