function solution(picks, minerals) {
  function dfs(depth, count, left) {
    if (depth >= minerals.length || left <= 0) {
      result = Math.min(result, count);

      return;
    }

    for (let i = 0; i < 3; i++) {
      if (picks[i] === 0) continue;

      let num = 0;
      let temp = 0;

      while (num < 5) {
        if (depth + num >= minerals.length) break;

        temp += mapper[minerals[depth + num]][i];
        num++;
      }

      if (count < result) {
        picks[i]--;
        dfs(depth + num, count + temp, left - 1);
        picks[i]++;
      }
    }
  }

  const mapper = { diamond: [1, 5, 25], iron: [1, 1, 5], stone: [1, 1, 1] }; // 광물: [곡괭이(다이아, 철, 돌)]
  let result = Number.MAX_SAFE_INTEGER;

  dfs(
    0,
    0,
    picks.reduce((acc, v) => acc + v, 0)
  );

  return result;
}
