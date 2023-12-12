function solution(number, k) {
  const stack = [];

  for (const num of number) {
    while (k > 0 && stack.at(-1) < num) {
      stack.pop();
      k--;
    }

    stack.push(num);
  }

  return stack.join('').slice(0, stack.length - k);
}
