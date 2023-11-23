// 조건 i > 0, j > 0, dp[i][j] !== 0
// dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

function solution(board) {
  let result = 0;

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (i < 1 || j < 1) {
        result = Math.max(result, board[i][j]);
        continue;
      }

      if (board[i][j] !== 0) {
        board[i][j] =
          Math.min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1;
      }

      result = Math.max(result, board[i][j]);
    }
  }

  return result ** 2;
}
