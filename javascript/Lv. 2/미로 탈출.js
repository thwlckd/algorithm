function solution(maps) {
  function findCoordinate(target) {
    for (let row = 0; row < maps.length; row++) {
      for (let col = 0; col < maps[0].length; col++) {
        if (maps[row][col] === target) return [row, col];
      }
    }
  }

  function bfs(row, col, target) {
    const q = [];
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    const visited = Array.from({ length: maps.length }, () =>
      Array.from({ length: maps[0].length }, () => false)
    );

    q.push([row, col, 0]);
    visited[row][col] = true;

    while (q.length > 0) {
      const [y, x, count] = q.shift();

      if (maps[y][x] === target) return count;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];

        if (ny < 0 || ny >= maps.length || nx < 0 || nx >= maps[0].length)
          continue;
        if (visited[ny][nx] || maps[ny][nx] === 'X') continue;

        q.push([ny, nx, count + 1]);
        visited[ny][nx] = true;
      }
    }

    return -1;
  }

  maps = maps.map((row) => row.split(''));

  const [startRow, startCol] = findCoordinate('S');
  const [leverRow, leverCol] = findCoordinate('L');
  let route1 = 0;
  let route2 = 0;

  route1 += bfs(startRow, startCol, 'L');

  if (route1 === -1) return -1;

  route2 += bfs(leverRow, leverCol, 'E');

  return route2 === -1 ? -1 : route1 + route2;
}

// dfs 시간초과 -> 최단거리는 bfs!! 의심하지 말자
function solution(maps) {
  function dfs(y, x, target, count) {
    if (maps[y][x] === target) {
      distance = Math.min(distance, count);

      return;
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (ny < 0 || ny >= maps.length || nx < 0 || nx >= maps[0].length)
        continue;
      if (visited[ny][nx] || maps[ny][nx] === 'X') continue;
      if (count + 1 >= distance) continue;

      visited[ny][nx] = true;
      dfs(ny, nx, target, count + 1);
      visited[ny][nx] = false;
    }
  }

  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const visited = Array.from({ length: maps.length }, () =>
    Array.from({ length: maps[0].length }, () => false)
  );
  const start = {};
  const lever = {};
  let distance = Number.MAX_SAFE_INTEGER;
  let result = 0;

  maps = maps.map((row) => row.split(''));

  for (let row = 0; row < maps.length; row++) {
    if (start.row && lever.row) break;

    for (let col = 0; col < maps[0].length; col++) {
      if (maps[row][col] === 'S') {
        start['row'] = row;
        start['col'] = col;
      }

      if (maps[row][col] === 'L') {
        lever['row'] = row;
        lever['col'] = col;
      }
    }
  }

  visited[start.row][start.col] = true;
  dfs(start.row, start.col, 'L', 0);

  if (distance === Number.MAX_SAFE_INTEGER) return -1;
  result += distance;

  for (let row = 0; row < maps.length; row++) {
    for (let col = 0; col < maps[0].length; col++) {
      visited[row][col] = false;
    }
  }

  visited[lever.row][lever.col] = true;
  distance = Number.MAX_SAFE_INTEGER;
  dfs(lever.row, lever.col, 'E', 0);

  return distance === Number.MAX_SAFE_INTEGER ? -1 : result + distance;
}
