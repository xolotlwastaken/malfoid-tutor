# When does the Master Theorem fail?

## Sources

Analysis Techniques pp32–33; study notes 01-analysis §1.6.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Check before applying

When does the Master Theorem fail? We will test its required form, distinguish logarithmic and polynomial gaps, and explain why the regularity condition cannot simply be ignored.

### b01 — Wrong recurrence shape

First check that the recurrence really has a constant number of equal-shrink subproblems. T of n minus one plus n does not have a fixed shrink factor greater than one, so this Master Theorem does not directly apply.

### b02 — Unequal subproblems

Likewise, a call on n over two and another on n over three do not fit the equal-size form. That does not make the recurrence unsolvable; it means you must use another justified method.

### b03 — A valid form, but no case

Now consider three T of n over three plus n divided by log n, with a suitable constant-size base. Its form fits, and p equals one, so the benchmark is n.

### b04 — Smaller is insufficient

The local work is smaller than n, because dividing by log n makes its ratio to n approach zero. But case one needs more than simply being smaller: it needs a fixed polynomial gap.

### b05 — No positive epsilon works

Divide n over log n by n to the one minus epsilon. The ratio becomes n to the epsilon over log n, which grows without limit for every fixed positive epsilon, so the required case-one upper bound fails.

### b06 — The supplied case 2 misses it

Case two does not apply either, because n over log n is not Theta of n. The extended logarithmic version supplied by this course requires a nonnegative logarithmic exponent, whereas this example would need minus one.

### b07 — Identify the actual gap

Case three cannot help because this local cost is smaller, not polynomially larger, than the benchmark. The example lies between cases one and two of the stated theorem, correcting the case-number label on the slide.

### b08 — Use an appropriate alternative

A recursion-tree expansion offers a way forward without forcing the wrong theorem. At level i the combined work is n divided by log of n over three to the i, so you must sum those varying level costs with a proper base threshold.

### b09 — Why regularity matters

Now look at the other common omission, case-three regularity. A large value of f at one scale does not guarantee that the sum of the child-scale costs contracts by a constant factor.

### b10 — An irregular local-cost example

For a clean counterexample, define f of n as n cubed at powers of two and n otherwise, and consider T of n equals T of n over three plus f of n on exact multiples. Although f is always at least n, at n equal to three times a power of two the child cost can be cubic while the parent cost is only linear.

### b11 — Check the failed inequality

Consequently, no fixed contraction constant can establish regularity there, even though f exceeds the constant leaf benchmark by a polynomial factor. This is an explanatory example of the condition, not a transcription of the slide whose extracted formula is ambiguous.

### b12 — Things to take note of

Things to take note of: verify the recurrence shape and every case condition before using the conclusion. A logarithmic gap is not a polynomial gap, missing regularity matters, and iteration or substitution remains available when this theorem has nothing to say, hmph.
