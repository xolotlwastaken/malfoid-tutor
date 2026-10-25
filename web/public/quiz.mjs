export function isAnswerCorrect(question, answer) {
  return question.type === 'written' ? answer?.correct === true : answer === 'ABCD'.indexOf(question.answer);
}

const graded = (question, answer) => question.type === 'written' ? typeof answer?.correct === 'boolean' : answer !== undefined;
const validChoice = (question, choice) => question.type === 'written'
  ? typeof choice === 'string' : Number.isInteger(choice) && choice >= 0 && choice < question.options.length;

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
    if (question.type === 'written') {
      if (typeof choice?.text === 'string' && choice.text.trim() && (choice.correct === null || typeof choice.correct === 'boolean')) answers[question.id] = {...choice};
    } else if (validChoice(question, choice)) answers[question.id] = choice;
  }
  let index = Number.isInteger(saved.index) && saved.index >= 0 && saved.index < questions.length ? saved.index : 0;
  const selectedAnswer = question => question.type === 'written' ? answers[question.id]?.text : answers[question.id];
  let selected = selectedAnswer(questions[index]) ?? (validChoice(questions[index], saved.selected) ? saved.selected : null);
  let finished = saved.finished === true && questions.every(q => graded(q, answers[q.id]));
  const missed = () => questions.filter(q => graded(q, answers[q.id]) && !isAnswerCorrect(q, answers[q.id]));
  return {
    select(option) {
      if (finished || answers[questions[index].id] !== undefined || !validChoice(questions[index], option)) return;
      selected = option;
    },
    submit() {
      const question = questions[index];
      if (finished || selected === null || answers[question.id] !== undefined || (question.type === 'written' && !selected.trim())) return false;
      answers[question.id] = question.type === 'written' ? {text:selected.trim(), correct:null} : selected;
      return true;
    },
    assess(correct) {
      const question = questions[index], answer = answers[question.id];
      if (finished || question.type !== 'written' || !answer || graded(question, answer) || typeof correct !== 'boolean') return false;
      answer.correct = correct;
      return true;
    },
    next() {
      if (finished || !graded(questions[index], answers[questions[index].id])) return false;
      if (index === questions.length - 1) finished = true;
      else { index += 1; selected = selectedAnswer(questions[index]) ?? null; }
      return true;
    },
    retryMissed() { const retry = missed(); return retry.length ? createQuiz(retry) : null; },
    snapshot() { return {ids: questions.map(q => q.id), index, selected, answers: structuredClone(answers), finished}; },
    state() {
      return {index, selected, finished, question: questions[index], total: questions.length, answers: structuredClone(answers),
        questions, missedIds: missed().map(q => q.id), checked: answers[questions[index].id] !== undefined,
        graded: graded(questions[index], answers[questions[index].id]),
        completed: questions.filter(q => graded(q, answers[q.id])).length,
        score: questions.filter(q => isAnswerCorrect(q, answers[q.id])).length};
    },
  };
}
