function solution(elements) {
  const result = new Set();
  const arr = [...elements, ...elements];

  for (let i = 1; i <= elements.length; i++) {
    for (let j = 0; j < elements.length; j++) {
      result.add(arr.slice(j, j + i).reduce((acc, v) => acc + v, 0));
    }
  }

  return result.size;
}
