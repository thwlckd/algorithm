function solution(s) {
  const data = s
    .split('},{')
    .map((item) => item.replace(/[{}]/g, '').split(','));
  const result = [];
  const sorted = data.sort((a, b) => a.length - b.length);

  for (const arr of sorted) {
    for (const v of arr) {
      if (!result.includes(Number(v))) {
        result.push(Number(v));
        break;
      }
    }
  }

  return result;
}
