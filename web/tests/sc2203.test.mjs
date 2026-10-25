import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {importSc2203} from '../scripts/import_sc2203.mjs';
import {createQuiz} from '../public/quiz.mjs';

const catalog=JSON.parse(await readFile(new URL('../public/data/catalog.json',import.meta.url),'utf8'));
const markdown=await readFile(new URL('../../SC2203_exam_question_bank.md',import.meta.url),'utf8');
const topics=catalog.topics.filter(t=>t.courseId==='sc2203');

test('SC2203 practice includes the complete exam bank linked to relevant lessons',()=>{
  assert.equal(topics.length,11);
  assert.equal(topics.flatMap(t=>t.qs).length,176);
  assert.equal(topics.flatMap(t=>t.openEnded).length,44);
  for(const topic of topics){
    assert.equal(catalog.lessons.find(l=>l.slug===topic.lessonSlug).courseId,'sc2203');
    assert.deepEqual(['Easy','Medium','Hard','Baka'].map(level=>topic.qs.filter(q=>q.difficulty===level).length),[5,5,5,1]);
    assert.equal(topic.openEnded.length,4);
    for(const q of topic.qs){
      assert.ok([2,4].includes(q.options.length));
      assert.equal(q.options['ABCD'.indexOf(q.answer)],q.correct);
    }
  }
  for(const lesson of catalog.lessons.filter(l=>l.courseId==='sc2203')){
    assert.equal(lesson.topicIds.length,1);
    assert.ok(topics.some(t=>t.id===lesson.topicIds[0]));
  }
  assert.equal(topics[0].qs[10].correct,'have the same number of reachable states');
});

test('the authored bank can be imported repeatedly without changing existing progress IDs or other courses',()=>{
  assert.deepEqual(importSc2203(catalog,markdown),catalog);
});

test('SC2203 supports checked answers, resume, final scores and retry through the shared quiz',()=>{
  let quiz=createQuiz(topics[0].qs);
  for(let i=0;i<16;i++){
    const q=quiz.state().question;
    quiz.select(i===0?('ABCD'.indexOf(q.answer)+1)%q.options.length:'ABCD'.indexOf(q.answer));
    assert.equal(quiz.submit(),true);
    assert.equal(quiz.submit(),false);
    quiz.next();
    quiz=createQuiz(topics[0].qs,quiz.snapshot());
  }
  assert.equal(quiz.state().finished,true);
  assert.equal(quiz.state().score,15);
  const retry=quiz.retryMissed();
  assert.equal(retry.state().total,1);
  assert.equal(retry.state().question.id,1001);
  assert.equal(retry.state().checked,false);
});
