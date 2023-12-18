function solution(s) {
  let result = s.length;

  for (let i = 1; i <= Math.floor(s.length / 2); i++) {
    let compressed = '';
    let before = s.slice(0, i);
    let count = 1;

    for (let j = i; j < s.length; j += i) {
      const now = s.slice(j, j + i);

      if (before === now) {
        count++;
      } else if (count <= 1) {
        compressed += before;
        count = 1;
      } else {
        compressed += String(count) + before;
        count = 1;
      }

      before = now;
    }

    compressed += count === 1 ? before : String(count) + before;
    result = Math.min(result, compressed.length);
  }

  return result;
}
