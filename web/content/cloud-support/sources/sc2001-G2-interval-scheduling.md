# Why does earliest-finish interval scheduling work?

## Sources

Greedy Algorithms pp8–13; Review Week 9 p4; study notes 06-greedy-and-dp §§6.1,6.3.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Choose a compatible subset

Why does earliest-finish interval scheduling work? We will choose the largest compatible subset of jobs on one resource, trace every acceptance and rejection, and justify the greedy rule by an exchange argument.

### b01 — Endpoint convention

Represent a job as an interval including its start but excluding its finish. Two jobs that meet at an endpoint are therefore compatible, because the first has finished exactly when the second begins.

### b02 — Earliest finish first

The rule is to sort jobs by increasing finish time. Scan that order and accept a job exactly when its start is at least the finish of the last accepted job.

### b03 — Sort the jobs

Our five jobs are A from zero to three, B from one to two, C from two to four, D from three to five, and E from four to six. Their finish order is B, A, C, D, E, so the scan begins with B.

### b04 — Accept B; reject A

Accept B, which occupies the resource from one to two. Set the last accepted finish to two; A then starts at zero and conflicts, so reject A without changing that finish marker.

### b05 — Accept C; reject D

C starts at two, exactly the marker, so accept C and move the marker to four. D starts at three and conflicts, so it is rejected while the marker stays at four.

### b06 — Accept E

E starts at four, so accept it after C. The result B, C, E contains three jobs, and its touching endpoints are valid under our interval convention.

### b07 — Start the exchange argument

To prove the rule, consider an optimal solution agreeing with greedy for the longest possible prefix. At the first difference, greedy chooses a compatible job that finishes no later than the optimal solution's next job.

### b08 — Exchange without losing jobs

Replace that optimal job by greedy's choice. It remains compatible with the common prefix, and because it finishes no later, every later job from the optimal schedule still fits.

### b09 — Conclude optimality

The replacement preserves optimality and extends the agreeing prefix, contradicting its maximal choice. Repeating this reasoning establishes that earliest-finish greedy attains a maximum-cardinality compatible subset. If greedy stopped with another optimal job still compatible, its scan would have accepted another job, so it cannot terminate earlier than that agreeing optimum.

### b10 — Disprove other local rules

Choosing the smallest start time is not interchangeable: a job from zero to ten can block three jobs from one to two, two to three, and three to four. Shortest duration also fails, because the job from three to five blocks both zero to four and four to eight.

### b11 — Complexity and implementation

Sorting costs big O of n log n, and the scan costs big O of n, or linear total if finish order is already given. Only accepted jobs update the marker, and its initial value must be a valid lower bound on starts, rather than blindly zero when negative times are allowed.

### b12 — Things to take note of

Things to take note of: this is unweighted subset selection on one resource, and changing the objective can invalidate the proof. Interval partitioning schedules every job using the fewest resources and is excluded in the supplied review, so do not answer a different problem just because its name sounds familiar.
