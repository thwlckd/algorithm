function solution(numbers, target) {
  let result = 0;

  function dfs(acc, depth) {
    if (numbers.length === depth) {
      if (acc === target) result++;
      return;
    }

    dfs(acc + numbers[depth], depth + 1);
    dfs(acc - numbers[depth], depth + 1);
  }

  dfs(0, 0);

  return result;
}
