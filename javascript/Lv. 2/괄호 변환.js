function seperate(s) {
  let flag = 0;

  for (let i = 0; i < s.length; i++) {
    flag += s[i] === '(' ? 1 : -1;

    if (flag === 0) {
      return { left: s.slice(0, i + 1), right: s.slice(i + 1) || '' };
    }
  }
}

function isCompleteString(s) {
  let flag = 0;

  for (let i = 0; i < s.length; i++) {
    flag += s[i] === '(' ? 1 : -1;

    if (flag < 0) return false;
  }

  return true;
}

function recrusive(s) {
  if (s === '') return s;

  let { left: u, right: v } = seperate(s);

  return isCompleteString(u)
    ? u + recrusive(v)
    : '(' +
        recrusive(v) +
        ')' +
        u
          .split('')
          .slice(1, -1)
          .map((char) => (char === '(' ? ')' : '('))
          .join('');
}

function solution(p) {
  return recrusive(p);
}
