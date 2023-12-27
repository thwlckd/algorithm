function isCorrectString(s) {
  const pair = { '{': '}', '[': ']', '(': ')' };
  const openBracketStack = [];

  for (const char of s) {
    if (['{', '(', '['].includes(char)) openBracketStack.push(char);
    else {
      if (!(pair[openBracketStack.pop()] === char)) return false;
    }
  }

  return openBracketStack.length > 0 ? false : true;
}

function solution(s) {
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (isCorrectString(s.slice(i) + s.slice(0, i))) count++;
  }

  return count;
}
