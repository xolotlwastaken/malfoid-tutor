import {readFile,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

// Each exam topic is available from all lessons that teach its material.
const episodes=[[1,2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15],[16,17,18,19,20,24,25,26],[21,22,23,27],[28,29,30,31,32,33],[34,35,36],[37,38,39],[40,41,42,43,44],[45,46,47,48]];
const plain=text=>text.replace(/`([^`]+)`/g,'$1').trim();

/** Convert the authored exam bank into the same catalog interface as other subjects. */
export function importSc2203(catalog,markdown){
  const result=structuredClone(catalog);
  const previous=new Set(result.topics.filter(t=>t.courseId==='sc2203').map(t=>t.id));
  result.topics=result.topics.filter(t=>!previous.has(t.id));
  const lessons=result.lessons.filter(l=>l.courseId==='sc2203');
  for(const lesson of lessons)lesson.topicIds=lesson.topicIds.filter(id=>!previous.has(id));
  const sections=[...markdown.matchAll(/^## Topic (\d+) — (.+)\n([\s\S]*?)(?=^## |$(?![\s\S]))/gm)];
  if(sections.length!==11)throw Error('Expected eleven SC2203 exam topics');
  for(const [,number,title,body] of sections){
    const topicNumber=Number(number),id=500+topicNumber;
    const linked=episodes[topicNumber-1].map(episode=>{
      const lesson=lessons.find(l=>l.slug.startsWith(`sc2203-E${String(episode).padStart(2,'0')}-`));
      if(!lesson)throw Error(`Missing SC2203 episode ${episode}`);
      return lesson;
    });
    const context=`SC2203 · ${plain(title)}. Use the lecture definitions and state the assumptions behind each construction or proof.`;
    const source=`SC2203 supplied lecture slides and tutorials through Week 11; exam question bank, Topic ${number}: ${plain(title)}.`;
    const key=new Map([...body.match(/\*\*Answer key:\*\*([^\n]+)/)?.[1].matchAll(/(\d+)([ABCD])/g)||[]].map(([,n,answer])=>[Number(n),answer]));
    const qs=[...body.matchAll(/^(\d+)\. ([\s\S]*?)(?=^\d+\. |^### |^\*\*Answer key:)/gm)].map(([,n,text])=>{
      const localId=Number(n),parts=text.trim().split(/\s+[ABCD]\.\s+/);
      const stem=plain(parts.shift()),options=parts.map(plain),answer=key.get(localId);
      if(![2,4].includes(options.length)||!answer)throw Error(`Malformed SC2203 topic ${number} question ${n}`);
      // Rotate authored options: most source topics put every correct answer at A.
      const shift=(topicNumber+localId)%options.length;
      const correct=options['ABCD'.indexOf(answer)];
      const rotated=options.slice(shift).concat(options.slice(0,shift));
      return {id:1000+(topicNumber-1)*16+localId,difficulty:localId<=5?'Easy':localId<=10?'Medium':localId<=15?'Hard':'Baka',stem,options:rotated,answer:'ABCD'[rotated.indexOf(correct)],correct,why:correct,context,graph:null,source};
    });
    const openEnded=[...body.matchAll(/^- \*\*(Easy|Medium|Hard|Baka):\*\* (.+) \*\(Mark: (.+)\)\*$/gm)].map(([,difficulty,prompt,key])=>({id:`sc2203-written-${topicNumber}-${difficulty.toLowerCase()}`,type:'written',difficulty,stem:plain(prompt),prompt:`${difficulty}: ${plain(prompt)}`,key:plain(key)}));
    if(qs.length!==16||key.size!==16||openEnded.length!==4)throw Error(`Incomplete SC2203 topic ${number}`);
    if(result.topics.some(t=>t.id===id)||result.topics.some(t=>t.qs.some(q=>qs.some(added=>added.id===q.id))))throw Error(`SC2203 IDs collide for topic ${number}`);
    result.topics.push({id,courseId:'sc2203',title:plain(title),group:linked[0].group,lessonSlug:linked[0].slug,context,graph:null,source,qs,openEnded});
    for(const lesson of linked)lesson.topicIds.push(id);
  }
  return result;
}

if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  const catalogPath=new URL('../public/data/catalog.json',import.meta.url);
  const catalog=JSON.parse(await readFile(catalogPath,'utf8'));
  const markdown=await readFile(new URL('../../SC2203_exam_question_bank.md',import.meta.url),'utf8');
  await writeFile(catalogPath,JSON.stringify(importSc2203(catalog,markdown)));
  console.log('Imported 176 SC2203 interactive questions and 44 written prompts.');
}
