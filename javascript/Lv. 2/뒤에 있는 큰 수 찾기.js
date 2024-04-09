function solution(numbers) {
  const result = Array.from({ length: numbers.length }, () => -1);
  const stack = [0]; // index 저장용

  for (let i = 1; i < numbers.length; i++) {
    while (numbers[stack.at(-1)] < numbers[i]) {
      result[stack.pop()] = numbers[i];
    }

    stack.push(i);
  }

  return result;
}
