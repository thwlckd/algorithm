function decimalToBinary(num) {
  const result = [];

  while (num > 0) {
    result.unshift(num % 2);
    num = Math.floor(num / 2);
  }

  return result;
}

function solution(n) {
  const now = decimalToBinary(n).reduce(
    (acc, value) => (value === 1 ? acc + 1 : acc),
    0
  );

  while (true) {
    const next = decimalToBinary(++n).reduce(
      (acc, value) => (value === 1 ? acc + 1 : acc),
      0
    );

    if (now === next) {
      break;
    }
  }

  return n;
}

console.log(solution(78));
