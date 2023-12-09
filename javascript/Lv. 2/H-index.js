function solution(citations) {
  const result = [];

  for (let i = 0; i <= citations.length; i++) {
    if (citations.filter((v) => v >= i).length >= i) result.push(i);
  }

  return Math.max(...result);
}

// 모범 답안
function solution(citations) {
  let result = 0;

  citations.sort((a, b) => b - a);

  for (let i = 0; i < citations.length; i++) {
    if (i < citations[i]) result++;
    else break;
  }

  return result;
}
