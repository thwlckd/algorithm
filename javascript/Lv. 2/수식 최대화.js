function calculate(left, right, operator) {
  left = Number(left);
  right = Number(right);

  switch (operator) {
    case '+':
      return left + right;
    case '-':
      return left - right;
    case '*':
      return left * right;
    default:
      return;
  }
}

function findAllIndex(arr, value) {
  return arr.reduce((acc, v, i) => {
    if (v === value) acc.push(i);
    return acc;
  }, []);
}

function solution(expression) {
  const combinations = [
    ['+', '-', '*'],
    ['+', '*', '-'],
    ['-', '+', '*'],
    ['-', '*', '+'],
    ['*', '+', '-'],
    ['*', '-', '+'],
  ];
  const result = [];

  combinations.forEach(([first, second, third]) => {
    const data = expression.match(/[0-9]+/g);
    const operators = expression.match(/[\+\-\*]+/g);

    findAllIndex(operators, first).forEach((v, i) => {
      const value = calculate(data[v - i], data[v - i + 1], first);

      data.splice(v - i, 2, value);
      operators.splice(v - i, 1);
    });

    findAllIndex(operators, second).forEach((v, i) => {
      const value = calculate(data[v - i], data[v - i + 1], second);

      data.splice(v - i, 2, value);
      operators.splice(v - i, 1);
    });

    findAllIndex(operators, third).forEach((v, i) => {
      const value = calculate(data[v - i], data[v - i + 1], third);

      data.splice(v - i, 2, value);
      operators.splice(v - i, 1);
    });

    result.push(Math.abs(data.pop()));
  });

  return Math.max(...result);
}

console.log(solution('1+2*3+4-5'));
