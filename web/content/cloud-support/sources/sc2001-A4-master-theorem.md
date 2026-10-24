# How do we apply the full Master Theorem?

## Sources

Analysis Techniques pp20–31; Review Week 8 p13; Review Week 10 pp2–4; study notes 01-analysis §1.6.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — The full course theorem

How do we apply the full Master Theorem? We will identify its parameters, check the conditions in each case, and work through examples including the logarithmic extension required by this course.

### b01 — Extract the parameters

The theorem applies to a fixed number a of equal-shrink recursive subproblems, each of size n over b. The function f counts local work, and the comparison exponent p equals log base b of a.

### b02 — Where nᵖ comes from

Why compare against n to the p? The recursion has log base b of n levels and a to that power leaves, so n to the p is the scale of the constant-cost leaf work.

### b03 — Case 1: polynomially smaller

In case one, local work is polynomially smaller than n to the p. You must find a fixed positive epsilon such that f is big O of n to the p minus epsilon, and the result is Theta of n to the p.

### b04 — Case 1 example

Consider three T of n over three plus two. Here a and b are three, p is one, and the constant local cost is big O of the square root of n, so epsilon one half works and the answer is Theta of n.

### b05 — Case 2: equal scales

In case two, local work matches the leaf scale and each level contributes at the same overall order. If f is Theta of n to the p, summing across the levels gives Theta of n to the p times log n.

### b06 — Case 2 example

For four T of n over four plus n minus one, p is one and the local cost is Theta of n. This matches case two and gives Theta of n log n.

### b07 — Extended case 2

The course includes an extension of case two for additional nonnegative powers of a logarithm. If f is Theta of n to the p times log to the k of n, the solution adds one more logarithmic power.

### b08 — Logarithmic example

Apply that extension to two T of n over two plus n log n. We have p equal to one and k equal to one, so the result is Theta of n log squared n, rather than Theta of n log n.

### b09 — Case 3 has two conditions

Case three requires f to be polynomially larger than n to the p, and it also requires regularity. For all sufficiently large n, a times f of n over b must be at most c times f of n for a fixed c less than one.

### b10 — Case 3 example

For two T of n over four plus n, p is one half, and epsilon one half establishes the polynomial gap. Regularity holds because twice f of n over four is n over two, so c one half works and the solution is Theta of n.

### b11 — A less familiar recurrence

As a transfer example, seven T of n over two plus fifteen n squared over four has p equal to log base two of seven. The quadratic local cost is polynomially smaller, making this case one and giving Theta of n to that exponent.

### b12 — Things to take note of

Things to take note of: write a, b, f and p explicitly, then justify the selected case rather than merely stating its answer. Include epsilon for polynomial gaps and regularity for case three; the course review specifically asks for this full version, so do keep up.
