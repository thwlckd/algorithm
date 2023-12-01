function solution(str1, str2) {
  str1 = str1.toUpperCase();
  str2 = str2.toUpperCase();

  const set1 = {};
  const set2 = {};
  const regEx = /^[A-Z]*$/;

  for (let i = 0; i < str1.length - 1; i++) {
    const temp = str1[i] + str1[i + 1];
    if (!regEx.test(temp)) continue;

    set1[temp] ? (set1[temp] += 1) : (set1[temp] = 1);
  }

  for (let i = 0; i < str2.length - 1; i++) {
    const temp = str2[i] + str2[i + 1];
    if (!regEx.test(temp)) continue;

    set2[temp] ? (set2[temp] += 1) : (set2[temp] = 1);
  }

  const dividend = Object.entries(set1).reduce(
    (acc, [key, value]) =>
      key in set2 ? acc + Math.min(value, set2[key]) : acc,
    0
  );

  let divisor = 0;
  Object.entries(set1).forEach(([key, value]) => {
    key in set2
      ? (divisor += Math.max(value, set2[key]))
      : (divisor += set1[key]);
  });
  Object.entries(set2).forEach(([key, value]) => {
    if (!(key in set1)) divisor += value;
  });

  return divisor ? Math.floor((dividend / divisor) * 65536) : 65536;
}
