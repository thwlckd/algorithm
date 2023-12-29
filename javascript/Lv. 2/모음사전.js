function makeWord(prefixArr, newArr) {
  const alphabet = ['A', 'E', 'I', 'O', 'U'];

  prefixArr.forEach((word) => {
    alphabet.forEach((char) => {
      newArr.push(word + char);
    });
  });
}

function solution(word) {
  const word1 = ['A', 'E', 'I', 'O', 'U'],
    word2 = [],
    word3 = [],
    word4 = [],
    word5 = [];

  makeWord(word1, word2);
  makeWord(word2, word3);
  makeWord(word3, word4);
  makeWord(word4, word5);

  return (
    [...word1, ...word2, ...word3, ...word4, ...word5].sort().indexOf(word) + 1
  );
}

// dfs 풀이 예시
let idx = 0;
const result = {};
const vowels = [...'AEIOU'];

function solution(word) {
  dfs('', 0);
  return result[word];
}

const dfs = (word, length) => {
  if (length > 5) return;
  result[word] = idx++;
  vowels.forEach((vowel) => {
    dfs(word + vowel, length + 1);
  });
};
