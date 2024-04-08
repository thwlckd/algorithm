function solution(storey) {
  let result = 0;
  let rest = storey;

  while (rest > 0) {
    const now = rest % 10;

    if (now > 5) {
      result += 10 - now;
      rest += 10 - now;
    } else if (now < 5) {
      result += now;
      rest -= now;
    } else {
      const next = Math.floor(rest / 10) % 10;

      result += now;
      rest += next >= 5 ? now : -now;
    }

    rest /= 10;
  }

  return result;
}
