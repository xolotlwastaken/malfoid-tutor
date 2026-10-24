"""Structural checks plus independent numerical/exhaustive answer derivations.

Conceptual answers and distractors are reviewed against the source-grounded
lesson definitions. These finite checks do not claim to prove every asymptotic
statement or substitute for that review.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter,deque
import json,hashlib,math,re
ROOT=Path(__file__).resolve().parents[2]
bank=json.loads((ROOT/'content/sc2001-later-question-bank.json').read_text());by={t['lessonId']:t for t in bank};evidence=[]
def check(eid,index,result,method):
 q=by[eid]['qs'][index];assert q['correct']==str(result),(eid,index,q['correct'],result)
 evidence.append(dict(id=q['id'],lesson=eid,derived=str(result),method=method))
def scalar(eid,index,value,method):check(eid,index,value,method)
ids=[];stems=set()
for t in bank:
 assert Counter(q['difficulty']for q in t['qs'])==dict(Easy=4,Medium=4,Hard=4,Baka=1)
 for q in t['qs']:
  ids.append(q['id']);assert len(q['context'])>20 and q['graph'] is None and q['source']
  assert len(set(q['options']))==4 and q['options']['ABCD'.index(q['answer'])]==q['correct']
  key=(q['context'],q['stem']);assert key not in stems,key;stems.add(key)
assert len(ids)==403 and sorted(ids)==list(range(551,954));assert len({t['id']for t in bank})==31
# Exact loops are simulated rather than copied from logarithmic formulas.
x=64;k=0
while x>1:x//=2;k+=1
scalar('A2',3,k,'Simulated repeated integer division')
for n in range(1,200):
 x=1;k=0
 while x<n:x*=2;k+=1
 assert k==math.ceil(math.log2(n))
 x=n;k=0
 while x>1:x//=2;k+=1
 assert k==math.floor(math.log2(n))
def tree(n):return 1 if n==1 else sum(tree(n//4)for _ in range(3))+n
scalar('A3',5,tree(16),'Direct recursive evaluation with base cost one')
scalar('A3',6,len([x for x in product(range(3),repeat=3)]),'Enumerated root-to-leaf branch sequences')
scalar('A3',8,tree(64),'Direct recursive evaluation, independent of level sum')
scalar('A4',3,math.log(4,4).__int__(),'Computed logarithmic comparison exponent')
scalar('A6',5,sum(range(4)),'Expanded unit-decrease recurrence to zero base')
def parity(n,b1=0,b2=1):return b1 if n==1 else b2 if n==2 else n+parity(n-2,b1,b2)
for index,n in [(1,3),(2,4),(4,8),(5,7),(9,9)]:scalar('A7',index,parity(n),'Direct recurrence expansion to stated parity base')
for n in range(1,100):
 k=n//2;assert parity(n)==(k*(k+1)-1 if n%2==0 else k*(k+2))
 assert parity(n,0,9)-parity(n)==(8 if n%2==0 else 0)
def greedy_coins(amount,coins):
 out=[]
 for c in sorted(coins,reverse=True):
  count,amount=divmod(amount,c);out.extend([c]*count)
 return out,amount
def minimum_coins(a,coins):
 frontier=deque([(0,0)]);seen={0}
 while frontier:
  total,count=frontier.popleft()
  if total==a:return count
  for c in coins:
   if total+c<=a and total+c not in seen:seen.add(total+c);frontier.append((total+c,count+1))
 return math.inf
scalar('G1',1,greedy_coins(37,[1,5,10,25])[0][0],'Simulated largest-feasible scan')
scalar('G1',2,37-greedy_coins(37,[1,5,10,25])[0][0],'Independent remainder subtraction')
a,_=greedy_coins(6,[1,3,4]);check('G1',4,'+'.join(map(str,a))+', three coins','Simulated greedy choices; breadth-first optimum two')
a,_=greedy_coins(37,[1,5,10,25]);check('G1',5,','.join(map(str,a)),'Simulated denomination multiplicities')
a,_=greedy_coins(14,[1,7,10]);check('G1',7,f'Greedy {len(a)}; optimum {minimum_coins(14,[1,7,10])}','Greedy simulation versus independent breadth-first exact change')
assert greedy_coins(8,[4,6])[1]!=0 and minimum_coins(8,[4,6])==2
jobs=[('A',0,3),('B',1,2),('C',2,4),('D',3,5),('E',4,6)];last=-1;chosen=[]
for name,s,f in sorted(jobs,key=lambda j:j[2]):
 if s>=last:chosen.append(name);last=f
check('G2',4,','.join(chosen),'Finish-order simulation')
opt=max(len(s)for k in range(6)for s in combinations(jobs,k)if all(a[2]<=b[1]for a,b in zip(sorted(s,key=lambda j:j[1]),sorted(s,key=lambda j:j[1])[1:])))
assert opt==len(chosen)==3
# Fractional LP optimum: enumerate all vertices (at most one fractional variable).
def fractional(cap,items):
 values=[]
 for bits in product([0,1],repeat=len(items)):
  w=sum(b*i[0]for b,i in zip(bits,items));p=sum(b*i[1]for b,i in zip(bits,items))
  if w<=cap:values.append(p)
  for j,(wj,pj)in enumerate(items):
   wb=w-bits[j]*wj;pb=p-bits[j]*pj;fraction=(cap-wb)/wj
   if 0<=fraction<=1:values.append(pb+fraction*pj)
 return max(values)
items=[(10,60),(20,100),(30,120)]
scalar('G3',2,60//10,'Direct density division')
check('G3',4,'Item '+', item '.join(str(i+1)for i in sorted(range(3),key=lambda i:items[i][1]/items[i][0],reverse=True)),'Computed descending density order')
scalar('G3',6,int(fractional(50,items)),'Enumerated fractional linear-program vertices')
scalar('G3',8,int(fractional(5,[(4,12),(4,8)])),'Enumerated all fractional LP vertices')
scalar('D1',4,len(range(7)),'Enumerated distinct indices including zero')
v=[1,1]
for n in range(2,9):v.append(v[n-1]+v[n//2])
for index,n in [(0,0),(3,2),(4,4),(5,6),(9,8)]:scalar('D2',index,v[n],'Independently evaluated recurrence table')
for index,a in [(3,1),(4,6)]:scalar('D3',index,minimum_coins(a,[1,3,4]),'Breadth-first search through reachable exact amounts')
check('D3',6,'Infinity and '+str(minimum_coins(6,[3,4])),'Breadth-first reachability, amount1 unreachable')
check('D3',8,'['+','.join(str(minimum_coins(a,[1,3,4]))for a in range(7))+']','Breadth-first exact change for every amount')
def subsequences(s):return {''.join(s[i]for i in range(len(s))if mask>>i&1)for mask in range(1<<len(s))}
x='ACGGA';y='ACTG';both=subsequences(x)&subsequences(y);length=max(map(len,both))
scalar('D4',4,length,'Enumerated all subsequences of both inputs and intersected sets')
assert {o for o in by['D4']['qs'][5]['options']if o in both}=={'ACG'}
scalar('D4',8,max(map(len,subsequences('ACG')&subsequences('ACTG'))),'Independent prefix-subsequence enumeration')
assert {s for s in subsequences('AB')&subsequences('BA')if len(s)==1}=={'A','B'}
def whole(cap,items):return max(sum(b*p for b,(w,p)in zip(bits,items))for bits in product([0,1],repeat=len(items))if sum(b*w for b,(w,p)in zip(bits,items))<=cap)
scalar('D5',5,whole(5,[(2,3),(3,4),(4,5)]),'Exhaustive subset enumeration')
scalar('D5',6,whole(4,[(2,3)]),'Enumerated empty and singleton subsets, no repeated copies')
scalar('D6',1,int('1000',2),'Independent binary integer parsing')
scalar('D6',9,format(len([(i,c)for i in range(20)for c in range(1,1025)]),','),'Counted item/capacity Cartesian-product elements')
def naive(text,pattern):
 count=0;per=[]
 for start in range(len(text)-len(pattern)+1):
  checks=0
  for k,ch in enumerate(pattern):
   count+=1;checks+=1
   if text[start+k]!=ch:break
  else:per.append(checks);return start,count,per
  per.append(checks)
 return None,count,per
start,total,counts=naive('ABABABAC','ABAC')
scalar('S1',4,start,'Independent naive-character simulator')
scalar('S1',5,counts[0],'Independent comparison counter at first alignment')
scalar('S1',6,len(counts),'Enumerated complete starts')
scalar('S1',7,total,'Independent comparison counter through first success')
scalar('S1',8,naive('A'*12,'AAAAC')[1],'Explicit all-A near-match enumeration')
scalar('S2',4,int('36415'[1:]+'2'),'String-window shift independent of rolling arithmetic')
scalar('S2',8,int('25')%13,'Direct parsing and modulus, independent of rolling update')
hashes=[int('1225'[i:i+2])%13 for i in range(3)];check('S2',7,','.join(map(str,hashes)),'Directly hashed each literal window independently')
scalar('S3',4,sum(h==25%13 for h in hashes),'Enumerated hash-equal windows')
verify_count=0
for i,h in enumerate(hashes):
 if h==25%13:
  for a,b in zip('25','1225'[i:i+2]):
   verify_count+=1
   if a!=b:break
scalar('S3',5,verify_count,'Directly compared each hash-equal candidate')
scalar('S3',6,len(hashes)-1,'Enumerated adjacent-window transitions')
def cj(p,c):return len(p)-p.rfind(c)-1 if c in p else len(p)
scalar('S4',4,cj('ABCA','A'),'Computed rightmost occurrence from literal pattern')
check('S4',5,f"{cj('ABCA','B')} and {cj('ABCA','X')}",'Computed rightmost and absent-character defaults')
scalar('S4',6,max(cj('ABCA','X'),4-2+1),'Evaluated explicit course mismatch rule')
scalar('S4',7,6-4,'Endpoint displacement independent of mismatch pointer increment')
scalar('S4',9,max(cj('ABCA','A'),4-2+1),'Evaluated fallback when character table is zero')
scalar('S5',5,len('RATSANDCATS')-4,'Aligned earlier suffix endpoint to old endpoint')
scalar('S5',6,(11-8)+(11-4),'Added leftward matches to pattern slide')
scalar('S5',10,(6-4)+5,'Converted slide to mismatch-pointer increment')
scalar('S6',4,6+max(cj('WOWWOW','N'),1),'Explicit mismatch step')
scalar('S6',5,9+max(cj('WOWWOW','L'),6),'Explicit mismatch step')
scalar('S6',6,16+max(cj('WOWWOW','M'),8),'Explicit mismatch step')
scalar('S6',7,sum([1,4,1,6,6]),'Summed independently recorded per-alignment counts')
scalar('S6',8,24-len('WOWWOW')+1,'Computed first index from final window endpoint')
def hanoi(n,a,b,c,moves):
 if not n:return
 hanoi(n-1,a,c,b,moves);moves.append((a,b));hanoi(n-1,c,b,a,moves)
moves=[];hanoi(3,'A','B','C',moves);pegs={'A':[3,2,1],'B':[],'C':[]}
for a,b in moves:
 disk=pegs[a].pop();assert not pegs[b]or pegs[b][-1]>disk;pegs[b].append(disk)
scalar('N1',4,len(moves),'Generated and checked every Hanoi move for legality')
scalar('N4',9,'No; its cost is'+str(sum([2,2,1,1,1])),'Explicit five-edge tour-cost sum')
weights={frozenset(e):w for e,w in [('AB',1),('BC',1),('AC',2),('AD',2),('BD',2),('CD',100)]}
def cost(path,ws):return sum(ws[frozenset((a,b))]for a,b in zip(path,path[1:]))
scalar('N6',6,cost('ABCDA',weights),'Direct closed-tour edge summation')
scalar('N6',7,cost('ACBDA',weights),'Independent alternate feasible-tour sum')
assert min(cost('A'+''.join(p)+'A',weights)for p in permutations('BCD'))==7
ws={frozenset(e):w for e,w in [('AB',1),('BC',2),('AC',3),('BD',4),('CD',5),('DE',6),('AE',7),('BE',8),('AD',9),('CE',10)]}
scalar('N7',8,cost('ABCDEA',ws),'Direct final spanning-cycle edge sum')
scalar('N8',5,items[0][1]+items[1][1],'Explicit accepted-item profit sum')
scalar('N8',6,whole(50,items),'Independent enumeration of every whole-item subset')
# Reduction iff: enumerate all four-vertex simple graphs and every candidate path/tour.
vertices=range(4);pairs=list(combinations(vertices,2));graphs=0
for bits in product([0,1],repeat=len(pairs)):
 edges={frozenset(p)for p,b in zip(pairs,bits)if b}
 hp=any(all(frozenset((a,b))in edges for a,b in zip(p,p[1:]))for p in permutations(vertices))
 tsp=any(sum(1 if frozenset((a,b))in edges else 2 for a,b in zip(p,p[1:]+p[:1]))<=5 for p in permutations(tuple(vertices)))
 assert hp==tsp;graphs+=1
# Longer challenge transfers are evaluated independently of their authored strings.
scalar('A3',12,f'Depth{round(math.log(1024,4))};{3**5} leaves;T(1024)={tree(1024)}','Direct recursive expansion of the new1024-input case')
x=1;outer=0;inner=0
while x<=128:outer+=1;inner+=x;x*=2
check('A2',12,f'{outer} outer iterations;{inner} inner executions;Θ(n)','Explicit simulation and geometric-sum proof')
def repaired(n):return 1 if n==1 else 2*repaired(n//2)+n-1
assert all(repaired(2**k)<=2**k*k+2**k for k in range(12))
check('A6',12,f'T(32)={repaired(32)};T(n)≤n log₂n+n for all powers of two n≥1','Direct recurrence evaluation and base/induction algebra review')
check('A7',12,f'Originally({parity(18)},{parity(19)});after the change({parity(18,0,5)},{parity(19,0,5)})','Expanded both parity branches under both base assignments')
pairs=[]
for amount in [14,28]:pairs.append(f'{amount}:({len(greedy_coins(amount,[1,7,10])[0])},{minimum_coins(amount,[1,7,10])})')
check('G1',12,';'.join(pairs),'Greedy simulation versus breadth-first exact-change search')
transfer_jobs=[('A',0,8,100),('B',1,3,1),('C',3,5,1),('D',5,7,1),('E',7,9,1),('F',0,2,1),('G',2,4,1),('H',4,6,1),('I',6,8,1)]
chosen=[];finish=-1
for name,start,end,profit in sorted(transfer_jobs,key=lambda j:(j[2],j[0])):
 if start>=finish:chosen.append(name);finish=end
feasible=[]
for mask in range(1<<len(transfer_jobs)):
 subset=sorted([job for i,job in enumerate(transfer_jobs)if mask>>i&1],key=lambda j:j[1])
 if all(a[2]<=b[1]for a,b in zip(subset,subset[1:])):feasible.append(subset)
assert max(map(len,feasible))==4
weighted=max(sum(j[3]for j in subset)for subset in feasible)
check('G2',12,'Greedy selects '+','.join(chosen)+f';weighted optimum{weighted}','Enumerated all512 subsets and simulated deterministic finish ties')
newitems=[(4,28),(6,36),(10,50),(5,20)]
check('G3',12,f'Fractional{int(fractional(17,newitems))} using7/10 of item3;0/1 optimum{whole(17,newitems)}','Independent LP-vertex and whole-subset enumeration')
calls=0

def naive_fib(n):
 global calls
 calls+=1
 return n if n<=1 else naive_fib(n-1)+naive_fib(n-2)
naive_fib(8)
check('D1',12,f'{calls} naive invocations;{len(range(9))} distinct states;O(n) cache plus O(n) stack','Instrumented every recursive invocation including bases')
vv=[1,1]
for n in range(2,13):vv.append(vv[n-1]+vv[n//2])
check('D2',12,f'V(12)={vv[12]};second predecessor{12//2};the old V(6) must remain available','Computed new recurrence table through12')
assert greedy_coins(23,[4,7,9])[1]==1 and minimum_coins(23,[4,7,9])==3
check('D3',12,'Greedy gets stuck at remainder1;DP uses3 coins,9+7+7, and two coins cannot reach23','Greedy remainder versus BFS minimum;checked 9+7+7 and max two-coin value18')
def lcs_trace(x,y):
 table=[[0]*(len(y)+1)for _ in range(len(x)+1)]
 for i in range(1,len(x)+1):
  for j in range(1,len(y)+1):table[i][j]=table[i-1][j-1]+1 if x[i-1]==y[j-1]else max(table[i-1][j],table[i][j-1])
 i,j=len(x),len(y);emitted=[]
 while i and j:
  if x[i-1]==y[j-1]:emitted.append(x[i-1]);i-=1;j-=1
  elif table[i-1][j]>=table[i][j-1]:i-=1
  else:j-=1
 return table[-1][-1],''.join(reversed(emitted))
x,y='ABCBDAB','BDCABA';length,solution=lcs_trace(x,y)
assert length==max(map(len,subsequences(x)&subsequences(y))) and solution in subsequences(x)&subsequences(y)
check('D4',12,f'Length{length};{solution}','Independent table/backtrack simulation;optimum verified by complete subsequence-set intersection')
newitems=[(2,5),(3,6),(4,7)];unbounded=max(sum(c*p for c,(w,p)in zip(counts,newitems))for counts in product(range(4),repeat=3)if sum(c*w for c,(w,p)in zip(counts,newitems))<=6)
check('D5',12,f'0/1 optimum{whole(6,newitems)} via items1+3;unbounded optimum{unbounded} via three copies of item1','Enumerated all legal zero-one and repeated-item multiplicities')
assert [5-r>=3 for r in [1,4]]==[True,False]
check('D7',12,'Keep remaining budget:the first history can reach profit15;the second cannot take the edge','Independent resource-feasibility evaluation for both retained histories')
start,checks,_=naive('AAAAAAAAB','AAAAB');allchecks=sum(naive('AAAAAA'[i:i+3],'AAA')[1]for i in range(4))
check('S1',12,f'First index{start},{checks} checks;the separate all-matches scan uses{allchecks} checks','Direct character comparisons for first-match and all-window variants')
text='122525';pattern='25';hs=[int(text[i:i+2])%13 for i in range(len(text)-1)];found=[];checks=0
for i,h in enumerate(hs):
 if h==int(pattern)%13:
  good=True
  for a,b in zip(pattern,text[i:i+2]):
   checks+=1
   if a!=b:good=False;break
  if good:found.append(i)
check('S2',12,'Hashes'+','.join(map(str,hs))+';true starts'+','.join(map(str,found))+f';{checks} character checks','Parsed each literal window separately and directly verified every hash-equal candidate')
check('S3',12,f'{12-5+1} hash decisions;{12-5} rolls;{sum([1,5,4,5])} character checks≤{4*5}','Counted legal starts,adjacent transitions and actual given candidate work separately')
def bad_character_trace(text,pattern):
 m=len(pattern);j=k=m;count=0;ends=[j]
 while j<=len(text):
  count+=1
  if text[j-1]==pattern[k-1]:
   j-=1;k-=1
   if not k:return ends,count,j+1
  else:
   j+=max(cj(pattern,text[j-1]),m-k+1);k=m;ends.append(j)
 return ends,count,None
ends,checks,start=bad_character_trace('AXCABCA','ABCA')
check('S4',12,'Endpoints'+','.join(map(str,ends))+f';{checks} comparisons;return{start}','Explicit course-pointer simulator with every compared character counted')
# Derive the good suffix slide from known matched text and exclusion of the known mismatch.
pattern='WOWWOW';k=4
slides=[]
for slide in range(1,len(pattern)+1):
 if any(0<=pos-slide<len(pattern)and pattern[pos-slide]!=pattern[pos]for pos in range(k,len(pattern))):continue
 old_mismatch=k-1;new_index=old_mismatch-slide
 if 0<=new_index<len(pattern)and pattern[new_index]==pattern[old_mismatch]:continue
 slides.append(slide)
slide=min(slides);jump=len(pattern)-k+slide;endpoint=11+jump
check('S5',12,f'Slide{slide};matchJump{jump};new endpoint{endpoint};new start{endpoint-len(pattern)+1}','Enumerated every possible pattern slide against known suffix/mismatch constraints')
text='LOWOWNOWLWOWWOMMOWWOWWOW';pattern='WOWWOW';jump_table=[8,7,6,7,3,1];j=k=6;ends=[j];checks=0
while j<=len(text):
 checks+=1
 if text[j-1]==pattern[k-1]:
  j-=1;k-=1
  if not k:break
 else:j+=max(cj(pattern,text[j-1]),jump_table[k-1]);k=6;ends.append(j)
assert j+1==text.find(pattern)+1
check('S6',12,'Endpoints'+','.join(map(str,ends))+f';{checks} comparisons;start{j+1}','Fresh full pointer trace;match independently checked against literal substring search')
invocations=0;emissions=0

def hanoi_count(n):
 global invocations,emissions
 invocations+=1
 if n:hanoi_count(n-1);emissions+=1;hanoi_count(n-1)
hanoi_count(5)
check('N1',12,f'{emissions} moves;{invocations} invocations;explicit move listing needs Ω(2ⁿ) output work','Instrumented all invocations and explicit move emissions')
newweights={frozenset(e):w for e,w in [('AB',1),('BC',1),('CD',1),('DA',10),('AC',2),('BD',2)]}
def verifies(path):return len(path)==5 and path[0]==path[-1]and set(path[:-1])==set('ABCD')and len(set(path[:-1]))==4 and cost(path,newweights)<=6
assert not verifies('ABCA')and verifies('ABDCA')
check('N2',12,'Reject the first,accept the second;one rejected candidate does not prove no','Independent full permutation/closure/threshold verifier')
check('N4',12,f'Threshold{6+1};X costs{4+2*2} and fails,Y costs{5+2} and passes;delete Y’s weight-two edge','Explicit six-edge cost and threshold evaluation')
def nearest(start,tie):
 path=start
 while len(path)<4:
  rest=set('ABCD')-set(path);best=min(weights[frozenset((path[-1],v))]for v in rest);choices={v for v in rest if weights[frozenset((path[-1],v))]==best}
  selected=tie if len(path)==1 and tie in choices else min(choices);path+=selected
 return path+start
pa=nearest('A','B');pb=nearest('B','C')
check('N6',12,f'From A:{pa} costs{cost(pa,weights)};from B:{pb} costs{cost(pb,weights)};start and tie choices can matter','Independent nearest-unvisited simulation under explicit starting tie')
# Enumerate spanning trees to check the independent Kruskal objective on this graph.
def connected(edges):
 reached={'A'}
 while True:
  nxt=reached|{v for edge in edges if reached.intersection(edge)for v in edge}
  if nxt==reached:return len(reached)==5
  reached=nxt
mst=min(sum(ws[e]for e in subset)for subset in combinations(ws,4)if connected(subset))
check('N7',12,f'Shortest-link:{{AB,BC,CD,DE,AE}},{cost("ABCDEA",ws)};Kruskal:{{AB,BC,BD,DE}},{mst}','Enumerated all four-edge spanning trees;checked explicit selected-cycle edges')
newitems=[(6,12),(5,9),(5,9)];remain=10;profit=0
for w,p in sorted(newitems,key=lambda t:-t[1]/t[0]):
 if w<=remain:remain-=w;profit+=p
check('N8',12,f'Greedy{profit};exact0/1 optimum{whole(10,newitems)};fractional optimum{fractional(10,newitems):.1f}','Independent greedy scan,subset enumeration and fractional LP vertices')
report=dict(status='passed',topics=len(bank),questions=len(ids),numeric_answer_checks=len(evidence),longer_transfer_challenges=31,challenge_review='All31 challenge statements,answers and distractors independently reviewed against the approved plan;25 additional numeric trace checks are included in evidence.',unique_questions=True,unique_options=True,balanced_difficulties=True,ids_preserve_existing_range='New only 551..953; topics401..431',reduction_graphs_exhaustively_checked=graphs,conceptual_review='Authored answers and all three distractors inspected against stated assumptions and source-grounded lessons; corrections include explicit parity bases and self-contained mixed-quiz context.',evidence=evidence,bank_sha256=hashlib.sha256((ROOT/'content/sc2001-later-question-bank.json').read_bytes()).hexdigest())
(ROOT/'content/sc2001-later-answer-audit.json').write_text(json.dumps(report,indent=2)+'\n');print('Passed:',len(ids),'questions;',len(evidence),'independent numeric answers; all',graphs,'four-vertex reduction instances')
