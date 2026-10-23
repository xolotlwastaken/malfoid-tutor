import test from 'node:test';
import assert from 'node:assert/strict';
import { createProgress } from '../public/progress.mjs';
const storage = () => { const values = new Map(); return {getItem:k=>values.get(k) ?? null,setItem:(k,v)=>values.set(k,v),removeItem:k=>values.delete(k)}; };
test('question answers and video position survive creating a new study session', () => {
  const disk = storage();
  const first = createProgress(disk);
  first.answer(4, true);
  first.video('merge-sort', 87, 213);
  first.saveQuiz('topic-2:All', {index:1,answers:{4:1}});
  const resumed = createProgress(disk).read();
  assert.equal(resumed.answers[4].correct, true);
  assert.equal(resumed.videos['merge-sort'].time, 87);
  assert.equal(resumed.lastLesson, 'merge-sort');
  assert.equal(resumed.sessions['topic-2:All'].index, 1);
});
test('unavailable or corrupt storage leaves study usable without claiming to save', () => {
  const inaccessible={getItem(){throw new Error('Blocked');},setItem(){throw new Error('Blocked');}};
  const progress=createProgress(inaccessible);
  assert.doesNotThrow(()=>progress.answer(4,true));
  assert.equal(progress.persistent, false);
  assert.equal(progress.read().answers[4].correct,true);
  const damaged=createProgress({getItem:()=>'{bad',setItem(){}});
  assert.deepEqual(damaged.read().answers,{});
});
test('replaying a lesson does not clear completion, and invalid saved shapes are recovered', () => {
  const disk=storage();const progress=createProgress(disk);
  progress.video('prim',480,481,true);progress.video('prim',10,481);
  assert.equal(progress.read().videos.prim.completed,true);
  const damaged=createProgress({getItem:()=>'{"version":1,"answers":null}',setItem(){}});
  assert.doesNotThrow(()=>damaged.answer(4,true));
});
