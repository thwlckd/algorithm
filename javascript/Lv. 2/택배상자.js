function solution(order) {
  const stack = [];
  let result = 0;
  let index = 0;

  for (let i = 1; i <= order.length; i++) {
    if (order[index] === i) {
      result++;
      index++;
    } else {
      stack.push(i);
    }

    while (stack.length > 0 && stack.at(-1) === order[index]) {
      stack.pop();
      result++;
      index++;
    }
  }

  return result;
}
