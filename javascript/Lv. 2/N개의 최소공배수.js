function getDivisor(n) {
  const divisor = {};

  while (n > 1) {
    for (let i = 2; i <= n; i++) {
      if (n % i === 0) {
        if (divisor[i]) {
          divisor[i] += 1;
        } else {
          divisor[i] = 1;
        }
        n /= i;
        break;
      }
    }
  }

  return divisor;
}

function solution(arr) {
  const result = {};

  arr.forEach((n) => {
    Object.entries(getDivisor(n)).forEach(([base, pow]) => {
      if (!result[base] || result[base] < pow) result[base] = pow;
    });
  });

  return Object.entries(result).reduce(
    (acc, [base, pow]) => acc * Number(base) ** pow,
    1
  );
}
