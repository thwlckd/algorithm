function solution(want, number, discount) {
  let result = 0;

  while (discount.length >= 10) {
    const data = discount.slice(discount.length - 10);
    const rest = [...number];

    data.forEach((v) => {
      const index = want.indexOf(v);

      if (index !== -1) rest[index]--;
    });

    result += rest.every((v) => v === 0) ? 1 : 0;

    discount.pop();
  }

  return result;
}
