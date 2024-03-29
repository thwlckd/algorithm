// 1 -> 1: 1
// 2 -> 11, 2: 2
// 3 -> 111, 12, 21: 3
// 4 -> 1111, 112, 121, 211, 22: 5
// 5 -> 11111, 1112, 1121, 1211, 2111, 122, 212, 221: 8
// dp[i] = dp[i-1] + dp[i-2]

function solution(n) {
  const dp = [0, 1, 2];

  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
  }

  return dp[n];
}
