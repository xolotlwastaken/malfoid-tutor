# How does Hamiltonian path reduce to TSP?

## Sources

Introduction to NP pp22–23, physical p22 visually checked; study notes 08-np-and-heuristics §8.7.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Source problem → target problem

How does Hamiltonian path reduce to TSP? We will construct a complete weighted graph, choose the correct threshold, and prove both directions instead of relying on one persuasive picture.

### b01 — Path versus tour

A Hamiltonian path visits every vertex exactly once without requiring a return to its start. A Hamiltonian tour additionally closes the route, and that extra closing edge is why the threshold in this construction needs care.

### b02 — Complete the graph

Assume an undirected graph G with at least three vertices, and call its vertex count n. Build a complete graph T on exactly the same vertices, so every missing original connection now also has an edge.

### b03 — The transformation

Assign weight one to edges already in G and weight two to the newly added edges. Ask whether T has a Hamiltonian tour of total cost at most n plus one.

### b04 — An explicit source witness

In the five-vertex slide graph, original edges are A B, A C, A D, B E, C E and C D. The route E, B, A, C, D visits every vertex once using four original edges, so it is a Hamiltonian path in G.

### b05 — Close the path

Close that path from D back to E in the complete graph. The closing edge was absent from G and therefore costs two, giving total four plus two equal to six, which is n plus one.

### b06 — Forward implication

The forward proof is general: a Hamiltonian path uses n minus one original edges of cost one. Its closing edge costs either one or two, so the resulting tour costs at most n plus one.

### b07 — Reverse: count the expensive edges

For the reverse proof, suppose the transformed graph has a tour costing at most n plus one. A Hamiltonian tour has exactly n edges, each costing at least one, so there is room for at most one weight-two edge.

### b08 — Remove the added edge

If the tour includes a weight-two edge, delete that single edge. What remains is a Hamiltonian path using only weight-one edges, all of which belong to the original graph G.

### b09 — Also handle zero expensive edges

If every tour edge has weight one, remove any one of them instead. Again the remaining route visits all vertices exactly once using original edges, completing the reverse implication.

### b10 — Transformation cost

The construction inspects vertex pairs and assigns their weights in big O of n squared time under a suitable graph representation. Its output size is also polynomial, and the threshold n plus one has a short binary encoding.

### b11 — Why the threshold is not n

Using threshold n would demand that every tour edge already existed in G. That would ask for an original Hamiltonian cycle and could reject a graph that has a Hamiltonian path but needs one missing edge to close it.

### b12 — Things to take note of

Things to take note of: preserve the same vertices, distinguish original and added edges, and prove both directions with the exact threshold n plus one. One added closing edge is allowed, two are not; that simple count is the argument your diagram must actually explain, hmph.
