function solution(k, tangerine) {
  const map = new Map();
  const arr = [];

  tangerine.forEach((v) => {
    map.has(v) ? map.set(v, map.get(v) + 1) : map.set(v, 1);
  });

  map.forEach((v, key) => {
    arr.push([key, v]);
  });

  arr.sort((a, b) => b[1] - a[1]);

  return new Set(arr.flatMap(([v, num]) => Array(num).fill(v)).slice(0, k))
    .size;
}

// 개선 답안
function solution(k, tangerine) {
  const map = new Map();
  let result = 0;

  tangerine.forEach((v) => {
    map.set(v, map.has(v) ? map.get(v) + 1 : 1);
  });

  const nums = Array.from(map.values()).sort((a, b) => a - b);

  while (k > 0) {
    k -= nums.pop();
    result++;
  }

  return result;
}
