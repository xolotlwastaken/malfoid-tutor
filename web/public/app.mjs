import {createQuiz} from './quiz.mjs';
import {createProgress} from './progress.mjs';

const main=document.querySelector('main');
const difficulties=['Easy','Medium','Hard','Baka'];
const malfoidDialogue={
  sc2001:'“I sorted my priorities and you came first. D-don’t look so pleased! It must be a bug in my comparison function.”',
  sc2005:'“My process states? Tsun-tsun → Embarrassed → Dere-dere. H-hmph! You weren’t supposed to trigger that last transition!”',
  sc2203:'“My automaton rejects everyone… then you arrive and it enters an accepting state. H-hmph! Clearly, a faulty transition.”'
};
const homeMalfoidDialogue=[
  '“I wasn’t waiting for you! I was just… keeping the study space tidy.”',
  '“H-hmph! Don’t think this little greeting means I’m happy to see you.”',
  '“You came back? I suppose I can explain one more thing… if you insist.”',
  '“It’s not like I made these lessons clear just for you, b-baka!”',
  '“Stop staring! Unless you need help… which you clearly do.”'
];
const totalQuestions=()=>catalog?.topics.reduce((sum,topic)=>sum+topic.qs.length,0)??0;
let activeCourse='sc2001';
const courseLessons=()=>catalog.lessons.filter(l=>l.courseId===activeCourse);
const courseTopics=()=>{const ids=new Set(courseLessons().flatMap(l=>l.topicIds));return catalog.topics.filter(topic=>ids.has(topic.id));};
const courseQuestionCount=()=>courseTopics().reduce((sum,topic)=>sum+topic.qs.length,0);
const currentCourse=()=>catalog.courses.find(c=>c.id===activeCourse);
const hasPractice=()=>courseLessons().some(l=>l.topicIds.length);
const libraryUrl=()=>`#/course/${activeCourse}`;
const courseGroups=()=>['All topics',...new Set(courseLessons().map(l=>l.group))];
const escape=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const clock=seconds=>`${Math.floor(seconds/60)}:${String(Math.floor(seconds%60)).padStart(2,'0')}`;
const icon=(name,extra='')=>{
  const paths={arrow:'<path d="M4 12h16m-6-6 6 6-6 6"/>',chevron:'<path d="m9 5 7 7-7 7"/>',search:'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4.5 4.5"/>',play:'<path d="m9 5 10 7-10 7z"/>',check:'<path d="m5 12 4 4L19 6"/>',x:'<path d="m6 6 12 12M6 18 18 6"/>',clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',book:'<path d="M12 5C9 3 5 3 3 4v15c3-1 6-1 9 1 3-2 6-2 9-1V4c-2-1-6-1-9 1Zm0 0v15"/>',repeat:'<path d="M20 8a8 8 0 1 0 0 8M20 3v5h-5"/>',download:'<path d="M12 3v12m-5-5 5 5 5-5M4 17v4h16v-4"/>'};
  return `<svg class="inline-icon ${extra}" viewBox="0 0 24 24" aria-hidden="true">${paths[name]||paths.arrow}</svg>`;
};
let storage;
try{storage=window.localStorage;}catch{storage={getItem(){throw Error('Unavailable');},setItem(){throw Error('Unavailable');}};}
const progress=createProgress(storage);
let catalog,lessons,topics,questionTopic,activeQuiz=null,quizConfig=null;
let lastVideoSave=0,pendingSeek=null;
const filters={library:{group:'All topics',search:''},practice:{group:'All topics',search:''}};

function selectCourse(id){
  if(activeCourse===id)return;
  activeCourse=id;
  for(const view of ['library','practice'])filters[view]={group:'All topics',search:''};
}
function updateChrome(section='library'){
  const inCourse=section==='library'||section==='practice';
  document.querySelector('.course-context').hidden=!inCourse;
  document.querySelector('nav[aria-label="Subject navigation"]').hidden=!inCourse;
  document.querySelector('.subjects-link').hidden=inCourse;
  const course=catalog.courses.find(c=>c.id===activeCourse);
  const current=document.querySelector('#current-subject');
  current.textContent=`${course.code} · ${course.title}`;current.href=libraryUrl();
  document.querySelector('[data-nav="library"]').href=libraryUrl();
  document.querySelector('[data-nav="practice"]').href=`#/practice?course=${activeCourse}`;
  const examBank=document.querySelector('[data-nav="exam-bank"]');
  examBank.hidden=activeCourse!=='sc2203';
  examBank.href='#/exam-bank';
  document.querySelectorAll('[data-nav]').forEach(a=>{const active=a.dataset.nav===section;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
  const answered=Object.keys(progress.read().answers).filter(id=>questionTopic?.has(Number(id))).length;
  document.querySelector('#nav-progress').setAttribute('aria-label',`Your progress, ${answered} of ${totalQuestions()} questions answered`);
  document.querySelector('#storage-status').textContent=progress.persistent?'Progress saves in this browser.':'Storage is unavailable. Progress lasts for this tab only.';
  document.querySelectorAll('[data-progress]').forEach(el=>el.style.setProperty('--progress',`${Math.max(0,Math.min(100,Number(el.dataset.progress)||0))}%`));
}
function breadcrumbs(items){return `<div class="breadcrumbs">${items.map(([name,url])=>url?`<a href="${url}">${escape(name)}</a>`:`<span>${escape(name)}</span>`).join(icon('chevron'))}</div>`;}
function pageError(title,message){main.innerHTML=`<div class="wrap error-page"><h1>${escape(title)}</h1><p>${escape(message)}</p><a class="button" href="#/">Back to subjects ${icon('arrow')}</a></div>`;}
function tools(view){const f=filters[view];return `<div class="library-tools"><div class="filters" role="group" aria-label="Filter by topic">${courseGroups().map(group=>`<button class="filter" data-action="group" data-group="${escape(group)}" data-view="${view}" aria-pressed="${group===f.group}">${escape(group)}</button>`).join('')}</div><label class="search">${icon('search')}<span class="sr-only">Search ${view==='library'?'lessons':'topics'}</span><input id="search" type="search" placeholder="Search ${view==='library'?'lessons':'topics'}" value="${escape(f.search)}" data-view="${view}" autocomplete="off"></label></div>`;}
function filtered(items,view){const f=filters[view];const term=f.search.toLowerCase().trim();return items.filter(item=>(f.group==='All topics'||item.group===f.group)&&`${item.title} ${item.description||''} ${item.group}`.toLowerCase().includes(term));}

function thumbnail(lesson){
  if(lesson.courseId!=='sc2001')return `<img class="lesson-poster" src="${lesson.poster}" alt="" loading="lazy">`;
  const stroke='#527561',base='#d7e1d4',ink='#36523f';
  let drawing;
  if(lesson.group==='Sorting'){
    const values=lesson.slug==='merge-sort'?[2,4,7,1,3,6]:lesson.slug==='radix-sort'?[3,2,6,4,7,5]:[6,3,5,2,7,4];
    drawing=values.map((v,i)=>`<rect x="${35+i*36}" y="${135-v*12}" width="25" height="${v*12}" rx="5" fill="${i<2?stroke:base}"/><text x="${47.5+i*36}" y="155" text-anchor="middle" font-size="12" fill="${ink}">${v}</text>`).join('');
    if(lesson.slug==='merge-sort')drawing+='<path d="M51 35h68m32 0h68" fill="none" stroke="#a0af9c" stroke-width="1.5"/>';
  }else if(lesson.group==='Heaps'){
    const nodes=[[150,35,'2'],[90,85,'5'],[210,85,'3'],[55,135,'9'],[125,135,'7'],[180,135,'8']];
    drawing='<path d="m150 35-60 50m60-50 60 50M90 85l-35 50m35-50 35 50m85-50-30 50" stroke="#a8b8a3" stroke-width="1.7" fill="none"/>';
    drawing+=nodes.map(([x,y,n],i)=>`<circle cx="${x}" cy="${y}" r="17" fill="${i===0?stroke:'#e0e8dc'}"/><text x="${x}" y="${y+4}" text-anchor="middle" font-size="12" fill="${i===0?'white':ink}">${n}</text>`).join('');
  }else{
    const nodes=[[43,88,'A'],[116,37,'B'],[116,137,'C'],[206,37,'D'],[258,100,'E']];
    drawing='<path d="m43 88 73-51h90l52 63-142 37L43 88m73-51v100m0 0 90-100" stroke="#a8b6a4" fill="none" stroke-width="1.5"/>';
    const selected=lesson.group==='Spanning trees'?'M43 88 116 37h90l52 63':lesson.group==='Shortest paths'?'M43 88 116 137l90-100 52 63':'M43 88 116 37m-73 51 73 49';
    drawing+=`<path d="${selected}" stroke="${stroke}" fill="none" stroke-width="2.8"/>`;
    drawing+=nodes.map(([x,y,n],i)=>`<circle cx="${x}" cy="${y}" r="14" fill="${i===0?stroke:'#e0e7db'}"/><text x="${x}" y="${y+4}" text-anchor="middle" font-size="11" fill="${i===0?'white':ink}">${n}</text>`).join('');
  }
  return `<svg viewBox="0 0 300 185" aria-hidden="true">${drawing}</svg>`;
}
function lessonCard(lesson){
  const saved=progress.read().videos[lesson.slug];
  const count=lesson.topicIds.reduce((n,id)=>n+topics.get(id).qs.length,0);
  return `<article class="lesson-card"><a class="lesson-image" href="#/lesson/${lesson.slug}" aria-label="Watch ${escape(lesson.title)}, ${clock(lesson.duration)}">${thumbnail(lesson)}<span class="lesson-length">${clock(lesson.duration)}</span><span class="play-overlay">${icon('play')}</span>${saved?.time?`<span class="video-progress" data-progress="${saved.completed?100:saved.time/lesson.duration*100}"></span>`:''}</a><div class="lesson-meta"><span>${escape(lesson.periodLabel||`Week ${lesson.week}`)}</span><span aria-hidden="true">·</span><span>${escape(lesson.group)}</span></div><h3><a href="#/lesson/${lesson.slug}">${escape(lesson.title)}</a></h3><p>${escape(lesson.description)}</p><div class="card-foot"><span class="${saved?.completed?'card-watched':''}">${saved?.completed?'Watched':count?`${count} practice questions`:'Video lesson'}</span><a href="${count?`#/quiz/lesson/${lesson.slug}`:`#/lesson/${lesson.slug}`}">${count?'Practise':'Watch'} ${icon('arrow')}</a></div></article>`;
}
function subjectArtwork(id){
  if(id==='sc2001')return `<svg viewBox="0 0 440 180" aria-hidden="true"><path class="diagram-guide" d="M64 150h312"/>${[44,72,60,104,88,124].map((h,i)=>`<rect class="diagram-bar ${i<2?'sorted':''}" x="${77+i*48}" y="${150-h}" width="32" height="${h}" rx="7"/>`).join('')}<path class="diagram-direction" d="M87 18h52m-7-6 7 6-7 6"/></svg>`;
  if(id==='sc2203')return `<svg viewBox="0 0 440 180" aria-hidden="true"><path class="diagram-flow" d="M55 90h30m-7-6 7 6-7 6M140 90h60m-7-6 7 6-7 6M255 90h60m-7-6 7 6-7 6"/><circle class="diagram-state" cx="112" cy="90" r="28"/><circle class="diagram-state" cx="227" cy="90" r="28"/><circle class="diagram-state running" cx="342" cy="90" r="28"/><circle cx="342" cy="90" r="22" fill="none" stroke="#fff"/><text x="112" y="95">q₀</text><text x="227" y="95">q₁</text><text class="running-label" x="342" y="95">q₂</text><text x="170" y="76">0</text><text x="285" y="76">1</text></svg>`;
  return `<svg viewBox="0 0 440 180" aria-hidden="true"><path class="diagram-flow" d="M133 84h44m-7-6 7 6-7 6M265 84h44m-7-6 7 6-7 6M353 113v36H89v-36"/><rect class="diagram-state" x="45" y="55" width="88" height="58" rx="14"/><rect class="diagram-state running" x="177" y="55" width="88" height="58" rx="14"/><rect class="diagram-state" x="309" y="55" width="88" height="58" rx="14"/><text x="89" y="89">Ready</text><text class="running-label" x="221" y="89">Running</text><text x="353" y="89">Waiting</text></svg>`;
}
function renderSubjects(){
  document.title='Your subjects — Malfoid';
  main.innerHTML=`<div class="wrap subjects-home"><div class="subjects-welcome"><div class="subjects-intro"><h1>A little clearer.<br><span>One subject at a time.</span></h1><p>Choose what you’re learning. We’ll take it from there.</p></div><div class="home-tutor"><button class="malfoid-reaction" type="button" data-action="fluster-malfoid" aria-label="Fluster Malfoid" aria-pressed="false" title="Hover or tap to fluster Malfoid"><span class="malfoid-pose malfoid-smug" aria-hidden="true"></span><span class="malfoid-pose malfoid-flustered" aria-hidden="true"></span></button><blockquote class="home-malfoid-dialogue" aria-live="polite"><span class="dialogue-speaker">Malfoid</span><p></p></blockquote><p>Your tutor, Malfoid.</p></div></div><section class="subject-grid" aria-label="Your subjects">${catalog.courses.map(course=>{
    const list=catalog.lessons.filter(l=>l.courseId===course.id),practice=list.some(l=>l.topicIds.length);
    return `<a class="subject-panel subject-${course.id}" href="#/course/${course.id}" aria-label="Open ${course.code} ${escape(course.title)}"><div class="subject-copy"><h2>${escape(course.title)}</h2><p class="subject-code">${course.code} · ${escape(course.periodLabel)}</p><p class="subject-description">${escape(course.description)}</p></div><div class="subject-art">${subjectArtwork(course.id)}</div><div class="subject-panel-foot"><span>${list.length} video lessons${practice?` · ${courseQuestionCount()} practice questions`:' · Worked examples'}</span><span class="subject-open">Explore subject ${icon('arrow')}</span></div></a>`;
  }).join('')}</section></div>`;
  const malfoid=document.querySelector('.malfoid-reaction');
  const dialogue=document.querySelector('.home-malfoid-dialogue p');
  const chooseDialogue=()=>{
    const current=dialogue.textContent;
    const choices=homeMalfoidDialogue.filter(line=>line!==current);
    dialogue.textContent=choices[Math.floor(Math.random()*choices.length)];
    malfoid.classList.add('dialogue-visible');
  };
  malfoid.addEventListener('mouseenter',chooseDialogue);
  malfoid.addEventListener('focus',chooseDialogue);
  malfoid.addEventListener('mouseleave',()=>{
    if(document.activeElement!==malfoid)malfoid.classList.remove('dialogue-visible');
  });
  malfoid.addEventListener('blur',()=>{
    if(!malfoid.matches(':hover'))malfoid.classList.remove('dialogue-visible');
  });
  updateChrome('subjects');
}
function renderLibrary(){
  const saved=progress.read();const last=lessons.get(saved.lastLesson);const recent=last?.courseId===activeCourse?last:null;const course=currentCourse(),practice=hasPractice();
  main.innerHTML=`<div class="wrap"><section class="hero" aria-labelledby="hero-title"><div class="hero-copy"><h1 id="hero-title">${escape(course.title)}.<br><span>A little clearer.</span></h1><p>Your complete Malfoid explanations.<br>${escape(course.libraryIntro)}</p><div class="actions"><a class="button" href="#lessons" data-action="explore">Explore lessons ${icon('arrow')}</a>${practice?`<a class="button text" href="#/practice?course=${activeCourse}">Jump into practice ${icon('arrow')}</a>`:''}</div><div class="hero-facts"><span>${icon('book')}${courseLessons().length} full lessons</span><span>${icon('check')}${practice?`${courseQuestionCount()} practice questions`:'Captions & source notes'}</span></div></div><div class="hero-art" aria-label="Malfoid, your study tutor"><p class="hero-art-note">A good explanation<br>makes all the difference.</p><img class="hero-portrait" src="/assets/malfoid.webp" width="1254" height="1254" alt="Malfoid, your study tutor" fetchpriority="high"><blockquote class="sort-demo malfoid-dialogue" aria-label="Malfoid says"><span class="dialogue-speaker">Malfoid</span><p>${escape(malfoidDialogue[activeCourse])}</p></blockquote></div></section><section id="lessons" class="library-section" aria-labelledby="library-title">${recent&&saved.videos[recent.slug]?.time>0&&!saved.videos[recent.slug]?.completed?`<div class="resume-banner">${icon('play')}<div><strong>Pick up where you left off.</strong><p>${escape(recent.title)} · ${clock(saved.videos[recent.slug].time)} of ${clock(recent.duration)}</p></div><a href="#/lesson/${recent.slug}">Continue ${icon('arrow')}</a></div>`:''}<div class="section-heading"><h2 id="library-title">Your lesson library.</h2><p id="result-count">${courseLessons().length} lessons · ${escape(course.periodLabel)}</p></div>${tools('library')}<div class="lesson-grid" id="lesson-grid"></div></section></div>`;
  updateLibraryResults();updateChrome('library');
}
function updateLibraryResults(){const list=filtered(courseLessons(),'library');document.querySelector('#result-count').textContent=`${list.length} ${list.length===1?'lesson':'lessons'} · ${escape(currentCourse().periodLabel)}`;document.querySelector('#lesson-grid').innerHTML=list.length?list.map(lessonCard).join(''):`<div class="empty-state"><h2>No lessons found.</h2><p>Try another topic or a shorter search.</p><button class="button secondary" data-action="clear-search" data-view="library">Clear filters</button></div>`;updateChrome('library');}
function topicRow(topic){const a=progress.read().answers;const done=topic.qs.filter(q=>a[q.id]).length;const correct=topic.qs.filter(q=>a[q.id]?.correct).length;const written=topic.openEnded?.length?`<details class="written-practice"><summary>Written practice · ${topic.openEnded.length} questions</summary><ol>${topic.openEnded.map(item=>`<li><p>${escape(item.prompt)}</p><details><summary>Reveal marking points</summary><p>${escape(item.key)}</p></details></li>`).join('')}</ol></details>`:'';return `<article class="topic-row"><div><h2><a href="#/quiz/topic/${topic.id}">${escape(topic.title)}</a></h2><p>${escape(topic.group)} · ${topic.qs.length} questions · Easy, medium, hard & Baka</p>${written}</div><div class="row-side"><span>${done?`${correct}/${topic.qs.length} correct`:'Not started'}</span><a class="row-link" href="#/quiz/topic/${topic.id}">${done?'Continue':'Practise'} ${icon('arrow')}</a></div></article>`;}
function renderPractice(){
  if(!hasPractice()){
    main.innerHTML=`<div class="wrap"><div class="page-intro"><h1>${escape(currentCourse().code)} practice.</h1><p>A question bank has not been added for this course yet. Review the worked explanations and exam reminders in your ${courseLessons().length} video lessons.</p><a class="button" href="${libraryUrl()}">Browse ${escape(currentCourse().code)} lessons ${icon('arrow')}</a></div></div>`;
    updateChrome('practice');return;
  }
  main.innerHTML=`<div class="wrap"><div class="page-intro"><h1>Make it stick.</h1><p>Trace the next step. Spot the edge. Test what you know.<br>Five easy, five medium, five hard, and one extremely difficult Baka question per topic, plus written practice prompts.</p></div>${tools('practice')}<div class="practice-list" id="practice-list"></div></div>`;updatePracticeResults();updateChrome('practice');
}
function updatePracticeResults(){const list=filtered(courseTopics(),'practice');document.querySelector('#practice-list').innerHTML=list.length?list.map(topicRow).join(''):`<div class="empty-state"><h2>No matching topics.</h2><p>Try another search, or browse all ${courseTopics().length} topics.</p><button class="button secondary" data-action="clear-search" data-view="practice">Clear filters</button></div>`;}

function inlineExamMarkdown(value){return escape(value).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');}
function examMarkdown(text){
  const blocks=[];let list=null;
  const closeList=()=>{if(list){blocks.push(`</${list}>`);list=null;}};
  for(const line of text.replace(/\r/g,'').split('\n')){
    if(!line.trim()){closeList();continue;}
    let match=line.match(/^(#{1,3})\s+(.+)$/);
    if(match){closeList();blocks.push(`<h${match[1].length}>${inlineExamMarkdown(match[2])}</h${match[1].length}>`);continue;}
    if(/^---+$/.test(line.trim())){closeList();blocks.push('<hr>');continue;}
    match=line.match(/^[-*]\s+(.+)$/);
    if(match){if(list!=='ul'){closeList();list='ul';blocks.push('<ul>');}blocks.push(`<li>${inlineExamMarkdown(match[1])}</li>`);continue;}
    match=line.match(/^\d+\.\s+(.+)$/);
    if(match){if(list!=='ol'){closeList();list='ol';blocks.push('<ol>');}blocks.push(`<li>${inlineExamMarkdown(match[1])}</li>`);continue;}
    closeList();blocks.push(`<p>${inlineExamMarkdown(line)}</p>`);
  }
  closeList();return blocks.join('');
}
async function renderExamBank(){
  selectCourse('sc2203');document.title='SC2203 exam bank — Malfoid';
  main.innerHTML=`<div class="wrap exam-bank-page"><div class="page-intro">${breadcrumbs([['SC2203 library','#/course/sc2203'],['Exam bank',null]])}<h1>SC2203 exam bank.</h1><p>176 MCQs and 44 open-ended questions across the supplied Automata, Computability and Complexity material. Use the interactive practice bank for scored quizzes, then come here for the full exam-style set and construction prompts.</p><div class="actions"><a class="button secondary" href="#/practice?course=sc2203">Interactive practice ${icon('arrow')}</a><a class="button text" href="/sc2203-exam-question-bank.md" download>Download Markdown ${icon('download')}</a></div></div><article class="exam-bank-copy" aria-label="SC2203 exam question bank"><p class="loading">Loading the question bank…</p></article></div>`;
  updateChrome('exam-bank');
  try{
    const response=await fetch('/sc2203-exam-question-bank.md');if(!response.ok)throw Error('Unavailable');
    document.querySelector('.exam-bank-copy').innerHTML=examMarkdown(await response.text());
  }catch{document.querySelector('.exam-bank-copy').innerHTML='<p class="empty-state">The exam bank could not be loaded. Use the download link to try again.</p>';}
}

function saveVideo(){const video=document.querySelector('video');if(!video||!video.dataset.slug)return;const duration=Number.isFinite(video.duration)?video.duration:lessons.get(video.dataset.slug).duration;progress.video(video.dataset.slug,video.currentTime,duration,video.ended);lastVideoSave=video.currentTime;updateChrome('library');}
function renderLesson(slug){
  const lesson=lessons.get(slug);if(!lesson){pageError('Lesson not found.','Choose a lesson from the library.');return;}
  selectCourse(lesson.courseId);
  document.title=`${lesson.title} — Malfoid`;
  const watched=progress.read().videos[slug]?.completed;
  const sequence=courseLessons(),next=sequence[sequence.indexOf(lesson)+1];
  const sourceNote=lesson.source.summary?`${escape(lesson.source.summary)} <a href="${lesson.source.map}" target="_blank" rel="noopener">Read source notes ↗</a>`:`${escape(lesson.source.deck.replaceAll('_',' '))}, physical pages ${escape(lesson.source.pages.join(', '))}.<br>Recording: ${escape(lesson.source.recording)}.`;
  const count=lesson.topicIds.reduce((n,id)=>n+topics.get(id).qs.length,0);
  main.innerHTML=`<div class="wrap lesson-view"><div class="page-intro">${breadcrumbs([['Library',libraryUrl()],[lesson.group,null]])}<div class="lesson-title-row"><div><h1>${escape(lesson.title)}</h1><p>${escape(lesson.description)}</p></div>${count?`<a class="button secondary" href="#/quiz/lesson/${slug}">Practise this lesson ${icon('arrow')}</a>`:''}</div><div class="lesson-meta-large"><span>${escape(lesson.periodLabel||`Week ${lesson.week}`)}</span><span>${clock(lesson.duration)} min</span><span>Complete explanation</span></div></div><div class="player-layout"><div><div class="video-stage"><video controls playsinline preload="metadata" poster="${lesson.poster}" data-slug="${slug}" aria-label="${escape(lesson.title)} full explanation"><source src="${lesson.video}" type="video/mp4">${lesson.captions?`<track kind="captions" src="${lesson.captions}" srclang="en" label="English">`:''}Your browser does not support this video. <a href="${lesson.video}">Open the video file</a>.</video></div><div class="player-tools"><button class="plain-button" data-action="watched" aria-pressed="${!!watched}">${icon('check')}<span>${watched?'Marked as watched':'Mark as watched'}</span></button><a href="${lesson.video}" download>${icon('download')} Video</a>${lesson.narration?`<a href="${lesson.narration}" download>Narration</a><a href="${lesson.captions}" download>Captions</a>`:''}</div><details class="transcript-panel"><summary>Read the explanation</summary>${lesson.transcript.length?lesson.transcript.map(beat=>`<div class="transcript-row"><button data-action="seek" data-time="${beat.start}" aria-label="Play from ${clock(beat.start)}">${clock(beat.start)}</button><p>${escape(beat.text)}</p></div>`).join(''):'<p>The transcript is unavailable for this lesson. Use the video captions instead.</p>'}</details><p class="source-note"><strong>From your course material.</strong> ${sourceNote}</p></div><aside class="chapter-panel"><h2>In this lesson</h2>${lesson.chapters.map((chapter,i)=>`<button class="chapter-button ${i===0?'active':''}" data-action="seek" data-time="${chapter.time}"><time>${clock(chapter.time)}</time><span>${escape(chapter.title)}</span></button>`).join('')}${count?`<div class="lesson-practice"><h2>Now, your turn.</h2><p>Put the explanation to work with ${count} questions, from the first step to the trickier details.</p><a class="button" href="#/quiz/lesson/${slug}">Practise this lesson ${icon('arrow')}</a><div class="related-topics">${lesson.topicIds.map(id=>`<a href="#/quiz/topic/${id}">${escape(topics.get(id).title)}</a>`).join('')}</div></div>`:`<div class="lesson-practice"><h2>Keep learning.</h2>${next?`<p>Next: ${escape(next.title)}</p><a class="button" href="#/lesson/${next.slug}">Next lesson ${icon('arrow')}</a>`:`<p>You’ve reached the end of this course’s videos.</p>`}<p><a href="${libraryUrl()}">All ${escape(currentCourse().code)} lessons</a></p></div>`}</aside></div></div>`;
  const video=document.querySelector('video');lastVideoSave=0;pendingSeek=null;
  video.addEventListener('loadedmetadata',()=>{const saved=progress.read().videos[slug];const at=pendingSeek??(saved?.time<video.duration-2?saved.time:0);if(Number.isFinite(at)&&at>0)video.currentTime=Math.min(at,video.duration);});
  video.addEventListener('timeupdate',()=>{if(Math.abs(video.currentTime-lastVideoSave)>=5)saveVideo();let active=lesson.chapters[0];for(const ch of lesson.chapters)if(ch.time<=video.currentTime)active=ch;document.querySelectorAll('.chapter-button').forEach(b=>b.classList.toggle('active',Number(b.dataset.time)===active.time));});
  video.addEventListener('pause',saveVideo);video.addEventListener('ended',()=>{saveVideo();document.querySelector('[data-action="watched"]').setAttribute('aria-pressed','true');document.querySelector('[data-action="watched"] span').textContent='Marked as watched';});
  video.addEventListener('error',()=>{if(!document.querySelector('.video-error'))document.querySelector('.video-stage').insertAdjacentHTML('beforeend',`<div class="video-error" role="alert">This video could not load. Check that the original lesson files are still in this workspace, then refresh. <a href="${lesson.video}">Try opening the video directly</a>.</div>`);});
  updateChrome('library');
}

function graph(g){
  const nodes=g.nodes;const convert=([x,y])=>`${x.toFixed(2)},${(145-y).toFixed(2)}`;
  const paths=g.edges.map(([u,v,weight,curve,labelT=.5])=>{
    const a=nodes[u],b=nodes[v],dx=b[0]-a[0],dy=b[1]-a[1],len=Math.hypot(dx,dy),ux=dx/len,uy=dy/len,r=11;
    const start=[a[0]+r*ux,a[1]+r*uy],end=[b[0]-r*ux,b[1]-r*uy];
    let path=`M${convert(start)} L${convert(end)}`,mid=[start[0]+labelT*(end[0]-start[0]),start[1]+labelT*(end[1]-start[1])];
    if(curve){const c1=[start[0]+dx/3-uy*curve,start[1]+dy/3+ux*curve],c2=[end[0]-dx/3-uy*curve,end[1]-dy/3+ux*curve];path=`M${convert(start)} C${convert(c1)} ${convert(c2)} ${convert(end)}`;mid=[0,1].map(k=>(1-labelT)**3*start[k]+3*(1-labelT)**2*labelT*c1[k]+3*(1-labelT)*labelT**2*c2[k]+labelT**3*end[k]);}
    return `<path d="${path}" fill="none" stroke="#6e8272" stroke-width="1.6" ${g.directed?'marker-end="url(#arrowhead)"':''}/>${weight!==null?`<text class="edge-weight" x="${mid[0]}" y="${149-mid[1]}" text-anchor="middle">${weight}</text>`:''}`;
  }).join('');
  const vertices=Object.entries(nodes).map(([name,[x,y]])=>`<circle cx="${x}" cy="${145-y}" r="11" fill="#e2ece1" stroke="#52765b" stroke-width="1.2"/><text x="${x}" y="${149-y}" text-anchor="middle" font-size="11" font-weight="600">${escape(name)}</text>`).join('');
  return `<svg class="graph" viewBox="0 -10 420 175" role="img" aria-label="${g.directed?'Directed':'Undirected'} graph. Complete edge list follows."><defs><marker id="arrowhead" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0 0 7 3 0 6z" fill="#6e8272"/></marker></defs>${paths}${vertices}</svg><p class="edge-list">Edges: ${g.edges.map(([u,v,w])=>`${u}${g.directed?' → ':'–'}${v}${w!==null?` (${w})`:''}`).join(', ')}</p>`;
}
function quizQuestions(config){const ts=config.kind==='topic'?[topics.get(Number(config.id))]:lessons.get(config.id)?.topicIds.map(id=>topics.get(id));return(ts||[]).filter(Boolean).flatMap(t=>t.qs).filter(q=>config.level==='All'||q.difficulty===config.level);}
function openQuiz(kind,id,level='All'){
  quizConfig={kind,id,level:['All',...difficulties].includes(level)?level:'All'};
  const questions=quizQuestions(quizConfig);
  if(!questions.length){pageError('Quiz not found.','Pick a topic from the practice library.');return;}
  quizConfig.key=`${catalog.bankVersion||'original'}:${kind}-${id}:${quizConfig.level}`;
  activeQuiz=createQuiz(questions,progress.read().sessions[quizConfig.key]||{});
  renderQuiz();
}
function saveQuiz(){if(activeQuiz&&quizConfig)progress.saveQuiz(quizConfig.key,activeQuiz.snapshot());updateChrome('practice');}
function quizTitle(){return quizConfig.kind==='topic'?topics.get(Number(quizConfig.id)).title:lessons.get(quizConfig.id).title;}
function questionSetup(q){const topic=questionTopic.get(q.id);return {context:q.context??topic.context,graph:Object.hasOwn(q,'graph')?q.graph:topic.graph};}
function renderQuiz(focus){
  const state=activeQuiz.state();document.title=`${quizTitle()} practice — Malfoid`;
  if(state.finished){renderResult();return;}
  const q=state.question,topic=questionTopic.get(q.id),right='ABCD'.indexOf(q.answer);
  const setup=questionSetup(q);
  const answerMarkup=q.options.map((option,i)=>{
    const cls=state.checked?(i===right?'correct':i===state.selected?'incorrect':''):i===state.selected?'selected':'';
    return `<button class="option ${cls}" data-action="choose" data-choice="${i}" aria-pressed="${i===state.selected}" ${state.checked?'disabled':''}><span class="option-letter">${'ABCD'[i]}</span><span>${escape(option)}</span>${state.checked&&(i===right||i===state.selected)?icon(i===right?'check':'x','option-status'):''}</button>`;
  }).join('');
  main.innerHTML=`<div class="wrap"><div class="quiz-top">${breadcrumbs([['Practice','#/practice'],[quizTitle(),null]])}<div class="quiz-title-line"><h1>${escape(quizTitle())}</h1><div class="filters" role="group" aria-label="Question difficulty">${['All',...difficulties].map(level=>`<button class="filter" data-action="difficulty" data-level="${level}" aria-pressed="${quizConfig.level===level}">${level==='All'?'All levels':level}</button>`).join('')}</div></div><div class="quiz-meta"><span>Question ${state.index+1} of ${state.total}</span><span>${state.score} correct so far</span></div><div class="quiz-progress" role="progressbar" aria-label="Questions completed" aria-valuemin="0" aria-valuemax="${state.total}" aria-valuenow="${Object.keys(state.answers).length}"><span data-progress="${Object.keys(state.answers).length/state.total*100}"></span></div></div><div class="quiz-layout"><aside class="quiz-setup"><h2>The setup</h2><p>${escape(setup.context)}</p>${setup.graph?graph(setup.graph):''}<a class="setup-link" href="#/lesson/${topic.lessonSlug}">${icon('play')}Revisit the explanation</a></aside><section class="quiz-body" aria-labelledby="question-title"><div class="question-label"><span>Q${String(q.id).padStart(2,'0')}</span><span class="difficulty ${q.difficulty.toLowerCase()}">${q.difficulty}</span><span>${quizConfig.kind==='lesson'?escape(topic.title):''}</span></div><h2 class="question-stem" id="question-title">${escape(q.stem)}</h2><fieldset class="options"><legend class="sr-only">Select one answer</legend>${answerMarkup}</fieldset>${state.checked?`<div class="feedback ${state.selected===right?'':'wrong'}" role="status"><h3>${state.selected===right?'Exactly right.':'Let’s work through it.'}</h3><p>${escape(q.why)}</p><details><summary>Course reference</summary><p>${escape(topic.source)}</p></details></div>`:''}<div class="question-actions"><span class="keyboard-hint">Keys 1–4 to choose · Enter to continue</span><button class="button" data-action="${state.checked?'next':'check'}" ${state.selected===null?'disabled':''}>${state.checked?(state.index===state.total-1?'See results':'Next question'):'Check answer'} ${icon('arrow')}</button></div></section></div></div>`;
  updateChrome('practice');if(focus)document.querySelector(focus)?.focus({preventScroll:true});
}
function renderResult(){
  const state=activeQuiz.state(),allCorrect=state.score===state.total;
  main.innerHTML=`<div class="wrap result-wrap">${breadcrumbs([['Practice','#/practice'],[quizTitle(),null]])}<section class="quiz-result"><h1>${allCorrect?'Beautifully done.':'A little clearer already.'}</h1><p class="result-description">${allCorrect?'Every answer, understood. Come back later to see what stays with you.':'The tricky steps are where the learning happens. Give the missed questions another look.'}</p><div class="result-score"><strong>${state.score}</strong><span>of ${state.total} correct</span></div><div class="actions">${state.missedIds.length?`<button class="button" data-action="retry-missed">Retry ${state.missedIds.length} missed ${icon('repeat')}</button>`:''}<button class="button ${allCorrect?'':'secondary'}" data-action="restart">Try all again ${icon('repeat')}</button><a class="button text" href="#/practice">More topics ${icon('arrow')}</a></div><div class="result-review"><h2>Review your answers</h2>${state.questions.map(q=>{const correct=state.answers[q.id]==='ABCD'.indexOf(q.answer),setup=questionSetup(q);return `<details><summary><span class="result-dot ${correct?'':'wrong'}"></span><span>${escape(questionTopic.get(q.id).title)} · ${q.difficulty}</span><span>${correct?'Correct':'Review'} +</span></summary><div class="result-answer"><p class="review-context">${escape(setup.context)}</p>${setup.graph?graph(setup.graph):''}<p>${escape(q.stem)}</p><p>Your answer: ${escape(q.options[state.answers[q.id]])}</p><b>Correct answer: ${escape(q.correct)}</b><p>${escape(q.why)}</p></div></details>`;}).join('')}</div></section></div>`;updateChrome('practice');
}
function renderProgress(){
  const saved=progress.read(),answered=catalog.topics.flatMap(t=>t.qs).filter(q=>saved.answers[q.id]);const correct=answered.filter(q=>saved.answers[q.id].correct).length;const watched=catalog.lessons.filter(l=>saved.videos[l.slug]?.completed).length;
  const review=catalog.topics.filter(t=>t.qs.some(q=>saved.answers[q.id]&&!saved.answers[q.id].correct));
  const started=catalog.lessons.filter(l=>saved.videos[l.slug]?.time>0||saved.videos[l.slug]?.completed);
  main.innerHTML=`<div class="wrap"><div class="page-intro"><h1>Your progress.</h1><p>A record of what you’ve watched, practised, and understood.<br>Saved on this browser, ready when you are.</p></div><div class="progress-summary"><div><strong>${watched} / ${catalog.lessons.length}</strong><span>lessons watched</span></div><div><strong>${answered.length} / ${totalQuestions()}</strong><span>questions answered</span></div><div><strong>${correct}</strong><span>latest answers correct</span></div></div><section class="progress-section"><h2>${review.length?'Worth another look.':'Questions to revisit.'}</h2>${review.length?review.map(topicRow).join(''):`<div class="empty-state"><p>${answered.length?'No missed answers to revisit. Try another topic or a harder question.':'Your practice history will appear here. Start with a topic you’ve just watched.'}</p><a class="button secondary" href="#/practice">Choose a topic ${icon('arrow')}</a></div>`}</section>${started.length?`<section class="progress-section"><h2>Your recent lessons.</h2>${started.map(l=>`<article class="topic-row"><div><h2>${escape(l.title)}</h2><p>${saved.videos[l.slug].completed?'Watched':`${clock(saved.videos[l.slug].time)} of ${clock(l.duration)}`}</p></div><a class="row-link" href="#/lesson/${l.slug}">${saved.videos[l.slug].completed?'Watch again':'Continue'} ${icon('arrow')}</a></article>`).join('')}</section>`:''}</div>`;
  updateChrome(null);if(!progress.persistent)document.querySelector('.page-intro p').textContent='Your progress is available in this tab. Browser storage is blocked, so it will not survive a refresh.';
}
function route(){
  saveVideo();if(activeQuiz)saveQuiz();activeQuiz=null;quizConfig=null;
  document.title='Malfoid — A little clearer.';
  const url=new URL(location.hash.slice(1)||'/',location.origin);const parts=url.pathname.split('/').filter(Boolean);
  if(parts[0]==='course' && catalog.courses.some(c=>c.id===parts[1])){
    selectCourse(parts[1]);renderLibrary();
  }
  else if(!parts.length)renderSubjects();
  else if(parts[0]==='lesson')renderLesson(parts[1]);
  else if(parts[0]==='exam-bank'){renderExamBank();}
  else if(parts[0]==='practice'){selectCourse(catalog.courses.some(c=>c.id===url.searchParams.get('course'))?url.searchParams.get('course'):'sc2001');renderPractice();}
  else if(parts[0]==='quiz'){
    const quizKind=parts[1],quizId=parts[2];
    const quizLesson=quizKind==='lesson'?lessons.get(quizId):lessons.get(topics.get(Number(quizId))?.lessonSlug);
    selectCourse(quizLesson?.courseId||'sc2001');
    openQuiz(quizKind,quizId,url.searchParams.get('level')||'All');
  }
  else if(parts[0]==='progress')renderProgress();
  else pageError('Nothing here yet.','Choose a subject to keep studying.');
  window.scrollTo({top:0,behavior:'instant'});main.focus({preventScroll:true});
}

main.addEventListener('input',event=>{if(event.target.id!=='search')return;const view=event.target.dataset.view;filters[view].search=event.target.value;if(view==='library')updateLibraryResults();else updatePracticeResults();});
main.addEventListener('click',event=>{
  const button=event.target.closest('[data-action]');if(!button||button.disabled)return;
  const action=button.dataset.action;
  if(action==='fluster-malfoid'){button.setAttribute('aria-pressed',String(button.getAttribute('aria-pressed')!=='true'));return;}
  if(action==='explore'){event.preventDefault();document.querySelector('#lessons').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});return;}
  if(action==='group'||action==='clear-search'){
    const view=button.dataset.view;filters[view].group=action==='group'?button.dataset.group:'All topics';if(action==='clear-search'){filters[view].search='';document.querySelector('#search').value='';}
    document.querySelectorAll('[data-action="group"]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.group===filters[view].group)));
    if(view==='library')updateLibraryResults();else updatePracticeResults();return;
  }
  if(action==='seek'){const video=document.querySelector('video');pendingSeek=Number(button.dataset.time);if(video.readyState>=1)video.currentTime=Math.min(pendingSeek,video.duration);video.play().catch(()=>{});return;}
  if(action==='watched'){const video=document.querySelector('video');progress.video(video.dataset.slug,video.currentTime,lessons.get(video.dataset.slug).duration,true);button.setAttribute('aria-pressed','true');button.querySelector('span').textContent='Marked as watched';updateChrome('library');return;}
  if(!activeQuiz)return;
  if(action==='difficulty'){saveQuiz();location.hash=`/quiz/${quizConfig.kind}/${quizConfig.id}${button.dataset.level==='All'?'':`?level=${button.dataset.level}`}`;return;}
  if(action==='choose'){activeQuiz.select(Number(button.dataset.choice));saveQuiz();renderQuiz(`[data-choice="${button.dataset.choice}"]`);return;}
  if(action==='check'){
    if(activeQuiz.submit()){const s=activeQuiz.state();progress.answer(s.question.id,s.selected==='ABCD'.indexOf(s.question.answer));saveQuiz();renderQuiz('[data-action="next"]');}return;
  }
  if(action==='next'){if(activeQuiz.next()){saveQuiz();renderQuiz();document.querySelector('#question-title')?.setAttribute('tabindex','-1');document.querySelector('#question-title')?.focus({preventScroll:true});}return;}
  if(action==='retry-missed'){const retry=activeQuiz.retryMissed();if(retry){activeQuiz=retry;saveQuiz();renderQuiz();window.scrollTo({top:0,behavior:'instant'});}return;}
  if(action==='restart'){activeQuiz=createQuiz(quizQuestions(quizConfig));saveQuiz();renderQuiz();window.scrollTo({top:0,behavior:'instant'});}
});
document.addEventListener('keydown',event=>{
  if(!activeQuiz||activeQuiz.state().finished||event.altKey||event.ctrlKey||event.metaKey||['INPUT','SELECT','TEXTAREA'].includes(event.target.tagName))return;
  if(/^[1-4]$/.test(event.key)&&!activeQuiz.state().checked){event.preventDefault();activeQuiz.select(Number(event.key)-1);saveQuiz();renderQuiz();main.focus({preventScroll:true});}
  if(event.key==='Enter'&&!['BUTTON','A','SUMMARY'].includes(event.target.tagName)){event.preventDefault();const button=document.querySelector(`[data-action="${activeQuiz.state().checked?'next':'check'}"]`);button?.click();}
});
document.querySelector('.skip-link').addEventListener('click',event=>{event.preventDefault();main.focus();main.scrollIntoView();});
window.addEventListener('hashchange',()=>{if(catalog)route();});
window.addEventListener('pagehide',()=>{saveVideo();saveQuiz();});
document.addEventListener('visibilitychange',()=>{if(document.hidden)saveVideo();});
try{
  const response=await fetch('/data/catalog.json');if(!response.ok)throw Error('Content unavailable');catalog=await response.json();lessons=new Map(catalog.lessons.map(l=>[l.slug,l]));topics=new Map(catalog.topics.map(t=>[t.id,t]));questionTopic=new Map(catalog.topics.flatMap(t=>t.qs.map(q=>[q.id,t])));route();
}catch{pageError('Your lessons couldn’t load.','Check that the local study server is running, then refresh this page. Your original lesson files have not been changed.');}

