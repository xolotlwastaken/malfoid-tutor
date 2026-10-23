"""Frozen, reproducible fresh practice inputs; computed traces, not guessed answer keys."""
from pathlib import Path
from collections import deque,Counter
import json,random,math,itertools
ROOT=Path(__file__).resolve().parents[2];WEB=ROOT/'web'
BASE=json.loads((WEB/'content/catalog-before-expansion.json').read_text())
bank=BASE['topics'];audit=[];next_id=91
LEVELS=['Easy','Medium','Hard','Baka']
def rng(t,v,level):return random.Random(200100+t*1000+v*31+LEVELS.index(level)*173)
def arr(a):return '['+', '.join(map(str,a))+']'
def vec(a):return '('+', '.join('INF' if x==math.inf else '-INF' if x==-math.inf else str(x) for x in a)+')'
def variants(correct,wrong):
 out=[]
 for x in wrong:
  if x!=correct and x not in out:out.append(x)
 assert len(out)>=3,(correct,out)
 return out[:3]
def choices_array(a):
 out=[]
 for i,j in itertools.combinations(range(len(a)),2):
  b=a[:];b[i],b[j]=b[j],b[i]
  if b!=a:out.append(arr(b))
 for i in range(len(a)):
  if isinstance(a[i],int):
   for delta in [1,-1,2]:b=a[:];b[i]+=delta;out.append(arr(b))
  elif len(str(a[i]))==1:
   for alt in ['A','B','-']:b=a[:];b[i]=alt;out.append(arr(b))
 return variants(arr(a),out)
def valid_heap_variants(a,mini=True):
 out=[]
 def valid(b):return all((b[(i-1)//2]<=b[i] if mini else b[(i-1)//2]>=b[i]) for i in range(1,len(b)))
 for i,j in reversed(list(itertools.combinations(range(len(a)),2))):
  b=a[:];b[i],b[j]=b[j],b[i]
  if b!=a and valid(b) and b not in out:out.append(b)
 if len(out)<3 and len(a)<=8:
  for b in itertools.permutations(a):
   b=list(b)
   if b!=a and valid(b) and b not in out:out.append(b)
   if len(out)>=3:break
 assert len(out)>=3
 return out[:3]

def trace_variants(a,fixed=()):
 out=[]
 for i,j in reversed(list(itertools.combinations([i for i in range(len(a)) if i not in fixed],2))):
  b=a[:];b[i],b[j]=b[j],b[i]
  if b!=a and arr(b) not in out:out.append(arr(b))
 return variants(arr(a),out)

def number_wrong(n):return [str(n+d) for d in [1,-1,2,-2,3,4] if n+d>=0]
def make(t,level,v,stem,correct,wrong,why,context,graph=None,evidence=None):
 global next_id
 wrong=variants(correct,wrong);opts=wrong[:];pos=rng(t,v,level).randrange(4);opts.insert(pos,correct)
 q=dict(id=next_id,difficulty=level,stem=stem,correct=correct,options=opts,answer='ABCD'[pos],why=why,context=context,graph=graph)
 bank[t-1]['qs'].append(q);audit.append(dict(id=next_id,topic=t,difficulty=level,evidence=evidence));next_id+=1

def heapify(a,i,mini=True,n=None):
 n=len(a) if n is None else n;swaps=[]
 while 2*i+1<n:
  j=2*i+1
  if j+1<n and ((a[j+1]<a[j]) if mini else (a[j+1]>a[j])):j+=1
  if (a[i]<=a[j]) if mini else (a[i]>=a[j]):break
  a[i],a[j]=a[j],a[i];swaps.append((i,j));i=j
 return swaps

def build(a,mini=True):
 a=a[:];states=[];sw=[]
 for i in range(len(a)//2-1,-1,-1):sw+=heapify(a,i,mini);states.append((i,a[:]))
 return a,states,sw

def insert(a,x):
 a.append(x);i=len(a)-1
 while i and a[(i-1)//2]>a[i]:p=(i-1)//2;a[p],a[i]=a[i],a[p];i=p

def extract(a):
 result=a[0];a[0]=a[-1];a.pop();heapify(a,0);return result

def insertion(a):
 a=a[:];states=[];sw=comp=0
 for i in range(1,len(a)):
  j=i-1
  while j>=0:
   comp+=1
   if a[j]<=a[j+1]:break
   a[j],a[j+1]=a[j+1],a[j];j-=1;sw+=1
  states.append((a[:],sw,comp))
 return states

def quick(a,right_first=False,less_equal=False):
 a=a[:];calls=[];comparisons=0;swaps=0
 def rec(lo,hi):
  nonlocal comparisons,swaps
  if lo>=hi:return
  p=a[hi];j=lo;scan=[]
  for i in range(lo,hi):
   comparisons+=1
   if (a[i]<=p if less_equal else a[i]<p):
    if i!=j:swaps+=1
    a[i],a[j]=a[j],a[i];j+=1
   scan.append((i,j,a[:]))
  if j!=hi:swaps+=1
  a[j],a[hi]=a[hi],a[j];calls.append(dict(lo=lo,hi=hi,pivot=p,q=j,array=a[:],scan=scan,comparisons=comparisons,swaps=swaps));
  if right_first:rec(j+1,hi);rec(lo,j-1)
  else:rec(lo,j-1);rec(j+1,hi)
 rec(0,len(a)-1);return a,calls,comparisons,swaps

def merge_trace(a):
 comps=writes=0;records=[]
 def rec(a):
  nonlocal comps,writes
  if len(a)<2:return a[:]
  mid=len(a)//2;left=rec(a[:mid]);right=rec(a[mid:]);out=[];i=j=0;local=0
  while i<len(left) and j<len(right):
   comps+=1;local+=1
   if left[i]<=right[j]:out.append(left[i]);i+=1
   else:out.append(right[j]);j+=1
  out+=left[i:]+right[j:];writes+=len(out);records.append((left,right,out,local));return out
 final=rec(a);return final,records,comps,writes

def graph_data(nodes,edges,directed=False):
 n=len(nodes);positions={u:[round(205+170*math.cos(2*math.pi*i/n)),round(72+55*math.sin(2*math.pi*i/n))] for i,u in enumerate(nodes)}
 es=[];labels=[]
 for index,(u,v,w) in enumerate(edges):
  curve=15 if directed and any(a==v and b==u for a,b,_ in edges) else 0
  a,b=positions[u],positions[v];dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy);ux,uy=dx/length,dy/length
  start=[a[0]+11*ux,a[1]+11*uy];end=[b[0]-11*ux,b[1]-11*uy]
  c1=[start[0]+dx/3-uy*curve,start[1]+dy/3+ux*curve];c2=[end[0]-dx/3-uy*curve,end[1]-dy/3+ux*curve]
  best=None
  for t in [.5,.35,.65,.25,.75]:
   p=[(1-t)**3*start[k]+3*(1-t)**2*t*c1[k]+3*(1-t)*t*t*c2[k]+t**3*end[k] for k in [0,1]]
   score=min([math.dist(p,z) for z in labels]+[math.dist(p,z)-6 for z in positions.values()])
   if best is None or score>best[0]:best=(score,t,p)
  if w is not None:labels.append(best[2])
  es.append([u,v,w,curve,best[1]])
 return dict(nodes=positions,edges=es,directed=directed)

def adjacency(nodes,edges,directed=False):
 out={u:[] for u in nodes}
 for u,v,w in edges:
  out[u].append((v,w))
  if not directed:out[v].append((u,w))
 return {u:sorted(vs) for u,vs in out.items()}

def bfs(nodes,edges,start,directed=False):
 adj=adjacency(nodes,edges,directed);dist={u:math.inf for u in nodes};par={u:'-' for u in nodes};dist[start]=0;q=deque([start]);states=[]
 while q:
  u=q.popleft()
  for v,w in adj[u]:
   if dist[v]==math.inf:dist[v]=dist[u]+1;par[v]=u;q.append(v)
  states.append((u,list(q),dist.copy(),par.copy()))
 return states,dist,par

def dfs(nodes,edges,directed=True):
 adj=adjacency(nodes,edges,directed);color={u:0 for u in nodes};parent={u:'-' for u in nodes};pre=[];post=[];stacks={};classes={};roots=[]
 def go(u,stack):
  color[u]=1;pre.append(u);stacks[u]=stack+[u]
  for v,w in adj[u]:
   if not color[v]:parent[v]=u;classes[u+v]='tree';go(v,stack+[u])
   elif color[v]==1:classes[u+v]='back'
   else:classes[u+v]='forward' if pre.index(u)<pre.index(v) else 'cross'
  post.append(u);color[u]=2
 for u in sorted(nodes):
  if not color[u]:roots.append(u);go(u,[])
 return dict(pre=pre,post=post,parent=parent,stacks=stacks,classes=classes,roots=roots)

def topo(nodes,edges):
 adj=adjacency(nodes,edges,True);ind={u:0 for u in nodes}
 for u,v,w in edges:ind[v]+=1
 order=[];ready_states=[]
 while len(order)<len(nodes):
  ready=sorted(u for u in nodes if ind[u]==0 and u not in order)
  if not ready:break
  u=ready[0];order.append(u)
  for v,w in adj[u]:ind[v]-=1
  ready_states.append(sorted(u for u in nodes if ind[u]==0 and u not in order))
 return order,ready_states

def topo_count(nodes,edges):
 count=0
 for p in itertools.permutations(nodes):
  rank={u:i for i,u in enumerate(p)}
  if all(rank[u]<rank[v] for u,v,w in edges):count+=1
 return count

def components(nodes,edges):
 a=adjacency(nodes,edges);seen=set();groups=[]
 for u in sorted(nodes):
  if u in seen:continue
  q=[u];seen.add(u);part=[]
  while q:
   v=q.pop();part.append(v)
   for w,_ in a[v]:
    if w not in seen:q.append(w);seen.add(w)
  groups.append(''.join(sorted(part)))
 return groups

def weighted(nodes,edges,start,mode='dijkstra',strategy='normal'):
 adj=adjacency(nodes,edges,mode!='prim');d={u:math.inf for u in nodes};par={u:'-' for u in nodes};d[start]=0;order=[];states=[];decreases=0
 while len(order)<len(nodes):
  u=min((u for u in nodes if u not in order),key=lambda u:((0 if u==start else 1,u) if strategy=='alphabet' else (d[u],-ord(u) if strategy=='reverse' else ord(u))));order.append(u)
  for v,w in adj[u]:
   if v in order:continue
   cand=w if mode=='prim' else d[u]+w
   if cand<d[v] and (strategy!='first' or d[v]==math.inf):d[v]=cand;par[v]=u;decreases+=1
  states.append((u,d.copy(),par.copy(),decreases))
 return order,d,par,states,decreases

def mst_all(nodes,edges):
 results=[]
 for chosen in itertools.combinations(edges,len(nodes)-1):
  p={u:u for u in nodes}
  def find(x):
   while x!=p[x]:x=p[x]
   return x
  valid=True
  for u,v,w in chosen:
   a,b=find(u),find(v)
   if a==b:valid=False;break
   p[a]=b
  if valid:results.append((sum(w for _,_,w in chosen),frozenset(''.join(sorted([u,v])) for u,v,w in chosen)))
 best=min(w for w,_ in results);trees=[s for w,s in results if w==best];return best,trees

def vector_wrong(vals,formatter=vec):
 out=[]
 indices=[i for i,x in enumerate(vals) if isinstance(x,(int,float)) and math.isfinite(x) and x!=0]
 if not indices:indices=[i for i,x in enumerate(vals) if isinstance(x,(int,float)) and math.isfinite(x)]
 for delta in [1,-1,2]:
  for i in indices:b=vals[:];b[i]+=delta;out.append(formatter(b))
 return variants(formatter(vals),out)

def sort_data(t,v,level,duplicates=False):
 r=rng(t,v,level);n={'Easy':5,'Medium':6,'Hard':8,'Baka':11}[level]+(v if level!='Baka' else 0)
 return [r.randrange(1,9) for _ in range(n)] if duplicates else r.sample(range(1,50),n)

def generate(t,level,v):
 r=rng(t,v,level);baka=level=='Baka';idx=LEVELS.index(level)
 if t==1:
  n=10 if baka else 5+idx+v;records=[(r.choice('ABC'),r.randrange(1,4),i+1) for i in range(n)]
  # Stable secondary-then-primary sorts. Three stable passes for the final tier.
  initial=[f'{a}{b}:{i}' for a,b,i in records]
  if baka:
   passes=[('letter',lambda z:z[0]),('number',lambda z:z[1]),('parity of number',lambda z:z[1]%2)]
  else:passes=[('number',lambda z:z[1]),('letter',lambda z:z[0])][:1 if level=='Easy' else 2]
  result=records[:]
  for _,key in passes:result=sorted(result,key=key)
  result=[f'{a}{b}:{i}' for a,b,i in result]
  wrong=choices_array(result)
  if baka:
   wrong=[]
   for reverse_pass in range(3):
    alt=records[:]
    for pass_index,(_,key) in enumerate(passes):
     if pass_index==reverse_pass:alt=list(reversed(alt))
     alt=sorted(alt,key=key)
    wrong.append(arr([f'{a}{b}:{i}' for a,b,i in alt]))
  make(t,level,v,'What is the final record sequence after these stable passes?',arr(result),wrong,'Apply the passes in the stated order. Each later stable pass preserves the earlier order inside equal-key groups. Result: '+arr(result)+'.','Records are letter, number, and identity: A2:7 means letter A, number 2, identity 7. Input '+arr(initial)+'. Perform stable ascending sorts by '+', then by '.join(k for k,_ in passes)+'. Parity is 0 for even and 1 for odd.' if baka else 'Input '+arr(initial)+'. Each record is letter + number : identity. Stably sort ascending by '+', then by '.join(k for k,_ in passes)+'. Move whole records.',evidence=dict(input=records,passes=[k for k,_ in passes],result=result))
 elif t==2:
  a=sort_data(t,v,level,baka);ss=insertion(a);stop=1 if level=='Easy' else min(3+v,len(a)-1) if level=='Medium' else len(a)-1;state,sw,co=ss[stop-1]
  if level in ['Easy','Medium']:
   correct=arr(state);wrong=choices_array(state);stem=f'What is the array after the complete outer iteration i={stop}?'
  else:
   correct=f'{arr(state)}; {sw} swaps; {co} key comparisons';wrong=[f'{arr(state)}; {sw+1} swaps; {co} key comparisons',f'{arr(state)}; {sw} swaps; {co+1} key comparisons',f'{arr(state)}; {sw+2} swaps; {co-1} key comparisons'];stem='What are the final array, total adjacent swaps, and total key comparisons?'
  make(t,level,v,stem,correct,wrong,f'The first {stop+1} positions form the sorted prefix. Through i={stop}, the trace makes {sw} swaps and {co} key comparisons. An unsuccessful key comparison counts; an index-bound test does not. State: '+arr(state)+'.',f'Input {arr(a)}. Zero-based adjacent-swap insertion sort: i=1..n-1, j=i-1; while j>=0, compare A[j]>A[j+1], swap and decrement j if true, otherwise stop. Equal keys do not swap.',evidence=dict(algorithm='insertion',input=a,stop=stop,result=state,swaps=sw,comparisons=co))
 elif t==3:
  a=sort_data(t,v,level);final,trace,co,writes=merge_trace(a);left,right,_,local=trace[-1]
  if level=='Easy':correct=arr(left);wrong=choices_array(left);stem='What is the sorted LEFT half immediately before the final top-level merge?'
  elif level=='Medium':take=min(5,len(final));correct=arr(final[:take]);wrong=choices_array(final[:take]);stem=f'What are the first {take} records written by the final top-level merge?'
  elif level=='Hard':correct=f'{arr(left)} + {arr(right)}; {local} front-key comparisons';wrong=[f'{arr(left)} + {arr(right)}; {local+d} front-key comparisons' for d in [1,-1,2]];stem='Which sorted halves are merged at the top level, and how many front-key comparisons does that merge use?'
  else:correct=f'{co} key comparisons; {writes} output writes';wrong=[f'{co+1} key comparisons; {writes} output writes',f'{co} key comparisons; {writes+len(a)} output writes',f'{co-1} key comparisons; {writes+2} output writes'];stem='Across the ENTIRE recursive sort, how many key comparisons and merge-output writes occur?'
  make(t,level,v,stem,correct,wrong,f'The final merge combines {arr(left)} and {arr(right)}, using {local} front-key comparisons. All merges together use {co} comparisons and {writes} output writes. Copying a remainder writes entries without further front-key comparisons.',f'Input {arr(a)}. Top-down merge sort; half-open ranges, midpoint floor((start+end)/2), left recursion first, left record first on ties. Count one key comparison only while both merge fronts exist. Count each write into a merge output, including remainder copies; do not count copying into temporary buffers.',evidence=dict(algorithm='merge',input=a,comparisons=co,writes=writes,halves=[left,right]))
 elif t==4:
  a=sort_data(t,v,level,baka);final,calls,co,sw=quick(a);first=calls[0]
  if level=='Easy':correct=f'{arr(first["array"])}; pivot index {first["q"]}';wrong=[f'{z}; pivot index {first["q"]}' for z in choices_array(first['array'])];stem='After the first complete partition, which array and settled pivot index result?'
  elif level=='Medium':scan=first['scan'][min(3+v,len(first['scan'])-1)];i,j,st=scan;correct=f'{arr(st)}; j={j}';wrong=[f'{z}; j={j}' for z in choices_array(st)];stem=f'Immediately after processing scan index i={i}, before the final pivot swap, what are A and j?'
  elif level=='Hard':qs=[c['q'] for c in calls[:4]];correct=arr(qs);wrong=vector_wrong(qs,arr);stem=f'What are the first {len(qs)} returned pivot indices in the actual recursive execution?'
  else:qs=[c['q'] for c in calls];correct=f'pivot indices {arr(qs)}; {co} comparisons; {sw} actual swaps';wrong=[f'pivot indices {arr([c["q"] for c in alt])}; {ac} comparisons; {asw} actual swaps' for _,alt,ac,asw in [quick(a,True),quick(a,False,True),quick(a,True,True)]];stem='Complete the entire sort. Which pivot-index sequence and operation totals are correct?'
  make(t,level,v,stem,correct,wrong,'First partition: '+arr(first['array'])+f', pivot at {first["q"]}. Recursive partition ranges/pivots are '+', '.join(f'[{c["lo"]},{c["hi"]}]->{c["q"]}' for c in calls)+f'. The full sort uses {co} comparisons and {sw} swaps between DISTINCT indices.',f'Input {arr(a)}. Inclusive one-scan quicksort: p=A[hi], j=lo; for i=lo..hi-1 compare A[i]<p, swap with A[j] and increment j when true; finally swap A[j],A[hi]. Recurse left before right, excluding the settled pivot. Self-swaps do not count as actual swaps.',evidence=dict(algorithm='quick',input=a,pivots=[c['q'] for c in calls],comparisons=co,swaps=sw))
 elif t==5:
  a=sort_data(t,v,level,True);p=4+(v%2);b=a[:];lo=mid=0;hi=len(b)-1;states=[];comparisons=0
  while mid<=hi:
   comparisons+=1
   if b[mid]<p:b[lo],b[mid]=b[mid],b[lo];lo+=1;mid+=1
   else:
    comparisons+=1
    if b[mid]>p:b[mid],b[hi]=b[hi],b[mid];hi-=1
    else:mid+=1
   states.append((b[:],lo,mid,hi))
  k=1 if level=='Easy' else min(4+v,len(states)) if level=='Medium' else len(states);st,l,m,h=states[k-1]
  correct=f'{arr(st)}; (lo,mid,hi)={vec([l,m,h])}';wrong=[f'{z}; (lo,mid,hi)={vec([l,m,h])}' for z in choices_array(st)]
  if baka:
   correct+=f'; {comparisons} key comparisons';wrong=[]
   # All alternatives respect the final three-way regions; trace their within-region order.
   for delta,z in zip([0,1,-1],trace_variants(st,range(m))):
    wrong.append(f'{z}; (lo,mid,hi)={vec([l,m,h])}; {comparisons+delta} key comparisons')
  make(t,level,v,f'After {k} complete loop iterations'+(' and counting all key tests' if baka else '')+', which state is correct?',correct,wrong,f'Inspect the unknown element at mid each time. A greater-than-pivot exchange decrements hi without advancing mid. After {k} iterations: A={arr(st)}, pointers={vec([l,m,h])}. The complete partition uses {comparisons} comparisons.',f'Input {arr(a)}, fixed pivot VALUE {p}. Three-way partition: lo=mid=0, hi=n-1. While mid<=hi: if A[mid]<p swap A[lo],A[mid], increment both; else test A[mid]>p, and if true swap A[mid],A[hi], decrement hi ONLY; otherwise increment mid. Each < or > evaluation is one key comparison.',evidence=dict(algorithm='dnf',input=a,pivot=p,iterations=k,result=st,pointers=[l,m,h],comparisons=comparisons))
 elif t==6:
  n=12 if baka else 5+idx+v;k=6 if baka else 4+v;a=[r.randrange(k) for _ in range(n)];records=[f'{x}{chr(97+i)}' for i,x in enumerate(a)];counts=[a.count(x) for x in range(k)];c=list(itertools.accumulate(counts));initial=c[:];b=['_']*n
  stop=1 if level=='Easy' else 3 if level=='Medium' else 5 if not baka else 8
  for i in range(n-1,n-1-stop,-1):c[a[i]]-=1;b[c[a[i]]]=records[i]
  correct=f'B={arr(b)}; C={arr(c)}';wrong=[f'B={arr(b)}; C={z}' for z in vector_wrong(c,arr)]
  if baka:
   wrong=[]
   for indices in [range(stop),range(n-2,n-2-stop,-1),list(range(n-1,n-1-stop,-1))[::-1]]:
    cc=initial[:];bb=['_']*n
    for i in indices:cc[a[i]]-=1;bb[cc[a[i]]]=records[i]
    wrong.append(f'B={arr(bb)}; C={arr(cc)}')
  make(t,level,v,f'What are output B and mutable cumulative counts C after exactly {stop} backward placements?',correct,wrong,f'Initial cumulative counts are {arr(initial)}. Scan records from the right, decrement their key count before placing. After {stop} records, B={arr(b)} and C={arr(c)}. Equal-key identities keep their original order.',f'Input records {arr(records)}, keys 0..{k-1}; letters identify whole records. Stable counting sort uses cumulative COUNTS, not last-index counts. For each record scanned right-to-left: decrement C[key], then write B[C[key]]. B is zero-based and _ means unfilled.',evidence=dict(algorithm='counting',input=a,records=records,placements=stop,result=b,counts=c))
 elif t==7:
  base=4 if baka else 10;n=11 if baka else 6+idx+v;a=r.sample(range(base**3),n)
  if baka:a=[8,11]+r.sample([x for x in range(64) if x not in [8,11]],n-2);r.shuffle(a)
  b=a[:];states=[]
  for digit in range(3):b=sorted(b,key=lambda x:x//base**digit%base);states.append(b[:])
  if baka:
   first=states[0];groups={}
   for x in first:groups.setdefault(x//base%base,[]).append(x)
   broken=[x for k in sorted(groups) for x in groups[k][::-1]];last=sorted(broken,key=lambda x:x//(base**2)%base);wrongcount=sum(x!=y for x,y in zip(last,sorted(a)));correct=f'{arr(last)}; {wrongcount} misplaced positions';wrong=[f'{z}; {wrongcount} misplaced positions' for z in choices_array(last)];stem='Units pass is stable. The next digit pass reverses each equal-digit group. The final most-significant pass is stable. What output and number of positions differing from a correct numeric sort result?';why=f'After the broken middle pass: {arr(broken)}. The last stable pass yields {arr(last)}, leaving {wrongcount} positions different from {arr(sorted(a))}. A higher pass cannot restore lost lower-digit order within equal high-digit groups.'
  else:passes=1 if level=='Easy' else 2 if level=='Medium' else 3;correct=arr(states[passes-1]);wrong=choices_array(states[passes-1]);stem=f'What is the array after {passes} stable digit pass'+('es' if passes>1 else '')+'?';why='Pass states: '+'; '.join(arr(s) for s in states)+'. Each stable pass preserves the previous lower-digit ordering within its ties.'
  if baka:
   rotated=[x for key in sorted(groups) for x in (groups[key][1:]+groups[key][:1])];rotated=sorted(rotated,key=lambda x:x//(base**2)%base)
   highgroups={}
   for x in broken:highgroups.setdefault(x//(base**2)%base,[]).append(x)
   reversedhigh=[x for key in sorted(highgroups) for x in highgroups[key][::-1]]
   wrong=[f'{arr(z)}; {sum(x!=y for x,y in zip(z,sorted(a)))} misplaced positions' for z in [sorted(a),rotated,reversedhigh]]
  make(t,level,v,stem,correct,wrong,why,f'Input {arr(a)}. Numbers are written in DECIMAL. Use base-{base} LSD radix sort with exactly three digits, including leading zero digits. A normal digit pass sorts stably in ascending digit order, least significant first.',evidence=dict(algorithm='radix',input=a,base=base,states=states,brokenMiddle=broken if baka else None,final=last if baka else states[-1],misplaced=wrongcount if baka else 0))
 elif t==8:
  if baka:
   counts=[5,4,3,2];a=[i for i,c in enumerate(counts) for _ in range(c)];r.shuffle(a);distinct=math.factorial(len(a))//math.prod(math.factorial(c) for c in counts);bound=(distinct-1).bit_length();correct=f'{distinct} distinct key sequences; at least {bound} binary comparisons';wrong=[f'{m} distinct key sequences; at least {b} binary comparisons' for m,b in [(math.factorial(len(a)),(math.factorial(len(a))-1).bit_length()),(distinct,bound-1),(distinct*2,(distinct*2-1).bit_length())]];why=f'There are {len(a)}!/(5!4!3!2!)={distinct} distinct arrangements of this multiset. A Boolean comparison tree needs that many distinguishable leaves, so height >=ceil(log2({distinct}))={bound}.';context=f'Input multiset shown as {arr(a)}. Consider a deterministic sorter whose only key test is one BOOLEAN comparison (two outcomes). Restrict inputs to all permutations of precisely this multiset; each key carries an opaque payload that must move with it. Only rearranging the supplied records and Boolean key comparisons are permitted; equal-key records may be output in either order.';stem='What are the number of distinct input key sequences and the resulting worst-case decision-tree lower bound?'
  else:
   n=[16,32,64][v];base=[4,8,16][idx];digits=3+v;k=base**digits;cost=digits*(n+base);correct=f'{digits} passes; {cost} work units; {n+base} auxiliary entries';wrong=[f'{digits+d} passes; {cost} work units; {n+base} auxiliary entries' for d in [1,-1,2]];why=f'{k}=base^{digits}, so every key fits {digits} base-{base} digits. The specified bill is {digits}*({n}+{base})={cost}; reuse n output and base count entries.';context=f'There are n={n} word-sized keys in 0..{k-1}. Use base-{base} LSD radix sort. For this question ONLY, charge exactly n+base work units for each digit pass and count n+base reusable auxiliary entries. Ignore constant loop overhead.';stem='Which digit-pass count, total work bill, and reusable auxiliary-storage count are correct?'
  make(t,level,v,stem,correct,wrong,why,context,evidence=dict(distinct=distinct,bound=bound) if baka else dict(n=n,base=base,digits=digits,work=cost))
 elif t==9:
  a,_,_=build(sort_data(t,v,level));n=len(a)
  if level=='Easy':i=r.randrange(1,n//2);vals=[(i-1)//2,2*i+1,2*i+2 if 2*i+2<n else -1];correct=vec(vals);wrong=vector_wrong(vals);stem=f'For zero-based node index {i}, what are (parent index, left-child index, right-child index)? Use -1 for an absent child.';why=f'Use floor((i-1)/2), 2i+1 and 2i+2, then check against n={n}. The result is {correct}.'
  elif level=='Medium':leaves=a[n//2:];correct=arr(leaves);wrong=choices_array(leaves);stem='Which are the leaf KEYS in increasing array-index order?';why=f'Leaf indices are floor(n/2)..n-1, here {n//2}..{n-1}. Reading those entries gives {correct}.'
  elif level=='Hard':target=max(a);i=a.index(target);anc=[]
  if level=='Hard':
   while i>0:i=(i-1)//2;anc.append(a[i])
   correct=arr(anc);wrong=choices_array(anc);stem=f'Start at key {target}. Which sequence of ancestor KEYS do you encounter moving towards the root, excluding the starting key?';why='Follow parent indices repeatedly, not neighbouring array positions. Ancestors are '+correct+'.'
  if baka:
   original=a[:];insert(a,-2);insert(a,-1);returned=extract(a);target=original[0];i=a.index(target);path=[]
   while True:
    path.append(i)
    if i==0:break
    i=(i-1)//2
   ancestors=[a[j] for j in path[1:]];correct=f'target index {path[0]}; ancestor keys {arr(ancestors)}; leaf indices {len(a)//2}..{len(a)-1}';wrong=[]
   for other in range(1,len(a)):
    if other==path[0]:continue
    chain=[];j=other
    while j:j=(j-1)//2;chain.append(a[j])
    wrong.append(f'target index {other}; ancestor keys {arr(chain)}; leaf indices {len(a)//2}..{len(a)-1}')
   stem=f'Insert -2, then -1, then Extract-Min. Locate ORIGINAL root key {target}. What are its new index, ancestor KEYS (parent first, root last), and the final leaf-index range?';why=f'After insertion and extraction (which returns {returned}), the heap is {arr(a)}. Locate {target}, then follow parent indices: {arr(path)}. Leaves depend on the final size, not on key order.';a=original
  make(t,level,v,stem,correct,wrong,why,f'Zero-based min-heap {arr(a)}. Complete binary tree; parent=floor((i-1)/2). In repairs choose the smaller child, using the LEFT child on equal keys. Insertion appends and bubbles up; extraction replaces the root by the last entry and repairs down.',evidence=dict(input=a,result=correct))
 elif t==10:
  a,_,_=build(sort_data(t,v,level));a[0]=max(a)+10;original=a[:];sw=heapify(a,0)
  if level=='Easy':x=original[:];u,w=sw[0];x[u],x[w]=x[w],x[u];correct=arr(x);wrong=choices_array(x);stem='What is A immediately after the FIRST swap in Min-Heapify(A,0)?';why=f'Compare both child roots and swap with the smaller child at index {w}. First state: '+correct+'.'
  elif level=='Medium':correct=arr(a);wrong=choices_array(a);stem='What is A after Min-Heapify(A,0) finishes?';why=f'The repair follows swaps {sw}. The child subtrees were already valid; the final array is {correct}.'
  elif level=='Hard':path=[0]+[j for i,j in sw];correct=f'{arr(a)}; visited swap path {arr(path)}';wrong=[f'{z}; visited swap path {arr(path)}' for z in choices_array(a)];stem='Which final array and root-to-leaf swap path are correct?';why=f'At each level choose the smaller existing child, not whichever is first in array order. The key moves through indices {arr(path)}.'
  else:
   first=a[:];a[1]=max(a)+11;second=heapify(a,1);correct=f'{arr(a)}; {len(sw)+len(second)} actual swaps';wrong=[f'{arr(z)}; {len(sw)+len(second)+delta} actual swaps' for z,delta in zip(valid_heap_variants(a),[1,0,-1])];stem='First fully heapify at 0. Then replace A[1] by one more than the CURRENT maximum key plus 10, and fully heapify at 1. What are the final array and total swaps across both calls?';why=f'First call gives {arr(first)} using {len(sw)} swaps. Replacing A[1] and repairing its already-valid child subtrees gives {arr(a)}, adding {len(second)} swaps.'
  make(t,level,v,stem,correct,wrong,why,f'Input {arr(original)}. Its two root-child subtrees are valid min-heaps. Min-Heapify chooses the smaller child (left on a tie), swaps only if smaller than the parent, and continues down. Count exchanges of distinct indices.',evidence=dict(algorithm='heapify',input=original,result=a,swaps=sw,secondSwaps=second if baka else []))
 elif t==11:
  a=sort_data(t,v,level);final,states,sw=build(a);k=1 if level=='Easy' else min(2+v,len(states)) if level=='Medium' else len(states);i,state=states[k-1]
  if baka:correct=f'{arr(final)}; {len(sw)} actual swaps';wrong=[f'{arr(z)}; {len(sw)+d} actual swaps' for z,d in zip(valid_heap_variants(final),[1,0,-1])];stem='Build the entire heap. What are the final array and total swaps across ALL heapify calls?'
  else:correct=arr(state);wrong=choices_array(state);stem=f'What is the array after {k} complete bottom-up heapify call'+('s' if k>1 else '')+'?'
  make(t,level,v,stem,correct,wrong,'Heapify calls use indices '+arr([i for i,_ in states])+'. States: '+'; '.join(f'i={i}: {arr(s)}' for i,s in states)+f'. Total actual swaps: {len(sw)}.',f'Input {arr(a)}. Build-Min-Heap runs Min-Heapify from floor(n/2)-1 down to 0, using the smaller child and the LEFT child on ties. Zero-based indexing. Each complete call may do several swaps; leaves are not separate build-loop calls.',evidence=dict(algorithm='build',input=a,result=final,swaps=len(sw)))
 elif t==12:
  a,_,_=build(sort_data(t,v,level));original=a[:];x=r.randrange(0,12);y=r.randrange(0,12)
  if level=='Easy':insert(a,x);operations=f'Insert({x})';returned=[]
  elif level=='Medium':returned=[extract(a)];insert(a,x);operations=f'Extract-Min, Insert({x})'
  elif level=='Hard':insert(a,x);returned=[extract(a)];insert(a,y);returned.append(extract(a));operations=f'Insert({x}), Extract-Min, Insert({y}), Extract-Min'
  else:
   x=original[len(original)//2];y=-3;z=max(original)+5;returned=[extract(a)];insert(a,x);returned.append(extract(a));insert(a,y);insert(a,z);returned.append(extract(a));returned.append(extract(a));insert(a,2);operations=f'Extract-Min, Insert({x}), Extract-Min, Insert({y}), Insert({z}), Extract-Min, Extract-Min, Insert(2)'
  correct=f'returned {arr(returned)}; heap {arr(a)}';wrong=[f'returned {arr(returned)}; heap {z}' for z in choices_array(a)]
  if baka:wrong=[f'returned {arr(ret)}; heap {arr(z)}' for z,ret in zip(valid_heap_variants(a),[returned[:-1]+[returned[-1]+1],returned,returned[:1]+list(reversed(returned[1:]))])]
  make(t,level,v,'After the entire operation sequence, which return sequence and heap array are correct?',correct,wrong,'Simulate each insertion from the new last index and each removal by moving the last entry to the root. Extracted keys are '+arr(returned)+'; the final LEVEL-ORDER heap is '+arr(a)+', not necessarily sorted.',f'Initial min-heap {arr(original)}. Operations in order: {operations}. On a repair tie choose the left child. Insert swaps upwards only on strict inequality; Extract-Min returns the old root, shrinks the array, and repairs down.',evidence=dict(algorithm='pq',input=original,operations=operations,returns=returned,result=a))
 elif t==13:
  a,_,_=build(sort_data(t,v,level),False);original=a[:];active=len(a);states=[];swaps=0;passes=1 if level=='Easy' else 2 if level=='Medium' else 3 if level=='Hard' else 5
  for _ in range(passes):a[0],a[active-1]=a[active-1],a[0];swaps+=1;active-=1;swaps+=len(heapify(a,0,False,active));states.append(a[:])
  correct=arr(a[:active])+' | '+arr(a[active:])
  wrong=[]
  for i,j in itertools.combinations(range(len(a)),2):
   z=a[:];z[i],z[j]=z[j],z[i];wrong.append(arr(z[:active])+' | '+arr(z[active:]))
  wrong=variants(correct,wrong)
  if baka:correct+=f'; {swaps} swaps';wrong=[arr(z)+' | '+arr(a[active:])+f'; {swaps+d} swaps' for z,d in zip(valid_heap_variants(a[:active],False),[0,1,-1])]
  make(t,level,v,f'After {passes} complete extraction-and-repair rounds, what are the active heap and sorted suffix'+(', and total actual swaps' if baka else '')+'?',correct,wrong,'The active size falls to '+str(active)+'. Each root/end exchange fixes one maximum in the suffix, which repairs must exclude. Round states: '+'; '.join(arr(s) for s in states)+f'. Exchanges across all rounds: {swaps}.',f'Start from MAX-heap {arr(original)}. Ascending heapsort swaps root with the active last entry, shrinks active size, then Max-Heapifies at 0 using the larger child (left on a tie). | separates active prefix and sorted suffix. Count root/end exchanges and internal exchanges, excluding self-swaps.',evidence=dict(algorithm='heapsort',input=original,rounds=passes,result=a,active=active,swaps=swaps))
 elif t==14:
  nodes=list('ABCDEFGH'[:8 if baka else 5+v]);pairs=list(itertools.permutations(nodes,2));r.shuffle(pairs);edges=[(u,w,None) for u,w in pairs[:len(nodes)+3+idx]];g=graph_data(nodes,edges,True);u=nodes[1+v%2]
  if level=='Easy':values=[sum(b==u for a,b,_ in edges),sum(a==u for a,b,_ in edges)];correct=vec(values);wrong=vector_wrong(values);stem=f'What are (indegree({u}), outdegree({u}))?';why=f'Count arrows INTO {u} and OUT OF {u} separately: {correct}. Reciprocal arrows count separately.'
  elif level=='Medium':row=[int(any(a==u and b==w for a,b,_ in edges)) for w in nodes];correct=arr(row);wrong=vector_wrong(row,arr);stem=f'With rows/columns {arr(nodes)}, what is outgoing adjacency-matrix row {u}?';why='A row marks outgoing targets, not incoming sources. The row is '+correct+'.'
  elif level=='Hard':simple={tuple(sorted([a,b])) for a,b,_ in edges};values=[len(simple),2*len(simple),2*len(simple)];correct=vec(values);wrong=vector_wrong(values);stem='Ignore directions and merge reciprocal edges. For the resulting simple undirected graph, what are (edge count, degree sum, adjacency-list entries)?';why=f'There are {len(simple)} distinct unordered endpoint pairs. Each contributes two to degree sum and two neighbour-list entries.'
  else:
   keep=[x for x in nodes if x not in ['C','F']];simple={tuple(sorted([a,b])) for a,b,_ in edges if a in keep and b in keep};degrees=[sum(u in e for e in simple) for u in keep];correct=f'order {arr(keep)}; degree vector {arr(degrees)}; {2*len(simple)} list entries';wrong=[f'order {arr(keep)}; degree vector {arr(ds)}; {sum(ds)} list entries' for ds in [degrees[:1]+[degrees[1]+1]+degrees[2:-1]+[degrees[-1]+1],[sum(u in (a,b) for a,b,_ in edges) for u in keep],degrees[:-2]+[degrees[-2]+2,degrees[-1]]]];stem='Delete vertices C and F with incident arrows, then ignore directions and merge reciprocals. What are the retained vertex order, undirected degrees and total neighbour-list entries?';why='Retained unordered edges: '+', '.join(''.join(e) for e in sorted(simple))+'. Compute degrees only after deletion and reciprocal merging; every surviving edge appears in two lists.'
  make(t,level,v,stem,correct,wrong,why,'The diagram is a directed simple graph with exactly the listed arrows. M[u,v]=1 iff u->v exists. Vertex order is '+arr(nodes)+'. Crossings are not extra vertices.',g,evidence=dict(nodes=nodes,edges=edges,result=correct))
 elif t==15:
  n=8 if baka else 6+v;nodes=list('ABCDEFGHI'[:n]);edges=[(nodes[i],nodes[i+1],None) for i in range(n-3)]+[(nodes[0],nodes[2],None),(nodes[-2],nodes[-1],None)];r.shuffle(edges)
  if level=='Medium':edges.append((nodes[0],nodes[3],None))
  elif level=='Hard':edges.append((nodes[1],nodes[3],None))
  g=graph_data(nodes,edges);original=components(nodes,edges)
  if level=='Easy':correct=' / '.join(original);wrong=variants(correct,[' / '.join([original[0]+original[1]]+original[2:]),' / '.join([original[0][:-1],original[0][-1]]+original[1:]),' / '.join([original[0]+original[-1],original[1]])]);stem='Which is the connected-component partition of the entire graph?';why='Maximal connected vertex sets are '+correct+'. A disconnected small edge forms its own component.'
  elif level=='Medium':keep=r.sample(nodes,n-2);keep.sort();kept=[(a,b,w) for a,b,w in edges if a in keep and b in keep];names=sorted(''.join(sorted([a,b])) for a,b,w in kept);correct=arr(names);wrong=variants(correct,[arr(names+[''.join(keep[:2])]),arr(names[:-1]),arr(sorted(''.join(sorted([a,b])) for a,b,w in edges)),arr(names+[''.join(keep[-2:])])]);stem=f'Which edge set belongs to the vertex-induced graph G[{arr(keep)}]?';why='Keep ALL and ONLY original edges with both endpoints in the retained vertex set. Result: '+correct+'.'
  elif level=='Hard':start=nodes[0];goal=nodes[n-3];_,dist,_=bfs(nodes,edges,start);correct=f'd({start},{goal})={dist[goal]}; components={len(original)}';wrong=[f'd({start},{goal})={dist[goal]+d}; components={len(original)}' for d in [1,-1,2]];stem='What are the shortest unweighted distance and total number of connected components?';why=f'The edge {nodes[0]}{nodes[2]} shortcuts the first two chain edges. The shortest route uses {dist[goal]} edges; the other component does not affect that distance.'
  else:
   nodes=list('ABCDEFGHI');edges=[(e[0],e[1],None) for e in ['AB','BC','CA','CD','DE','EF','FC','FG','GH','HF','HI','EI']];g=graph_data(nodes,edges)
   keptnodes=[u for u in nodes if u!='C'];filtered=[e for e in edges if 'C' not in e[:2] and set(e[:2])!=set('FG')]
   def report(es):
    groups=components(keptnodes,es);bridgecount=sum(len(components(keptnodes,es[:i]+es[i+1:]))>len(groups) for i in range(len(es)));_,ds,_=bfs(keptnodes,es,'D')
    return ' / '.join(groups)+f'; bridges {bridgecount}; (d(D,G),d(D,I))={vec([ds['G'],ds['I']])}'
   correct=report(filtered);wrong=[report([e for e in filtered if set(e[:2])!=set('EI')]),report([e for e in edges if 'C' not in e[:2] and set(e[:2])!=set('GH')]),report([e for e in filtered if set(e[:2])!=set('HF')])];stem='Delete vertex C with its incident edges, then delete edge FG. Give the component partition, number of bridges, and the two requested shortest unweighted distances.';why='Remaining edges: '+', '.join(a+b for a,b,w in filtered)+'. A bridge is an edge whose deletion increases component count. Recompute after BOTH deletions. Result: '+correct+'.'
  make(t,level,v,stem,correct,wrong,why,'Use the undirected graph shown. Every vertex, including any isolated vertex, belongs to exactly one component. Path length counts edges. Only the listed edges exist.',g,evidence=dict(nodes=nodes,edges=edges,result=correct))
 elif 16<=t<=21:
  n=8 if baka else 6+v;nodes=list('ABCDEFGH'[:n])
  if t in [16,17,18]:
   mandatory=[('A','B'),('B','C'),('C','A'),('A','D'),('D','B'),('D','E'),('E','F'),('F','D'),('A','C'),('A','G'),('G','H'),('H','E')]
   pairs={p for p in mandatory if all(u in nodes for u in p)}
   extra=[p for p in itertools.permutations(nodes,2) if p not in pairs];r.shuffle(extra);pairs.update(extra[:2+idx+v]);edges=[(u,w,None) for u,w in sorted(pairs)];g=graph_data(nodes,edges,True)
   context='Use this directed graph. Start at A, scan outgoing neighbours alphabetically, and mark vertices on discovery. For full DFS, consider new roots alphabetically. Only listed arrows exist. '
   if t==16:
    states,dist,par=bfs(nodes,edges,'A',True);k=1 if level=='Easy' else min(3+v,len(states)) if level=='Medium' else min(5+v,len(states));_,queue,ds,ps=states[k-1]
    if baka:
     k=min(5,len(states));_,queue,ds,ps=states[k-1];vals=[dist[u] for u in nodes];correct=f'queue {arr(queue)}; final distances {vec(vals)}; parent(H)={par["H"]}';wrong=[f'queue {arr(q)}; final distances {vec(ds)}; parent(H)={ph}' for q,ds,ph in [(list(reversed(queue)),vals[:],next(u for u,w,_ in edges if w=='H' and u!=par['H'])),(queue[1:]+queue[:1],[x+1 if u=='H' else x for u,x in zip(nodes,vals)],par['H']),(queue+[states[k-1][0]],vals[:],par['H'])]];stem=f'After {k} COMPLETE expansions, what queue remains, and what are the eventual full BFS distance vector and parent(H)?'
    elif level=='Hard':targets=nodes[-3:];correct=f'queue {arr(queue)}; parents {arr([ps[u] for u in targets])}';wrong=[f'queue {arr(queue)}; parents {z}' for z in choices_array([ps[u] for u in targets])];stem=f'After {k} complete expansions, what are the queue and parent vector for {arr(targets)}? Use - for still-undiscovered vertices.'
    else:
     correct=arr(queue);wrong=variants(correct,[arr(queue[::-1]),arr([states[k-1][0]]+queue),arr(queue+['A']),arr(queue[:-1]),arr(queue+['B'])]);stem=f'What is the FIFO queue after {k} vertices have been dequeued and fully expanded?'
    why='Expansion snapshots: '+'; '.join(f'{u}: Q={arr(q)}' for u,q,_,_ in states)+'. Vertices are marked when enqueued, so later discoveries do not replace parents.';context+='BFS queue is front-to-back. Initially only A is enqueued; distances count directed edges. Distance-vector order is '+arr(nodes)+'.'
   else:
    d=dfs(nodes,edges);pre,post=d['pre'],d['post'];classes=d['classes']
    if t==17:
     if level=='Easy':take=4;correct=arr(pre[:take]);wrong=choices_array(pre[:take]);stem='What are the first four DFS discoveries?'
     elif level=='Medium':target=pre[min(4+v,len(pre)-1)];st=d['stacks'][target];correct=arr(st);wrong=choices_array(st);stem=f'What active recursive stack exists immediately after {target} is first entered? Write bottom-to-top.'
     elif level=='Hard':correct=arr(post);wrong=choices_array(post);stem='What is the complete DFS finishing order, including every DFS root?'
     else:height=max(map(len,d['stacks'].values()));pv=[d['parent'][u] for u in nodes];correct=f'finish {arr(post)}; parents {arr(pv)}; max active calls {height}';wrong=[f'finish {order}; parents {parents}; max active calls {height+delta}' for order,parents,delta in zip(trace_variants(post),trace_variants(pv,[i for i,x in enumerate(pv) if x=='-']),[0,1,-1])];stem='Which complete finishing order, parent vector, and maximum active-call count are correct?'
     why=f'Discovery order is {arr(pre)}; finishing order is {arr(post)}. Parents in {arr(nodes)} order are {arr([d["parent"][u] for u in nodes])}. Maximum stack includes the current call and equals {max(map(len,d["stacks"].values()))}.'
    else:
     non=[e for e in sorted(classes) if classes[e]!='tree'];pick=([next((e for e in non if classes[e]==['forward','back','cross'][v]),non[v%len(non)])] if level=='Easy' else non[:3 if level=='Medium' else len(non)])
     if level=='Hard':counts=[sum(c==z for c in classes.values()) for z in ['tree','forward','back','cross']];correct=vec(counts);wrong=vector_wrong(counts);stem='How many (tree, forward, back, cross) edges occur in this fixed DFS forest?'
     else:
      result=[classes[e] for e in pick];correct=arr(result);wrong=[]
      for i in range(len(result)):
       for alt in ['tree','forward','back','cross']:
        x=result[:];x[i]=alt;wrong.append(arr(x))
      stem='Classify edges '+', '.join(e[0]+'->'+e[1] for e in pick)+' in that order.'
      if baka:
       target=nodes[-2];rank=(pre.index(target)+1,post.index(target)+1);correct+=f'; {target} ranks {vec(list(rank))}';wrong=[arr([(c if i%3!=shift else (('tree' if c=='forward' else 'forward') if pick[i][0]=='A' else ('cross' if c=='back' else 'back'))) for i,c in enumerate(result)])+f'; {target} ranks {vec([rank[0]+dp,rank[1]+dq])}' for shift,dp,dq in [(0,0,1),(1,1,0),(2,-1,1)]]
       stem+=f' Also give {target}\'s separate (preorder rank, postorder rank), each starting at 1.'
     why='Fixed discoveries '+arr(pre)+' and finishes '+arr(post)+'. Edge classes: '+', '.join(e+':'+classes[e] for e in sorted(classes))+'. Tree edges must be identified before ancestor/descendant tests.'
   make(t,level,v,stem,correct,wrong,why,context,g,evidence=dict(nodes=nodes,edges=edges,result=correct))
  elif t==19:
   perm=nodes[:];r.shuffle(perm);a,b,c,d,e,f=perm[:6];pairs=[(a,b),(b,c),(c,a),(d,e),(e,f),(f,d),(c,d)]+[(perm[i],perm[i+1]) for i in range(5,n-1)];edges=[(u,w,None) for u,w in pairs]
   if baka:edges=[(u,w,None) for u,w in [('A','B'),('B','C'),('C','A'),('C','D'),('D','E'),('E','C'),('B','D'),('E','F'),('F','B'),('D','G'),('G','H'),('H','D'),('A','H'),('H','C')]]
   g=graph_data(nodes,edges,True);data=dfs(nodes,edges);backs=[u+'->'+v for (u,v),typ in [(list(k),typ) for k,typ in data['classes'].items()] if typ=='back'];first=backs[0]
   if level=='Easy':correct=first;wrong=[u+'->'+w for u,w,_ in edges if u+'->'+w!=first];stem='Which edge is the FIRST back edge found by the stated full DFS?';why='A back edge points to an active ancestor. In this traversal the first such edge is '+first+'.'
   elif level=='Medium':correct=f'{len(backs)} back edges; roots {arr(data["roots"])}';wrong=[f'{len(backs)+delta} back edges; roots {arr(data["roots"])}' for delta in [1,-1,2]];stem='For the complete DFS forest, how many back edges occur and what are its root vertices?';why='Full-forest roots are '+arr(data['roots'])+' and back edges are '+arr(backs)+'. Finishing one root does not rule out a cycle elsewhere.'
   elif level=='Hard':u,w=first.split('->');remaining=[z for z in edges if z[:2]!=(u,w)];after=dfs(nodes,remaining);afterback=[k for k,c in after['classes'].items() if c=='back'];correct=f'Still cyclic; {len(afterback)} back edge(s) in a fresh full DFS';wrong=[f'Acyclic; 0 back edges in a fresh full DFS',f'Still cyclic; {len(afterback)+1} back edge(s) in a fresh full DFS',f'Still cyclic; {len(afterback)+2} back edge(s) in a fresh full DFS'];stem=f'Delete {first}, then rerun the entire DFS from scratch. What is the result?';why='The diagram contains two edge-disjoint directed triangle cycles. Breaking the first leaves the other; the rerun finds back edges '+arr(afterback)+'.'
   else:
    minimum=None
    for k in range(1,6):
     if any(not any(c=='back' for c in dfs(nodes,[e for i,e in enumerate(edges) if i not in cut])['classes'].values()) for cut in itertools.combinations(range(len(edges)),k)):minimum=k;break
    correct=f'back edges {arr(backs)}; minimum deletions {minimum}';nonbacks=[e[0]+'->'+e[1] for e in edges if data['classes'][e[0]+e[1]]!='back'];changed=backs[:];changed[-1]=nonbacks[0];wrong=[f'back edges {arr(backs)}; minimum deletions {minimum-1}',f'back edges {arr(changed)}; minimum deletions {minimum}',f'back edges {arr(backs[:-1])}; minimum deletions {minimum}'];stem='Which are ALL original DFS back edges, and what is the minimum number of directed edges that must be deleted to make the graph acyclic?';why='Back edges from the fixed DFS are '+arr(backs)+'. Testing removal sets against the whole graph shows that fewer than '+str(minimum)+' deletions always leave a cycle, and a set of '+str(minimum)+' deletions suffices. Shared cycles mean that counting visually drawn loops alone is unreliable.'
   make(t,level,v,stem,correct,wrong,why,'Full recursive DIRECTED DFS: roots alphabetically, outgoing neighbours alphabetically. Undiscovered, active and finished are distinct states. Deleting an edge does not delete either endpoint.',g,evidence=dict(nodes=nodes,edges=edges,backs=backs,result=correct))
  else:
   hidden=nodes[:];r.shuffle(hidden);pairs={(hidden[i],hidden[i+1]) for i in range(n-1) if i%3==0};possible=[(hidden[i],hidden[j]) for i in range(n) for j in range(i+1,n) if (hidden[i],hidden[j]) not in pairs];r.shuffle(possible);pairs.update(possible[:n-2+idx]);edges=[(u,w,None) for u,w in sorted(pairs)];g=graph_data(nodes,edges,True);order,ready=topo(nodes,edges);data=dfs(nodes,edges)
   if t==20:
    if level=='Easy':sources=sorted(u for u in nodes if not any(b==u for a,b,_ in edges));correct=arr(sources);wrong=variants(correct,[arr(order[-len(sources):]),arr(sources+[next(x for x in nodes if x not in sources)]),arr(sources[:-1]),arr(list(reversed(order))[:len(sources)])]);stem='Which are ALL initial zero-indegree sources?';why='Sources have no incoming arrows. Initially they are '+correct+'.'
    elif level=='Medium':k=2+v;correct=arr(ready[k-1]);wrong=variants(correct,[arr(ready[k-1][::-1]),arr(ready[k-1]+[order[k-1]]),arr(ready[k-1]+[order[-1]]),arr(ready[k-1][1:]),arr([order[-1]])]);stem=f'After exactly {k} source removals, what is the current sorted available zero-indegree set?';why=f'Removed prefix: {arr(order[:k])}. Decrement indegrees along every outgoing edge after each removal; the current available set is {correct}.'
    elif level=='Hard':correct=arr(order);wrong=choices_array(order);stem='What full topological order does alphabetically smallest CURRENT source removal produce?';why='Recompute the available set after every removal, rather than keeping only the original sources. The output is '+correct+'.'
    else:
     total=topo_count(nodes,edges);candidate=next(((u,w) for u,w in itertools.permutations(nodes,2) if order.index(u)<order.index(w) and not any(a==u and b==w for a,b,_ in edges) and topo_count(nodes,edges+[(u,w,None)])<total),(order[-1],order[0]));new=topo_count(nodes,edges+[(candidate[0],candidate[1],None)]);correct=f'{total} orders originally; {new} after adding {candidate[0]}->{candidate[1]}';wrong=[f'{total+d} orders originally; {new+delta} after adding {candidate[0]}->{candidate[1]}' for d,delta in [(1,-1),(-1,1),(0,2)]];stem=f'Count ALL valid topological orders, then count again after adding {candidate[0]}->{candidate[1]}. Which counts are correct?';why=f'Enumerating only choices among CURRENT sources gives {total} complete valid orders. The added precedence removes orders with {candidate[1]} before {candidate[0]}, leaving {new}. A topological sort algorithm\'s one output is not the number of possible orders.'
   else:
    if level=='Easy':take=3;correct=arr(data['post'][:take]);wrong=choices_array(data['post'][:take]);stem='Which are the first three vertices to FINISH in the full DFS?'
    elif level=='Medium':correct=arr(data['post'][::-1]);wrong=choices_array(data['post'][::-1]);stem='Which topological order does this full DFS output?'
    elif level=='Hard':pv=[data['parent'][u] for u in nodes];correct=f'reverse finishes {arr(data["post"][::-1])}; roots {arr(data["roots"])}';wrong=[f'reverse finishes {z}; roots {arr(data["roots"])}' for z in choices_array(data['post'][::-1])];stem='Which reverse-finishing order and list of DFS roots are correct?'
    else:
     target=nodes[-1];rank=[data['pre'].index(target)+1,data['post'].index(target)+1];num=topo_count(nodes,edges);correct=f'order {arr(data["post"][::-1])}; {target} ranks {vec(rank)}; {num} possible topological orders';wrong=[f'order {z}; {target} ranks {vec([rank[0]+dp,rank[1]+dq])}; {num+d} possible topological orders' for z,dp,dq,d in zip(choices_array(data['post'][::-1]),[0,1,-1],[1,0,1],[1,-1,0])];stem=f'Give the DFS topological output, {target}\'s separate preorder/postorder ranks, and the number of ALL valid topological orders.'
    why=f'Discoveries {arr(data["pre"])}; finishes {arr(data["post"])}; roots {arr(data["roots"])}. Reverse the COMPLETE finishing order, including every root. Different valid orders can exist even when this DFS is deterministic.'
   make(t,level,v,stem,correct,wrong,why,'Use this DAG. Source removal always picks the alphabetically smallest CURRENT source, updating indegrees immediately. Full DFS considers roots alphabetically and scans outgoing neighbours alphabetically. An arrow u->v means u precedes v.',g,evidence=dict(nodes=nodes,edges=edges,result=correct))
 elif t==22:
  nodes=['S','A','B','C','D','T','U','V'];w=r.randrange(2,7);tail=r.randrange(1,6);finite=r.randrange(5,12);edges=[('S','A',w),('A','B',tail),('B','A',-tail-1),('B','C',r.randrange(1,5)),('C','T',r.randrange(1,6)),('S','D',finite),('U','V',-3),('V','U',1)];g=graph_data(nodes,edges,True)
  if level=='Easy':d1=r.randrange(2,9);old=d1+r.randrange(1,6);edge=2+v;new=min(old,d1+edge);correct=f'd[v]={new}; '+('parent[v]=u' if new<old else 'parent[v] stays x');wrong=variants(correct,[f'd[v]={new+1}; parent[v]=u',f'd[v]={edge}; parent[v]=u',f'd[v]={old+2}; parent[v] stays x']);stem=f'Independently of the picture, d[u]={d1}, d[v]={old}, parent[v]=x, w(u,v)={edge}. What does one strict relaxation do?';why=f'The candidate is {d1}+{edge}={d1+edge}. Update both distance and parent only if this is strictly below {old}.'
  elif level=='Medium':correct=f'd[T]=-INF; d[D]={finite}; d[U]=INF';wrong=[f'd[T]=INF; d[D]={finite}; d[U]=-INF',f'd[T]=-INF; d[D]=-INF; d[U]=INF',f'd[T]={w+tail+sum(z[2] for z in edges[3:5])}; d[D]={finite}; d[U]=INF'];stem='From S, what are the shortest-distance statuses of T, D and U?';why='A-B-A has weight -1, is reachable from S, and reaches T. D cannot be reached from that cycle and has finite direct distance. U/V are unreachable from S despite having their own negative cycle.'
  elif level=='Hard':newdist=w+tail+edges[3][2]+edges[4][2];correct=f'{newdist}; S->A->B->C->T';wrong=[f'{newdist+d}; S->A->B->C->T' for d in [1,-1,2]];stem='Delete B->A only. What is the finite shortest distance to T and its route from S?';why=f'Removing BA breaks the reachable negative cycle. The only S-to-T route is S-A-B-C-T with cost {w}+{tail}+{edges[3][2]}+{edges[4][2]}={newdist}. The unreachable U/V cycle does not affect this query.'
  else:
   values=[0,-math.inf,-math.inf,-math.inf,finite,-math.inf,math.inf,math.inf];newdist=w+tail+edges[3][2]+edges[4][2];correct=f'original {vec(values)}; after deleting BA, d[T]={newdist}';alternatives=[values[:],values[:],values[:]];alternatives[0][4]=-math.inf;alternatives[1][6]=alternatives[1][7]=-math.inf;alternatives[2][1]=w;alternatives[2][2]=w+tail;wrong=[f'original {vec(z)}; after deleting BA, d[T]={newdist}' for z in alternatives];stem='Give the complete original S-distance status vector, then the shortest distance to T after deleting B->A.';why='Only A,B,C,T are downstream of the reachable negative cycle. D is finite and U/V remain unreachable. The post-deletion T route costs '+str(newdist)+'. A negative cycle elsewhere is irrelevant unless S can reach it.'
  make(t,level,v,stem,correct,wrong,why,'Directed weighted graph; source S; vector order '+arr(nodes)+'. INF means unreachable, -INF means unbounded below because a reachable negative cycle can reach that target. Repeating vertices is allowed for distance-status reasoning.',g,evidence=dict(nodes=nodes,edges=edges,result=correct))
 elif t==23:
  nodes=list('SABCDEFT'[:8 if baka else 5+v]);start='S'
  if baka:edges=[('F','T',2),('E','F',1),('D','E',2),('C','D',1),('B','C',-4),('C','B',1),('A','B',2),('S','A',3),('S','T',30)];passes=len(nodes)-1
  else:
   chain=[(nodes[i],nodes[i+1],r.randrange(-3,8)) for i in range(len(nodes)-1)];edges=chain[::-1]+[('S',nodes[-1],r.randrange(20,30))];passes=1 if level=='Easy' else 2 if level=='Medium' else len(nodes)-1
  d={u:math.inf for u in nodes};d[start]=0;states=[]
  for _ in range(passes):
   for a,b,w in edges:
    if d[a]+w<d[b]:d[b]=d[a]+w
   states.append([d[u] for u in nodes])
  values=states[-1];correct=vec(values);wrong=vector_wrong(values)
  if baka:
   first=next(a+'->'+b for a,b,w in edges if d[a]+w<d[b]);correct+=f'; first extra-check improvement {first}';wrong=[z+f'; first extra-check improvement {first}' for z in wrong];stem=f'After {passes} complete in-place passes, what is the distance vector and the FIRST edge that could improve in an extra scan (before applying that extra update)?'
  else:stem=f'What is the distance vector after {passes} complete passes?'
  make(t,level,v,stem,correct,wrong,'Pass vectors: '+'; '.join(vec(s) for s in states)+'. Edges earlier in a pass are not revisited. An extra improving edge proves a reachable negative cycle, but may be DOWNSTREAM rather than itself on the cycle.',f'Bellman-Ford starts d[S]=0, all other distances INF. Vector order {arr(nodes)}. Update IN PLACE. Each pass scans this EXACT edge order: '+', '.join(f'{a}->{b}({w})' for a,b,w in edges)+'. Do not stop early.',graph_data(nodes,edges,True),evidence=dict(algorithm='bellman',nodes=nodes,edges=edges,passes=passes,states=states))
 elif t==24:
  n=8 if baka else 5+v;nodes=list('ABCDEFGH'[:n]);pairs={(nodes[i],nodes[i+1]) for i in range(n-1)};other=[p for p in itertools.permutations(nodes,2) if p not in pairs];r.shuffle(other);pairs.update(other[:n-1+idx]);edges=[(a,b,r.randrange(0,10)) for a,b in sorted(pairs)];order,d,par,states,decs=weighted(nodes,edges,'A');k=1 if level=='Easy' else min(3+v,n) if level=='Medium' else n
  if baka:pv=[par[u] for u in nodes];correct=f'settle {arr(order)}; parents {arr(pv)}; {decs} successful relaxations';wrong=[f'settle {z}; parents {pa}; {decs+x} successful relaxations' for z,pa,x in zip(trace_variants(order,[0]),trace_variants(pv,[i for i,x in enumerate(pv) if x=='-']),[1,0,-1])];stem='Complete Dijkstra. What are the settling order, final parent vector and number of successful strict relaxations (including first finite offers)?'
  else:values=[states[k-1][1][u] for u in nodes];correct=vec(values);wrong=vector_wrong(values);stem=f'After {k} complete extract-and-relax steps, what is the tentative-distance vector?'
  if baka:
   wrong=[]
   for strategy,edge_input in [('first',edges),('alphabet',edges),('normal',[(u,w,c+2) for u,w,c in edges])]:
    ao,ad,ap,ast,ac=weighted(nodes,edge_input,'A',strategy=strategy)
    option=f'settle {arr(ao)}; parents {arr([ap[u] for u in nodes])}; {ac} successful relaxations'
    if option==correct or option in wrong:option=f'settle {arr(ao)}; parents {arr([ap[u] for u in nodes])}; {ac+len(wrong)+1} successful relaxations'
    wrong.append(option)
  make(t,level,v,stem,correct,wrong,'Settling order: '+arr(order)+'. Snapshots after each outgoing-edge scan: '+'; '.join(u+': '+vec([st[u2] for u2 in nodes]) for u,st,p,c in states)+f'. There are {decs} successful strict label decreases. Zero-weight edges are permitted.',f'Directed nonnegative graph; source A; vector order {arr(nodes)}. Dijkstra chooses the alphabetically first unsettled vertex on equal minimum labels. Scan outgoing neighbours alphabetically; only STRICT improvements change distance/parent. Settled vertices are never reopened.',graph_data(nodes,edges,True),evidence=dict(algorithm='dijkstra',nodes=nodes,edges=edges,order=order,distances=d,parents=par,decreases=decs))
 elif t==25:
  nodes=list('ASBCDEFT'[:8 if baka else 5+v]);desired=nodes[:];pairs={(desired[i],desired[i+1]) for i in range(1,len(nodes)-1)};pairs.add(('A','B'));other=[(desired[i],desired[j]) for i in range(len(nodes)) for j in range(i+1,len(nodes)) if (desired[i],desired[j]) not in pairs];r.shuffle(other);pairs.update(other[:3+idx]);edges=[(a,b,r.randrange(-6,9)) for a,b in sorted(pairs)];order,_=topo(nodes,edges);d={u:math.inf for u in nodes};d['S']=0;par={u:'-' for u in nodes};states=[]
  for u in order:
   for a,b,w in edges:
    if a==u and d[a]+w<d[b]:d[b]=d[a]+w;par[b]=a
   states.append((u,d.copy()))
  stop=order.index('S')+1 if level=='Easy' else min(len(order),order.index('S')+3) if level=='Medium' else len(order);values=[states[stop-1][1][u] for u in nodes]
  correct=vec(values);wrong=vector_wrong(values);stem=f'After processing the first {stop} vertices of the stated topological order, what is the distance vector?'
  if baka:pv=[par[u] for u in nodes];correct+=f'; parents {arr(pv)}';wrong=[z+f'; parents {pa}' for z,pa in zip(wrong,trace_variants(pv,[i for i,x in enumerate(pv) if x=='-']))];stem='After the entire topological relaxation, what are the final distance and parent vectors?'
  if baka:
   wrong=[]
   for skipped in [('D','E'),('E','F'),('F','T')]:
    dd={u:math.inf for u in nodes};dd['S']=0;pp={u:'-' for u in nodes}
    for u in order:
     for a,b,w in edges:
      if a==u and (a,b)!=skipped and dd[a]+w<dd[b]:dd[b]=dd[a]+w;pp[b]=a
    wrong.append(vec([dd[u] for u in nodes])+f'; parents {arr([pp[u] for u in nodes])}')
  make(t,level,v,stem,correct,wrong,'Process '+arr(order)+' in order. Snapshots: '+'; '.join(u+': '+vec([st[x] for x in nodes]) for u,st in states)+'. Unreachable tails stay INF; negative edges are allowed because this graph is acyclic.',f'Directed DAG. Source S; vector order {arr(nodes)}. Use topological order {arr(order)}. Initialise only d[S]=0; others INF. Relax outgoing edges alphabetically once per vertex with strict improvement, skipping unreachable tails. Parent - means unset.',graph_data(nodes,edges,True),evidence=dict(algorithm='dag',nodes=nodes,edges=edges,order=order,distances=d,parents=par))
 elif 26<=t<=27 or t==30:
  n=8 if baka else 5+v;nodes=list('ABCDEFGH'[:n]);pairs={tuple(sorted([nodes[i],nodes[i+1]])) for i in range(n-1)};other=[p for p in itertools.combinations(nodes,2) if p not in pairs];r.shuffle(other);pairs.update(other[:n-2+(1 if baka else 0)]);edges=[(a,b,r.randrange(1,8)) for a,b in sorted(pairs)]
  if baka and t==26:
   pairs.add(('A','C'));edges=[(a,b,1 if a+b in ['AB','AC','BC'] else r.randrange(2,8)) for a,b in sorted(pairs)]
  if baka and t==30:edges=[(e[0],e[1],w) for e,w in [('AB',1),('BC',2),('AC',2),('CD',3),('BD',3),('AD',4),('DE',4),('CE',5),('EF',5),('DF',6),('FG',6),('EG',6),('GH',7),('FH',8)]]
  g=graph_data(nodes,edges);best,trees=mst_all(nodes,edges);context='Use this connected UNDIRECTED weighted graph. Edge names list their endpoints alphabetically. Only listed edges exist. '
  if t==26:
   if level=='Easy':cut=set(nodes[:2+v%2]);cross=[a+b for a,b,w in edges if (a in cut)!=(b in cut)];correct=arr(cross);wrong=variants(correct,[arr(cross[:-1]),arr(cross+[next(a+b for a,b,w in edges if (a in cut)==(b in cut))]),arr([a+b for a,b,w in edges]),arr(cross+cross[:1])]);stem=f'Which are exactly the crossing edges of cut {arr(sorted(cut))} | {arr([u for u in nodes if u not in cut])}?';why='A crossing edge has exactly one endpoint in each side. Internal edges are excluded even if their weights are small.'
   elif level=='Medium':cut=set(nodes[:3]);cross=[(a+b,w) for a,b,w in edges if (a in cut)!=(b in cut)];light=min(w for _,w in cross);lightedges=[e for e,w in cross if w==light];correct=f'light edges {arr(lightedges)}; each belongs to SOME MST';wrong=[f'light edges {arr([cross[0][0]])}; every other crossing edge is forbidden',f'light edges {arr(lightedges)}; each is excluded from EVERY MST',f'light edges {arr([e for e,w in cross])}; each is equally light'];stem=f'For cut {arr(sorted(cut))} versus its complement, which minimum-weight crossing edges are safe choices under the general cut property?';why=f'Minimum crossing weight is {light}. Its edges are {arr(lightedges)}. A uniquely light crossing edge belongs to every MST. Tied light edges each belong to some MST; the tie alone does not determine whether either is mandatory.'
   elif level=='Hard':mandatory=sorted(set.intersection(*(set(s) for s in trees)));correct=f'weight {best}; {len(trees)} MST(s); mandatory edges {arr(mandatory)}';wrong=[f'weight {best}; {len(trees)+d} MST(s); mandatory edges {arr(mandatory)}' for d in [1,2,3]];stem='Which gives the minimum total spanning weight, number of distinct MST edge sets, and edges shared by EVERY MST?';why=f'Enumerating connected acyclic sets of {n-1} edges yields {len(trees)} minimum sets of weight {best}. Their intersection is {arr(mandatory)}. Equal edge weights do not by themselves determine uniqueness.'
   else:mandatory=sorted(set.intersection(*(set(s) for s in trees)));possible=sorted(set.union(*(set(s) for s in trees)));never=sorted(set(a+b for a,b,w in edges)-set(possible));correct=f'weight {best}; {len(trees)} MSTs; every-MST {arr(mandatory)}; no-MST {arr(never)}';wrong=[f'weight {bw}; {cnt} MSTs; every-MST {arr(mand)}; no-MST {arr(nev)}' for bw,cnt,mand,nev in [(best,1,sorted(trees[0]),sorted(set(a+b for a,b,w in edges)-set(trees[0]))),(best,len(trees)+1,mandatory+['AB'],never),(best+1,len(trees),mandatory,never[:-1])]];stem='Classify the entire MST family: minimum weight, distinct MST count, edges in EVERY MST, and edges in NO MST.';why=f'Among all {n-1}-edge spanning trees, exactly {len(trees)} minimise the sum to {best}. Intersect minimum edge sets for mandatory edges; subtract their union from all edges for impossible ones. Do not exclude all tied-heaviest edges merely because of a cycle.'
  elif t==27:
   order,key,par,states,decs=weighted(nodes,edges,'A','prim');k=1 if level=='Easy' else min(3+v,n-1) if level=='Medium' else n
   if level=='Easy':first=order[1];correct=f'{par[first]}{first}, key {key[first]}';wrong=variants(correct,[f'{a}{b}, key {w}' for a,b,w in edges]+[f'{first}{par[first]}, key {key[first]+1}']);stem='After starting at A, which attachment edge is accepted FIRST, and what key does it use?';why=f'Only edges crossing from the initial tree {{A}} are eligible. The next vertex is {first}, attached through {par[first]} for {key[first]}.'
   elif level=='Medium':values=[states[k-1][1][u] for u in nodes if u not in order[:k]];outside=[u for u in nodes if u not in order[:k]];correct=vec(values);wrong=vector_wrong(values);stem=f'After adding and scanning {arr(order[:k])}, what are keys for outside vertices {arr(outside)}?';why='Keys remember single attachment edges from ANY vertex already in the tree, not just from the last-added vertex and not total paths from A.'
   elif level=='Hard':selected=sorted(''.join(sorted([u,par[u]])) for u in nodes if u!='A');correct=f'edges {arr(selected)}; total {best}';wrong=[f'edges {arr(selected)}; total {best+d}' for d in [1,-1,2]];stem='What final MST edge set and total weight does the stated Prim run produce?';why='Vertex acceptance order '+arr(order)+'. Selected parent edges are '+arr(selected)+f', summing to {sum(key[u] for u in nodes if u!="A")}. Keys can decrease after the next vertex enters.'
   else:
    directed=[e for a,b,w in edges for e in [(a,b,w),(b,a,w)]];dorder,dists,dpar,_,_=weighted(nodes,directed,'A');target=nodes[-1];treeAdj={u:[] for u in nodes}
    for u in nodes:
     if u!='A':treeAdj[u].append((par[u],key[u]));treeAdj[par[u]].append((u,key[u]))
    stack=[('A',0)];seen=set();pathcost=None
    while stack:
     u,cost=stack.pop()
     if u==target:pathcost=cost;break
     seen.add(u)
     for w,c in treeAdj[u]:
      if w not in seen:stack.append((w,cost+c))
    correct=f'Prim total {best}; Prim-tree A-{target} path {pathcost}; shortest A-{target} distance {dists[target]}';wrong=[f'Prim total {best}; Prim-tree A-{target} path {pathcost+d}; shortest A-{target} distance {dists[target]}' for d in [1,-1,2]];stem=f'Run Prim and Dijkstra independently from A. Give MST total, the weight of the A-to-{target} route INSIDE Prim\'s selected tree, and the true shortest A-to-{target} distance.';why=f'Prim parent map: {par}. Its objective gives total {best}; its unique tree route to {target} costs {pathcost}. Dijkstra adds entire route costs and obtains {dists[target]}; a minimum spanning tree need not be a shortest-path tree.'
   context+='Prim starts A with key 0; all other keys INF. Extract the alphabetically first outside vertex on a tied key; scan neighbours alphabetically and update parents ONLY on strict edge-weight improvement. '
  else:
   sorted_edges=sorted(edges,key=lambda e:(e[2],e[0],e[1]));p={u:u for u in nodes};accepted=[];rejected=[];states=[];seen=0
   def find(x):
    while p[x]!=x:x=p[x]
    return x
   for a,b,w in sorted_edges:
    seen+=1;ra,rb=find(a),find(b)
    if ra!=rb:p[ra]=rb;accepted.append(a+b)
    else:rejected.append(a+b)
    parts={}
    for u in nodes:parts.setdefault(find(u),[]).append(u)
    states.append((accepted[:],rejected[:],sorted(''.join(s) for s in parts.values())))
    if len(accepted)==n-1:break
   k=2 if level=='Easy' else min(4+v,len(states)) if level=='Medium' else len(states)
   if baka:
    checkpoint=min(7,len(states));acc,rej,parts=states[checkpoint-1];correct=f'after {checkpoint}: accept {arr(acc)}, reject {arr(rej)}, components {arr(parts)}; final weight {best}; examined {seen}';wrong=[]
    # Alternative tied-candidate orderings preserve a seven-candidate checkpoint and a valid forest.
    alternatives=[sorted(edges,key=lambda e:(e[2],-ord(e[0]),-ord(e[1]))),sorted_edges[:3]+[sorted_edges[4],sorted_edges[3]]+sorted_edges[5:],sorted_edges[:1]+[sorted_edges[2],sorted_edges[1]]+sorted_edges[3:]]
    for alt in alternatives:
     pp={u:u for u in nodes};aa=[];rr=[];examined=0
     def rootof(x):
      while pp[x]!=x:x=pp[x]
      return x
     checkpoint_parts=None;weight=0
     for u,w,cost in alt:
      examined+=1;ra,rb=rootof(u),rootof(w)
      if ra!=rb:pp[ra]=rb;aa.append(u+w);weight+=cost
      else:rr.append(u+w)
      if examined==checkpoint:
       groups={}
       for node in nodes:groups.setdefault(rootof(node),[]).append(node)
       checkpoint_parts=(aa[:],rr[:],sorted(''.join(group) for group in groups.values()))
      if len(aa)==n-1:break
     sa,sr,sp=checkpoint_parts;wrong.append(f'after {checkpoint}: accept {arr(sa)}, reject {arr(sr)}, components {arr(sp)}; final weight {weight}; examined {examined}');stem=f'After examining exactly {checkpoint} sorted candidates, give the accepted edges, rejected edges and components. Also give the final MST weight and total candidates examined before stopping.'
   elif level=='Hard':correct=f'accepted {arr(accepted)}; rejected {arr(rejected)}; {seen} examined';wrong=[f'accepted {arr(accepted)}; rejected {arr(rejected)}; {seen+d} examined' for d in [1,-1,2]];stem='Run until n-1 edges have been accepted. What are the accepted sequence, rejected sequence, and number of examined candidates?'
   else:
    acc,rej,parts=states[k-1];correct=f'accept {arr(acc)}; reject {arr(rej)}; components {arr(parts)}';wrong=[f'accept {arr(acc)}; reject {arr(rej)}; components {arr(parts+[nodes[0]])}',f'accept {arr(acc)}; reject {arr(rej+[sorted_edges[k-1][0]+sorted_edges[k-1][1]])}; components {arr(parts)}',f'accept {arr(acc[:-1])}; reject {arr(rej)}; components {arr(parts)}'];stem=f'After examining {k} sorted candidates, which accepted/rejected sequences and forest components are correct?'
   why='Sorted candidates: '+', '.join(a+b+f'({w})' for a,b,w in sorted_edges)+'. Reject only when endpoints already share a component. Acceptance order '+arr(accepted)+f'; stop after {seen} examined candidates, not after that many acceptances. MST weight {best}.';context+='Kruskal sorts by (weight, alphabetical first endpoint, alphabetical second endpoint), tests candidates in that order, and stops immediately on n-1 ACCEPTED edges. '
  make(t,level,v,stem,correct,wrong,why,context,g,evidence=dict(nodes=nodes,edges=edges,mstWeight=best,mstCount=len(trees),result=correct))
 elif t==28 or t==29:
  n=12 if baka else 6+v;nodes=list('ABCDEFGHIJKLMNOP'[:n]);p={u:u for u in nodes};rank={u:0 for u in nodes}
  def find(x,compress):
   if p[x]==x:return x
   root=find(p[x],compress)
   if compress:p[x]=root
   return root
  def union(a,b,ranked,compress):
   a,b=find(a,compress),find(b,compress)
   if a==b:return
   if not ranked:p[a]=b
   elif rank[a]>rank[b]:p[b]=a
   else:
    p[a]=b
    if rank[a]==rank[b]:rank[b]+=1
  ops=[];snapshots=[]
  if t==28:
   perm=nodes[:];r.shuffle(perm)
   for a,b in zip(perm,perm[1:]):union(a,b,False,False);ops.append(f'Union({a},{b})')
   initial=p.copy();ops=[];target=perm[0] if level=='Easy' else perm[min(2+v,n-2)] if level=='Medium' else perm[1];compress=level!='Easy'
   root=find(target,compress);ops.append(f'Find({target})'+(' with full compression' if compress else ' without compression'))
   if level in ['Hard','Baka']:
    target2=perm[n//2];find(target2,True);ops.append(f'Find({target2}) with full compression')
   if baka:
    # A branch is deliberately left untraversed: global flattening is incorrect.
    find(perm[-3],True);ops.append(f'Find({perm[-3]}) with full compression')
   if baka:
    p={u:u for u in nodes}
    for indices in [[0,1,2,3],[4,5,6],[7,8],[9,10,11]]:
     for i,j in zip(indices,indices[1:]):p[perm[i]]=perm[j]
    initial=p.copy();ops=[];returns=[]
    for name,args in [('Find',[perm[0]]),('Union',[perm[4],perm[8]]),('Find',[perm[5]]),('Union',[perm[2],perm[10]]),('Find',[perm[0]]),('Find',[perm[4]])]:
     if name=='Find':returns.append(find(args[0],True))
     else:union(*args,False,True)
     ops.append(name+'('+','.join(args)+')')
   if level=='Easy':correct=root;wrong=[u for u in nodes if u!=root];stem=f'What representative does Find({target}) return?';why='Follow parent pointers to the unique self-parent root '+root+'. Without compression no parent changes.'
   else:values=[p[u] for u in nodes];correct=arr(values);wrong=choices_array(values);stem='What is the ENTIRE parent vector after the stated operations?' ;why='Only vertices on a queried path are redirected to the root. The final pointers are '+str(p)+'. Unvisited ancestors/branches do not get flattened merely because they belong to the same set.'
   context='Initial parent vector in '+arr(nodes)+' order is '+arr([initial[u] for u in nodes])+'. A root points to itself. Execute '+'; then '.join(ops)+'. Unless stated otherwise, finds fully compress their own traversed paths; Union(x,y) finds both roots with compression and attaches the FIRST root below the SECOND. These are union-find parent pointers, not graph traversal parents.'
  else:
   # Balanced root construction plus non-root arguments/compression in later operations.
   initial={u:u for u in nodes};pairs=[(nodes[i],nodes[i+1]) for i in range(0,n-1,2)];ops_pairs=pairs[:2 if level=='Easy' else len(pairs)]
   if level=='Easy':ops_pairs=[[(0,1),(2,3)],[(3,5),(1,3),(0,4)],[(6,2),(4,0),(6,4)]][v];ops_pairs=[(nodes[i],nodes[j]) for i,j in ops_pairs]
   if level!='Easy':
    ops_pairs +=[(nodes[0],nodes[2]),(nodes[4],nodes[6])] if n>=8 else [(nodes[0],nodes[2])]
   if level in ['Hard','Baka']:ops_pairs +=[(nodes[0],nodes[4])]
   if baka:ops_pairs +=[(nodes[8],nodes[10]),(nodes[0],nodes[8]),(nodes[2],nodes[7]),(nodes[1],nodes[11])]
   for a,b in ops_pairs:union(a,b,True,True);ops.append(f'Union({a},{b})');snapshots.append(p.copy())
   if level in ['Hard','Baka']:
    find(nodes[0],True);ops.append(f'Find({nodes[0]})')
   values=[p[u] for u in nodes];roots=sorted(u for u in nodes if p[u]==u);ranks=[rank[u] for u in roots]
   correct=f'parents {arr(values)}; roots {arr(roots)} with ranks {arr(ranks)}';wrong=[f'parents {arr(values)}; roots {arr(roots)} with ranks {z}' for z in vector_wrong(ranks,arr)];stem='What are the final parent vector and ranks of the remaining roots?';why='Find compresses only the paths it traverses. On equal root ranks attach the FIRST root below the SECOND and increment only the second rank. Same-root Union does nothing. Final parents '+str(p)+'; root ranks '+str({u:rank[u] for u in roots})+'.'
   if baka:
    heights=[]
    for u in nodes:
     h=0
     while p[u]!=u:u=p[u];h+=1
     heights.append(h)
    correct+=f'; actual maximum height {max(heights)}';wrong=[]
    for changed,rk in [({'I':'H','J':'H','K':'H'},ranks),({'I':'L','J':'H','K':'L'},[x-1 for x in ranks]),({'I':'J','J':'L','K':'L'},ranks)]:
     pp=p|changed;hh=[]
     for node in nodes:
      h=0
      while pp[node]!=node:node=pp[node];h+=1
      hh.append(h)
     wrong.append(f'parents {arr([pp[u] for u in nodes])}; roots {arr(roots)} with ranks {arr(rk)}; actual maximum height {max(hh)}')
    stem+=' Also give the maximum current tree height in parent edges.';why+=f' Compression does not reduce stored ranks, but current maximum height is {max(heights)}.'
   context='Start singleton sets '+arr(nodes)+' with rank 0. Execute '+', '.join(ops)+'. Every Union first performs FULL path-compressing finds on its arguments. Lower root rank attaches below higher; on a tie the FIRST root attaches below SECOND and only second rank increases. Parent-vector order is '+arr(nodes)+'.'
  make(t,level,v,stem,correct,wrong,why,context,evidence=dict(algorithm='dsu',nodes=nodes,parents=p,ranks=rank,operations=ops,result=correct))
 else:raise ValueError(t)

if __name__=='__main__':
 for t in range(1,31):
  for level in LEVELS:
   for v in range(1 if level=='Baka' else 3):generate(t,level,v)
  bank[t-1]['qs'].sort(key=lambda q:(LEVELS.index(q['difficulty']),q['id']))
  print(f'Topic {t:02d}: {len(bank[t-1]["qs"])} questions')
 assert next_id==391
 BASE['topics']=bank;BASE['bankVersion']='expanded-2026-10-22'
 (WEB/'public/data/catalog.json').write_text(json.dumps(BASE,ensure_ascii=False,separators=(',',':')))
 (WEB/'content/question-bank.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2))
 (WEB/'content/answer-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
 print('390 total, including 30 Baka questions. Original IDs 1-90 preserved.')
