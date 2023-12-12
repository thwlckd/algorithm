function solution(people, limit) {
  let result = 0;

  people.sort((a, b) => a - b);

  while (people.length > 0) {
    if (people.pop() + people[0] <= limit) people.shift();

    result++;
  }

  return result;
}
