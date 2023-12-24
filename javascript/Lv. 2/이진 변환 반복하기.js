function solution(s) {
  const result = [0, 0];

  while (s.length > 1) {
    const beforeLength = s.length;
    const temp = s.replaceAll('0', '');

    s = temp.length.toString(2);

    result[0]++;
    result[1] += beforeLength - temp.length;
  }

  return result;
}
