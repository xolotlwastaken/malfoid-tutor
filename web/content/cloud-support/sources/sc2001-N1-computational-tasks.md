# What makes a computational task hard?

## Sources

Introduction to NP pp3–8; study notes 08-np-and-heuristics §§8.1–8.2.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Specify the actual task

What makes a computational task hard? We will identify the required output, derive the work of printing a Hanoi solution, and distinguish decision questions from optimisation objectives.

### b01 — Difficulty is not coding effort

A task can be difficult to understand or code without having a bad asymptotic running time. Complexity analysis instead asks how the required resources grow as the encoded input grows, with a clear statement of what the algorithm must produce.

### b02 — The explicit Hanoi task

For Towers of Hanoi, move disks between three pegs without placing a larger disk on a smaller one. The standard recursive method transfers the smaller stack, moves the largest disk, and transfers the smaller stack again.

### b03 — A complete three-disk trace

With three disks, label the source A, destination B and spare C. The seven moves are A to B, A to C, B to C, A to B, C to A, C to B and A to B, with each move involving the only legal top disk for that step.

### b04 — Derive the output count

The move count has base one for one disk and recurrence M of n equals twice M of n minus one plus one. Expanding gives two to the n minus one, so printing every move necessarily requires time proportional to that exponentially long output.

### b05 — Different output, different task

Computing only the number of moves is a different output task from listing them all. The binary representation of two to the n minus one has only n bits, so an output-size argument about the full move list cannot be transferred unchanged to returning that count.

### b06 — Use a sound hardness argument

The slide's numerical estimate for sixty-four disks is incorrect, so retain the exact move-count derivation rather than memorising that runtime. An exponential output requirement is concrete evidence for this listing task, while a slow known algorithm alone is not a proof that every algorithm for another task must be slow.

### b07 — Decision versus optimisation

A decision problem asks for yes or no, such as whether a tour has cost at most K. An optimisation problem instead asks for the cheapest valid tour or its minimum cost.

### b08 — Write the correct thresholds

For a spanning tree, the decision question asks whether some spanning tree has total cost at most K. For zero-one knapsack, it asks whether some subset has weight at most C and profit at least K, keeping the two inequalities distinct.

### b09 — Relate the two versions

An exact optimisation solver can answer its related threshold question by comparing its optimum with K. Thus a hardness result for the decision version can imply difficulty for exact optimisation, but the formal P and NP definitions here classify decision problems.

### b10 — Connect to input encoding

Input representation also matters when numbers appear in a problem. A binary capacity has logarithmic encoding length in its numeric value, so an algorithm looping over that entire value needs a different complexity interpretation from one reading an explicitly listed string.

### b11 — Things to take note of

Things to take note of: state the input encoding, output requirement and objective before classifying a task. Distinguish a listing lower bound from a slow known search, preserve threshold inequalities, and avoid calling every inconvenient problem provably exponential, hmph.
