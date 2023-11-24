function solution(land) {
  const dp = land.map((arr) => [...arr]);

  for (let i = 1; i < land.length; i++) {
    for (let j = 0; j < 4; j++) {
      const arr = [...dp[i - 1]].filter((_, index) => index !== j);

      dp[i][j] = Math.max(...arr) + dp[i][j];
    }
  }

  return Math.max(...dp.at(-1));
}
