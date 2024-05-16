function solution(land) {
  const data = {}; // key: quantity
  const q = [];
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const visited = Array.from({ length: land.length }, () =>
    Array.from({ length: land[0].length }, () => false)
  ); // false -> 미방문, true -> 방문/0, string(random number) -> 방문/1

  for (let i = 0; i < land.length; i++) {
    for (let j = 0; j < land[0].length; j++) {
      if (visited[i][j]) continue;
      if (land[i][j] === 0) {
        visited[i][j] = true;
        continue;
      }

      const key = String(Math.random());

      q.push([i, j, key]);
      data[key] = 1;
      visited[i][j] = key;

      while (q.length > 0) {
        const [x, y, key] = q.shift();

        for (let i = 0; i < 4; i++) {
          const nx = x + dx[i];
          const ny = y + dy[i];

          if (nx < 0 || nx >= land.length || ny < 0 || ny >= land[0].length)
            continue;
          if (visited[nx][ny]) continue;
          visited[nx][ny] = true;
          if (land[nx][ny] === 0) continue;

          q.push([nx, ny, key]);
          data[key]++;
          visited[nx][ny] = key;
        }
      }
    }
  }

  let result = 0;

  for (let col = 0; col < land[0].length; col++) {
    const set = new Set();
    let count = 0;

    for (let row = 0; row < land.length; row++) {
      if (typeof visited[row][col] === 'string') set.add(visited[row][col]);
    }

    for (const key of set) {
      count += data[key];
    }

    result = Math.max(result, count);
  }

  return result;
}
