function isPrime(n) {
  if (n <= 1) return false;

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }

  return true;
}

function dfs(arr, str, set) {
  if (isPrime(Number(str))) set.add(Number(str));

  if (arr.length < 1) return;

  for (let i = 0; i < arr.length; i++) {
    const newArr = [...arr];
    const newStr = str + newArr.splice(i, 1);

    dfs(newArr, newStr, set);
  }

  return set;
}

function solution(numbers) {
  const primeSet = dfs(numbers.split(''), '', new Set());

  return primeSet.size;
}
