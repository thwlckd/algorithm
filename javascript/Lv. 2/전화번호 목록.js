function solution(phone_book) {
  phone_book.sort();

  for (let i = 1; i < phone_book.length; i++) {
    const prefix = phone_book[i - 1];
    if (phone_book[i].slice(0, prefix.length) === prefix) return false;
  }

  return true;
}

// 참고용 풀이
function solution(phone_book) {
  const result = phone_book
    .sort()
    .some((v, i, arr) => arr[i + 1]?.indexOf(v) === 0);

  return !result;
}
