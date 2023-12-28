function solution(rows, columns, queries) {
  const arr = Array.from({ length: rows }, (row, rowIdx) =>
    Array.from(
      { length: columns },
      (_, colIdx) => rowIdx * columns + colIdx + 1
    )
  );
  const result = [];

  for (const [row1, col1, row2, col2] of queries) {
    const indexArr = [];
    const valueArr = [];

    for (let i = col1 - 1; i < col2; i++) {
      indexArr.push([row1 - 1, i]);
    }

    for (let i = row1; i < row2; i++) {
      indexArr.push([i, col2 - 1]);
    }

    for (let i = col2 - 2; i > col1 - 2; i--) {
      indexArr.push([row2 - 1, i]);
    }

    for (let i = row2 - 2; i > row1 - 1; i--) {
      indexArr.push([i, col1 - 1]);
    }

    indexArr.forEach(([x, y]) => {
      valueArr.push(arr[x][y]);
    });

    valueArr.unshift(valueArr.pop());

    indexArr.forEach(([x, y], i) => {
      arr[x][y] = valueArr[i];
    });

    result.push(Math.min(...valueArr));
  }

  return result;
}
