function solution(priorities, location) {
  let result = 0;
  const q = priorities.map((v, i) => [v, i]);

  while (q.length > 0) {
    const now = q.shift();

    if (q.some((v) => v[0] > now[0])) {
      q.push(now);
      continue;
    }

    result++;

    if (now[1] === location) break;
  }

  return result;
}
