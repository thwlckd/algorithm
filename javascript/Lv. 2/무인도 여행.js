// 7, 10, 12 런타임 에러 why?
function solution(maps) {
  const result = [];
  const rows = maps.length;
  const cols = maps[0].length;
  const visited = Array.from({ length: cols }, () =>
    Array.from({ length: rows }, () => false)
  );
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (visited[i][j]) continue;
      if (maps[i][j] === 'X') {
        visited[i][j] = true;
        continue;
      }

      const q = [[i, j]];
      let acc = Number(maps[i][j]);

      visited[i][j] = true;

      while (q.length > 0) {
        const [x, y] = q.shift();

        for (let i = 0; i < 4; i++) {
          const nx = x + dx[i];
          const ny = y + dy[i];

          if (nx < 0 || nx >= rows || ny < 0 || ny >= cols) continue;

          if (!visited[nx][ny]) {
            visited[nx][ny] = true;

            if (maps[nx][ny] !== 'X') {
              q.push([nx, ny]);
              acc += Number(maps[nx][ny]);
            }
          }
        }
      }

      result.push(acc);
    }
  }

  return result.length === 0 ? [-1] : result.sort((a, b) => a - b);
}
