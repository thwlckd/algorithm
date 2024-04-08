function solution(weights) {
  const store = {};
  const multiple = [1, 4 / 3, 3 / 2, 2];
  const sortedWeights = weights.sort((a, b) => a - b);
  let result = 0;

  for (const weight of weights) {
    if (store[weight]) store[weight]++;
    else store[weight] = 1;
  }

  for (const weight of sortedWeights) {
    store[weight] -= 1;

    multiple.forEach((mul) => {
      const key = weight * mul;

      if (store[key]) {
        result += store[key];
      }
    });
  }

  return result;
}
