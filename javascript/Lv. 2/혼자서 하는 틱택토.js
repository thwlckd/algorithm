function solution(board) {
  function checkRow(line) {
    const target = board[line][0];

    if (target === '.') return false;

    return board[line].every((v) => v === target) ? target : false;
  }

  function checkCol(line) {
    const target = board[0][line];

    if (target === '.') return false;

    for (const row of board) {
      if (row[line] !== target) return false;
    }

    return target;
  }

  function checkCross(target) {
    const cross = [];

    for (let i = 0; i < 3; i++) {
      cross.push(board[i][i]);
    }

    if (cross.every((v) => v === target)) return true;

    cross.length = 0;

    for (let i = 0; i < 3; i++) {
      cross.push(board[2 - i][i]);
    }

    return cross.every((v) => v === target) ? true : false;
  }

  let numO = 0;
  let numX = 0;
  let isLineO = 0;
  let isLineX = 0;

  board = board.map((row) => {
    const arr = row.split('');

    arr.forEach((v) => {
      if (v === 'O') numO++;
      if (v === 'X') numX++;
    });
    return arr;
  });

  if (numX > numO || numO > numX + 1) return 0;

  for (let i = 0; i < 3; i++) {
    const rowResult = checkRow(i);
    const colResult = checkCol(i);

    if (rowResult === 'O') isLineO++;
    else if (rowResult === 'X') isLineX++;

    if (colResult === 'O') isLineO++;
    else if (colResult === 'X') isLineX++;
  }

  isLineO += checkCross('O') ? 1 : 0;
  isLineX += checkCross('X') ? 1 : 0;

  if (isLineX && numO > numX) return 0;
  if (isLineO && numO <= numX) return 0;

  return isLineO & isLineX ? 0 : 1;
}
