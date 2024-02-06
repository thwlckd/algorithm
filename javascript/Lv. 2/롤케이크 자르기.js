// 시간초과
function solution(topping) {
  let result = 0;

  for (let i = 0; i < topping.length - 1; i++) {
    const set1 = new Set(topping.slice(0, i + 1)); // Set -> O(N)
    const set2 = new Set(topping.slice(i + 1));

    if (set1.size === set2.size) result++;
  }

  return result;
}

function solution(topping) {
  const set = new Set(); // 형의 토핑
  const map = new Map(); // 동생의 토핑, 동생이 형에게 토핑을 하나씩 주기
  let result = 0;

  for (const v of topping) {
    map.has(v) ? map.set(v, map.get(v) + 1) : map.set(v, 1);
  }

  for (const v of topping) {
    const temp = map.get(v) - 1;

    temp === 0 ? map.delete(v) : map.set(v, temp);

    set.add(v);

    if (set.size !== 0 && set.size === map.size) result++;
  }

  return result;
}
