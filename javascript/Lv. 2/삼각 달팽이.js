function solution(n) {
  const arr = Array.from({ length: n }, () => []);
  let num = 1;
  let round = 0;

  while (true) {
    let lastArrIdx = 0;

    for (let i = round * 2; i < arr.length; i++) {
      if (arr[i].length < i + 1) {
        arr[i].splice(round, 0, num);
        lastArrIdx = i;
        num++;
      } else break;
    }

    for (let i = round + 1; i < arr[lastArrIdx][0] - round; i++) {
      arr[lastArrIdx].splice(i, 0, num);
      num++;
    }

    for (let i = lastArrIdx - 1; i > round * 2; i--) {
      arr[i].splice(arr[i].length - round, 0, num);
      num++;
    }

    if (num > (n * (n + 1)) / 2) break;

    round++;
  }

  return arr.flat();
}
