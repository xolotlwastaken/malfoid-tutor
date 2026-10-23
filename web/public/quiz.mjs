/** Quiz actions are the seam used by both the browser and behavioural tests. */
export function createQuiz(allQuestions, saved = {}) {
  if (!allQuestions.length) throw new Error('A quiz needs at least one question.');
  const allowed = new Map(allQuestions.map(q => [q.id, q]));
  const ids = Array.isArray(saved.ids) && saved.ids.length && new Set(saved.ids).size === saved.ids.length && saved.ids.every(id => allowed.has(id))
    ? saved.ids : allQuestions.map(q => q.id);
  const questions = ids.map(id => allowed.get(id));
  const answers = {};
  for (const question of questions) {
    const choice = saved.answers?.[question.id];
    if (Number.isInteger(choice) && choice >= 0 && choice < question.options.length) answers[question.id] = choice;
  }
  let index = Number.isInteger(saved.index) && saved.index >= 0 && saved.index < questions.length ? saved.index : 0;
  let selected = answers[questions[index].id] ?? (Number.isInteger(saved.selected) && saved.selected >= 0 && saved.selected < questions[index].options.length ? saved.selected : null);
  let finished = saved.finished === true && questions.every(q => answers[q.id] !== undefined);
  const missed = () => questions.filter(q => answers[q.id] !== undefined && answers[q.id] !== 'ABCD'.indexOf(q.answer));
  return {
    select(option) {
      if (finished || answers[questions[index].id] !== undefined || !Number.isInteger(option) || option < 0 || option >= questions[index].options.length) return;
      selected = option;
    },
    submit() {
      const question = questions[index];
      if (finished || selected === null || answers[question.id] !== undefined) return false;
      answers[question.id] = selected;
      return true;
    },
    next() {
      if (finished || answers[questions[index].id] === undefined) return false;
      if (index === questions.length - 1) finished = true;
      else { index += 1; selected = answers[questions[index].id] ?? null; }
      return true;
    },
    retryMissed() { const retry = missed(); return retry.length ? createQuiz(retry) : null; },
    snapshot() { return {ids: questions.map(q => q.id), index, selected, answers: {...answers}, finished}; },
    state() {
      return {index, selected, finished, question: questions[index], total: questions.length, answers: {...answers},
        questions, missedIds: missed().map(q => q.id), checked: answers[questions[index].id] !== undefined,
        score: questions.filter(q => answers[q.id] !== undefined && answers[q.id] === 'ABCD'.indexOf(q.answer)).length};
    },
  };
}
