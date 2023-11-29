// memo fibo -> 재귀 깊이 제한 초과로 인한 런타임 에러
function solution(n) {
  function fibo(n) {
    if (memo[n] !== -1) return memo[n];

    if (n <= 1) return n;

    memo[n] = (fibo(n - 2) + fibo(n - 1)) % 1234567;

    return memo[n];
  }

  const memo = Array.from({ length: n + 1 }).fill(-1);

  return fibo(n);
}

// 반복문을 이용한 fibo
function fibo(n) {
  const result = [0, 1];

  if (n <= 1) n;

  for (let i = 2; i < n + 1; i++) {
    result.push((result[i - 2] + result[i - 1]) % 1234567);
  }

  return result[n];
}

function solution(n) {
  return fibo(n);
}
