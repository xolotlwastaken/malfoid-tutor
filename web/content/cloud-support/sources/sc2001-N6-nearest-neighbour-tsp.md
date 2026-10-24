# How can nearest-neighbour TSP miss the best tour?

## Sources

Introduction to NP pp29–31; study notes 08-np-and-heuristics §§8.10–8.11. Fresh counterexample assumes a complete undirected graph without triangle inequality.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — A fast greedy heuristic

How can nearest-neighbour TSP miss the best tour? We will trace its locally cheapest moves, include the final return edge, and compare the completed route with a much cheaper feasible tour.

### b01 — Nearest-neighbour rule

Start at a specified vertex and repeatedly choose its cheapest unvisited neighbour. Keep a visited set, move to the chosen neighbour, and finally return to the starting vertex once every vertex has been visited.

### b02 — A fully specified graph

Our four vertices are A, B, C and D, with A B and B C both costing one. Edges A C, A D and B D cost two, while C D costs one hundred, making one late continuation very expensive.

### b03 — First local choice

Start at A and choose B, because its edge costs one rather than two. Mark B visited, and consider only vertices that have not already appeared in the partial route.

### b04 — Second local choice

From B, C costs one and D costs two, so choose C. The partial route A, B, C has cost two, but its cheap prefix has left only D unvisited.

### b05 — Pay the late continuation

The next move C to D is forced and costs one hundred. Then include the final return D to A costing two, giving a complete greedy tour of one hundred four.

### b06 — A better feasible tour

Now inspect the feasible tour A, C, B, D, A instead. Its edge costs are two, one, two and two, for a total of seven, strictly below one hundred four.

### b07 — What the counterexample proves

One better feasible tour is enough to show the greedy result is not optimal. We do not need an exhaustive optimality proof for the seven-cost route to refute the claim that the one-hundred-four route is always best.

### b08 — Heuristic versus guarantee

A heuristic aims to find a useful solution quickly without an automatic optimality guarantee. A proven approximation ratio is a different claim and requires explicit assumptions and a theorem, not merely a few successful runs.

### b09 — State the counterexample assumptions

This graph does not satisfy the triangle inequality, since the C to D edge is far more expensive than travelling through B. Keep that limitation explicit rather than using this example to assert a theorem about metric TSP variants.

### b10 — Complexity and reproducibility

Scanning all unvisited neighbours at each of n steps gives big O of n squared time and linear visited bookkeeping. The graph representation has its own storage cost, and different starting vertices or ties can change the produced tour.

### b11 — Feasibility assumption

On an incomplete graph, the simple rule can also get stuck or fail to close its tour. Our complete-graph assumption avoids that feasibility issue but does not repair its lack of optimality.

### b12 — Things to take note of

Things to take note of: show the start, visited set, local comparisons and final closing edge. Compare the whole tour with a concrete better route, state ties and graph assumptions, and remember that a cheap beginning can conceal a very expensive ending, how charming.
