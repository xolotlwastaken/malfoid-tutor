# How does shortest-link TSP differ from Kruskal?

## Sources

Introduction to NP pp32–33; study notes 08-np-and-heuristics §8.12. Fresh five-vertex trace; implementation cost derivation is an explanatory addition.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Global shortest-link choices

How does the shortest-link TSP heuristic differ from Kruskal? We will scan edges in global weight order, enforce both degree and cycle restrictions, and close a spanning path into a tour.

### b01 — The acceptance rule

Unlike nearest neighbour, shortest link considers the globally lightest remaining edge rather than only edges from one current vertex. Accept it only if neither endpoint would exceed degree two and it would not create a premature cycle.

### b02 — The full input

Use five vertices with the first six sorted edges A B one, B C two, A C three, B D four, C D five and D E six. The remaining edges are A E seven, B E eight, A D nine and C E ten, completing the graph.

### b03 — Accept the first two edges

Accept A B because both endpoints have degree zero and no cycle is possible. Then accept B C, leaving B with degree two and A and C with degree one.

### b04 — Reject a premature subtour

Next consider A C, which would close the three-vertex cycle A B C A. Reject it even though the endpoint degrees would remain at most two, because D and E have not yet joined the tour.

### b05 — Reject excessive degree

Next consider B D, which would give B a third incident accepted edge. Reject it for the degree rule, even though connecting D would not create a cycle.

### b06 — Complete the spanning path

C D passes both tests, so accept it and extend the current path. Then D E also passes, giving the spanning path A, B, C, D, E with four accepted edges.

### b07 — Close the two endpoints

A path spanning all five vertices has exactly two degree-one endpoints, A and E. Add their connecting edge A E to form the final tour; this is the permitted final cycle, not a premature subtour.

### b08 — Count the final tour

The total tour cost is one plus two plus five plus six plus seven, which equals twenty-one. This trace demonstrates the rules and feasibility; it does not prove shortest link always finds an optimal TSP tour.

### b09 — Compare with Kruskal

Kruskal also scans edges globally and rejects cycles, but it permits vertices of degree greater than two. Its goal is a spanning tree, whereas shortest link must maintain path-like pieces and eventually create one Hamiltonian cycle.

### b10 — An implementation-cost derivation

Sorting E edges costs big O of E log E, and union-find plus degree counters can check the scan efficiently. With suitable union-find operations, the scan contributes big O of E times inverse Ackermann of V, alongside the sorting cost.

### b11 — Storage and comparisons

In a complete V-vertex graph, E is order V squared, so edge storage and sorting can be substantial. State tie rules if equal weights occur, and do not claim this heuristic dominates nearest neighbour on every input just because it does better in one example.

### b12 — Things to take note of

Things to take note of: track endpoint degrees and connected components separately, because each rejects a different kind of invalid choice. Stop after the spanning path, include the final closing edge, and distinguish a TSP tour from an MST before borrowing Kruskal's explanation, hmph.
