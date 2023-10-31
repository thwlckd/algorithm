# 주사위 굴리기

n, m, x, y, k = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice = [0] * 6
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for c in commands:
    nx = x + dx[c - 1]
    ny = y + dy[c - 1]
    if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
        continue

    east, west, south, north, up, down = (
        dice[0],
        dice[1],
        dice[2],
        dice[3],
        dice[4],
        dice[5],
    )

    if c == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif c == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif c == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    else:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    if mtx[nx][ny] == 0:
        mtx[nx][ny] = dice[5]
    else:
        dice[5], mtx[nx][ny] = mtx[nx][ny], 0

    x, y = nx, ny
    print(dice[4])
