# How do both Boyer–Moore rules combine in a search?

## Sources

String Matching pp27,50,55–58; study notes 07-string-matching §7.8; independent trace in edit/planning/sc2001-post-week07/worked-example-checks.json.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — A complete course-convention scan

How do both Boyer–Moore rules combine in a full search? We will use the course's six-character pattern, track all eighteen comparisons, and explain why a pointer jump is the maximum of the two table suggestions.

### b01 — Combine safe exclusions

Character jump uses the mismatching text character, while match jump uses the suffix already matched. Both rule out impossible nearer alignments, so taking the maximum respects both exclusions rather than adding the suggestions together.

### b02 — The two tables

For this six-character pattern, character jumps are zero for W, one for O, and six for an absent character. The match-jump entries for k one through six are eight, seven, six, seven, three and one.

### b03 — First mismatch

Begin with j and k both six. Text position six contains N, so comparison one fails immediately; the maximum of character jump six and match jump one advances j to twelve.

### b04 — Three matches, then a mismatch

At position twelve, W matches W; then O matches O at eleven and W matches W at ten. L mismatches W at nine, so this alignment has used four comparisons and the running count is five.

### b05 — Jump, then reject M

At that mismatch, character L is absent and k is three, giving table suggestions six and six. Increment j from nine to fifteen and reset k to six, then text M mismatches W immediately for comparison six.

### b06 — A longer matched suffix

M is absent, so an increment of six takes j to twenty-one. The comparisons at twenty-one, twenty and nineteen match W, O and W. Positions eighteen and seventeen then match another W and O, bringing the count to eleven.

### b07 — Good suffix chooses the larger jump

At position sixteen, M disagrees with the first pattern W, giving comparison twelve. The bad-character suggestion is six, but match jump at k one is eight, so advance j by eight to twenty-four.

### b08 — Reset for the final alignment

This is why adding the two suggestions would be wrong: eight already describes the safe combined lower limit required here. Reset k to six and begin the next alignment with its right endpoint at twenty-four.

### b09 — The six final matches

At positions twenty-four, twenty-three and twenty-two, W, O and W match the last three pattern characters. At positions twenty-one, twenty and nineteen, W, O and W match the first three, giving six more comparisons.

### b10 — Return the first match

Now k has reached zero and j is eighteen, so return j plus one, position nineteen. The alignment counts were one, four, one, six and six, summing to eighteen actual character comparisons.

### b11 — What each algorithm reuses

Naive matching rechecks each next window, Rabin–Karp reuses a rolling hash, and Boyer–Moore reuses mismatch and suffix structure. Skipping many text comparisons can be excellent on suitable inputs, but the shown variant retains a general big O of n m scan upper bound.

### b12 — Do not overclaim the comparison

The comparison slides mention KMP and practical performance observations without developing its preprocessing algorithm here. Keep such context separate from a proven bound for this exact Boyer–Moore variant, and count table preprocessing separately when its implementation is specified.

### b13 — Things to take note of

Things to take note of: preserve the supplied table convention, decrement both pointers on matches, take the maximum after a mismatch and reset k. Return j plus one only after k reaches zero, keep a genuine comparison counter, and never confuse a moving pointer with a moving alignment, hmph.
