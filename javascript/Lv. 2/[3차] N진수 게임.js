function solution(n, t, m, p) {
  let result = '';

  for (let i = 0; i < t * m; i++) {
    result += i.toString(n);
  }

  return result
    .toUpperCase()
    .split('')
    .filter((_, i) => i % m === p - 1)
    .join('')
    .slice(0, t);
}
