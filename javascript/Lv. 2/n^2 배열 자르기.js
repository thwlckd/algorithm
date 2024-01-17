// 시간초과, 메모리 초과
function solution(n, left, right) {
  const arr = Array.from({ length: n }, (_, i1) =>
    Array.from({ length: n }, (_, i2) => (i1 >= i2 ? i1 + 1 : i2 + 1))
  );

  return arr
    .reduce((acc, value) => acc.concat(value), [])
    .slice(left, right + 1);
}

// num번째 좌표 (r, c) = (Math.floor(num / n), num % n)
function solution(n, left, right) {
  const arr = [];

  for (let i = left; i <= right; i++) {
    arr.push(Math.max(Math.floor(i / n), i % n) + 1);
  }

  return arr;
}
