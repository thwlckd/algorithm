function solution(begin, end) {
  const result = [];

  if (begin === 1) {
    begin++;
    result.push(0);
  }

  for (let i = begin; i <= end; i++) {
    const temp = [1];

    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) {
        temp.push(j);

        if (i / j <= 10000000) {
          temp.push(i / j);
          break;
        }
      }
    }

    result.push(Math.max(...temp));
  }

  return result;
}
