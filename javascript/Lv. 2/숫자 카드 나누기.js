function gcd(a, b) {
  if (a < b) {
    const temp = a;

    a = b;
    b = temp;
  }

  const remainder = a % b;

  return remainder === 0 ? b : gcd(b, remainder);
}

function solution(arrayA, arrayB) {
  let answer = 0;

  const gcdA = arrayA.reduce((acc, v) => (acc = gcd(acc, v)), arrayA[0]);
  const gcdB = arrayB.reduce((acc, v) => (acc = gcd(acc, v)), arrayB[0]);

  if (arrayB.every((v) => v % gcdA !== 0)) answer = gcdA;
  if (arrayA.every((v) => v % gcdB !== 0)) answer = Math.max(answer, gcdB);

  return answer;
}
