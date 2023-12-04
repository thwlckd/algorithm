function solution(msg) {
  const dict = {};
  const arr = Array.from(msg);
  const result = [];

  for (let i = 1; i < 27; i++) dict[String.fromCharCode(i + 64)] = i;

  let temp = '';
  for (let i = 1; i <= arr.length; i++) {
    temp += arr[i - 1];

    if (i < arr.length && temp + arr[i] in dict) continue;

    result.push(dict[temp]);
    dict[temp + arr[i]] = Object.keys(dict).length + 1;
    temp = '';
  }

  return result;
}
