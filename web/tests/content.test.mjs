import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
const catalog=JSON.parse(await readFile(new URL('../public/data/catalog.json',import.meta.url),'utf8'));
test('every topic has its course question distribution and valid options across all four levels',()=>{
 assert.equal(catalog.topics.flatMap(t=>t.qs).length,1129);
 const examTopicIds=new Set(catalog.lessons.filter(l=>l.courseId!=='sc2001').flatMap(l=>l.topicIds));
 const ids=new Set();
 for(const topic of catalog.topics){
  const expected=examTopicIds.has(topic.id)?{Easy:5,Medium:5,Hard:5,Baka:1}:{Easy:4,Medium:4,Hard:4,Baka:1};
  assert.deepEqual(Object.fromEntries(['Easy','Medium','Hard','Baka'].map(level=>[level,topic.qs.filter(q=>q.difficulty===level).length])),expected,topic.title);
  for(const q of topic.qs){assert.ok(!ids.has(q.id));ids.add(q.id);assert.equal(new Set(q.options).size,q.options.length);assert.equal(q.options['ABCD'.indexOf(q.answer)],q.correct);if(q.id>90){assert.ok(q.context?.length>20);assert.ok(Object.hasOwn(q,'graph'));}}
 }
 for(let id=1;id<=90;id++)assert.ok(ids.has(id),'Original progress IDs are preserved');
});
