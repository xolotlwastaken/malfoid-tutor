import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
const catalog=JSON.parse(await readFile(new URL('../public/data/catalog.json',import.meta.url),'utf8'));
const legacy=JSON.parse(await readFile(new URL('./fixtures/legacy-catalog.json',import.meta.url),'utf8'));
test('SC2001 offers the complete approved later sequence with linked practice and honest sources',()=>{
 const lessons=catalog.lessons.filter(l=>l.courseId==='sc2001');
 assert.equal(lessons.length,49);
 assert.equal(catalog.courses.find(c=>c.id==='sc2001').periodLabel,'Weeks 1–13');
 const later=lessons.filter(l=>l.week>7);
 assert.equal(later.length,31);
 for(const lesson of later){
  assert.equal(lesson.topicIds.length,1);
  const topic=catalog.topics.find(t=>t.id===lesson.topicIds[0]);
  assert.equal(topic.lessonSlug,lesson.slug);assert.equal(topic.qs.length,13);
  assert.equal(lesson.source.recording,null);assert.ok(lesson.source.summary.includes('recordings unavailable'));
  assert.ok(lesson.narration&&lesson.captions&&lesson.source.map);
  assert.ok(lesson.chapters.length>=10&&lesson.transcript.length>=10);
  assert.ok(lesson.chapters.every(c=>c.time>=0&&c.time<lesson.duration));
 }
 assert.equal(catalog.topics.flatMap(t=>t.qs).length,953);
});

test('the expansion preserves every existing topic, question body and progress identifier',async()=>{
 const {createHash}=await import('node:crypto');
 const ordered=value=>Array.isArray(value)?value.map(ordered):value&&typeof value==='object'?Object.fromEntries(Object.keys(value).sort().map(k=>[k,ordered(value[k])])):value;
 const questions=new Map(catalog.topics.flatMap(t=>t.qs).map(q=>[q.id,q]));
 for(const [id,hash] of Object.entries(legacy.questions)){
  assert.ok(questions.has(Number(id)),`Question ${id} remains available`);
  assert.equal(createHash('sha256').update(JSON.stringify(ordered(questions.get(Number(id))))).digest('hex'),hash,`Question ${id} is unchanged`);
 }
 for(const [id,old] of Object.entries(legacy.topics)){
  const topic=catalog.topics.find(t=>t.id===Number(id));assert.ok(topic);
  assert.deepEqual({title:topic.title,lessonSlug:topic.lessonSlug,questionIds:topic.qs.map(q=>q.id)},old);
 }
 assert.ok(legacy.lessons.every(slug=>catalog.lessons.some(l=>l.slug===slug)));
});
