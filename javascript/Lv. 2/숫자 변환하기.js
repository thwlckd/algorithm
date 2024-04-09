// bfs
// 최단거리 문제는 bfs!!
function solution(x, y, n) {
  let result = -1;
  const q = [[y, 0]];

  while (q.length > 0) {
    const [value, count] = q.shift();

    if (value === x) {
      result = count;
      break;
    }

    if (value % 3 === 0 && value / 3 >= x) {
      q.push([value / 3, count + 1]);
    }

    if (value % 2 === 0 && value / 2 >= x) {
      q.push([value / 2, count + 1]);
    }

    if (value - n >= x) {
      q.push([value - n, count + 1]);
    }
  }

  return result;
}

// dfs 풀이
// 시간초과 & 일부 테스트 케이스 런타임 에러
function solution(x, y, n) {
  let result = Number.MAX_SAFE_INTEGER;

  function dfs(depth, value) {
    if (value === y) {
      result = Math.min(result, depth);
      return;
    }

    if (value > y) return;

    dfs(depth + 1, value + n);
    dfs(depth + 1, value * 2);
    dfs(depth + 1, value * 3);
  }

  dfs(0, x);

  return result === Number.MAX_SAFE_INTEGER ? -1 : result;
}
