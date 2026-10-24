# What determines Rabin–Karp’s actual runtime?

## Sources

String Matching pp15–19,25,56; study notes 07-string-matching §7.4.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Count two kinds of work

What determines Rabin–Karp's actual runtime? We will keep rolling work separate from candidate verification, count the earlier collision example, and distinguish useful expected behaviour from a worst-case guarantee.

### b01 — The complete small scan

Use pattern twenty-five in text one two two five, base ten and modulus thirteen. There are three legal windows, twelve, twenty-two and twenty-five, whose hashes are twelve, nine and twelve.

### b02 — First candidate: collision

The first equal hash is a spurious hit, meaning a hash agreement whose strings differ. Verification rejects after comparing only the first digits, so that candidate costs one character check rather than the full pattern length.

### b03 — Other windows

The middle window has a different hash, so it needs no character verification. The final window has an equal hash and two matching digits, adding two character comparisons and returning the match.

### b04 — Keep distinct counters

The total is three window-hash decisions and three actual character comparisons, with two rolling updates after the first hash. A hash comparison, a modular arithmetic operation and a character comparison are related costs, but they are not interchangeable counters.

### b05 — A candidate-dependent bound

Let h be the number of equal-hash candidates actually verified during a scan. Each candidate can require up to m comparisons, in addition to the linear-scale rolling work and the pattern-length initialisation.

### b06 — Combine the components

This yields big O of n plus m plus h m under constant-time word arithmetic. The expression makes the assumption visible: a small number of candidate hits supports near-linear behaviour, while many expensive candidates do not.

### b07 — h·m is an upper bound

Equal hashes do not all have the same verification cost. Some fail immediately, some fail only after a long matching prefix, and the first genuine occurrence stops a first-match implementation.

### b08 — Worst-case scan work

For worst-case behaviour, many windows can pass the hash filter and disagree late in direct verification. Up to n minus m plus one windows can each require order m checks, giving the familiar quadratic-style product bound.

### b09 — Do not lose initialisation

The pattern-length initial work remains necessary even for a text with a single complete window. Keep it separate when stating precise parameter-sensitive bounds instead of silently assuming that n minus m plus one is large.

### b10 — Expected behaviour needs assumptions

A large prime can reduce typical spurious hits, but cannot eliminate the pigeonhole possibility of collisions. Expected near-linear statements require suitable assumptions about the inputs or hashing, not merely the adjective large.

### b11 — Asymptotics and practical overhead

The deck also discusses measured overheads such as function calls, character conversion and modular division. These observations explain why a good asymptotic model need not predict every small practical benchmark, and they are not new measurements of this implementation.

### b12 — Things to take note of

Things to take note of: count rolling work and verification work separately, identify genuine versus spurious hits, and state the model behind expected bounds. Verification keeps the algorithm exact, while the hash filter controls how much of that verification work it can avoid, do keep up.
