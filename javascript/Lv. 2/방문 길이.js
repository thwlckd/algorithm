function solution(dirs) {
  const step = { U: [0, 1], D: [0, -1], L: [-1, 0], R: [1, 0] };
  const routes = new Set();
  let x = 0;
  let y = 0;

  for (const dir of dirs) {
    let nx = x + step[dir][0];
    let ny = y + step[dir][1];

    if (nx < -5 || nx > 5 || ny < -5 || ny > 5) continue;

    routes.add(String([x, y, nx, ny]));
    routes.add(String([nx, ny, x, y]));

    x = nx;
    y = ny;
  }

  return routes.size / 2;
}
