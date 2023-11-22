function solution(n) {
  const mapper = [4, 1, 2];
  const result = [];

  while (n > 0) {
    const rest = n % 3;

    n = Math.floor(n / 3);

    if (rest == 0) n--;

    result.unshift(mapper[rest]);
  }

  return result.join('');
}
