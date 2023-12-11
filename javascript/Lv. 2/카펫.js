function solution(brown, yellow) {
  for (let width = Math.floor((brown - 6) / 2); width > 0; width--) {
    if ((width * (brown - 4 - 2 * width)) / 2 === yellow)
      return [width + 2, (brown - 4 - 2 * width) / 2 + 2];
  }
}
