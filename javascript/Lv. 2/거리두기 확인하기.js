function solution(places) {
  function bfs(place, visited, x, y) {
    const dx = [0, 1, 0, -1];
    const dy = [-1, 0, 1, 0];
    const q = [[x, y, 0]];

    while (q.length > 0) {
      const [x, y, n] = q.shift();

      if (n !== 0 && place[x][y] === 'P') return false;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];

        if (
          nx >= 0 &&
          nx < 5 &&
          ny >= 0 &&
          ny < 5 &&
          !visited[nx][ny] &&
          place[nx][ny] !== 'X'
        ) {
          if (n < 2) {
            visited[nx][ny] = true;
            q.push([nx, ny, n + 1]);
          }
        }
      }
    }

    return true;
  }

  function loop(place) {
    const visited = Array.from({ length: 5 }, () =>
      Array.from({ length: 5 }, () => false)
    );

    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        if (place[i][j] !== 'P') continue;

        visited[i][j] = true;

        if (!bfs(place, visited, i, j)) return 0;
      }
    }

    return 1;
  }

  return places.map((place) => loop(place));
}
