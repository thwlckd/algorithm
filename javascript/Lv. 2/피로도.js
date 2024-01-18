function solution(k, dungeons) {
  let result = 0;

  function dfs(remain, dungeons, depth) {
    result = Math.max(result, depth);

    if (remain <= 0) return;

    for (let i = 0; i < dungeons.length; i++) {
      const [need, consumption] = dungeons[i];

      if (remain >= need) {
        dfs(
          remain - consumption,
          [...dungeons.slice(0, i), ...dungeons.slice(i + 1)],
          depth + 1
        );
      }
    }
  }

  dfs(k, dungeons, 0);

  return result;
}
