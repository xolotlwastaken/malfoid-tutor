# How does greedy coin change work, and when does it fail?

## Sources

Greedy Algorithms pp3–7; study notes 06-greedy-and-dp §§6.1–6.2.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — A locally best choice

How does greedy coin change work, and when does it fail? We will make change with a locally best choice, count the work, and then use one counterexample to test whether that choice is always optimal.

### b01 — What greedy commits to

A greedy algorithm commits to its next choice using the information currently available. It does not systematically compare all future continuations or undo the choice when a later step becomes awkward.

### b02 — Largest affordable coin

For coin change, the natural rule is to select the largest coin that does not exceed the remaining amount. Repeat until the remainder is zero, assuming positive integer denominations and an unlimited supply of coins.

### b03 — First choice

Take denominations one, five, ten and twenty-five, and make thirty-seven. The largest affordable coin is twenty-five, leaving twelve; move that coin into the selected row rather than treating it as a mathematical wish.

### b04 — Second choice

For the remainder twelve, the largest affordable coin is ten. Selecting it leaves two, which neither five nor ten can fill exactly by itself.

### b05 — Finish the change

Take a one, leaving one, then a final one, leaving zero. The completed change is twenty-five plus ten plus one plus one, using four coins.

### b06 — Division-based implementation

A faster implementation handles one denomination at a time in descending order. Integer division tells how many copies to take, and the remainder moves directly to the next denomination without an iteration for every individual coin.

### b07 — Count the implementation

If k denominations are already ordered, this division-based scan uses big O of k arithmetic operations under the course word model. Printing the chosen coins separately adds output work, while an unsorted input may also require sorting.

### b08 — Do not mix cost models

The repeated-subtraction version instead performs one choice for every coin selected. Its cost depends on how the largest affordable coin is found; rescanning all k denominations each time adds a factor that a constant-denomination assumption would hide.

### b09 — A counterexample

Now change the denominations to one, ten and twenty-five, and request thirty. Greedy still takes twenty-five first, but the remainder five requires five separate one-coins, giving six coins in total.

### b10 — A better feasible solution

Three ten-coins also make thirty, and use only three coins. This single strictly better feasible solution is enough to disprove universal optimality of largest-first greedy on arbitrary denomination systems.

### b11 — Feasible is not optimal

Having a one-coin ensures every nonnegative integer amount is reachable, but it says nothing about minimum coin count. Some denomination systems do admit this greedy rule, whereas proving that property requires more than testing a few convenient amounts.

### b12 — Things to take note of

Things to take note of: state the objective, denomination assumptions, choice rule and actual implementation cost. A counterexample disproves a general greedy claim, while many successful traces cannot establish it; when the choice fails, dynamic programming can compare the alternatives, hmph.
