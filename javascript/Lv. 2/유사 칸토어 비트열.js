function check(num) {
  if (num % 5 === 2) return false;
  else if (num < 5) return true;

  return check(Math.floor(num / 5));
}

function solution(n, l, r) {
  let result = 0;

  for (let i = l - 1; i < r; i++) {
    if (check(i)) result++;
  }

  return result;
}
