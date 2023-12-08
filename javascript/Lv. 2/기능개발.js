function solution(progresses, speeds) {
  const result = [];

  while (progresses.length > 0) {
    let count = 0;
    const day = Math.ceil((100 - progresses[0]) / speeds[0]);

    while (progresses.length > 0) {
      if (100 <= progresses[0] + speeds[0] * day) {
        progresses.shift();
        speeds.shift();
        count++;
      } else break;
    }

    result.push(count);
  }

  return result;
}
