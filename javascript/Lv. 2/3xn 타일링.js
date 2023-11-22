// 기존의 타일에 추가될 수 있는 경우 3가지 + n = 4부터 경우의 수 2개씩 추가
// n 짝수 경우만 고려
// dp[i] = 3 * dp[i - 1] + 2 * (dp[i - 2] + dp[i - 3] + ... +dp[2] +1)

function solution(n) {
  const dp = [3];

  if (n % 2) return '짝수만 가능';

  for (let i = 4; i <= n; i += 2) {
    const sum = dp.reduce(
      (acc, value, index) => (index < dp.length - 1 ? acc + value : acc),
      1
    );
    dp.push((3 * dp.at(-1) + 2 * sum) % 1000000007);
  }

  return dp.at(-1);
}
