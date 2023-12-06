function solution(clothes) {
  const combi = {};

  for (const [_, type] of clothes) {
    if (combi[type]) combi[type] += 1;
    else combi[type] = 1;
  }

  return Object.values(combi).reduce((acc, v) => acc * (v + 1), 1) - 1;
}
