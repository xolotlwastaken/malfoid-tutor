# How do we compare growth rates?

## Sources

Analysis Techniques p13; Review Week 8 pp4–8; study notes 01-analysis §§1.1,1.3.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Simplify before ranking

How do we compare growth rates? We will simplify a collection of functions, put equivalent growth rates together, and connect logarithms to a loop that repeatedly divides by two.

### b01 — Constant growth

Begin with a constant function such as one thousand. Its value can be large, but it does not increase with input size, so its growth class is constant.

### b02 — Logarithm bases

Next put logarithmic functions together, regardless of their fixed base. The change-of-base formula turns one logarithm into a fixed constant times another, so their Theta class is the same.

### b03 — Simplify the expression

The logarithm of n squared belongs in that same group, because it equals twice the logarithm of n. Do not confuse squaring inside the logarithm with squaring the logarithm itself.

### b04 — Logarithms and powers

Now compare logarithmic growth with the square root of n and with n itself. Every fixed positive power of n eventually outgrows a logarithm, even if a small numerical example initially makes the difference look modest.

### b05 — Polynomial region

Multiplying n by log n places it above linear growth but below a quadratic. Larger fixed polynomial exponents follow, giving n squared before n to the fifth.

### b06 — Exponential region

Fixed-base exponentials eventually outgrow every fixed-degree polynomial. Changing an exponential base generally matters: two to the n, three to the n, and four to the n form different growth rates.

### b07 — Parentheses matter

Two to the power two n simplifies to four to the n. It is not the double exponential two raised to two to the n, so read the parentheses before rearranging your function cards.

### b08 — Complete growth order

Factorial eventually exceeds any fixed-base exponential, while n to the n grows faster still. Our full ordering therefore runs from constants through logarithms, powers and exponentials, then factorial, then n to the n.

### b09 — An actual halving loop

Let us now derive a logarithm instead of merely recognising its name. Starting from sixty-four, repeatedly divide by two to get thirty-two, sixteen, eight, four, two, then one, using six divisions.

### b10 — Derive the iteration count

For an exact power of two, solving n divided by two to the x equals one gives x equals log base two of n. Starting at one and repeatedly doubling until reaching at least n instead requires the ceiling of that logarithm.

### b11 — Specify the loop

For other input sizes, floor division and the stopping condition determine the exact integer count. A loop that keeps dividing while its value exceeds one differs in detail from a real-number loop that stops once it falls below one, although both have logarithmic order.

### b12 — Things to take note of

Things to take note of: simplify first, group Theta ties, and distinguish logarithm bases from exponential bases. Derive loop counts from their updates and stopping conditions, and remember that a finite graph illustrates growth but does not prove the eventual order, how charming.
