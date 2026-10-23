# SC2203 Automata, Computability and Complexity — examination question bank

Prepared from the SC2203 lecture slide decks/recordings and tutorial materials in the course folder. `Baka` means deliberately extreme: it combines several ideas and is intended as a stretch problem, not a prediction of exact exam wording.

## How to use this bank

- MCQs: choose one answer. The answer key is at the end of each topic.
- Open-ended questions: the short marking outline indicates the essential ingredients of a full solution.
- Notation follows the lectures: `ε` is the empty string, `Σ*` is the set of all strings over `Σ`, and `L(M)` is the language recognized by machine `M`.

---

## Topic 1 — Foundations, definitions, proofs and DFAs

### Easy MCQs

1. Which item is *not* part of the formal 5-tuple of a DFA?  
   A. A finite state set `Q`  B. An input alphabet `Σ`  C. A stack alphabet `Γ`  D. An accepting-state set `F`
2. In a DFA, `δ` has type:  
   A. `Q → Σ`  B. `Q × Σ → Q`  C. `Q × Q → Σ`  D. `Σ → P(Q)`
3. A DFA accepts a string exactly when:  
   A. some transition is unavailable  B. the run ends in an accepting state  C. the run visits every state  D. the string is nonempty
4. `ε` has length: A. `-1`  B. `0`  C. `1`  D. undefined
5. A language is regular iff: A. it is finite  B. it has a grammar  C. some DFA recognizes it  D. every string has even length

### Medium MCQs

6. If `δ(q0,a)=q1` and `δ(q1,b)=q2`, then the DFA's state after reading `ab` is: A. `q0` B. `q1` C. `q2` D. undefined
7. Which statement about a DFA transition function is required?  
   A. It may choose two next states. B. It must be defined for every state-symbol pair. C. It must contain an `ε` transition. D. It must be reversible.
8. For a DFA with start state `q0`, `ε` is accepted iff: A. `q0∈F` B. `F=∅` C. `q0` has a self-loop D. `Σ=∅`
9. The complement of a DFA language is obtained by: A. reversing all arrows B. swapping accepting and nonaccepting states, assuming a complete DFA C. deleting the start state D. adding a stack
10. A proof by contradiction begins by: A. assuming the desired conclusion B. assuming the negation of the claim C. drawing a DFA D. choosing a random example

### Hard MCQs

11. If two DFAs have identical transition functions but different accepting sets, they must: A. recognize the same language B. recognize complementary languages C. have the same number of reachable states D. be nondeterministic
12. A DFA with `n` states reading a string of length `m` performs how many input-consuming transitions? A. `n` B. `m` C. `n+m` D. `2^m`
13. If a DFA recognizes `A`, which statement is necessarily true? A. Every string in `A` has one accepting run. B. Every string outside `A` has no run. C. The DFA has no unreachable states. D. `A` must be infinite.
14. A theorem differs from an example because a theorem: A. needs no justification B. is intended to hold under stated hypotheses C. must concern graphs D. is always computationally efficient
15. A language over `{0,1}` containing exactly the strings with an even number of `1`s is: A. nonregular B. regular C. undecidable D. not a language

### Baka MCQ

16. Let a complete DFA have `n` states. Which is the strongest universally valid statement about the sequence of states reached while reading any string?  
   A. It visits each state at most once. B. After `n+1` visited states, some state repeats. C. It must end in an accepting state. D. It can branch into at most `n` runs.

**Answer key:** 1C, 2B, 3B, 4B, 5C, 6C, 7B, 8A, 9B, 10B, 11B, 12B, 13A, 14B, 15B, 16B.

### Open-ended questions

- **Easy:** Give a formal DFA for the language of binary strings ending in `1`. State `Q,Σ,δ,q0,F` and explain acceptance. *(Mark: complete transition table, start state, accepting state, and a brief correctness explanation.)*
- **Medium:** Design a DFA over `{0,1}` for strings containing an even number of `0`s and an odd number of `1`s. *(Mark: four parity states, correct start/accept state, all transitions, invariant.)*
- **Hard:** Prove that the language of strings over `{0,1}` containing exactly two `1`s is regular by giving a DFA and proving its invariant. *(Mark: states for 0/1/2/more than 2 ones and proof.)*
- **Baka:** Prove that every DFA with `n` states satisfies the finite-memory/pumping property: for every accepted string `w` with `|w|≥n`, there are `x,y,z` with `w=xyz`, `|xy|≤n`, `|y|>0`, and `xy^iz` accepted for every `i≥0`. *(Mark: repeated state among first `n+1` configurations, loop argument, all `i≥0`.)*

---

## Topic 2 — DFA design, regular operations and NFA basics

### Easy MCQs

1. The first design question for a DFA is usually: A. What do I need to remember? B. How do I use a stack? C. How do I enumerate? D. What certificate is supplied?
2. `A∪B` contains strings that are: A. in both only B. in at least one of `A,B` C. in neither D. of equal length
3. Concatenation `AB` consists of strings: A. `xy` with `x∈A,y∈B` B. in `A∩B` C. in `A*` only D. of length one
4. `A*` always contains: A. no strings B. `ε` C. only strings of length 1 D. the complement of `A`
5. An NFA may have: A. several possible next states B. no accepting state ever C. only one state D. no transitions

### Medium MCQs

6. To recognize strings ending in `001`, a useful DFA remembers: A. the entire input B. the longest suffix that is a prefix of `001` C. only the length D. the first symbol only
7. The product DFA for intersection uses state space: A. `Q1∪Q2` B. `Q1×Q2` C. `P(Q1)` D. `Σ×Σ`
8. An NFA accepts a string when: A. every branch accepts B. at least one branch accepts C. the first branch accepts D. it never uses an ε-move
9. The formal NFA transition function has codomain: A. `Q` B. `Σ` C. `P(Q)` or `P(Q)` with ε-inputs D. integers
10. A DFA is a special case of an NFA because: A. it has no accepting states B. every state-symbol pair has exactly one next state C. it always has ε-moves D. it can use a stack

### Hard MCQs

11. To recognize `A∩B` using DFAs, the product state `(p,q)` should be accepting when: A. `p` or `q` accepts B. both `p` and `q` accept C. neither accepts D. `p=q`
12. A correct DFA for “the third symbol from the end is `1`” generally needs to remember: A. at most two symbols B. a bounded suffix of length three C. the number of all previous `1`s D. a stack
13. Which construction is most naturally handled by NFA ε-branching? A. union of two machines B. exact binary addition C. tape reversal D. counting arbitrary equal blocks
14. If an NFA has no transition on the next input symbol from any currently possible state, it: A. rejects that branch set B. adds an arbitrary state C. automatically accepts D. becomes a DFA
15. In a complete DFA for a language, a missing NFA transition is simulated by: A. deleting the input B. the empty subset/dead state C. an accepting state D. an ε-loop

### Baka MCQ

16. Which claim best explains why an NFA can be exponentially smaller than an equivalent DFA?  
   A. NFAs use a larger alphabet. B. A subset of NFA states represents many simultaneous DFA possibilities. C. NFAs do not read input. D. DFAs are allowed stacks.

**Answer key:** 1A, 2B, 3A, 4B, 5A, 6B, 7B, 8B, 9C, 10B, 11B, 12B, 13A, 14A, 15B, 16B.

### Open-ended questions

- **Easy:** Construct a DFA for strings over `{a,b}` containing at least one `a` and at least one `b`. *(Mark: four “seen/not seen” states and correctness.)*
- **Medium:** Use a product construction to build a DFA for strings with an even number of `0`s and ending in `1`. *(Mark: component DFAs, product states, accepting condition, transition rule.)*
- **Hard:** Construct an NFA for `(0∪1)*01(0∪1)*`, then convert it to a DFA using subset construction. *(Mark: ε/branch structure, reachable subsets, acceptance.)*
- **Baka:** Explain and prove an `O(k)`-state NFA for “the `k`th symbol from the end is `1`”, and prove why the natural DFA needs at least `2^k` states using distinguishable suffixes. *(Mark: NFA guess, subset intuition, Myhill–Nerode lower bound.)*

---

## Topic 3 — NFA–DFA equivalence, closure and regular expressions

### Easy MCQs

1. The subset construction represents one DFA state by: A. a subset of NFA states B. one input symbol C. one stack string D. one grammar rule
2. The ε-closure of a state contains: A. states reachable using only ε-moves, including itself B. only accepting states C. all states D. no states
3. Every NFA has: A. an equivalent DFA B. an equivalent PDA only C. no equivalent machine D. an equivalent finite grammar only
4. In a regex, `R∪S` denotes: A. union B. intersection C. subtraction D. reversal
5. `R*` includes: A. one repetition only B. zero or more repetitions C. exactly two repetitions D. no repetitions

### Medium MCQs

6. In subset construction with ε-moves, after consuming symbol `a` one should generally: A. take ε-closure before and after the `a`-move B. ignore ε-moves C. complement the set D. reverse it
7. An NFA for `RS` is built by: A. adding ε-arrows from accept states of the `R` machine to the start of `S` B. intersecting states C. swapping arrows D. adding a stack
8. An NFA for `R*` needs a fresh start/accept arrangement mainly to allow: A. zero repetitions and repeated returns to `R` B. negative symbols C. deterministic branching D. complement
9. The identity `R∪∅` equals: A. `∅` B. `ε` C. `R` D. `R*`
10. The identity `Rε` equals: A. `ε` B. `R` C. `∅` D. `R∪ε`

### Hard MCQs

11. A subset in the constructed DFA is accepting iff: A. it contains at least one accepting NFA state B. all its states accept C. it has even size D. it contains the NFA start state
12. The closure proof for regular languages under concatenation is easiest through: A. an NFA construction B. a pumping contradiction C. a TM D. a CNF conversion
13. If two regexes differ syntactically but denote the same language, they are: A. necessarily different languages B. semantically equivalent C. both invalid D. not regular
14. Which expression denotes strings containing at least one `1`? A. `0*` B. `0*10*` C. `1*0*` D. `(0∪1)*`
15. In the subset construction, unreachable subsets: A. must be included in diagrams if convenient but do not affect the language B. always accept C. cause inconsistency D. become grammar variables

### Baka MCQ

16. The statement “NFAs are no more powerful than DFAs” means: A. every NFA has the same number of states as a DFA B. every NFA language is recognized by some DFA C. NFAs cannot branch D. every NFA is minimal.

**Answer key:** 1A, 2A, 3A, 4A, 5B, 6A, 7A, 8A, 9C, 10B, 11A, 12A, 13B, 14B, 15A, 16B.

### Open-ended questions

- **Easy:** Convert the regex `0*1` into an NFA and list the strings of length at most three that it accepts. *(Mark: correct fragment and language check.)*
- **Medium:** Carry out the ε-subset construction for an NFA with `s --ε→ p`, `p --a→ p`, `p --b→ f`, with `s` start and `f` accepting. *(Mark: closures, transitions, accepting subsets.)*
- **Hard:** Prove closure of regular languages under star by giving a complete NFA construction and proving both directions of correctness. *(Mark: fresh start/accept, ε-arrows, induction/segmentation argument.)*
- **Baka:** Prove the equivalence theorem “DFA = NFA = regex” as a cycle of constructions, clearly identifying which direction uses subset construction and which uses the six regex-to-NFA constructions. *(Mark: all three implications and conclusion about language classes.)*

---

## Topic 4 — DFA to regex, pumping lemma and Myhill–Nerode

### Easy MCQs

1. A GNFA transition label is a: A. regular expression B. stack string C. single state only D. TM configuration
2. State ripping removes: A. one intermediate state while updating regex labels B. all accepting states C. the alphabet D. the input
3. The pumping lemma for regular languages applies to: A. every regular language B. every language C. only finite languages D. only CFLs
4. The pumping lemma says a sufficiently long regular-language string has: A. a repeatable nonempty middle segment B. no repeated states C. a parse tree D. a stack
5. Myhill–Nerode distinguishes strings using: A. a suffix that changes membership B. a prefix that changes length only C. a stack D. a regex symbol

### Medium MCQs

6. In a GNFA, there is normally: A. one start state with no incoming edges and one accept state with no outgoing edges B. no start state C. no labels D. only deterministic labels
7. To disprove regularity with the pumping lemma, one must show: A. every valid decomposition fails for some pumping value B. one decomposition succeeds C. the language is infinite D. a DFA has many states
8. The quantifier order in a pumping-lemma contradiction is important because: A. the decomposition is chosen adversarially B. the prover may choose any decomposition after seeing `i` C. `p` is chosen after `w` D. `i` must be prime
9. If infinitely many strings are pairwise distinguishable, then the language is: A. not regular B. finite C. context-free only D. decidable only
10. The state-ripping recurrence for removing state `k` has the form: A. old paths ∪ paths through `k` B. old paths ∩ paths through `k` only C. complement D. reversal only

### Hard MCQs

11. For `L={0^n1^n:n≥0}`, the standard pumping string is: A. `0^p1^p` B. `0^p` C. `1^p` D. `0^p1^{p+1}`
12. In the pumping proof for `0^n1^n`, why is `y` restricted to the first block? A. `|xy|≤p` and the first `p` symbols are all `0` B. the lemma says `y` is a 0 C. the language has no 1s D. `p=0`
13. A pair `x,y` is distinguishable for `L` if: A. some `z` makes exactly one of `xz,yz` belong to `L` B. `|x|≠|y|` C. `x≠y` only D. both are accepted
14. Myhill–Nerode gives not only nonregularity but also: A. the number of equivalence classes equals the minimal DFA state count B. a PDA construction C. a TM simulation D. a CNF grammar
15. A pumping-lemma proof that merely finds one bad decomposition is: A. insufficient B. complete C. stronger than Myhill–Nerode D. a DFA construction

### Baka MCQ

16. Which proof strategy is valid for showing a language is not regular?  
   A. Assume regular, choose pumping length `p`, choose a suitable string, consider every legal split, and choose an `i` that breaks membership.  
   B. Choose one split and show it fails.  
   C. Show the language is infinite.  
   D. Show one DFA is inconvenient.

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Convert a two-state DFA for strings with an even number of `1`s into a regex using a GNFA. *(Mark: correct GNFA setup and an equivalent expression such as `0*(10*10*)*`.)*
- **Medium:** Use the regular pumping lemma to prove `{0^n1^n:n≥0}` is not regular. *(Mark: assume regular, choose `0^p1^p`, locate `y`, pump down/up, contradiction.)*
- **Hard:** Use Myhill–Nerode to prove `{0^n1^n:n≥0}` is not regular. *(Mark: pairwise distinguishable prefixes `0^i`, suffix `1^i`, infinite set.)*
- **Baka:** Prove that the language `{ww:w∈{0,1}*}` is not regular using either a carefully quantified pumping argument or an infinite distinguishability argument, and explain why `{ww^R}` behaves differently. *(Mark: valid quantifiers, boundary/parity issue handled, contrast with reversal.)*

---

## Topic 5 — CFGs, ambiguity, CNF, CFL pumping and PDAs

### Easy MCQs

1. A CFG is a 4-tuple `(V,Σ,R,S)` where `S` is the: A. start variable B. stack alphabet C. accepting state D. blank symbol
2. A production in a CFG has a variable on its: A. left-hand side B. right-hand side only C. both sides necessarily D. neither side
3. A parse tree represents: A. a derivation B. a DFA run only C. a TM tape only D. a reduction
4. A PDA is often described informally as: A. NFA + stack B. DFA + tape C. CFG + timer D. regex + counter only
5. The CFL pumping lemma pumps: A. two substrings in sync, `v` and `y` B. one state C. one symbol only D. the whole string

### Medium MCQs

6. A grammar is ambiguous if some generated string has: A. two parse trees/leftmost derivations B. no derivation C. length zero D. a terminal on the left
7. CNF rules are generally of the form: A. `A→BC` or `A→a`, with a possible start ε-rule B. `A→BCD` only C. `A→ε` for every variable D. `a→A`
8. CFLs are closed under: A. union, concatenation, star B. intersection and complement C. reversal only D. arbitrary quotient only
9. To show a language is not CFL using the pumping lemma, one must make every legal `uvxyz` split fail for some `i`. A. True B. False
10. A PDA stack provides: A. unbounded last-in-first-out memory B. random-access memory C. finite memory only D. a second input alphabet

### Hard MCQs

11. The language `{a^nb^nc^n:n≥0}` is: A. not context-free B. regular C. finite D. a CFL by `S→aSbSc`
12. The CFL pumping constraint `|vxy|≤p` ensures the pumped pieces lie: A. within a short parse-tree region B. at the ends only C. in separate tapes D. in the alphabet
13. In a PDA for `{0^n1^n}`, while reading `0`s it should generally: A. push markers, then pop one per `1` B. pop for every 0 C. ignore input D. reverse the stack
14. A CFL intersected with a regular language is always: A. context-free B. necessarily regular C. non-CFL D. undecidable
15. `S→aSb|ε` generates: A. `{a^nb^n:n≥0}` B. `{a^nb^m}` all pairs C. `{ww}` D. `{a,b}*`

### Baka MCQ

16. Why does the standard “intersection closure” argument fail for CFLs?  
   A. If CFLs were closed under intersection, intersecting two CFLs with `{a^*b^*c^*}` could force a known non-CFL such as `{a^nb^nc^n}`, contradicting non-context-freeness.  
   B. CFGs have no variables.  C. PDAs cannot read input.  D. CFLs are finite.

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Give a CFG for balanced parentheses. *(Mark: `S→SS|(S)|ε` and a short explanation.)*
- **Medium:** Give a CFG and PDA idea for `{0^n1^n:n≥0}`; trace acceptance of `0011`. *(Mark: grammar, stack push/pop behavior, correct trace.)*
- **Hard:** Prove `{a^nb^nc^n:n≥0}` is not context-free using the CFL pumping lemma. *(Mark: assume CFL, choose pumping string, exhaust placements of `v,y`, pump to break one count/order.)*
- **Baka:** Construct an unambiguous CFG for arithmetic expressions with variables, addition, multiplication and parentheses, explain precedence, and convert the core rules to CNF. *(Mark: precedence levels, associativity choice, ambiguity avoided, valid CNF conversion steps.)*

---

## Topic 6 — CFG–PDA equivalence and Turing-machine basics

### Easy MCQs

1. The CFG→PDA construction begins by putting the grammar’s: A. start variable on the stack B. terminals on the tape C. accepting state on input D. blank on stack only
2. A PDA can replace a variable on top of its stack using: A. a grammar production B. a DFA product C. a pumping lemma D. a reduction
3. A TM transition can: A. read, write and move left/right B. only read C. only move right D. branch only with ε
4. A TM has an infinite: A. tape B. finite stack C. alphabet of states D. input set
5. A recognizer may: A. loop B. never reject C. have no accept state D. only accept ε

### Medium MCQs

6. A TM is a 7-tuple including: A. `qaccept` and `qreject` B. a stack alphabet only C. a regex D. two start states
7. A decider differs from a recognizer because it: A. halts on every input B. has no reject state C. uses no tape D. must be deterministic
8. The backward PDA→CFG construction uses variables often written: A. `A_pq` B. `q_p` only C. `S_i` only D. `R_ij` only
9. A DFA is a PDA that: A. ignores its stack B. has two stacks C. cannot accept ε D. is nondeterministic
10. For the hierarchy, regular languages are: A. a subset of CFLs B. a superset of all Turing-recognizable languages C. incomparable with CFLs D. undecidable

### Hard MCQs

11. In the CFG→PDA simulation, a terminal on top of stack is matched by: A. consuming the same input symbol and popping it B. pushing a variable C. moving the TM head D. branching to all states
12. In the PDA→CFG construction, normalization is useful because it: A. makes stack behavior analyzable by `A_pq` variables B. removes the input alphabet C. makes all languages regular D. prevents ε
13. A TM that loops on some nonmember input recognizes but does not decide its language. A. True B. False
14. If a machine accepts `w`, then its accepting computation: A. reaches `qaccept` after finitely many steps B. must visit every tape cell C. must reject first D. must use a stack
15. `L(G)=L(P)` in the equivalence proof requires: A. both soundness and completeness directions B. only one derivation C. only finite language D. a deterministic PDA

### Baka MCQ

16. Which statement is strongest and correct?  
   A. CFGs and PDAs characterize exactly the context-free languages, while TMs can recognize languages beyond CFLs.  
   B. Every PDA language is regular.  C. Every TM halts.  D. Every CFL is nonregular.

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Describe a TM that decides strings over `{0,1}` ending in `1`. *(Mark: scan right, inspect final input symbol, halt accept/reject.)*
- **Medium:** Apply CFG→PDA construction to `S→0S1|ε` and trace the stack on `0011`. *(Mark: initialization, expansion, terminal matching, accept.)*
- **Hard:** Explain the `A_pq` variable construction for converting a normalized PDA to a CFG and prove one direction of correctness by induction on computation length. *(Mark: variable meaning, productions, induction base/step.)*
- **Baka:** Give a complete proof sketch of CFG–PDA equivalence, including normalization assumptions in the PDA→CFG direction, then place regular, context-free, decidable and recognizable languages in a justified inclusion diagram. *(Mark: both constructions, correctness, hierarchy.)*

---

## Topic 7 — Turing-machine programming, variants and Church–Turing thesis

### Easy MCQs

1. A TM “sweeping” technique means: A. scanning across the tape to locate/mark symbols B. using a regex C. pushing a stack D. branching on a certificate
2. A multitape TM has: A. several tapes/heads B. no input C. finite memory only D. no blank symbol
3. A nondeterministic TM accepts if: A. some computation branch accepts B. all branches accept C. the first branch accepts D. no branch loops
4. An enumerator is a TM with: A. an output mechanism that prints strings B. a DFA stack C. no states D. only one input symbol
5. The Church–Turing thesis is called a thesis because it: A. relates an informal notion to a formal model and is not a theorem inside the model B. has no evidence C. is a regex identity D. only concerns complexity

### Medium MCQs

6. Marking symbols is useful for: A. remembering which input items have been processed B. increasing alphabet size only C. avoiding halting D. proving P=NP
7. A standard TM can simulate a multitape TM with: A. polynomial/acceptable overhead, so language power is unchanged B. no overhead and no construction C. a stack only D. an NFA
8. Dovetailing is used to: A. interleave simulations so one looping branch does not block all others B. minimize DFAs C. convert regexes D. count states
9. A TM state-diagram label `a→b,R` means: A. read `a`, write `b`, move right B. read `b`, write `a`, move left C. accept D. reject
10. The formal, implementation and high-level descriptions of a TM differ mainly in: A. level of detail B. language power C. alphabet definition D. halting status

### Hard MCQs

11. To decide equal numbers of 0s and 1s, a useful algorithm: A. repeatedly pair one unmarked 0 with one unmarked 1 B. accept after first 0 C. count with a finite state only D. erase the tape immediately
12. NTM and deterministic TM have the same: A. language-recognition power, though not necessarily the same time complexity B. number of states C. transition functions D. running time
13. An enumerator can produce strings in: A. an order unrelated to input order B. only lexicographic order C. exactly one string D. finite time for every language
14. “Loop” in the accept/reject/loop trichotomy means: A. computation never halts B. input contains a cycle C. TM has no states D. machine rejects
15. A list-management TM technique typically uses: A. delimiters and marked regions to store multiple items on one tape B. only the finite control C. an intersection construction D. a CNF formula

### Baka MCQ

16. Which conclusion follows from the standard simulation results?  
   A. Multitape and nondeterministic TMs do not change which languages are recognizable, but their efficiency can differ.  
   B. Nondeterminism makes undecidable languages decidable.  C. Enumerators decide every language.  D. A TM model is irrelevant to both power and complexity.

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Give an implementation-level TM description deciding `{w∈{0,1}*: w has equally many 0s and 1s}`. *(Mark: repeated pairing/marking and halt conditions.)*
- **Medium:** Give a TM algorithm deciding strings with twice as many `0`s as `1`s. *(Mark: pair each 1 with two unmarked 0s, reject on failure, verify no leftovers.)*
- **Hard:** Explain how a single-tape TM simulates a two-tape TM and argue that the simulation preserves language recognition. *(Mark: encoded tape regions, head markers, scan/update cycle.)*
- **Baka:** Prove “a language is Turing-recognizable iff some enumerator enumerates it” using dovetailing in the recognizable→enumerator direction and a recognizer that searches the enumerator output in the other direction. *(Mark: both directions and loop-safe scheduling.)*

---

## Topic 8 — Complexity measures, Big-O and model robustness

### Easy MCQs

1. `T(n)=O(f(n))` is an asymptotic: A. upper bound B. lower bound C. exact equality D. probability
2. `T(n)=Ω(f(n))` is an asymptotic: A. lower bound B. upper bound C. finite bound D. language
3. `Θ(f(n))` means: A. both `O(f(n))` and `Ω(f(n))` B. neither C. only exponential D. only exact equality
4. Input length is commonly denoted: A. `n` B. `p` only C. `q` D. `Γ`
5. Polynomial time means `O(n^k)` for: A. some constant `k` B. every real `k` C. no `k` D. `k=n`

### Medium MCQs

6. `1000n+100` is: A. `O(n)` B. `O(log n)` C. `O(2^n)` only D. `Ω(2^n)`
7. `n^2+n+1` is: A. `Θ(n^2)` B. `Θ(n)` C. `Θ(2^n)` D. `Θ(log n)`
8. `2^{log_2 n}` equals: A. `n` B. `2n` C. `log n` D. `n^2`
9. A polynomial composed with a polynomial is: A. polynomial B. always exponential C. undefined D. noncomputable
10. Complexity classes aim to be robust because: A. reasonable machine models simulate one another with manageable overhead B. all algorithms have same steps C. input length is irrelevant D. every problem is easy

### Hard MCQs

11. If `T(n)=O(n^3)` and `S(n)=O(n^2)`, sequentially running both is: A. `O(n^3)` B. `O(n^5)` necessarily C. `O(n^6)` D. exponential
12. A number `N` represented in binary has input length roughly: A. `log N` B. `N` C. `N^2` D. `1`
13. A DP algorithm running `O(nt)` is not automatically polynomial in the binary input length if: A. `t` may be exponentially large in its bit-length B. `n=1` C. it uses a table D. it has a recurrence
14. Which ordering is correct? A. `log n = O(√n)=O(n)=O(n log n)=O(n^2)` B. reverse of this C. `2^n=O(n^2)` D. `n!=O(2^n)`
15. A constant factor usually does not affect: A. membership in a standard asymptotic class B. correctness C. input encoding D. acceptance

### Baka MCQ

16. A student calls Subset Sum polynomial because a DP takes `O(nt)` and each number is at most `2^n`. The key error is: A. confusing pseudopolynomial time in the numeric target with polynomial time in the binary input length B. using dynamic programming C. measuring `n` D. using positive integers

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Prove `7n-2=O(n)` and `7n-2=Ω(n)`. *(Mark: explicit constants and threshold.)*
- **Medium:** Arrange `√n`, `log n`, `n`, `n log n`, `2^n` in ascending growth order and justify each adjacent comparison. *(Mark: correct order and asymptotic reasoning.)*
- **Hard:** Explain why the Subset Sum DP with runtime `O(nt)` is pseudopolynomial when numbers are binary encoded. *(Mark: input bit-length, `t` can be exponential, distinction from polynomial.)*
- **Baka:** Prove polynomial model robustness at the level expected in the course: if a multitape algorithm takes polynomial time, explain why the standard single-tape simulation remains polynomial, identifying the source of the overhead. *(Mark: configuration encoding, simulated scan/update, polynomial bound.)*

---

## Topic 9 — The class P

### Easy MCQs

1. `P` is the class of decision problems decidable in: A. deterministic polynomial time B. any finite time C. exponential time only D. no time
2. `PATH` asks whether: A. a path exists between specified vertices B. a formula is satisfiable C. a DFA is minimal D. a TM loops
3. Polynomial time is considered a formal notion of: A. efficient computation B. undecidability C. grammar ambiguity D. randomness
4. `n^100` is: A. polynomial B. exponential C. factorial D. not a function
5. `2^n` is generally: A. not polynomial B. linear C. constant D. logarithmic

### Medium MCQs

6. `P=∪_{k≥0}`: A. `DTIME(n^k)` B. `NTIME(2^k)` C. `SPACE(log k)` D. `REGEX(k)`
7. If an algorithm calls a polynomial-time subroutine polynomially many times, the combined algorithm is: A. polynomial B. necessarily exponential C. undecidable D. not an algorithm
8. A graph represented by an adjacency matrix of `n` vertices has input size: A. `Θ(n^2)` B. `Θ(log n)` C. `Θ(2^n)` D. `Θ(1)`
9. Model independence of P means: A. reasonable models differ at most by polynomial overhead B. all exact runtimes match C. every language is in P D. P is machine-free
10. `MODEXP` is an example in the lecture of a problem in: A. P B. undecidable languages C. non-CFLs D. NP only

### Hard MCQs

11. If a problem is in `DTIME(n^5)`, then it is: A. in P B. not in P C. in NP only D. undecidable
12. Why is `n=1000` comparison between `n^3` and `2^n` illustrative? A. polynomial and exponential growth diverge dramatically B. both are equal C. input encoding disappears D. it proves P≠NP
13. Closure under composition is useful because: A. larger algorithms can be assembled from polynomial subroutines B. it eliminates correctness proofs C. it makes every function linear D. it changes deterministic to nondeterministic
14. A problem having no known polynomial algorithm means: A. it may still be in P; lack of knowledge is not a proof B. it is definitely outside P C. it is undecidable D. it is NP-complete
15. `P` contains: A. all regular-language decision problems with ordinary encodings B. no graph problems C. only finite languages D. all undecidable problems

### Baka MCQ

16. Which inference is valid? If `A≤P B` and `B∈P`, then: A. `A∈P` B. `B∉P` C. `A` is NP-complete D. `P=NP` necessarily

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Determine whether `n^100 log n`, `10^{log_2 n+10}`, `n^{log n}`, and `(log n)^{100}` are polynomially bounded. *(Mark: simplify each and classify.)*
- **Medium:** Give a polynomial-time algorithm for PATH and analyze it under adjacency-list representation. *(Mark: BFS/DFS and `O(V+E)`.)*
- **Hard:** Prove that the composition of two polynomial-time algorithms is polynomial-time. *(Mark: if outer makes polynomially many calls and each call has polynomial input/time, compose bounds.)*
- **Baka:** Explain why a claimed polynomial-time algorithm must specify the input encoding, then analyze a problem whose numeric values are binary-encoded and show how the same code can be polynomial in value but exponential in input length. *(Mark: encoding-sensitive complexity argument.)*

---

## Topic 10 — The class NP and polynomial-time reductions

### Easy MCQs

1. NP can be defined using: A. nondeterministic polynomial time B. only deterministic exponential time C. finite automata D. undecidability
2. A certificate is: A. a polynomial-size witness B. a TM state C. a regex operator D. a stack symbol
3. A verifier should run in: A. polynomial time B. factorial time C. no time D. exponential time necessarily
4. `A≤P B` means instances of `A` can be: A. transformed to instances of `B` in polynomial time B. deleted C. solved only by a PDA D. complemented
5. The direction of a reduction is: A. from the problem being reduced to the target problem B. target to source only C. arbitrary D. from answer to input

### Medium MCQs

6. To prove `L∈NP`, specify certificate, verifier, and: A. polynomial runtime B. a DFA C. a pumping length D. a grammar ambiguity
7. If `A≤P B` and `B∈P`, then: A. `A∈P` B. `A` is undecidable C. `B∉NP` D. `P=NP`
8. If `A` is NP-hard and `A∈P`, then: A. `P=NP` B. `P≠NP` C. `A` is regular D. no conclusion
9. A reduction proof needs correctness in: A. both directions `w∈A iff f(w)∈B` B. one direction only C. neither direction D. only on yes-instances
10. Verifying a proposed Sudoku completion involves: A. checking rows, columns and subgrids in polynomial time B. searching all completions C. using a stack D. pumping

### Hard MCQs

11. The distinction between finding and verifying explains why: A. NP may contain problems with easy verification but unknown efficient search B. verification is always hard C. P has no certificates D. all NP problems are outside P
12. A polynomial reduction may: A. increase instance size polynomially B. increase size exponentially C. change yes to no arbitrarily D. use an oracle for the target
13. To prove `A` is NP-hard using known NP-hard `B`, one should show: A. `B≤P A` B. `A≤P B` only C. `A∈P` D. `B∈P`
14. A Karp reduction is generally a: A. many-one transformation producing one target instance B. randomized walk C. grammar derivation D. stack simulation
15. NP is known to satisfy: A. `P⊆NP` B. `NP⊆P` proven C. `P=NP` proven D. `NP` has no certificates

### Baka MCQ

16. A student proves `A≤P B` and then says this proves `B` is at least as easy as `A`. The correct interpretation is: A. `B` is at least as hard as `A` under polynomial reductions; an efficient solver for `B` would give one for `A`. B. `A` is harder than `B` always. C. they are equivalent. D. no relation exists.

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Show that CLIQUE is in NP by giving a certificate and verifier. *(Mark: vertex subset, size/edge checks, polynomial runtime.)*
- **Medium:** Describe a polynomial-time reduction from Independent Set to Clique using graph complementation. *(Mark: map `(G,k)` to `(`complement of `G`,k`)`, equivalence proof, polynomial construction.)*
- **Hard:** Prove that a proposed reduction is invalid if it only proves “yes in source implies yes in target” but not the reverse direction. Give a concrete counterexample pattern. *(Mark: false positives and failure of solver transfer.)*
- **Baka:** Design and prove a reduction for a new problem, such as `VERTEX-COVER≤P INDEPENDENT-SET`, including the transformation, both correctness directions, and a polynomial bound on output size/time. *(Mark: complement relationship and full reduction proof.)*

---

## Topic 11 — SAT, 3SAT, Cook–Levin and NP-completeness

### Easy MCQs

1. SAT asks whether a Boolean formula has: A. a satisfying assignment B. a parse tree C. a DFA D. a shortest path
2. A CNF formula is an AND of: A. clauses, each an OR of literals B. variables only C. TMs D. stacks
3. 3SAT restricts clauses to: A. at most/exactly three literals depending on convention; in this course the reduction uses 3-literal clauses B. zero literals C. one variable total D. arbitrary grammars
4. Cook–Levin proves SAT is: A. NP-complete B. regular C. undecidable D. in coNP only
5. To prove a problem NP-complete, show it is in NP and: A. NP-hard B. regular C. finite D. outside P

### Medium MCQs

6. In proving `L∈NP`, the verifier receives: A. input `w` and certificate `c` B. only `c` C. only a DFA D. a pumping length
7. A reduction from SAT to 3SAT must preserve: A. satisfiability, via `φ` satisfiable iff `φ'` satisfiable B. exact syntax only C. number of variables exactly D. runtime only
8. A long clause can be converted to 3CNF by: A. introducing auxiliary variables and chained clauses B. deleting literals C. replacing AND with OR D. using a PDA
9. Cook–Levin encodes a polynomial-time NTM computation as: A. a Boolean formula describing a valid accepting tableau B. a DFA only C. a regex D. a CFG only
10. If SAT is NP-complete and SAT∈P, then: A. P=NP B. P≠NP C. SAT is undecidable D. NP disappears

### Hard MCQs

11. The Cook–Levin reduction must be generic because: A. it handles any `L∈NP` by encoding the accepting computation of its verifier/NTM B. there are finitely many NP languages C. SAT has no variables D. reductions need no correctness proof
12. A clause `(x)` can be represented in 3CNF while preserving satisfiability by: A. padding with auxiliary variables in a gadget B. deleting it C. changing `x` to `¬x` D. making it a PDA
13. For NP-hardness of 3SAT, the useful direction is: A. SAT≤P3SAT B. 3SAT≤PSAT only C. 3SAT∈P D. SAT∈coNP
14. A computation tableau records: A. successive configurations of a bounded-time TM computation B. only the input string C. parse trees D. DFA states only
15. NP-complete problems are: A. in NP and at least as hard as every NP problem under polynomial reductions B. outside NP C. all undecidable D. necessarily in P

### Baka MCQ

16. Which is the core logical structure of Cook–Levin?  
   A. For every `L∈NP`, choose an NTM `M` and polynomial time bound `p`, construct in polynomial time a formula `φ_{M,w}` that is satisfiable iff `M` accepts `w` within `p(|w|)` steps.  
   B. Convert every DFA directly to SAT.  
   C. Show SAT has no verifier.  
   D. Enumerate all assignments in polynomial time.

**Answer key:** 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A, 9A, 10A, 11A, 12A, 13A, 14A, 15A, 16A.

### Open-ended questions

- **Easy:** Given a CNF formula, explain how to verify a proposed satisfying assignment in polynomial time. *(Mark: evaluate each literal/clause and runtime in formula length.)*
- **Medium:** Convert a CNF clause with four literals into an equisatisfiable 3CNF gadget and explain the role of the new variable. *(Mark: valid chain gadget and both satisfiability directions.)*
- **Hard:** Prove a standard NP-completeness result such as `3SAT≤P CLIQUE` at a high level: define the graph, clique size, and the two correctness directions. *(Mark: one vertex per literal occurrence, compatible edges, one-per-clause argument.)*
- **Baka:** Give a structured Cook–Levin proof outline: encode tableau cells, enforce exactly one symbol/state per cell, enforce the initial row and local consistency, and explain why the formula is polynomial-size and satisfiable exactly for accepting computations. *(Mark: all constraint families, local-window argument, size bound, iff proof.)*

---

## Compact revision checklist

Before the test, practise drawing and tracing machines by hand; writing quantified pumping-lemma proofs; identifying the direction of reductions; and stating the input encoding when discussing time complexity. For open-ended answers, correctness should be argued with an invariant, an induction, or both directions of an iff statement—not only with a diagram or an example.

