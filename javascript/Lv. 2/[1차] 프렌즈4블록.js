function solution(m, n, board) {
  board = [...board].map((now) => now.split(''));

  while (true) {
    const toErase = [];

    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        const temp = board[i][j];
        if (
          temp &&
          temp === board[i + 1][j] &&
          temp === board[i][j + 1] &&
          temp === board[i + 1][j + 1]
        )
          toErase.push([i, j]);
      }
    }

    if (!toErase.length)
      return board.reduce(
        (acc, row) => acc + row.filter((char) => !char).length,
        0
      );

    toErase.forEach(([i, j]) => {
      board[i][j] = 0;
      board[i + 1][j] = 0;
      board[i][j + 1] = 0;
      board[i + 1][j + 1] = 0;
    });

    for (let i = m - 1; i >= 0; i--) {
      for (let j = 0; j < n; j++) {
        for (let k = i - 1; k >= 0; k--) {
          if (board[i][j]) break;

          if (board[k][j]) {
            board[i][j] = board[k][j];
            board[k][j] = 0;
            break;
          }
        }
      }
    }
  }
}
