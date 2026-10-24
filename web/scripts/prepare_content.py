"""Import the vetted MCQs and existing full lessons without copying video masters."""
from pathlib import Path
import json,re,subprocess,shutil
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
WEB=ROOT/'web';PUBLIC=WEB/'public';DATA=PUBLIC/'data'
DATA.mkdir(parents=True,exist_ok=True)
(PUBLIC/'captions').mkdir(exist_ok=True)
(PUBLIC/'assets').mkdir(exist_ok=True)
bank_path=WEB/'content/question-bank.json'
bank=json.loads((bank_path if bank_path.exists() else ROOT/'tmp/pdfs/sc2001-mcq/bank.json').read_text())
sc2005_bank_path=WEB/'content/sc2005-question-bank.json'
sc2005_bank=json.loads(sc2005_bank_path.read_text()) if sc2005_bank_path.exists() else []
library={x['slug']:x for x in json.loads((ROOT/'edit/series/complete-weeks01-07/library.json').read_text())}
# Every PDF topic appears in exactly one lesson collection; topics remain individually selectable.
content=[
 ('insertion-sort','Insertion sort','Sorting',[0,1],'Build a sorted prefix, one carefully placed element at a time.'),
 ('merge-sort','Merge sort','Sorting',[2],'Split the problem. Merge the answers. Understand every level.'),
 ('quicksort','Quicksort','Sorting',[3,4],'Follow the pivot, the partition, and the recursive calls.'),
 ('counting-sort','Counting sort','Sorting',[5],'Turn key frequencies into stable output positions.'),
 ('radix-sort','Radix sort','Sorting',[6],'See why one stable digit pass builds on the last.'),
 ('heapify','Heapify','Heaps',[8,9],'Read the heap, then repair it from the inside out.'),
 ('build-heap','Build a heap','Heaps',[10],'Start at the last parent and discover why building is linear.'),
 ('priority-queue','Priority queues','Heaps',[11],'Insert, extract, and follow every change in the heap.'),
 ('heapsort','Heapsort','Heaps',[7,12],'Shrink the active heap. Grow the sorted suffix.'),
 ('breadth-first-search','Breadth-first search','Graph search',[13,14,15],'Explore layer by layer, with a queue to keep your place.'),
 ('depth-first-search','Depth-first search','Graph search',[16,17,18],'Follow the call stack, classify edges, and find cycles.'),
 ('topological-sort','Topological sorting','Graph search',[19,20],'Put dependencies in order with source removal and DFS.'),
 ('bellman-ford','Bellman-Ford','Shortest paths',[21,22],'Relax every edge and see what each pass guarantees.'),
 ('dijkstra','Dijkstra’s algorithm','Shortest paths',[23],'Track tentative distances until the next minimum is certain.'),
 ('dag-shortest-paths','DAG shortest paths','Shortest paths',[24],'Use a topological order to handle even negative edges.'),
 ('prim','Prim’s algorithm','Spanning trees',[25,26],'Grow one tree by choosing its cheapest outward edge.'),
 ('union-find','Union-find','Spanning trees',[27,28],'Watch sets merge, paths compress, and ranks change.'),
 ('kruskal','Kruskal’s algorithm','Spanning trees',[29],'Sort edges, reject cycles, and bring the forest together.'),
]
lessons=[];mounts={};covered=[]
for slug,title,group,indices,description in content:
 # Published series copies are the current full-length masters, including updated graph lessons.
 candidates=[ROOT/'edit/series/revisions'/slug, ROOT/'edit/revisions'/slug]
 candidates=[d for d in candidates if (d/f'malfoid-{slug}.mp4').exists()]
 folder=max(candidates,key=lambda d:(d/f'malfoid-{slug}.mp4').stat().st_mtime)
 video=folder/f'malfoid-{slug}.mp4'
 duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(video)],text=True))
 timelinepath=ROOT/'edit/revisions'/slug/'timeline.json'
 tl=json.loads(timelinepath.read_text()) if timelinepath.exists() else {}
 beats=tl.get('beats',[])
 transcript=[dict(id=b['id'],start=round(b['start'],2),end=round(b['end'],2),text=b['text']) for b in beats]
 # Choose chapter boundaries from actual spoken beats, never invented timestamps.
 chapters=[dict(title='The idea',time=0)]
 used={0};patterns=[('Worked example',r'(split4|pass1|scan|example|trace|start|extract|step1|pick|first|grow|relax1|edge1|round1)'),('Why it works',r'(invariant|correct|proof|safe|why)'),('Time complexity',r'(runtime|complexity|worst|cost|sum|general|bill|time)'),('Things to remember',r'(notes|exam|takeaway|recap|limits|caveat)')]
 for label,pattern in patterns:
  b=next((b for b in beats[1:] if re.search(pattern,b['id'],re.I) and b['start'] not in used),None)
  if b:chapters.append(dict(title=label,time=round(b['start'],2)));used.add(b['start'])
 if len(chapters)<3:
  for ix,label in [(len(beats)//3,'Worked example'),(2*len(beats)//3,'Details and complexity')]:
   if beats and beats[ix]['start'] not in used:chapters.append(dict(title=label,time=round(beats[ix]['start'],2)));used.add(beats[ix]['start'])
 chapters.sort(key=lambda b:b['time'])
 src=library.get(slug,{}).get('source',{})
 week=library.get(slug,{}).get('week',1 if slug=='insertion-sort' else 2)
 captionpath=folder/'captions.srt'
 if captionpath.exists():
  srt=captionpath.read_text();vtt='WEBVTT\n\n'+re.sub(r'(\d\d:\d\d:\d\d),(\d{3})',r'\1.\2',srt)
  (PUBLIC/'captions'/f'{slug}.vtt').write_text(vtt)
 poster=PUBLIC/'assets'/f'{slug}.webp'
 originalposter=folder/'poster.png'
 if originalposter.exists():
  im=Image.open(originalposter).convert('RGB');im.thumbnail((540,960));im.save(poster,'WEBP',quality=82)
 else:
  subprocess.run(['ffmpeg','-loglevel','error','-y','-ss','0.8','-i',str(video),'-frames:v','1','-vf','scale=540:-1',str(poster)],check=True)
 url=f'/media/{slug}.mp4';mounts[url]=str(video.relative_to(ROOT))
 lessons.append(dict(slug=slug,title=title,group=group,description=description,week=week,duration=round(duration,2),video=url,poster=f'/assets/{slug}.webp',captions=f'/captions/{slug}.vtt' if captionpath.exists() else None,chapters=chapters,transcript=transcript,topicIds=[i+1 for i in indices],source=dict(deck=src.get('deck','01_Sorting'),pages=src.get('pages',list(range(8,10)) if slug=='insertion-sort' else list(range(11,16))),recording=src.get('recording','w01_sorting_2_insertion_sort' if slug=='insertion-sort' else 'w02_sorting_3_merge_sort'))))
 for i in indices:
  bank[i]['id']=i+1;bank[i]['slug']=re.sub(r'[^a-z0-9]+','-',bank[i]['title'].lower()).strip('-');bank[i]['lessonSlug']=slug;bank[i]['group']=group
  # No separate wrong-option list is needed by the player.
  for q in bank[i]['qs']:q.pop('wrong',None)
  covered.append(i)
assert sorted(covered)==list(range(30))
# Import the published SC2005 sequence in its reviewed order.
for lesson in lessons: lesson['courseId']='sc2001'
for entry in json.loads((ROOT/'edit/series/sc2005-weeks01-07/manifest.json').read_text()):
 folder=Path(entry['folder']);slug=folder.name;video=folder/f'malfoid-{slug}.mp4'
 if not video.is_file():raise FileNotFoundError(video)
 beats=json.loads((folder/'timeline.json').read_text())['beats']
 transcript=[dict(id=b['id'],start=round(b['start'],2),end=round(b['end'],2),text=b['text']) for b in beats]
 chapters=[dict(title='The idea',time=0)]
 for index,label in [(len(beats)//3,'Worked explanation'),(2*len(beats)//3,'Details and reminders')]:
  if index and beats[index]['start']>chapters[-1]['time']:chapters.append(dict(title=label,time=round(beats[index]['start'],2)))
 srt=(folder/'captions.srt').read_text()
 (PUBLIC/'captions'/f'{slug}.vtt').write_text('WEBVTT\n\n'+re.sub(r'(\d\d:\d\d:\d\d),(\d{3})',r'\1.\2',srt))
 poster=next((folder/name for name in ['poster.jpg','poster.png'] if (folder/name).exists()),None)
 if poster is None:poster=next((ROOT/'edit/series/revisions'/slug/name for name in ['poster.jpg','poster.png'] if (ROOT/'edit/series/revisions'/slug/name).exists()),None)
 if poster is None:raise FileNotFoundError(f'Poster for {slug}')
 im=Image.open(poster).convert('RGB');im.thumbnail((540,960));im.save(PUBLIC/'assets'/f'{slug}.webp','WEBP',quality=82)
 url=f'/media/{slug}.mp4';audio=f'/media/{slug}.wav';source=f'/sources/{slug}.md'
 mounts[url]=str(video.relative_to(ROOT));mounts[audio]=str((folder/'narration.wav').relative_to(ROOT))
 sourcefile=ROOT/'edit/series/revisions'/slug/'sources.md'
 if not sourcefile.exists():sourcefile=folder/'README.md'
 mounts[source]=str(sourcefile.relative_to(ROOT))
 lessons.append(dict(slug=slug,courseId='sc2005',title=entry['title'],group=entry['group'],description=f"SC2005 · {entry['group']} · Through Week 7",periodLabel='Through Week 7',duration=round(entry['seconds'],2),video=url,poster=f'/assets/{slug}.webp',captions=f'/captions/{slug}.vtt',narration=audio,chapters=chapters,transcript=transcript,topicIds=[],source=dict(summary=entry['sources'],map=source)))
# The broad exam-bank topics complement the smaller video lessons.  The last
# three topics are based on the supplied lecture decks even though the video
# manifest ends before those lecture units; they point to the foundations
# lesson so the existing quiz UI still has a useful explanation link.
os_topic_lessons=[
 ('sc2005-01-os-foundations','Foundations'),
 ('sc2005-05-process-states','Processes and threads'),
 ('sc2005-10-scheduling-metrics','CPU scheduling'),
 ('sc2005-16-race-conditions','Synchronization'),
 ('sc2005-25-deadlock-graphs','Deadlocks'),
 ('sc2005-29-real-time-model','Real-time OS'),
 ('sc2005-32-virtualization-abstractions','Virtualization'),
 ('sc2005-01-os-foundations','Foundations'),
 ('sc2005-01-os-foundations','Foundations'),
 ('sc2005-01-os-foundations','Foundations'),
]
os_offset=max((question['id'] for topic in bank for question in topic['qs']),default=0)
for index,(topic, (lesson_slug, group)) in enumerate(zip(sc2005_bank,os_topic_lessons),start=1):
 topic['id']=os_offset+index
 topic['lessonSlug']=lesson_slug
 topic['group']=group
 for question_index,question in enumerate(topic['qs'],start=1):
  question['id']=os_offset+(index-1)*16+question_index
  question.setdefault('context',topic['context'])
  question.setdefault('graph',None)
  question['correct']=question['options']['ABCD'.index(question['answer'])]
 bank.append(topic)
 for lesson in lessons:
  if lesson['slug']==lesson_slug: lesson['topicIds'].append(topic['id'])
# The later SC2001 sequence is appended after legacy OS IDs have been allocated.
from import_sc2001_later import import_later_lessons
import_later_lessons(ROOT,WEB,lessons,bank,mounts)
# Import the reviewed Automata playlist, keeping its episode order and real chapters.
automata=ROOT/'edit/series/sc2203'
for entry in json.loads((automata/'playlist.json').read_text()):
 video=(automata/entry['path']).resolve();folder=video.parent;slug=folder.name
 timeline=folder/'timeline.json'
 if not timeline.exists():timeline=ROOT/'edit/revisions'/slug/'timeline.json'
 beats=json.loads(timeline.read_text())['beats']
 transcript=[dict(id=b['id'],start=round(b['start'],2),end=round(b['end'],2),text=b['text']) for b in beats]
 chapters=[dict(title=c['title'],time=round(c['start'],2)) for c in entry['chapters']]
 caption=automata/entry['vtt'];poster=automata/entry['poster']
 shutil.copyfile(caption,PUBLIC/'captions'/f'{slug}.vtt')
 im=Image.open(poster).convert('RGB');im.thumbnail((540,960));im.save(PUBLIC/'assets'/f'{slug}.webp','WEBP',quality=82)
 url=f'/media/{slug}.mp4';audio=f'/media/{slug}.wav';source=f'/sources/{slug}.md'
 for route,file in [(url,video),(audio,(automata/entry['audio']).resolve()),(source,(automata/entry['sources']).resolve())]:
  if not file.is_file():raise FileNotFoundError(file)
  mounts[route]=str(file.relative_to(ROOT))
 sourcecopy=WEB/'content/cloud-support'/source.lstrip('/');sourcecopy.parent.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(automata/entry['sources'],sourcecopy)
 lessons.append(dict(slug=slug,courseId='sc2203',title=entry['title'],group=entry['group'],description=f"{entry['id']} · {entry['group']}",periodLabel='Weeks 1–11',duration=round(entry['seconds'],2),video=url,poster=f'/assets/{slug}.webp',captions=f'/captions/{slug}.vtt',narration=audio,chapters=chapters,transcript=transcript,topicIds=[],source=dict(summary='SC2203 supplied lecture slides and tutorials through Week 11. Weeks 12–13 materials were not supplied.',map=source)))
courses=[dict(id='sc2001',code='SC2001',title='Algorithms',periodLabel='Weeks 1–13',description='From the first sorted element to the shortest path.',libraryIntro='Thoughtful practice. One topic at a time.'),dict(id='sc2005',code='SC2005',title='Operating Systems',periodLabel='Weeks 1–7',description='Processes, scheduling and the systems behind every program.',libraryIntro='Slides, examples and exam reminders through Week 7.'),dict(id='sc2203',code='SC2203',title='Automata',periodLabel='Weeks 1–11',description='From finite automata to Turing machines, reductions and NP-completeness.',libraryIntro='Proofs, constructions and worked examples from the supplied Weeks 1–11 materials. Weeks 12–13 materials were not supplied.')]
Image.open(ROOT/'edit/v2/assets/malfoid-encouraging.png').save(PUBLIC/'assets/malfoid.webp','WEBP',quality=90)
(DATA/'catalog.json').write_text(json.dumps(dict(courses=courses,lessons=lessons,topics=bank,bankVersion='sc2001-complete-2026-10-24' if bank_path.exists() else 'original'),ensure_ascii=False,separators=(',',':')))
(WEB/'media-manifest.json').write_text(json.dumps(mounts,indent=2))
print(f'Prepared {len(lessons)} full lessons, {len(bank)} topics, {sum(len(t["qs"]) for t in bank)} questions, captions and chapter links.')
