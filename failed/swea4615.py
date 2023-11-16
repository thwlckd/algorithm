# 재미있는 오셀로 게임


def conquer(x, y, color, d):
    global flag
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        return

    if not mtx[nx][nx]:
        return

    if mtx[nx][ny] == color:
        flag = True
        return

    toggle.append([nx, ny])
    conquer(nx, ny, color, d)


def count_color():
    black = 0
    white = 0
    for i in range(N + 1):
        for j in range(N + 1):
            if mtx[i][j] == "B":
                black += 1
            elif mtx[i][j] == "W":
                white += 1
    return black, white


T = int(input())

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    mtx = [[False] * (N + 1) for _ in range(N + 1)]
    center = N // 2
    mtx[center][center], mtx[center + 1][center + 1] = "W", "W"
    mtx[center][center + 1], mtx[center + 1][center] = "B", "B"
    for _ in range(M):
        x, y, color = map(int, input().split())
        color = "B" if color == 1 else "W"
        mtx[x][y] = color
        for i in range(8):
            flag = False
            toggle = []
            conquer(x, y, color, i)
            if flag:
                for coor in toggle:
                    mtx[coor[0]][coor[1]] = color
    black, white = count_color()
    print(f"#{test_case} {black} {white}")
