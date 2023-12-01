function solution(n, a, b) {
  let round = 1;

  while (true) {
    if (Math.abs(a - b) === 1 && Math.max(a, b) % 2 === 0) break;

    a = Math.ceil(a / 2);
    b = Math.ceil(b / 2);
    round++;
  }

  return round;
}
