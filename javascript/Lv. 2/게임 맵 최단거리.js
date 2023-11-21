// bfs 풀이
// 최단거리 탐색 - bfs
function solution(
  maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ]
) {
  function bfs() {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    while (q.length > 0) {
      const [x, y] = q.shift();

      if (x === n - 1 && y === m - 1) break;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        const cost = maps[x][y];

        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

        if (maps[nx][ny] !== 1 || maps[nx][ny] > cost) continue;

        maps[nx][ny] = cost + 1;
        q.push([nx, ny]);
      }
    }
  }

  const n = maps.length;
  const m = maps[0].length;

  const q = [];
  q.push([0, 0]);
  bfs();

  return maps[n - 1][m - 1] !== 1 ? maps[n - 1][m - 1] : -1;
}

// dfs 풀이
// 런타임 에러 + 시간 초과
// function solution(
//   maps = [
//     [1, 0, 1, 1, 1],
//     [1, 0, 1, 0, 1],
//     [1, 0, 1, 1, 1],
//     [1, 1, 1, 0, 1],
//     [0, 0, 0, 0, 1],
//   ]
// ) {
//   function dfs(x, y, count) {
//     if (x === n - 1 && y === m - 1) {
//       result = Math.min(result, count);
//       return;
//     }

//     for (let i = 0; i < 4; i++) {
//       const nx = x + dx[i];
//       const ny = y + dy[i];

//       if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

//       if (maps[nx][ny] === 1) {
//         maps[nx][ny] = 2;
//         dfs(nx, ny, count + 1);
//         maps[nx][ny] = 1;
//       }
//     }
//   }

//   const n = maps.length;
//   const m = maps[0].length;
//   const dx = [0, 0, -1, 1];
//   const dy = [1, -1, 0, 0];
//   let result = Infinity;
//   dfs(0, 0, 1);

//   return result === Infinity ? -1 : result;
// }
