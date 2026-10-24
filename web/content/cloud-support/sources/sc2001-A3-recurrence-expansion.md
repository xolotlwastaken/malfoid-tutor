# How do we build and expand a recurrence?

## Sources

Analysis Techniques pp14–19,21–22,24–27; study notes 01-analysis §§1.4–1.5.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — A recurrence models work

How do we build and expand a recurrence? We will count subproblems, track the work at every level, and include the leaves before deriving a tight running-time bound.

### b01 — Identify the ingredients

A recurrence must describe what the algorithm actually does. Count the number of recursive calls, the input size of each call, and the local work outside those calls, instead of guessing from the height alone.

### b02 — The example recurrence

Our course example makes three recursive calls on quarter-size inputs and performs n units of local work. With constant base cost one, this becomes T of n equals three T of n over four plus n, with T of one equal to one. For this expansion, take n to be a power of four.

### b03 — Root and first level

Start at input size sixty-four and draw the first three children, each of size sixteen. The root performs sixty-four units locally, while those three children together perform forty-eight units.

### b04 — Second level

Each size-sixteen child creates three size-four children, giving nine nodes on the next level. Their local work totals thirty-six, which is another factor of three quarters smaller.

### b05 — Reach the leaves

One more expansion creates twenty-seven size-one leaves. Each costs one by the base condition, so their total cost is twenty-seven rather than thirty-six or sixty-four.

### b06 — General level

At a general level i, there are three to the i subproblems, each with size n over four to the i. Multiplying those quantities gives n times three quarters to the i as the total non-leaf work on that level.

### b07 — Stopping depth and leaves

Stop when n divided by four to the L reaches one. The depth L is therefore log base four of n, and the number of leaves is three to the L, equivalently n to the log base four of three.

### b08 — Sum all the work

Now add every internal level and the leaf cost, without counting the leaf level twice. The internal sum is n times a geometric series with ratio three quarters, ending just before depth L.

### b09 — Prove an upper bound

The infinite version of that geometric series sums to four, so our finite internal sum is at most four n. The leaf exponent is less than one, so the leaves do not raise the order above linear.

### b10 — Make the bound tight

The root alone already performs n units, supplying a matching linear lower bound. Combining the lower and upper bounds proves Theta of n, not merely big O of n.

### b11 — Compare familiar shapes

Compare this with merge sort, where two half-size calls make total work per level stay linear. There the linear work repeats for logarithmically many levels, giving Theta of n log n; binary search instead follows one branch with constant local work.

### b12 — Things to take note of

Things to take note of: state the base case, count branches and shrinkage separately, and find the stopping depth before simplifying the sum. Include the leaf work, justify both sides of a tight bound, and never mistake tree depth for total work, hmph.
