function solution(k, ranges) {
  const sequence = [k];
  const acc = [0];
  const result = [];

  while (k > 1) {
    if (k % 2 === 0) k /= 2;
    else k = 3 * k + 1;

    sequence.push(k);
  }

  for (let i = 1; i < sequence.length; i++) {
    acc.push(acc.at(-1) + (sequence[i] + sequence[i - 1]) / 2);
  }

  for (const range of ranges) {
    const [x, y] = [range[0], sequence.length - 1 + range[1]];

    if (x > y) result.push(-1);
    else result.push(acc[y] - acc[x]);
  }

  return result;
}
