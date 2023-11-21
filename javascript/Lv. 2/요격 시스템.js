function solution(targets) {
  targets.sort((a, b) => b[0] - a[0]);

  let start = targets[0][0];
  let count = 1;

  targets.forEach((target) => {
    if (target[1] <= start) {
      start = target[0];
      count++;
    }
  });

  return count;
}
