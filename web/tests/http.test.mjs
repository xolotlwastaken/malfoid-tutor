import test from 'node:test';
import assert from 'node:assert/strict';
import {once} from 'node:events';
import {studyServer} from '../server.mjs';

test('the app serves lessons and seekable video without exposing source files', async t => {
  const server=studyServer().listen(0,'127.0.0.1');await once(server,'listening');
  t.after(()=>new Promise(resolve=>server.close(resolve)));
  const base=`http://127.0.0.1:${server.address().port}`;
  const catalog=await (await fetch(base+'/data/catalog.json')).json();
  const examBank=await fetch(base+'/sc2203-exam-question-bank.md');
  assert.equal(examBank.status,200);
  assert.match(await examBank.text(),/## Topic 11 — SAT, 3SAT, Cook–Levin and NP-completeness/);
  assert.equal(catalog.lessons.length,107);
  assert.equal(catalog.lessons.filter(l=>l.courseId==='sc2001').length,18);
  const operatingSystems=catalog.lessons.filter(l=>l.courseId==='sc2005');
  assert.equal(operatingSystems.length,41);
  assert.equal(new Set(operatingSystems.map(l=>l.slug)).size,41);
  assert.deepEqual(catalog.courses.map(c=>c.id),['sc2001','sc2005','sc2203']);
  const automata=catalog.lessons.filter(l=>l.courseId==='sc2203');
  assert.equal(automata.length,48);
  assert.equal(automata[0].slug,'sc2203-E01-strings-languages');
  assert.match(automata.at(-1).slug,/sc2203-E48/);
  assert.equal(catalog.courses.find(c=>c.id==='sc2203').periodLabel,'Weeks 1–11');
  for(const lesson of automata){
    assert.equal(lesson.topicIds.length,0);
    assert.ok(lesson.transcript.length>=10);
    assert.ok(lesson.chapters.length>=3);
    assert.ok(lesson.chapters.every((c,i)=>c.time>=0&&c.time<lesson.duration&&(!i||c.time>lesson.chapters[i-1].time)));
    const video=await fetch(base+lesson.video,{headers:{Range:'bytes=0-63'}});
    assert.equal(video.status,206,lesson.slug);assert.equal((await video.arrayBuffer()).byteLength,64);
    for(const route of [lesson.poster,lesson.narration,lesson.source.map]){
      const response=await fetch(base+route,{method:'HEAD'});assert.equal(response.status,200,route);
    }
  }
  assert.equal(operatingSystems[0].slug,'sc2005-01-os-foundations');
  assert.equal(operatingSystems.at(-1).slug,'sc2005-L04-user-thread-context');
  const osRange=await fetch(base+operatingSystems[0].video,{headers:{Range:'bytes=0-1023'}});
  assert.equal(osRange.status,206);assert.equal((await osRange.arrayBuffer()).byteLength,1024);
  assert.equal(new Set(operatingSystems.flatMap(l=>l.topicIds)).size,10);
  assert.ok(operatingSystems.every(l=>l.transcript.length && l.chapters.length));
  for(const lesson of operatingSystems){
    const narration=await fetch(base+lesson.narration,{method:'HEAD'});
    assert.equal(narration.status,200);assert.equal(narration.headers.get('content-type'),'audio/wav');
    const sourceMap=await fetch(base+lesson.source.map);
    assert.equal(sourceMap.status,200);assert.ok((await sourceMap.text()).length>100);
    const poster=await fetch(base+lesson.poster,{method:'HEAD'});assert.equal(poster.status,200);
  }
  assert.equal(catalog.topics.flatMap(t=>t.qs).length,550);
  assert.equal(new Set(catalog.lessons.flatMap(l=>l.topicIds)).size,40);
  const range=await fetch(base+catalog.lessons[0].video,{headers:{Range:'bytes=0-1023'}});
  assert.equal(range.status,206);assert.equal((await range.arrayBuffer()).byteLength,1024);
  assert.match(range.headers.get('content-range'),/^bytes 0-1023\//);
  const suffix=await fetch(base+catalog.lessons[0].video,{headers:{Range:'bytes=-64'}});
  assert.equal(suffix.status,206);assert.equal((await suffix.arrayBuffer()).byteLength,64);
  const invalid=await fetch(base+catalog.lessons[0].video,{headers:{Range:'bytes=999999999999-'}});assert.equal(invalid.status,416);await invalid.text();
  const source=await fetch(base+'/server.mjs');assert.equal(source.status,404);await source.text();
  const traversal=await fetch(base+'/%2e%2e%2fmedia-manifest.json');assert.equal(traversal.status,403);await traversal.text();
  for(const lesson of catalog.lessons){
    const video=await fetch(base+lesson.video,{method:'HEAD'});assert.equal(video.status,200,lesson.slug);assert.equal(video.headers.get('content-type'),'video/mp4');
    if(lesson.captions){const captions=await fetch(base+lesson.captions);assert.ok((await captions.text()).startsWith('WEBVTT'));}
  }
});
