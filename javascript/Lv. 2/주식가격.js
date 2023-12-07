function solution(prices) {
  const result = [];

  for (let i = 0; i < prices.length; i++) {
    let temp = 0;

    for (let j = i + 1; j < prices.length; j++) {
      temp++;
      if (prices[i] > prices[j]) break;
    }

    result.push(temp);
  }

  return result;
}
