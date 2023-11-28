function solution(n) {
  let result = 1;

  for (let i = 1; i <= Math.floor(n / 2); i++) {
    let sum = 0;

    for (let j = i; j <= Math.ceil(n / 2); j++) {
      sum += j;

      if (sum === n) {
        result += 1;
        break;
      }

      if (sum > n) break;
    }
  }

  return result;
}
