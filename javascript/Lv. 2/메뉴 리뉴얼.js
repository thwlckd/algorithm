const getCombinations = (arr, num) => {
  const results = [];

  if (num === 1) return arr.map((v) => [v]);

  arr.forEach((fixed, index, self) => {
    const rest = self.slice(index + 1);
    const combinations = getCombinations(rest, num - 1);
    const attached = combinations.map((v) => [fixed, ...v]);

    results.push(...attached);
  });

  return results;
};

function solution(orders, course) {
  const answer = [];

  course.forEach((num) => {
    const result = {};
    let max = 0;

    orders.forEach((order) => {
      const combinations = getCombinations(Array.from(order), num);

      combinations.forEach((combi) => {
        const key = combi.sort().join('');

        if (result[key]) result[key]++;
        else result[key] = 1;

        max = Math.max(max, result[key]);
      });
    });

    if (max >= 2) {
      Object.entries(result).forEach(([key, value]) => {
        if (value === max) answer.push(key);
      });
    }
  });

  return answer.sort();
}
