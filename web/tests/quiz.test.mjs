import test from 'node:test';
import assert from 'node:assert/strict';
import { createQuiz } from '../public/quiz.mjs';
const questions = [
  {id:4,options:['[7,3,5,2]','[3,7,5,2]','[2,3,5,7]','[3,5,7,2]'],answer:'B'},
  {id:5,options:['Wrong','Correct','Wrong too','Also wrong'],answer:'B'},
  {id:6,options:['Correct','Wrong','Wrong too','Also wrong'],answer:'A'},
];
test('an answer is locked after checking and cannot be counted twice', () => {
  const quiz = createQuiz(questions);
  assert.equal(quiz.submit(), false);
  quiz.select(1);
  assert.equal(quiz.submit(), true);
  quiz.select(0);
  assert.equal(quiz.submit(), false);
  assert.equal(quiz.state().selected, 1);
  assert.equal(quiz.state().checked, true);
  assert.equal(quiz.state().score, 1);
});
test('only checked questions advance; final score counts each answer once', () => {
  const quiz = createQuiz(questions);
  assert.equal(quiz.next(), false);
  quiz.select(1); quiz.submit(); quiz.next();
  quiz.select(0); quiz.submit(); quiz.next();
  quiz.select(0); quiz.submit(); quiz.next();
  assert.equal(quiz.state().finished, true);
  assert.equal(quiz.state().score, 2);
  assert.deepEqual(quiz.state().missedIds, [5]);
});
test('retry contains only missed questions and starts with no locked answers', () => {
  const quiz = createQuiz(questions);
  for (const answer of [1,0,0]) { quiz.select(answer); quiz.submit(); quiz.next(); }
  const retry = quiz.retryMissed();
  assert.equal(retry.state().total, 1);
  assert.equal(retry.state().question.id, 5);
  assert.equal(retry.state().checked, false);
  retry.select(1); retry.submit(); retry.next();
  assert.equal(retry.state().score, 1);
  assert.equal(retry.state().finished, true);
});
test('a saved run restores its position, locked feedback and score', () => {
  const quiz = createQuiz(questions);
  quiz.select(1); quiz.submit(); quiz.next();
  quiz.select(0); quiz.submit();
  const resumed = createQuiz(questions, JSON.parse(JSON.stringify(quiz.snapshot())));
  assert.equal(resumed.state().question.id, 5);
  assert.equal(resumed.state().selected, 0);
  assert.equal(resumed.state().checked, true);
  assert.equal(resumed.state().score, 1);
  resumed.next();
  assert.equal(resumed.state().question.id, 6);
});
test('a pending choice survives refresh without being submitted or locked', () => {
  const quiz=createQuiz(questions);quiz.select(2);
  const resumed=createQuiz(questions,quiz.snapshot());
  assert.equal(resumed.state().selected,2);
  assert.equal(resumed.state().checked,false);
  assert.equal(resumed.state().score,0);
  resumed.select(1);assert.equal(resumed.state().selected,1);
  const invalid=createQuiz(questions,{selected:99});assert.equal(invalid.state().selected,null);
});
