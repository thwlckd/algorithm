function solution(cards) {
  const visited = Array.from({ length: cards.length + 1 }).fill(-1);
  const result = [];
  let group = [];
  let index = cards[0];
  visited[0] = 1;

  while (index !== -1) {
    if (visited[index] === -1) {
      group.push(cards[index - 1]);
      visited[index] = 1;
      index = cards[index - 1];
    } else {
      result.push(group);
      group = [];
      index = visited.indexOf(-1);
    }
  }

  result.sort((a, b) => b.length - a.length);

  return result.length > 1 ? result[0].length * result[1].length : 0;
}
