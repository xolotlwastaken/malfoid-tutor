"""Authoring helpers; choices are explicit and shuffled reproducibly."""
import json,random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=json.loads((ROOT/'web/content/sc2001-later-lessons.json').read_text())
BANK={}
CONTEXTS={
'A1':'Functions are eventually nonnegative, n is a positive integer, and asymptotic constants are fixed independently of n.',
'A2':'Compare eventual growth as n tends to infinity. Logarithm bases are fixed constants greater than one; exact loop counts use the explicitly stated update and stopping test.',
'A3':'Unless a question states another recurrence, use T(1)=1 and T(n)=3T(n/4)+n for powers of four. The root is depth zero; count each base call as cost one.',
'A4':'Use the supplied equal-shrink Master Theorem with fixed a≥1,b>1 and p=log_b a. The course logarithmic case-2 extension allows k≥0; case3 also requires regularity.',
'A5':'Use the supplied Master-Theorem cases and the course logarithmic extension with k≥0. Every polynomial-gap epsilon must be one fixed positive constant.',
'A6':'Substitution means a quantified induction proof, not merely substitution of sample values. Use each question’s stated recurrence and base; powers-of-two recurrences are restricted to that domain.',
'A7':'Unless explicitly changed, T(1)=0,T(2)=1 and T(n)=T(n−2)+n for integer n≥3. Write even n=2k and odd n=2k+1, preserving the terminal base.',
'G1':'Unlimited positive integer coin denominations; form the exact target. Largest-first greedy repeatedly chooses the largest feasible denomination. Do not invent unavailable coins.',
'G2':'Unweighted maximum-cardinality interval selection. Intervals are half-open [s,f), so touching endpoints are compatible. The worked jobs are A=[0,3),B=[1,2),C=[2,4),D=[3,5),E=[4,6).',
'G3':'Fractional knapsack has positive weights, nonnegative profits, optional items and at-most capacity. Worked instance: capacity50; items1=(10,60),2=(20,100),3=(30,120), written (weight,profit).',
'D1':'Use F(0)=0,F(1)=1,F(n)=F(n−1)+F(n−2) for the Fibonacci examples. Complexity counts constant-time arithmetic operations unless bit costs are explicitly discussed.',
'D2':'Use V(0)=V(1)=1 and V(n)=V(n−1)+V(floor(n/2)) for integer n≥2. Values are indexed by integer n; time counts constant-time arithmetic unless stated otherwise.',
'D3':'Minimum-coin exact change with unlimited positive integer denominations. Default worked set {1,3,4}; C[0]=0 and unreachable amounts have infinity. Explicit question sets override the default.',
'D4':'Default worked strings X=ACGGA,Y=ACTG. L[i,j] is the LCS length of first i and j characters. Backtrack from bottom-right; on unequal-character ties choose up. Explicit alternative strings override these.',
'D5':'0/1 knapsack: each positive-weight item is available at most once; capacity is an upper bound. P[c,j] uses the first j items. Worked items are (2,3),(3,4),(4,5), capacity5, as (weight,profit).',
'D6':'Measure encoded input length, distinguishing numeric capacity C or amount A from its binary digit count. O(nC) and O(kA) count assumed constant-time arithmetic operations.',
'D7':'DP states must preserve future legality and value; transitions must represent every relevant choice. State and graph assumptions are part of the problem, not implicit permissions to replace constraints.',
'S1':'Default text T=ABABABAC,pattern P=ABAC. Use zero-based indices, left-to-right naive comparisons, reset pattern index at each window and return the first match. Count character checks only.',
'S2':'Exact verified Rabin–Karp. Worked decimal example T=1225,P=25,d=10,q=13,window length2,H=10. Use canonical residues 0..q−1; zero-based occurrence starts.',
'S3':'Exact first-match Rabin–Karp. Worked decimal example T=1225,P=25,d=10,q=13. Count hash decisions, rolling updates and direct character checks separately; h counts verified equal-hash candidates.',
'S4':'Course one-based mismatch-pointer variant. P=ABCA,m=4; charJump[c]=m−rightmost(c), absent defaults m. On mismatch j+=max(charJump[T[j]],m−k+1), then k=m. A string drawing may use an independently labelled alignment.',
'S5':'Course one-based pattern positions. At mismatch k, suffix P[k+1..m] is matched. matchJump[k]=(m−k)+Slide[k]. Default table example WOWWOW,m=6, entries ordered k=1..6.',
'S6':'Course one-based scan for P=WOWWOW,m=6. matchJump[1..6]=[8,7,6,7,3,1]. On mismatch add max(charJump[T[j]],matchJump[k]) to j, then k=m; successful comparisons decrement both pointers.',
'N1':'Distinguish decision, exact optimisation and explicit enumeration. Standard Hanoi uses three pegs, moves one disk at a time and never places a larger disk on a smaller one.',
'N2':'P and NP refer to decision languages measured in encoded input length. Use the full feasibility predicate when checking a proposed certificate.',
'N3':'Use deterministic polynomial-time many-one reductions, denoted A≤pB. Keep source and target roles distinct; both logical directions must be considered.',
'N4':'HP→decision-TSP construction for a simple undirected n-vertex graph,n≥3: complete graph on the same vertices, original edges weight1, nonedges weight2, tour threshold n+1.',
'N5':'Consider formal NP-completeness for decision languages with polynomial many-one reductions. A and B are language names; any stated NP-completeness of A is a given premise.',
'N6':'Complete undirected graph with AB=1,BC=1,AC=2,AD=2,BD=2,CD=100. Nearest-neighbour starts A, picks the cheapest unvisited neighbour and finally returns A. No triangle-inequality assumption.',
'N7':'Five-vertex complete undirected graph, sorted edge weights AB1,BC2,AC3,BD4,CD5,DE6,AE7,BE8,AD9,CE10. Shortest-link rejects degree>2 and premature cycles; final spanning closure is allowed.',
'N8':'0/1 density heuristic sorts descending profit/weight, takes an item only if it fits, then continues. Worked capacity50; items1=(10,60),2=(20,100),3=(30,120) as(weight,profit). Fractions are forbidden.'
}
def topic(eid,items):
 assert len(items)==13,(eid,len(items))
 entry=next(e for e in MANIFEST if e['id']==eid);index=MANIFEST.index(entry);qs=[]
 for n,item in enumerate(items):
  stem,correct,wrong,why=item;assert len(wrong)==3 and len(set([correct]+wrong))==4,(eid,n)
  qid=551+13*index+n;options=[correct]+wrong;random.Random(qid).shuffle(options)
  qs.append(dict(id=qid,difficulty=('Easy' if n<4 else 'Medium' if n<8 else 'Hard' if n<12 else 'Baka'),stem=stem,correct=correct,options=options,answer='ABCD'[options.index(correct)],why=why,source=entry['sources'],lessonId=eid,context=CONTEXTS[eid],graph=None))
 BANK[eid]=dict(id=401+index,title=entry['title'],week=str(entry['week']),source=entry['sources']+' Matching later recordings unavailable; approved slides-and-notes grounding.',context=CONTEXTS[eid],graph=None,lessonId=eid,qs=qs)
def save():
 assert len(BANK)==31
 out=[BANK[e['id']]for e in MANIFEST];p=ROOT/'content/sc2001-later-question-bank.json';p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(len(out),'topics;',sum(len(t['qs'])for t in out),'questions;',p)
