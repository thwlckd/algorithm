function solution(s) {
  let pair = 0;

  for (const char of s) {
    char === '(' ? pair++ : pair--;
    if (pair < 0) return false;
  }

  return pair === 0 ? true : false;
}
