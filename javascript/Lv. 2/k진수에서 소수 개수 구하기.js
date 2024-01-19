function isPrime(n) {
  if (n < 2) return false;

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }

  return true;
}

function solution(n, k) {
  const num = n.toString(k);

  return num
    .split('0')
    .reduce((acc, v) => (isPrime(Number(v)) ? acc + 1 : acc), 0);
}
