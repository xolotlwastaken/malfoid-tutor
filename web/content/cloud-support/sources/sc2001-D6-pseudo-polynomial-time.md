# Why is knapsack DP only pseudo-polynomial?

## Sources

Dynamic Programming pp64–65; Introduction to NP p14; study notes 06-greedy-and-dp §6.11.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Value versus encoded size

Why is knapsack dynamic programming only pseudo polynomial? We will distinguish a numeric value from the number of bits encoding it, then compare knapsack and coin change with longest common subsequence.

### b01 — What counts as input length?

A polynomial-time claim is measured against the length of the input representation. Writing a string of n characters explicitly supplies n symbols, but a binary integer can represent a much larger numeric value in only a few bits.

### b02 — A concrete representation

For example, binary one thousand is the number eight, represented by four bits. A capacity-eight table uses entries up to eight even though the capacity field itself has only four written symbols.

### b03 — Substitute the bit length

With b bits, the largest unsigned capacity is two to the b minus one. A table indexed through every capacity may therefore require exponentially many entries in b, despite being linear in the value C.

### b04 — Knapsack cost in bits

The zero-one knapsack table has n item choices and C capacity values, giving big O of n C work. If C is near two to the b, that expression becomes order n times two to the b, not a polynomial in n and b.

### b05 — Meaning of pseudo-polynomial

We call this pseudo polynomial time. The runtime is polynomial in the numeric capacity, without a polynomial bound in the encoded input length. This describes the given algorithm and representation, not a claim that every input always takes its largest possible table.

### b06 — Coin change has the same issue

Minimum-coin DP has the same issue with its target amount A. Big O of k A depends on all amounts up to A, while the binary target field occupies only order log A bits.

### b07 — LCS is polynomial

Longest common subsequence is different because its two strings are explicitly listed. Their lengths n and m already contribute n plus m input symbols, so the n m table is polynomial in that total length.

### b08 — Name the parameters

The symbols n and m alone do not decide the classification. You must state whether a parameter measures an explicit sequence length, a numeric amount, or an encoding length before interpreting its appearance in a runtime.

### b09 — State the arithmetic model

Our operation counts use the course assumption of constant-time arithmetic on suitable machine words. For enormous exact integers, the cost of addition, comparison and storage also depends on bit length, which should be included in a full bit-operation analysis.

### b10 — No contradiction with NP

An exact knapsack DP therefore does not establish that the knapsack decision problem has a polynomial-time algorithm in binary input size. It removes repeated subproblems effectively, but the number of capacity states still carries the numeric-magnitude dependence.

### b11 — Things to take note of

Things to take note of: separate numeric values from encoding lengths and substitute the bit-length relationship before classifying a bound. LCS is polynomial in its explicit string lengths, whereas the capacity and amount DPs depend on numeric magnitudes; a table can be neatly organised and still be very large, hmph.
