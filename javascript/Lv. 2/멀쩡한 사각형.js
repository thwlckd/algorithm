// 대각선이 지나는 사각형 개수 공식 -> w * h - (w + h - gcd(w, h))

function gcd(a, b) {
  if (a < b) {
    let temp = a;
    a = b;
    b = temp;
  }

  if (b === 0) return a;

  return gcd(b, a % b);
}

function solution(w, h) {
  return w * h - (w + h - gcd(w, h));
}
