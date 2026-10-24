# SC2001 after week 7: analysis and lesson breakdown

Prepared 24 October 2026 (source analysis began 23 October). **Status: awaiting approval of this plan.**

This stage covers source analysis, lesson design, and a reusable pipeline skill. No narration, videos, question bank, website content, commits, pushes, or deployments have been produced for this expansion. Question coverage below is a blueprint, not authored questions.

## Scope and evidence

The supplied schedule is in **Analysis Techniques, physical PDF p3**:

| Week | Scheduled material | Proposed lessons |
|---|---|---|
| 8 | Analysis techniques | A1–A4 |
| 9 | Greedy algorithms and DP; analysis review | A5–A7, G1–G3, D1 |
| 10 | Dynamic programming | D2–D4 |
| 11 | Dynamic programming and string matching | D5–D7, S1–S2 |
| 12 | String matching | S3–S6 |
| 13 | Introduction to NP | N1–N8 |

The allocation of individual lessons is a proposed teaching order, not a claim that each subtopic was delivered in that exact week. Chapter file prefixes 11–15 are **not week numbers**. Review decks reinforce the relevant topics rather than becoming duplicate courses.

**Recommendation: 31 complete lessons**, approximately **115–148 minutes** in total. These are planning estimates; teaching clarity determines final length. Most lessons should take 3–5 minutes; full DP and Boyer–Moore traces may need 5–7. Do not fragment an algorithm's mechanism, example, complexity and takeaways into unrelated micro-reels.

### Sources actually checked

Readable originals are under `/Users/joelloh/Documents/School/SC2001/SC2001_slides_recordings/`. The workspace's Google Drive source folder contains corresponding named entries. Source verification in this pass used the readable local originals; it did not assume cloud placeholders were fully downloaded.

All **272 physical pages across eight later PDFs** were checked against the existing page-text caches using fresh local PDF extraction; page counts and normalized extracted text match throughout. SHA-256 hashes and results are in `edit/planning/sc2001-post-week07/source-verification.json`. Relevant text and study-note sections were reviewed. Three diagrams were also rendered and visually inspected: String Matching p40; Introduction to NP p22; Dynamic Programming p44.

| Short name used below | PDF | Physical pages | Study-note companion |
|---|---|---:|---|
| Analysis | `11 - AnalysisTechniques.pdf` | 46 | `study-notes/sc2001/01-analysis.md` §§1.1–1.7 |
| Greedy | `12 - GreedyAlgorithms.pdf` | 18 | `06-greedy-and-dp.md` §§6.1–6.4 |
| DP | `13 - DynamicProgramming.pdf` | 67 | `06-greedy-and-dp.md` §§6.5–6.12 |
| Strings | `14 - StringMatching.pdf` | 58 | `07-string-matching.md` §§7.1–7.8 |
| NP | `15 - IntroductionToNP.pdf` | 36 | `08-np-and-heuristics.md` §§8.1–8.13 |
| R8 | `Review_Week 8.pdf` | 16 | Analysis notes and source ledger |
| R9 | `Review Week 9.pdf` | 13 | Analysis / DP notes |
| R10 | `Review Week 10.pdf` | 18 | Analysis / DP notes |

**Recording gap:** both discovered SC2001 recording collections and the existing transcript cache stop at week 7. No matching later lecture recording or transcript was found. No later recording ranges can be claimed. Lessons below have slide-and-note grounding only; proceeding to their production requires acceptance of this limitation or supplying the missing recordings. Approval of this plan can explicitly accept the limitation. Earlier recordings may support named prerequisites but cannot stand in for later lectures.

The note source ledger is `study-notes/sc2001/SOURCES.md`. It contains useful corrections, but its extracted diagrams are not automatically authoritative: for example, fresh visual inspection confirms DP p44 has **X=ACGGA, Y=ACTG**, not the reversed strings suggested by raw text order.

### Prerequisites and format

Reuse weeks 1–7 rather than recreating sorting, heaps, graph search, shortest paths, MST or union-find. The dependency sequence is:

`analysis → greedy → DP → string matching → P/NP and reductions → heuristics`

NP also draws on the graph and knapsack lessons. Each video opens by naming the topic, states the problem and assumptions, animates real intermediate states, explains correctness and the relevant complexity/proof, and closes with **“Things to take note of.”** Follow `$malfoid-explainer`: approved fixed-reference local Qwen voice, seven clean main poses changing every 2–3 spoken sentences, vertical graph-paper format, final caption layer, and independently verified examples. Target durations below are estimates.

## Analysis techniques — seven lessons

### A1 — What do O, Ω and Θ actually mean? · 3–4 min

- **Sources:** Analysis pp5–12; R8 pp2–3; notes §§1.1–1.2. Prerequisite: simple operation counts from sorting.
- **Teaching sequence:** choose an input-size parameter and counted operation; distinguish an upper, lower and tight bound; introduce constants and an eventual threshold; separate bound notation from best/worst/average case.
- **Animated example:** grow `f(n)=3n²+7n+4` between `3n²` and `14n²` for `n≥1`. Highlight each inequality and then contrast the valid but loose `O(n³)` claim. Present a ratio-limit test as a shortcut when the limit exists.
- **Reasoning and takeaways:** show both sides for Θ. O does not mean worst case, nor Ω best case. A nonconvergent ratio need not prevent asymptotic bounds; do not repeat the slides' limit shortcut as an equivalent definition for every function.
- **Future question coverage:** identify true bounds, choose constants/thresholds, repair notation/case confusion, classify a ratio argument.

### A2 — How do we compare growth rates? · 3–4 min

- **Sources:** Analysis p13; R8 pp4–8; notes §§1.1, 1.3.
- **Teaching sequence:** simplify expressions before ranking; group Θ-equivalent functions; distinguish constant factors from exponent changes; derive the count for repeated halving/doubling.
- **Animated example:** sort function cards into `1, log n, √n, n, n log n, n², n⁵, 2ⁿ, 3ⁿ, 4ⁿ, n!, nⁿ`; place `log(n²)` alongside `log n`, and rewrite `2^(2n)` as `4ⁿ`. Trace `64→32→…→1` and `1→2→…→64`.
- **Reasoning and takeaways:** logarithm-base change is a constant multiplier; exponential-base change generally is not. For non-powers, specify integer rounding and stopping conditions. Small-input plots do not prove asymptotic order.
- **Future question coverage:** growth ordering with ties, expression simplification, loop counts, distinguishing asymptotic and measured time.

### A3 — How do we build and expand a recurrence? · 4–5 min

- **Sources:** Analysis pp14–19, 21–22, 24–27; notes §§1.4–1.5.
- **Teaching sequence:** identify branch count, shrink factor, local work and base case; expand by levels; solve stopping depth; include both internal work and leaves.
- **Animated example:** `T(n)=3T(n/4)+n`, `T(1)=1`, beginning at `n=64`. Show 3, 9 and 27 subproblems; per-level work `n(3/4)^i`; depth `log₄n`; leaf count `n^(log₄3)`.
- **Derivation:** `T(n)=n^(log₄3)+n Σ(i=0..L−1)(3/4)^i=Θ(n)`. The root supplies the lower bound. Compare binary search and merge-sort recurrences briefly to reinforce modelling.
- **Takeaways:** depth alone is not runtime; branch count need not equal shrink factor. The geometry in the slide is motivation for its stipulated recurrence, not a universal spatial-data assumption.
- **Future question coverage:** derive a recurrence from pseudocode, fill expansion levels, include leaf work, simplify geometric sums.

### A4 — How do we apply the full Master Theorem? · 5–6 min

- **Sources:** Analysis pp20–31; R8 p13; R10 pp2–4; notes §1.6. Requires A3.
- **Teaching sequence:** identify `a,b,f(n),p=log_b a`; compare against `n^p`; teach all three cases, polynomial gaps, the logarithmic case-2 extension, and case-3 regularity.
- **Animated worked examples:** `3T(n/3)+2 → Θ(n)`; `4T(n/4)+n−1 → Θ(n log n)`; `2T(n/2)+n log n → Θ(n log²n)`; `2T(n/4)+n → Θ(n)`. For the last show `ε=1/2` and `2f(n/4)=n/2`.
- **Derivation and takeaways:** compare leaf work against work higher in the tree. Display the actual course theorem with its conditions; R10 explicitly requires that version. Use the matrix recurrence `7T(n/2)+15n²/4` as a transfer example, not a new matrix-multiplication lesson.
- **Future question coverage:** identify cases, provide epsilon, check regularity, use the log extension, write a complete course-format application.

### A5 — When does the Master Theorem fail? · 3–4 min

- **Sources:** Analysis pp32–33; notes §1.6. Requires A4.
- **Teaching sequence:** test the form before testing a case; distinguish a polynomial gap from a logarithmic gap; explain the purpose of regularity; select iteration or substitution when necessary.
- **Animated example:** compare `n/log n` against `n` and `n^(1−ε)` in `T(n)=3T(n/3)+n/log n`. The stated theorem has no matching case. Contrast `T(n)=T(n−1)+n` and unequal-size subproblems, which fail the standard form.
- **Reasoning and takeaways:** correct Analysis p32's label: this is the gap **between cases 1 and 2**. A polynomially larger `f` is insufficient for case 3 without regularity; inspect the p33 irregular example without guessing its broken extracted symbols. Solving the logarithmic-gap recurrence beyond showing nonapplicability is optional enrichment.
- **Future question coverage:** justify nonapplicability, detect a missing condition, choose a different solving method.

### A6 — How do we prove a recurrence bound by substitution? · 4–5 min

- **Sources:** Analysis pp35–42, 46; R8 pp14–16; R9 pp2–3; notes §1.7. Requires A3.
- **Teaching sequence:** guess a concrete inequality; choose constants; verify the base; state the induction hypothesis; substitute and close the step. Show ordinary induction and induction over powers of two.
- **Animated example:** `T(1)=0`, `T(n)=T(n−1)+n−1`; prove `T(n)≤n²` via `T(k+1)≤k²+k≤(k+1)²`. Then show why `cn log n` fails at `n=1` if `T(1)=1`, and verify a later base before using it.
- **Reasoning and takeaways:** an O proof alone does not establish Θ. Distinguish the merge-sort key-comparison recurrence in the review from total copy/write work. A valid base-case adjustment must preserve the induction domain.
- **Future question coverage:** complete an induction, diagnose circular reasoning/base failures, distinguish upper and tight bounds.

### A7 — How do parity and rounding affect recurrence solutions? · 3–4 min

- **Sources:** R8 pp10–12; Analysis pp43–45; notes §§1.5, 1.7. Requires A3/A6.
- **Teaching sequence:** expand a decrement-by-two recurrence to the correct base; separate even and odd inputs; then explain extending standard monotone divide-and-conquer bounds beyond exact powers.
- **Animated example:** under the review's median-of-three counting convention, `T(n)=T(n−2)+n`, `T(1)=0`, `T(2)=1`. Derive even `n=2k`: `k(k+1)−1`; odd `n=2k+1`: `k(k+2)`; both Θ(n²).
- **Reasoning and takeaways:** median-of-three does not guarantee balanced partitions. State the review's three pivot-selection comparisons plus `n−3` partition comparisons. Explain smoothness `g(2n)=Θ(g(n))` using polynomials versus `2ⁿ`, and monotone sandwiching between nearby powers; do not erase floors/ceilings in arbitrary recurrences.
- **Future question coverage:** parity-sensitive bases, exact expansion totals, conditions for ignoring rounding.

## Greedy algorithms — three lessons

### G1 — How does greedy coin change work, and when does it fail? · 3–4 min

- **Sources:** Greedy pp3–7; notes §§6.1–6.2. Prerequisite: A1/A2.
- **Teaching sequence:** define local choice, irrevocable commitment and the minimum-coin objective; trace largest-affordable selection; compare repeated subtraction with denomination-wise division; disprove general optimality.
- **Animated example:** `{1,5,10,25}`, amount 37 gives `25+10+1+1`. Switch to the deck's `{1,10,25}`, amount 30: greedy uses six coins; `10+10+10` uses three.
- **Derivation and takeaways:** O(k) denomination scan when sorted and arithmetic is unit cost; repeated-coin work depends on coins emitted and lookup implementation. Coin 1 guarantees feasibility, not optimality. A single counterexample disproves a universal claim; many successes cannot prove it.
- **Future question coverage:** trace choices, count coins, construct counterexamples, analyse a specified implementation.

### G2 — Why does earliest-finish interval scheduling work? · 4–5 min

- **Sources:** Greedy pp8–13; R9 p4 for exclusion boundary; notes §§6.1, 6.3. Requires G1.
- **Teaching sequence:** maximise compatible job count on one resource; sort by finish time; accept/reject with a visible last-finish marker; prove the first differing greedy choice can replace an optimum's choice.
- **Animated example:** `[0,3),[1,2),[2,4),[3,5),[4,6)`; choose `[1,2),[2,4),[4,6)`. Show separate counterexamples to earliest-start and shortest-duration rules.
- **Derivation and takeaways:** O(n log n) sort plus O(n) scan. Update last finish only on acceptance; touching endpoints are compatible. This is unweighted subset selection. Interval partitioning's minimum-resource objective is explicitly outside the supplied scope.
- **Future question coverage:** accepted jobs/rejections, exchange-proof steps, bad-rule counterexamples, endpoint ties and presorted cost.

### G3 — Why is density greedy optimal for fractional knapsack? · 4–5 min

- **Sources:** Greedy pp14–17; notes §6.4. Requires G1.
- **Teaching sequence:** define divisible items and proportional profit; order by profit/weight; fill capacity; animate an equal-weight exchange to justify optimality.
- **Animated example:** capacity 50 and `(weight,profit)=(10,60),(20,100),(30,120)`. Densities 6,5,4; select the first two and two-thirds of the third; profit 240. This is a compact note example, not a claimed recording example.
- **Derivation and takeaways:** O(n log n) sorting plus O(n) scan; positive weights; stop when full **or items run out**. Contrast highest absolute profit/smallest weight. Explain exactly where divisibility is used in the proof; N8 will revisit indivisible items.
- **Future question coverage:** density order, fractions/profit, exchange logic, exhausted-item cases and variant identification.

## Dynamic programming — seven lessons

### D1 — How do memoisation and tabulation remove repeated work? · 4–5 min

- **Sources:** DP pp3–18; notes §§6.5–6.7. Prerequisite: recursion, A3.
- **Teaching sequence:** draw the recursion tree for `F(6)`; merge equal calls into distinct states; implement cache lookup/store conceptually; fill the same states bottom up.
- **Animated example:** repeated `F(4),F(3),…` nodes collapse into a dependency graph; table `F[0..6]=[0,1,1,2,3,5,8]`. Highlight cache hits separately from first computations.
- **Derivation and takeaways:** uncached recursion has exponential growth; O(2ⁿ) is an upper bound. DP has n+1 states, O(1) arithmetic work/state, O(n) time/table storage, and top-down stack overhead. Length-only Fibonacci can use O(1) words. Graph arrows here run caller→dependency; compute dependencies first. DP is not universally polynomial.
- **Future question coverage:** state versus call counts, memoisation order, cache sentinel, recursion-tree/state-graph distinctions.

### D2 — How do we turn a recurrence into a DP? · 3–4 min

- **Sources:** R9 pp8–13; DP pp15–18; notes §§6.6–6.7. Requires D1.
- **Teaching sequence:** use the review's definition of Virahanka; identify states/base cases and smaller dependencies; derive both a cached function and increasing-index loop.
- **Animated example:** `V(0)=V(1)=1`, `V(n)=V(n−1)+V(⌊n/2⌋)` for n>1; build `V[0..6]=[1,1,2,3,5,7,10]` and connect each cell to the two source cells.
- **Derivation and takeaways:** O(n) arithmetic operations and O(n) table space; memoised recursion also needs stack space. Do not replace this supplied recurrence with a familiar Fibonacci naming convention. Special-case n=0 before writing array slot 1. Two rolling values are insufficient for this dependency pattern.
- **Future question coverage:** new-state design, dependency order, missing cache/base logic, table values and complexity.

### D3 — How does DP find the minimum number of coins? · 4–5 min

- **Sources:** DP pp19–27; notes §§6.5, 6.8. Requires G1/D1.
- **Teaching sequence:** define `C[a]` for an exact amount; derive the last-coin minimum; initialise zero and unreachable states; fill amounts in increasing order; reconstruct an optimum with stored choices.
- **Animated example:** `{1,3,4}`, amount 6; table `[0,1,2,1,1,2,2]`; compare candidates for six and recover `3+3` against greedy's `4+1+1`. Briefly show `{3,4}`, amount 2 as unreachable outside the deck's guaranteed-coin-1 setting.
- **Derivation and takeaways:** A amounts × k denominations gives O(kA) time, O(A) table storage; reconstruction adds output work. Prove optimal substructure by replacing a nonoptimal remainder. Do not copy DP p20's unsupported blanket factorial count. Counting coin combinations is a different problem.
- **Future question coverage:** derive/fill the recurrence, reconstruct, handle impossibility, distinguish minimum count from number of ways.

### D4 — How does longest common subsequence work? · 5–7 min

- **Sources:** DP pp30–51; notes §6.9. Requires D1.
- **Teaching sequence:** distinguish subsequence from substring; define a prefix-pair state; derive equal-terminal and unequal-terminal cases; fill values and hint arrows; backtrack and reverse emitted characters.
- **Animated example:** use the visually verified slide example **X=ACGGA, Y=ACTG**. Fill a readable 6×5 table including the zero borders; optimum 3; reconstruct `ACG`, with the slide's top-on-tie rule. Demonstrate skipped characters and a tie explicitly.
- **Derivation and takeaways:** nm states with constant transition work → Θ(nm) time/O(nm) table; O(n+m) backtracking. Several valid LCSs can exist. Memoised top-down is efficient; DP p39's warning concerns uncached recursion. Rolling rows are optional length-only enrichment, not a replacement for the reconstruction lesson.
- **Future question coverage:** prefix states, table/arrows, backtracking, valid alternative optima, complexity and memoisation misconceptions.

### D5 — How does 0/1 knapsack DP enforce single use? · 5–6 min

- **Sources:** DP pp52–63; notes §6.10. Requires D1/G3.
- **Teaching sequence:** define capacity and first-j-items state; enumerate exclude/include choices; guard overweight inclusion; fill the table; reconstruct selected items.
- **Animated example:** capacity 5, `(2,3),(3,4),(4,5)`; best profit 7 from the first two items. Each transition visibly goes to column `j−1`; no item can be reused. Show at-most-capacity feasibility and unused space.
- **Derivation and takeaways:** O(nC) table work/space and O(n) backtracking. Include-item transitions exist only when `w_j≤c`, correcting the unguarded formula on DP p55. Distinguish fractional, 0/1 and unbounded variants. Optional space note: one-dimensional capacities must update downward for 0/1 use.
- **Future question coverage:** state/overweight branch, table/reconstruction, reused-item bug, zero capacity and unused capacity.

### D6 — Why is knapsack DP only pseudo-polynomial? · 3–4 min

- **Sources:** DP pp64–65; NP p14; notes §6.11. Requires D3–D5/A2.
- **Teaching sequence:** distinguish encoded input length from numeric magnitude; count bits used by capacity; substitute `C≈2^b`; compare knapsack/coin change with LCS's explicitly listed strings.
- **Animated example:** double a binary capacity's bit length and show the table-width consequence; `O(nC)` becomes `O(n2^b)` in capacity bit length. Place `O(kA)` coin change and `O(nm)` LCS in the appropriate categories.
- **Reasoning and takeaways:** arithmetic uses the course word-operation model unless bit costs are requested; do not call magnitude-dependent DP polynomial in input bit length. This DP does not establish P=NP. State parameter meanings before quoting complexity.
- **Future question coverage:** bit-length conversions, polynomial/pseudo-polynomial classification, explaining the apparent knapsack paradox.

### D7 — How do we choose a correct state and algorithmic strategy? · 3–4 min

- **Sources:** DP pp20–21, 28–29, 66–67; Greedy p18; notes §§6.5, 6.12. Requires G1–G3/D1–D6.
- **Teaching sequence:** compare local commitment, independent recursive work and stored alternative subsolutions; use replacement reasoning to test optimal substructure; ask whether the state retains all relevant history.
- **Animated example:** contrast shortest-path subpaths with a longest **simple** path whose continuation depends on already visited vertices. Cross-link coin change and the two knapsack variants; show why matching a problem name is insufficient to select an algorithm.
- **Reasoning and takeaways:** optimal substructure alone does not guarantee a small efficient DP. Longest simple paths can require visited-set state; do not claim every longest-path variant is impossible for DP. DP can be recursive and need not try every numerical split. This is synthesis and transfer, not another full rerun of earlier examples.
- **Future question coverage:** diagnose an incomplete state, choose/prove a strategy, distinguish structural assumptions from slogans.

## String matching — six lessons

### S1 — How does naive string matching scan the text? · 3–4 min

- **Sources:** Strings pp2–10; notes §§7.1–7.2. Prerequisite: loops and A1.
- **Teaching sequence:** define text length n/pattern length m and first-occurrence output; align; compare left to right; reset after mismatch; stop at the last valid alignment.
- **Animated example:** `T=ABABABAC`, `P=ABAC`; test starts 0,1,2,3,4 and return 4. Then show an all-A text against `AAAAC` to derive repeated near-matches.
- **Derivation and takeaways:** at most n−m+1 starts × m comparisons gives O((n−m+1)m) scan work, with a matching worst-case family. Keep zero-based bounds explicit; m>n has no valid window. State an empty-pattern convention if implemented rather than inheriting invalid P[0] access.
- **Future question coverage:** pointer resets, first index, comparisons, boundary cases, near-match worst case.

### S2 — How do rolling hashes make Rabin–Karp work? · 4–5 min

- **Sources:** Strings pp11–15, 20–24; notes §§7.3–7.4. Requires S1.
- **Teaching sequence:** map symbols to digits; Horner-encode a window; derive removal/shift/append; reduce modulo q; compare hashes and then verify actual characters.
- **Animated example:** derive `36415→64152`: `(36415−3·10⁴)·10+2`. Then use `P=25,T=1225,d=10,q=13,H=10`: hashes 12,9,12; the first candidate collides and fails verification, the last matches at index 2.
- **Derivation and takeaways:** O(m) preprocessing and constant modular rolling work per alignment under word arithmetic. Equal hashes are candidates; unequal hashes reject. Normalize negative residues and roll only if another complete window exists. The decimal example is deliberate; do not copy the slide's reversed binary extraction.
- **Future question coverage:** Horner values, rolling updates/modulo, collisions, verification and legal last-window access.

### S3 — What determines Rabin–Karp's actual runtime? · 3–4 min

- **Sources:** Strings pp15–19, 25, 56; notes §7.4. Requires S2.
- **Teaching sequence:** separate initial hashing, rolling operations and character verification; distinguish a spurious hit from a genuine match; state assumptions behind expected performance.
- **Animated example:** carry S2's trace into two counters: three window hashes and three verification comparisons (one to reject `12`, two to accept `25`). Contrast a collision-heavy late/no-match family with a sparse-hit scan.
- **Derivation and takeaways:** with h checked hash hits, O(n+m+hm); worst-case repeated near-matches/collisions can give Θ((n−m+1)m) scan work. Preprocessing still exists in cases with very few windows. A large prime does not remove all collisions or guarantee unconditional linear time; historical implementation measurements are not universal benchmark claims.
- **Future question coverage:** count verification separately, calculate candidate-dependent cost, challenge unconditional expected/worst-case claims.

### S4 — How does Boyer–Moore use the bad character? · 4–5 min

- **Sources:** Strings pp26–38; notes §§7.5–7.6. Requires S1.
- **Teaching sequence:** explicitly switch to the course's one-based indices; compare right to left; build charJump from rightmost occurrences; illustrate why a fallback must restore progress after matching a suffix.
- **Animated example:** `P=ABCA,m=4`: `charJump[A]=0,B=2,C=1,absent=4`. After a two-character suffix match, mismatch at k=2: use `j+=max(charJump[T[j]],m−k+1)` and reset k=m. Show old right endpoint, mismatch pointer and new endpoint as separate markers.
- **Derivation and takeaways:** char table O(|Σ|+m) time/storage; simple scan O(nm) general upper bound. Pointer increment and pattern slide differ once j has moved left. charJump alone can suggest nonprogressing/backward alignment. Return `j+1` on full match under this convention.
- **Future question coverage:** repeated/absent-character tables, compute the new j/alignment, fallback and one-based return index.

### S5 — How does Boyer–Moore use the good suffix? · 5–6 min

- **Sources:** Strings pp39–49, 51–54; notes §7.7. Requires S4.
- **Teaching sequence:** identify the matched suffix; test earlier occurrence with a different preceding character; otherwise use longest prefix overlap; otherwise move beyond the suffix; convert Slide to matchJump.
- **Animated example:** verified `P=RATSANDCATS,m=11,k=8`, matching ATS. Earlier ATS ends at q=4; preceding R differs from C. `Slide[8]=7`, `matchJump[8]=3+7=10`. Then build WOWWOW's entries in increasing k: Slide `[3,3,3,5,2,1]`, matchJump `[8,7,6,7,3,1]`.
- **Reasoning and takeaways:** show why k=4's suffix OW cannot use the occurrence preceded by the same W; prefix overlap gives slide 5. Empty matched suffix uses Slide[m]=1. The deck gives cases/tables without a full preprocessing implementation, so do not invent an established preprocessing bound for that implementation.
- **Future question coverage:** all three suffix cases, preceding-character condition, table construction and pointer/slide conversion.

### S6 — How do the two Boyer–Moore rules combine in a full search? · 5–7 min

- **Sources:** Strings pp27, 50, 55–58; notes §7.8. Requires S4–S5.
- **Teaching sequence:** run both tables, select the maximum safe pointer increment, reset k, and trace until a full match; compare what naive, Rabin–Karp and Boyer–Moore reuse.
- **Animated example:** course `P=WOWWOW`, `T=LOWOWNOWLWOWWOMMOWWOWWOW`; show every comparison and mismatch jump, with a running counter. Independent computation in this analysis confirms the slide's **18 comparisons**, with first match at one-based position **19**. Full events are in `edit/planning/sc2001-post-week07/worked-example-checks.json`; revalidate against the authored animation before rendering. Keep tables in increasing k to avoid the PDF's reversed text order.
- **Derivation and takeaways:** the maximum combines exclusions from both rules. Explain skipped comparisons without promising sublinear worst-case time for the shown variant; retain O(nm) general scan upper bound. KMP is only mentioned in comparison slides and does not become a new core algorithm. Distinguish supplied practical observations from guarantees.
- **Future question coverage:** complete trace/count, max-rule selection, start index, table convention and justified algorithm comparisons.

## Introduction to NP and heuristics — eight lessons

### N1 — What makes a computational task hard? · 3–4 min

- **Sources:** NP pp3–8; notes §§8.1–8.2. Prerequisite: A2/A3.
- **Teaching sequence:** identify input encoding and required output; distinguish implementation difficulty from growth; distinguish decision and optimisation; convert objectives into threshold questions.
- **Animated example:** Hanoi with three disks prints seven moves; derive `M(n)=2M(n−1)+1=2ⁿ−1`. Contrast printing every move with returning only the move count. Turn TSP, MST and knapsack objectives into their correct threshold decision questions.
- **Reasoning and takeaways:** large explicit output forces proportional output work. A slow known search is not a lower-bound proof for every algorithm. Correct NP p5's numerical runtime rather than repeating 140,000 hours; the exact output-count argument is enough. Formal P/NP classifications concern decision problems.
- **Future question coverage:** task/output distinctions, decision inequalities, input-size assumptions and invalid hardness arguments.

### N2 — What are P and NP, and what does verification mean? · 4–5 min

- **Sources:** NP pp9–19; notes §§8.3–8.5. Requires N1/D6.
- **Teaching sequence:** define deterministic polynomial solving and polynomial-length yes-certificates; verify every feasibility/threshold condition; explain P⊆NP and what is unresolved.
- **Animated example:** inspect a candidate TSP tour and a knapsack subset: repeated/missing vertices or items, missing edges, total weight/profit and threshold all receive explicit checks. Contrast “there exists a cheap tour” with “every tour is cheap”.
- **Reasoning and takeaways:** a rejected candidate does not prove the instance is no. NP does not mean not-polynomial; no known fast algorithm is not part of the NP definition. Do not copy NP p18's unsupported claim that the universal-tour question is outside NP/provably exponential. A costly tour witnesses its complementary condition; that observation does not settle separation.
- **Future question coverage:** complete certificates/verifiers, class implications, existential/universal logic, P=NP misconceptions.

### N3 — Which direction does a polynomial reduction go? · 3–4 min

- **Sources:** NP pp20–23; notes §8.6. Requires N2.
- **Teaching sequence:** transform an A-instance into a B-instance; call a B solver; preserve yes iff yes; account for transformation runtime; derive hardness direction and transitivity.
- **Animated example:** pass an instance through `A → f(x) → B solver → answer for A`. For the deck's pairing/sorting intuition, sort X=[3,1,2], Y=[30,10,20] and pair equal ranks. Clearly label this as an algorithm-use illustration, not the complete formal decision reduction proof.
- **Reasoning and takeaways:** A≤pB means B is at least as hard as A. B∈P then implies A∈P. To prove a new B hard, reduce known-hard A **to B**; reversing the arrow does not establish that conclusion. Both correctness directions are required.
- **Future question coverage:** arrow direction, valid implications, reduction proof obligations and transitive chains.

### N4 — How does Hamiltonian path reduce to TSP? · 4–5 min

- **Sources:** NP pp22–23; notes §8.7. Requires N3 and graph prerequisites.
- **Teaching sequence:** create a complete graph on the same n vertices; assign old edges weight 1/missing edges weight 2; set threshold n+1; prove both directions.
- **Animated example:** the five-vertex slide graph has edges AB,AC,AD,BE,CE,CD. Highlight path E–B–A–C–D; complete with D–E (weight 2), total 6=n+1. In reverse, a tour with n edges and cost≤n+1 has at most one weight-2 edge; remove it (or any edge if all weights are 1).
- **Derivation and takeaways:** O(n²) construction is polynomial; n≥3 for the standard undirected-tour convention. Threshold n would instead demand all-weight-1 tour edges and breaks this Hamiltonian-path construction. A path visits each vertex once without a required closing edge; a tour returns.
- **Future question coverage:** construct weights/threshold, forward/reverse proof, detect an incorrect reduction and preserve vertex count.

### N5 — How do we prove NP-completeness? · 4–5 min

- **Sources:** NP pp24–28; notes §§8.8–8.9. Requires N2–N4.
- **Teaching sequence:** show membership in NP; reduce an already NP-complete problem to the target; use transitivity; explain the consequence of a polynomial solver for any NP-complete problem.
- **Animated example:** a tiny Boolean circuit/formula receives a candidate assignment and evaluates gate by gate. Then animate `every NP problem → CIRCUIT-SAT → SAT` using the theorem assumed by the deck, and separately mark SAT's membership check. Use a fresh simple formula such as `(A∨B)∧(¬A∨C)` with A=true, B=false, C=true for readability.
- **Reasoning and takeaways:** hardness alone omits membership. NP-complete problems' mutual reductions do not imply identical exponents or practical runtime. P versus NP is unresolved. Verifier-to-circuit construction on p25 and formal NP-hard material on p36 are excluded from core production.
- **Future question coverage:** the two proof obligations, valid chains, satisfiability/certificates and consequences of a fast NP-complete solver.

### N6 — How does nearest-neighbour TSP fail to find the best tour? · 3–4 min

- **Sources:** NP pp29–31; notes §§8.10–8.11. Requires N1/N2 and weighted graphs.
- **Teaching sequence:** start at a named vertex; repeatedly choose its cheapest unvisited neighbour; close the tour; compare with a better feasible tour; distinguish a heuristic from an approximation guarantee.
- **Animated example:** complete undirected graph AB=1, AC=2, AD=2, BC=1, BD=2, CD=100. From A, trace A–B–C–D–A, cost 104; show A–C–B–D–A, cost 7.
- **Derivation and takeaways:** scanning unvisited candidates yields O(n²) time/O(n) bookkeeping. Include the return edge; specify ties and start; assume a complete graph. This counterexample does not satisfy triangle inequality, so do not transfer its conclusion to metric approximation claims without qualification.
- **Future question coverage:** route/cost, tie/start effects, a concrete better tour, feasibility versus optimality.

### N7 — How does the shortest-link TSP heuristic differ from Kruskal? · 4–5 min

- **Sources:** NP pp32–33; notes §8.12. Requires N6 and week-7 Kruskal/union-find.
- **Teaching sequence:** consider edges globally in sorted order; reject degree>2 and premature cycles; build a spanning path; join its endpoints to finish the tour.
- **Animated example:** complete five-vertex graph with AB=1,BC=2,AC=3,BD=4,CD=5,DE=6,AE=7,BE=8,AD=9,CE=10. Accept AB,BC; reject AC (subtour), BD (B already degree 2); accept CD,DE; close EA. Tour cost 21. This deliberately fresh example exposes both rejection rules.
- **Derivation and takeaways:** O(E log E) sorting plus appropriate degree/component bookkeeping; union-find scan can cost O(E α(V)). This implementation-cost derivation is an explanatory addition. Kruskal permits branching degrees and never closes a cycle; shortest-link must make one final cycle. Neither a good trace nor an MST relation proves TSP optimality.
- **Future question coverage:** accept/reject reasons, degrees/components, final closure and differences from Kruskal.

### N8 — Why does density greedy fail for 0/1 knapsack? · 3–4 min

- **Sources:** NP pp34–35; Greedy pp14–17; DP pp52–65; notes §8.13. Requires G3/D5/D6.
- **Teaching sequence:** sort by density; take whole fitting items; skip those that do not fit and continue; update weight/profit only on acceptance; compare greedy, fractional optimum and exact DP.
- **Animated example:** reuse capacity 50 and `(10,60),(20,100),(30,120)`. Whole-item density greedy gives 160; items two and three give the 0/1 optimum 220; fractional optimum is 240.
- **Derivation and takeaways:** O(n log n) sorting/O(n) scan; the equal-weight exchange argument fails because items are indivisible. Fix NP p34's conditional grouping. The deck's example where greedy happens to attain the optimum is not a general proof. A capacity threshold and profit threshold are distinct constraints.
- **Future question coverage:** greedy trace including skips, compare the three variants, counterexample, conditional bug and pseudo-polynomial DP contrast.

## Coverage boundaries and corrections

Do not create core lessons/questions for **interval partitioning** (R9 p4), **LIS** (R10 p5), **verifier-to-circuit construction** (NP p25), or the formal **NP-hard extension** (NP p36). Do not add KMP mechanics merely because the comparison slide names it. Optional enrichment can be proposed separately after approval; no optional video is included in the 31-lesson count.

Corrections to carry into scripts/source maps include: limit tests are sufficient shortcuts; Master needs polynomial gaps/regularity; Analysis p32 has the wrong case-gap label; ordinary rounding shortcuts need assumptions; greedy conditional grouping/item exhaustion; DP is not universally polynomial; cached top-down LCS is efficient; 0/1 inclusion needs the overweight guard; Boyer–Moore pointer increments differ from alignment slides; NP includes P; a rejected certificate is not a no-proof; universal-tour separation is unproved; the Hamiltonian-path threshold is n+1.

The concrete compact examples, reconstruction details and some cost arguments above are explanatory additions grounded in the course algorithms; they are not claimed as lecturer quotations or unseen recording content.

## Future question-bank blueprint — after verified videos

Propose **one practice topic per lesson**, preserving the current SC2001 convention of **4 Easy + 4 Medium + 4 Hard + 1 Baka = 13 questions/topic**. That gives **403 new questions** across 31 topics, bringing the existing SC2001 bank from 390 to **793**, if this topic granularity is approved. These are proposed counts, not completed questions or an exam prediction.

| Group | Topics | Proposed questions | Skill emphasis |
|---|---:|---:|---|
| Analysis | 7 | 91 | Constants, expansions, epsilon/regularity, induction and nonapplicability |
| Greedy | 3 | 39 | Traces, counterexamples, feasibility and exchange reasoning |
| DP | 7 | 91 | State/recurrence, tables, reconstruction, order and encoded size |
| Strings | 6 | 78 | Alignments, hashes/collisions, jump tables, exact pointer conventions |
| NP/heuristics | 8 | 104 | Certificates, reductions, proof obligations and heuristic traces |
| **Total** | **31** | **403** | |

Easy checks definitions/one transition; Medium uses a complete small trace; Hard combines derivation, proof reasoning or a diagnosed mistake; Baka uses a longer but unambiguous transfer/trace. Avoid creating difficulty through ambiguous wording. Each MCQ needs explicit inputs/conventions, four distinct options, one defensible correct option, worked feedback and physical source pages. A proof MCQ tests a logical step/obligation; it does not replace learning to write the proof.

Before importing, recompute numerical answers independently, check every option and tie convention, preserve existing IDs, and allocate collision-free new IDs based on the actual bank at that time. Do not infer new IDs solely from the current question count or from other courses' IDs. Keep stable lesson/topic mappings and update the bank version for progress compatibility.

## Production and integration sequence after approval

1. **Record approval and source decision.** Confirm acceptance of this coverage, 31 lessons and the missing later recordings. A request for revisions keeps the gate closed. Supplying recordings triggers additional source review, cached transcription if needed and plan updates where content changes.
2. **Produce lessons using `$malfoid-explainer`.** Adapt the accepted insertion/merge helpers in `edit/revisions/<slug>/`. Store lesson-level source maps, narration beats, trace specifications, caption/ASR data, expression schedules, voice-reference provenance and verifier results. No ElevenLabs or lecture uploads. Prefer batch completion by group in the dependency order above, while preserving each complete lesson's narrative.
3. **Verify before creating the question bank.** Independently compute examples/counters/boundaries; inspect actual encoded motion and captions; check spoken maths, voice hash, 2–3-sentence main-pose cadence, full decode, duration and 1080×1920/30fps H.264/AAC format. Reuse no old-topic verifier unchanged. Save raw ASR, investigate errors, and retain source-gap labels.
4. **Author and verify the question bank.** Use the approved topics and actual finished lessons; questions must not cite nonexistent recording times or fabricated video chapters. Validate all 403 proposed items before declaring completion; do not fill quotas with wording-only duplicates.
5. **Add verified content to the website.** Read repository instructions and relevant Matt Pocock `codebase-design`, `tdd` where behaviour warrants tests, and `code-review`; inspect/configure `docs/agents/` with `setup-matt-pocock-skills` if those workflows need missing configuration. Extend `web/scripts/prepare_content.py` deliberately: it currently hardcodes the old lesson list, week range and week-1/2 recording defaults. Explicitly map the new lessons/topics and represent missing recordings honestly. Update SC2001's coverage label to weeks 1–13 only once the new content is complete; preserve other courses and progress IDs.
6. **Validate integration, then push to GitHub under the user's authorization.** Check catalog/media/captions/source links, quizzes and progress; run the relevant existing checks (`npm test`, `npm run check`, production build as applicable) plus focused browser checks. Inspect the diff and Git status; include only intended files; preserve unrelated untracked work. The initial state included `web/content/answer-audit.json`, `web/content/catalog-before-expansion.json` and `web/tests/browser.mjs` as untracked. Inspect the actual current state again before staging.

**Git/media constraint discovered:** `.gitignore` excludes `/edit/`, `/output/`, `/tmp/`, `/study-notes/` and `/skills/`. A GitHub push alone cannot deliver newly generated videos to the hosted website. Inspect `web/DEPLOYMENT.md` and hosting configuration at the integration stage; stage the approved hosted-media mappings/supporting files through the established workflow when authorized. Do not force-add recordings/models/masters to Git. Pushing may trigger configured CI/deployment; inspect repository configuration first and report the actual result. Do not treat “push to GitHub” as authorization to create a different hosting service or upload lecture sources.

## Approval checkpoint

Approve or revise the **31-lesson breakdown**, the proposed **403-question allocation**, and the use of **slides plus notes while later recordings are unavailable**. Once approved, the next stage is video production using `$malfoid-explainer`; the bank, website integration and GitHub push follow in that order. No additional approval gate is implied for routine actions already authorized by the request.
