from common import topic

topic('A1',[
('What does f(n)=O(g(n)) assert for eventually nonnegative functions?', 'An eventual constant-factor upper bound',['Equality for every n','An eventual lower bound only','The same running time on every input'],'There must be fixed c>0 and n0 with f(n)≤c g(n) for all n≥n0.'),
('Which notation requires both an eventual upper and lower constant-factor bound?','Θ',['O alone','Ω alone','An exact equality sign'],'Θ combines O and Ω for the same comparison function.'),
('For f(n)=3n²+7n+4, which term determines its tight growth class?','n²',['7n','4','The coefficient 3 alone'],'For n≥1 all lower terms are bounded by constants times n²; the quadratic term supplies a lower bound.'),
('Can constants c and n0 depend on n in a Big-O proof?','No; they must be fixed',['Only c may depend on n','Only n0 may depend on n','Both may vary with every input'],'The quantifier order chooses constants before requiring the inequality for every sufficiently large n.'),
('For n≥1, which pair witnesses 3n²+7n+4∈Θ(n²)?','3n²≤f(n)≤14n²',['14n²≤f(n)≤3n²','f(n)=3n² for all n','n³≤f(n)≤14n²'],'Use n≤n² and 1≤n² to obtain the upper coefficient 3+7+4=14.'),
('A worst-case cost W(n) is Θ(n²). Which statement must hold?','W(n) is also O(n³)',['Every input takes Θ(n²)','W(n) is Ω(n³)','The best case is Θ(n²)'],'For n≥1, n²≤n³; an upper bound need not be tight. Worst-case information does not determine every input.'),
('If f∈O(g) and g∈O(h), which implication follows?','f∈O(h)',['h∈O(f)','f∈Θ(h)','f∈Ω(h)'],'Multiply the two fixed upper-bound constants and take the larger threshold.'),
('Which statement correctly distinguishes a bound from a case?','O is an upper bound; worst case selects a cost function',['O means worst case by definition','Ω means best case by definition','Θ means average case by definition'],'One can give O, Ω or Θ bounds on best-, average- or worst-case functions.'),
('Let f(n)=n² for even n and n for odd n. What is true relative to n²?','f∈O(n²) but f∉Ω(n²)',['f∈Θ(n²)','f∉O(n²)','f∈Ω(n²) but not O(n²)'],'On odd n, f/n²=1/n tends to zero, preventing a positive eventual lower constant.'),
('For f(n)=n and g(n)=n(2+sin n), what tight relation holds for n≥1?','f∈Θ(g)',['f grows strictly faster than g','No relation because g oscillates','f∉O(g)'],'Since 1≤2+sin n≤3, g/3≤f≤g despite oscillation.'),
('For f(n)=n² and g(n)=n³, which combination is true?','f∈O(g), g∈Ω(f), f∉Θ(g)',['f∈Ω(g), g∈O(f)','f∈Θ(g) because both are polynomials','Neither bounds the other'],'The ratio f/g=1/n tends to zero; upper and reverse lower bounds hold, but not tight equivalence.'),
('If f,g are eventually positive and f∈Θ(g), what follows?','g∈Θ(f)',['f(n)=g(n) eventually','Their leading coefficients are equal','Their exact operation counts are equal'],'Invert the two positive constant inequalities; Θ is symmetric, exact equality is unnecessary.'),
('Malfoid sees an O(n²) upper bound and declares the algorithm cannot be linear. What is wrong?','A linear function also satisfies O(n²)',['Big O forbids loose bounds','Every O(n²) function is Ω(n²)','Only constants can have multiple upper bounds'],'An upper bound alone does not establish a matching lower bound; n≤n² for n≥1.')])

topic('A2',[
('What is the growth class of the constant function 1000?','Θ(1)',['Θ(n)','Θ(log n)','Θ(1000ⁿ)'],'Its value does not change with n; the magnitude of a fixed constant does not change its class.'),
('For fixed bases greater than one, how do log₂n and log₁₀n compare?','They are Θ of each other',['log₂n is polynomially larger','log₁₀n is constant','They have equal values'],'The change-of-base formula relates them by a fixed positive factor.'),
('Which eventually grows faster: √n or log n?','√n',['log n','They are Θ-equivalent','Neither has an eventual comparison'],'Every fixed positive power eventually dominates a logarithm.'),
('How many divisions by two take 64 to 1?','6',['5','7','64'],'64→32→16→8→4→2→1 contains six divisions.'),
('Put log n, n, n log n, n² in increasing eventual growth order.','log n < n < n log n < n²',['n < log n < n² < n log n','log n < n log n < n < n²','n² < n log n < n < log n'],'A logarithm is below a positive power; multiplying n by log n exceeds n but remains below n² eventually.'),
('Simplify Θ(7n²+2n log n+90).','Θ(n²)',['Θ(n log n)','Θ(n³)','Θ(1)'],'The quadratic term dominates n log n and the constant.'),
('For fixed k>0, compare nᵏ with 2ⁿ as n grows.','nᵏ=o(2ⁿ)',['2ⁿ=o(nᵏ)','They are Θ-equivalent','The answer depends only on the first ten n values'],'Every fixed-degree polynomial is eventually dominated by a fixed-base exponential.'),
('A loop starts x=1 and repeatedly doubles x while x<n. For integer n≥1, how many iterations occur?','⌈log₂n⌉',['⌊log₂n⌋+1 always','n−1 always','2ⁿ'],'After k iterations x=2ᵏ; the smallest k with 2ᵏ≥n is the ceiling logarithm, including zero for n=1.'),
('Order n⁵, 2ⁿ, 3ⁿ and n! by eventual growth.','n⁵ < 2ⁿ < 3ⁿ < n!',['n! < n⁵ < 2ⁿ < 3ⁿ','n⁵ < n! < 2ⁿ < 3ⁿ','2ⁿ < 3ⁿ < n⁵ < n!'],'Fixed-degree polynomials precede fixed-base exponentials, whose larger base wins; factorial eventually dominates every fixed base.'),
('What is 2^(log₂n), and what is 2^(2 log₂n)?','n and n²',['log₂n and 2n','n and 2n','2n and n²'],'Use inverse exponent/log identities, then 2^(2log₂n)=(2^log₂n)².'),
('A loop uses x=n, then x=⌊x/2⌋ while x>1. For integer n≥1, how many iterations occur?','⌊log₂n⌋',['⌈log₂n⌉ always','n/2 exactly','⌊log₂n⌋+1'],'The floor-halving sequence reaches one after the number of full powers of two in n. For n=1 there are zero iterations.'),
('Which is a valid reason that n log n∈O(n²)?','log n∈O(n), so multiplying by n gives the bound',['log n=n for all n','n log n and n² have identical leading terms','All products are quadratic'],'An eventual bound on the logarithm can be multiplied by the nonnegative factor n.'),
('An exponential algorithm wins at n=8. Does that establish better asymptotic growth than a quadratic algorithm?','No; finite measurements do not determine eventual growth',['Yes; one input determines asymptotics','Yes if the exponential has a smaller constant','Both must therefore be Θ(n²)'],'Constants and small-input effects can dominate finite tests; asymptotic comparison concerns sufficiently large n.')])

topic('A3',[
('In T(n)=3T(n/4)+n, what do 3 and 4 describe?','Three recursive calls, each on size n/4',['Four calls on size n/3','Three units of total work','A recursion depth of four'],'The multiplier counts children; the divisor shrinks each child size.'),
('For n=64 in T(n)=3T(n/4)+n, what are the first-level child sizes?','16,16,16',['4,4,4','21,21,22','16,16,16,16'],'Each of three calls receives one quarter of 64.'),
('For T(n)=aT(n/b)+f(n), what is the number of nodes at depth i?','aⁱ',['bⁱ','i a','n/bⁱ'],'Each level multiplies the number of calls by a.'),
('For n=bᴸ and constant-size leaves, what is the recursion depth?','L=log_b n',['n/b','log_a n always','a log_b n'],'Solve n/bᴸ=1. The branch count does not set the shrink depth.'),
('For T(n)=3T(n/4)+n, what is the total nonrecursive work at depth i?','n(3/4)ⁱ',['n(4/3)ⁱ','n/4ⁱ','3n at every level'],'There are 3ⁱ nodes, each doing n/4ⁱ work.'),
('Let T(1)=1 and T(n)=3T(n/4)+n on powers of four. What is T(16)?','37',['28','21','64'],'T(4)=3+4=7, then T(16)=3·7+16=37.'),
('Under that recurrence, what is the leaf count for n=64?','27',['16','64','9'],'The depth is log₄64=3, so there are 3³ leaves.'),
('For T(n)=2T(n/2)+n, what is the work per non-leaf level?','n',['n/2','2ⁿ','log₂n'],'At depth i, 2ⁱ nodes each do n/2ⁱ work, yielding n.'),
('Let T(1)=1 and T(n)=3T(n/4)+n. What is T(64)?','175',['148','192','85'],'Level costs are 64+48+36, with 27 leaves of cost one: total 175.'),
('Why must leaf costs be included when summing a recursion tree?','They may dominate or change the total even when internal work shrinks',['Leaves always cost zero','Only the root contributes to time','Leaf count equals depth'],'Leaves represent actual base-case calls; their aggregate cost is count times per-leaf cost.'),
('For T(n)=4T(n/2)+n, T(1)=1, what is the leaf contribution on powers of two?','n²',['n','log₂n','4n'],'Depth log₂n gives 4^(log₂n)=n² leaves, each costing one.'),
('Does drawing all nodes at a level mean ordinary recursive code executes them simultaneously?','No; a level sum is an analysis device',['Yes; every recursive program is parallel','Yes if calls have equal sizes','Only leaves execute sequentially'],'Ordinary depth-first recursion visits branches sequentially; the tree groups their total work without asserting a schedule.'),
('A student multiplies root cost n by depth and ignores changing level work for 3T(n/4)+n. What should replace that calculation?','Sum n(3/4)ⁱ and include leaves',['Multiply n by number of children only','Assume all levels cost n','Use depth as total time'],'The geometric level ratio is 3/4, so work decreases; copying the n log n merge-sort argument is invalid.')])

topic('A4',[
('For T(n)=aT(n/b)+f(n), what is the Master-Theorem comparison exponent?','p=log_b a',['p=log_a b','p=a/b','p=a−b'],'The leaf count is a^(log_b n)=n^(log_b a).'),
('Which supplied case covers f(n)=Θ(nᵖ)?','Case 2',['Case 1','Case 3 automatically','None for any recurrence'],'Equal-order per-level contributions add one logarithmic factor.'),
('What must accompany polynomially larger f(n) in supplied case 3?','Regularity a f(n/b)≤c f(n), c<1 eventually',['Equality a=b','A negative f(n)','A fixed recursion depth'],'The regularity condition controls the decrease of work away from the root.'),
('For T(n)=4T(n/4)+n, what is p?','1',['0','2','4'],'log₄4=1.'),
('For T(n)=4T(n/2)+n, what is the tight solution?','Θ(n²)',['Θ(n)','Θ(n log n)','Θ(n² log n)'],'p=2 and n=O(n^(2−1)); supplied case 1 applies.'),
('For T(n)=4T(n/4)+n, what is the tight solution?','Θ(n log n)',['Θ(n)','Θ(log n)','Θ(n²)'],'p=1 and f=Θ(n); case 2 adds a logarithm.'),
('For T(n)=2T(n/4)+n, which regularity multiplier works?','c=1/2',['c=2','c=1','No c<1 exists'],'2f(n/4)=n/2=(1/2)f(n).'),
('For T(n)=2T(n/4)+n, what is the tight solution?','Θ(n)',['Θ(√n)','Θ(n log n)','Θ(n²)'],'p=1/2; n is polynomially larger and the regularity multiplier is 1/2.'),
('Using the course logarithmic case-2 extension with k≥0, solve T(n)=2T(n/2)+n log²n.','Θ(n log³n)',['Θ(n log²n)','Θ(n² log n)','Θ(log³n)'],'Here p=1, k=2; summing logarithmic level costs adds one power of log.'),
('For T(n)=8T(n/2)+n² log n, which conclusion follows?','Θ(n³) by a polynomial gap below n³',['Θ(n³ log n) by case 2','Θ(n² log n) by case 3','The log factor prevents every case'],'Since log n=O(n^(1/2)), f=O(n^(5/2)); choose epsilon 1/2 below p=3.'),
('For T(n)=2T(n/2)+n², verify case-3 regularity and solve.','2f(n/2)=n²/2; Θ(n²)',['2f(n/2)=2n²; Θ(n²)','2f(n/2)=n; Θ(n log n)','No regularity bound exists'],'The ratio is 1/2, and n² exceeds the comparison n by a polynomial factor.'),
('What is wrong with choosing epsilon=1/log n in a Master-Theorem polynomial-gap proof?','Epsilon must be a fixed positive constant',['Epsilon must always be exactly 1','Logarithms cannot appear anywhere','Only integer epsilon values are allowed'],'The theorem requires one fixed positive gap exponent for all sufficiently large n.'),
('A student sees f(n)>nᵖ for n=100 and chooses case 3. What evidence is missing?','An eventual polynomial gap and regularity',['The value of T(100) only','The proof that a=b','A graph at ten more inputs only'],'A single inequality does not establish the theorem hypotheses.')])

topic('A5',[
('Why does the supplied equal-subproblem Master Theorem not directly fit T(n)=T(n/2)+T(n/3)+n?','The recursive subproblem sizes differ',['The recurrence contains a plus sign','n is not a valid toll','The function is certainly exponential'],'There is no single common shrink factor b for both calls.'),
('If a theorem does not apply, what follows about the recurrence?','Another method is needed',['No asymptotic bound exists','The recurrence is invalid','The answer must be exponential'],'Failure of sufficient hypotheses is not a statement about solvability.'),
('Does n log n exceed n by a polynomial factor n^epsilon for some fixed epsilon>0?','No',['Yes with epsilon=1','Yes with epsilon=log n','Only for base-two logs'],'For every fixed positive epsilon, log n=o(n^epsilon).'),
('For n>1, how does n/log n compare with n in tight order?','It is not Θ(n)',['It is Θ(n)','It is Ω(n log n)','It equals n−1'],'The ratio (n/log n)/n=1/log n tends to zero.'),
('For 2T(n/2)+n/log n, why does supplied case 1 fail?','n/log n is not O(n^(1−epsilon)) for any fixed epsilon>0',['The toll is larger than n²','a must exceed b','The toll is negative'],'The ratio (n/log n)/n^(1−epsilon)=n^epsilon/log n is unbounded.'),
('For 2T(n/2)+n/log n, why does supplied plain case 2 fail?','The toll is not Θ(n)',['There is no recursion','log₂2 is undefined','The toll is exactly n'],'The comparison exponent is one, but the toll-to-n ratio tends to zero.'),
('The course case-2 log extension assumes k≥0. Can it be used with f=n log^(−1)n?','No; k=−1 lies outside its stated hypothesis',['Yes by replacing −1 with 0','Yes because −1 is a constant','Only if n is a power of two'],'An extension must be used with its actual stated range; another proof can handle this recurrence.'),
('For 2T(n/2)+n/log n, why does supplied case 3 fail?','The toll is smaller than n, not polynomially larger',['Its regularity ratio is always zero','Case 3 requires a=1','Case 3 applies automatically'],'Comparison is against n^(log₂2)=n; the required lower polynomial gap is absent.'),
('Suppose a toll is n log n and comparison term is n. What does the course k≥0 logarithmic extension give?','Θ(n log²n)',['Θ(n²)','Θ(n log n)','No logarithmic extension can apply'],'This is k=1 within the extension; unlike k=−1, it adds one log power.'),
('A proof claims log n≥n^0.01 eventually. What is the consequence for its case-3 argument?','The premise is false; n^0.01 eventually exceeds log n',['The proof is valid because 0.01 is small','The premise holds only for base-two logs','It proves Θ(n²)'],'Every fixed positive power eventually dominates the logarithm, however slowly.'),
('For T(n)=T(n−1)+1, what prevents the standard Master-Theorem form?','The shrink factor is not a fixed b>1',['There is only one recursive call','The toll is constant','The recurrence has a base case'],'Subtracting one is not division by one fixed b>1; expansion gives a different-depth tree.'),
('Can one infer that f(n)=Ω(nᵖ) implies case 3?','No; case 3 needs a fixed positive polynomial gap plus regularity',['Yes; Ω always means a strict gap','Yes; equality is enough','Only when f has positive coefficients'],'The equal case f=Θ(nᵖ) itself disproves that inference.'),
('A student writes “Master Theorem fails, therefore no solution.” What is the sound correction?','The chosen theorem is insufficient; expand or prove a bound another way',['All such recurrences are NP-complete','The base case must be deleted','Use a guessed case without hypotheses'],'Recursion trees, substitution and other applicable methods remain available.')])

topic('A6',[
('What is the first step of a substitution proof?','State a precise bound and induction domain',['Assume the desired conclusion without conditions','Delete the base case','Compute one large input only'],'A quantified claim specifies constants, valid n values and bases to prove.'),
('In an induction proof, where may the induction hypothesis be used?','On smaller arguments covered by the hypothesis',['On the current n without proof','On all real values automatically','Only on the base case'],'Recursive child sizes must lie in the chosen domain and precede n.'),
('Does proving T(n)≤c n² alone prove Θ(n²)?','No; it proves an upper bound only',['Yes; any upper bound is tight','Yes if c=1','It proves only a lower bound'],'A matching eventual lower bound must be supplied separately.'),
('Why check base cases after choosing constants?','The constants must satisfy both bases and induction step',['Base cases never affect constants','They replace the induction step','Only the largest input matters'],'An induction cannot start if the chosen bound fails at its initial inputs.'),
('For T(1)=0 and T(n)=T(n−1)+n−1, prove T(n)≤n². Which inductive expression appears?','(n−1)²+n−1=n²−n',['(n−1)²+n−1=n²+n','n²+n−1','(n−1)³'],'Substituting T(n−1)≤(n−1)² gives slack n, enough for the upper bound.'),
('Under T(1)=0 and T(n)=T(n−1)+n−1, what is T(4)?','6',['7','10','16'],'The successive values are 0,1,3,6 by adding 1,2,3.'),
('Why can a stronger induction claim be easier to prove?','Extra slack can absorb additive terms',['Stronger claims require no bases','It changes the algorithm','It permits circular reasoning'],'A carefully chosen lower-order subtraction or extra constant may close the algebra.'),
('For T(n)=2T(n/2)+n−1, T(1)=1 on powers of two, why does T(n)≤c n log₂n fail at n=1?','The right side is zero but T(1)=1',['log₂1 is infinite','T(1) is undefined','It fails only for negative c'],'No finite c makes a zero upper expression cover a positive base.'),
('For T(1)=1,T(n)=2T(n/2)+n−1 on powers of two, start the claim T(n)≤c n log₂n at n=2. Which c is sufficient for the base and usual step?','Any c≥2',['Only c=0','Any 0<c<1','No finite c'],'T(2)=3≤4 when c=2; substitution yields c n log₂n−c n+n−1≤c n log₂n.'),
('For T(1)=1, T(n)=2T(n/2)+n−1, which exact solution fits powers of two?','n log₂n+1',['n log₂n','n²','2n−1'],'Substitute: 2[(n/2)(log₂n−1)+1]+n−1=n log₂n+1; it also fits n=1.'),
('An induction proves its step only for even n but claims every positive integer n. What is missing?','A proof covering odd n or a restricted stated domain',['A larger constant alone always fixes it','No issue; all integers are even asymptotically','Only T(1)'],'Rounding and child domains must be justified; a powers-of-two proof cannot silently become an all-integer proof.'),
('If a guessed bound fails in the induction algebra, what is justified?','Revise the claim or method and prove the new statement',['Declare the guess false in all cases','Drop the troublesome positive term','Use the induction conclusion as a premise'],'An unsuccessful proof attempt does not itself disprove a bound; missing slack or an unsuitable hypothesis may be responsible.'),
('Malfoid guesses O(n log n), checks n=2, and stops. What is still required?','An induction step and all relevant bases/domains',['Only a timing benchmark','Nothing; one base proves all n','A picture with a logarithm'],'A guess plus one numeric check is not a quantified asymptotic proof.')])

topic('A7',[
('For T(n)=n+T(n−2), which property determines the terminal base?','Whether n is even or odd',['Whether n is prime only','The logarithm base','The value of n modulo three'],'Repeated subtraction by two preserves parity.'),
('With T(1)=0, T(2)=1, what is T(3)?','3',['4','2','6'],'T(3)=3+T(1)=3.'),
('With T(1)=0, T(2)=1, what is T(4)?','5',['4','7','8'],'T(4)=4+T(2)=5.'),
('For positive integer n≥2, when is ⌊n/2⌋ equal to ⌈n/2⌉?','When n is even',['When n is odd','For all n','Only when n=2'],'Even halves are integral; odd halves round in opposite directions.'),
('For T(n)=n+T(n−2), T(1)=0, T(2)=1, what is T(8)?','19',['20','16','21'],'T(8)=8+6+4+1=19; the base T(2) is one, not two.'),
('Under the same recurrence, what is T(7)?','15',['16','12','20'],'7+5+3+T(1)=7+5+3+0=15.'),
('For n=2k, which exact formula follows?','T(2k)=k(k+1)−1',['T(2k)=k²','T(2k)=2k²+1','T(2k)=k(k+2)'],'Sum 2+4+…+2k=k(k+1), then replace the first 2 by base value one.'),
('For n=2k+1, which exact formula follows?','T(2k+1)=k(k+2)',['T(2k+1)=(k+1)²','T(2k+1)=k(k+1)−1','T(2k+1)=2k+1'],'Sum 3+5+…+(2k+1), with T(1)=0: the odd-number square sum minus one gives k(k+2).'),
('Why can exact formulas differ by parity while both have Θ(n²) growth?','Their leading terms are quadratic and lower-order corrections differ',['Θ requires the exact same formula','Parity disappears from every exact count','Odd inputs are never asymptotic inputs'],'Put k=n/2 or (n−1)/2 into the formulas; each has leading coefficient 1/4.'),
('For T(n)=T(n−2)+n, T(1)=0 and T(2)=1, what is T(9)?','24',['25','23','36'],'9+7+5+3+0=24; equivalently k=4 gives k(k+2)=24.'),
('When extending a divide recurrence from powers of two to all n, what needs justification?','Rounding, bases and any monotonicity used to compare sizes',['Only renaming n','Assuming floor and ceiling are always identical','Deleting odd inputs'],'Floors/ceilings alter child sizes; the comparison argument must be stated rather than presumed.'),
('If T(2) changes from 1 to 9 but T(1) stays 0 in the subtraction-by-two recurrence, which inputs change?','Only even inputs, each by 8',['All inputs, each by 8','Only odd inputs','Even inputs, each multiplied by 9'],'Every even expansion reaches T(2) once; odd expansions reach T(1) instead.'),
('A student expands T(8) as 8+6+4+2. What correction is needed for T(2)=1?','Replace the terminal 2 by 1, giving 19',['Add T(1) as well','Replace every even term by 1','No correction; base values are optional'],'Expansion stops at the stated base function value; it does not apply the recurrence to that base.')])
