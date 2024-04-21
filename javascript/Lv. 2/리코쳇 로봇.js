function solution(board) {
  const start = [];

  for (let row = 0; row < board.length; row++) {
    if (start.length > 0) break;

    for (let col = 0; col < board[0].length; col++) {
      if (board[row][col] === 'R') {
        start.push(row);
        start.push(col);
      }
    }
  }

  const visited = Array.from({ length: board.length }, () =>
    Array.from({ length: board[0].length }, () => false)
  );
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  const q = [];

  q.push([...start, 0]);
  visited[start[0]][start[1]] = true;

  while (q.length > 0) {
    const [row, col, count] = q.shift();

    if (board[row][col] === 'G') return count;

    for (let i = 0; i < 4; i++) {
      let nx = col;
      let ny = row;

      while (
        nx + dx[i] >= 0 &&
        nx + dx[i] < board[0].length &&
        ny + dy[i] >= 0 &&
        ny + dy[i] < board.length
      ) {
        if (board[ny + dy[i]][nx + dx[i]] === 'D') break;

        nx += dx[i];
        ny += dy[i];
      }

      if (visited[ny][nx]) continue;

      visited[ny][nx] = true;
      q.push([ny, nx, count + 1]);
    }
  }

  return -1;
}
