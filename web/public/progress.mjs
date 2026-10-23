const KEY = 'malfoid-study:v1';
const fresh = () => ({version:1, answers:{}, videos:{}, sessions:{}, lastLesson:null});
const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);

/** Browser storage is optional: blocked storage must not prevent studying. */
export function createProgress(storage) {
  let data = fresh();
  let persistent = true;
  let raw;
  try { raw = storage.getItem(KEY); } catch { persistent = false; }
  try {
    const value = JSON.parse(raw);
    if (value?.version === 1) {
      for (const field of ['answers','videos','sessions']) {
        if (object(value[field])) data[field] = value[field];
      }
      data.lastLesson = typeof value.lastLesson === 'string' ? value.lastLesson : null;
    }
  } catch { /* A damaged record starts a fresh session. */ }
  const persist = () => {
    try { storage.setItem(KEY, JSON.stringify(data)); } catch { persistent = false; }
  };
  return {
    get persistent() { return persistent; },
    read: () => structuredClone(data),
    answer(id, correct) {
      data.answers[id] = {correct:correct === true, attempts:(Number(data.answers[id]?.attempts) || 0)+1};
      persist();
    },
    video(slug,time,duration,completed=false) {
      if (!Number.isFinite(time) || !Number.isFinite(duration) || duration <= 0) return;
      data.videos[slug]={time:Math.max(0,Math.min(time,duration)),duration,completed:completed || data.videos[slug]?.completed === true};
      data.lastLesson=slug;
      persist();
    },
    saveQuiz(key, snapshot) { data.sessions[key]=structuredClone(snapshot);persist(); },
  };
}
