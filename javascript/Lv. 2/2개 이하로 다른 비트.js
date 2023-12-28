// 시간 초과 풀이
function solution(numbers) {
  const result = [];

  numbers.forEach((number) => {
    let num = number;
    let originBinary = number.toString(2);

    while (true) {
      num++;
      const binary = num.toString(2);
      let diff = 0;

      if (binary.length > originBinary.length)
        originBinary = '0' + originBinary;

      for (let i = 0; i < binary.length; i++) {
        if (originBinary[i] !== binary[i]) diff++;
      }

      if (diff <= 2) {
        result.push(num);
        break;
      }
    }
  });

  return result;
}

// 이진수의 특성을 이용한 풀이 (2진 표기에서 두자리 이하로 바뀌는 가장 작은 수)
// 짝수일 경우: 짝수 + 1 -> 2진수로 표기할 때 마지막 자리만 1로 바뀜
// 홀수일 경우: 뒤에서 부터 01 찾아서 10으로 바꾸기
function solution(numbers) {
  const result = [];

  numbers.forEach((number) => {
    if (number % 2 === 0) result.push(number + 1);
    else {
      const binary = '0' + number.toString(2);
      let zeroIdx;

      for (let i = binary.length - 1; i >= 0; i--) {
        if (binary[i] === '0') {
          zeroIdx = i;
          break;
        }
      }

      result.push(
        parseInt(binary.slice(0, zeroIdx) + '10' + binary.slice(zeroIdx + 2), 2)
      );
    }
  });

  return result;
}
