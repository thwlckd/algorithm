function solution(data, col, row_begin, row_end) {
  let result = 0;

  data.sort((a, b) =>
    a[col - 1] === b[col - 1] ? b[0] - a[0] : a[col - 1] - b[col - 1]
  );

  for (let i = row_begin; i <= row_end; i++) {
    const s_i = data[i - 1].reduce((acc, v) => {
      acc += v % i;

      return acc;
    }, 0);

    result ^= s_i;
  }

  return result;
}
