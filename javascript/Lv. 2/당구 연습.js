function solution(m, n, startX, startY, balls) {
  return balls.map(([x1, y1]) => {
    const posibleCoor = [];

    if (startX !== x1 || startY > y1)
      posibleCoor.push([startX, 2 * n - startY]); // top
    if (startY !== y1 || startX > x1)
      posibleCoor.push([2 * m - startX, startY]); // right
    if (startX !== x1 || startY < y1) posibleCoor.push([startX, -startY]); // bottom
    if (startY !== y1 || startX < x1) posibleCoor.push([-startX, startY]); // left

    return posibleCoor.reduce(
      (distance, [x2, y2]) =>
        Math.min(distance, (x2 - x1) ** 2 + (y2 - y1) ** 2),
      Number.MAX_SAFE_INTEGER
    );
  });
}
