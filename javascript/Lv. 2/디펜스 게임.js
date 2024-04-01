function solution(n, k, enemy) {
  let left = 0;
  let right = enemy.length;
  let mid = Math.floor((left + right) / 2);

  while (left <= right) {
    let chance = k;
    const arr = enemy.slice(0, mid).sort((a, b) => b - a);
    const boundary = arr.reduce((acc, v) => {
      if (chance > 0) {
        chance--;

        return acc;
      }

      return acc + v;
    }, 0);

    if (boundary > n) right = mid - 1;
    else left = mid + 1;

    mid = Math.floor((left + right) / 2);
  }

  return left - 1;
}
