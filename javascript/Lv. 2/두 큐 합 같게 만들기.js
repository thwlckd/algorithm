function solution(queue1, queue2) {
  let sum1 = queue1.reduce((acc, v) => acc + v, 0);
  const sum2 = queue2.reduce((acc, v) => acc + v, 0);
  const half = (sum1 + sum2) / 2;
  const q = [...queue1, ...queue2];
  let pointer1 = 0;
  let pointer2 = queue1.length;

  for (let i = 0; i < queue1.length * 3; i++) {
    if (sum1 === half) return i;

    sum1 += sum1 > half ? -q[pointer1++ % q.length] : q[pointer2++ % q.length];
  }

  return -1;
}
