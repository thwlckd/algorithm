function solution(cacheSize, cities) {
  const q = [];
  let result = 0;

  if (cacheSize === 0) return cities.length * 5;

  cities.forEach((city) => {
    const temp = city.toUpperCase();

    if (q.includes(temp)) {
      q.splice(q.indexOf(temp), 1);
      result += 1;
    } else if (q.length < cacheSize) {
      result += 5;
    } else {
      q.shift();
      result += 5;
    }

    q.push(temp);
  });

  return result;
}
