function solution(n, k) {
  const result = [];
  const arr = Array.from({ length: n }, (_, i) => i + 1);
  let fact = arr.reduce((acc, v) => acc * v, 1);

  while (arr.length) {
    fact /= arr.length;

    result.push(...arr.splice(Math.floor((k - 1) / fact), 1));

    k %= fact;
  }

  return result;
}
