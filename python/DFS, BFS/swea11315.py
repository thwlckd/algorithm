# 오목 판정

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(x, y, d, count):
    global result
    if graph[x][y] == ".":
        return
    if count >= 5:
        result = "YES"
        return

    nx = dx[d] + x
    ny = dy[d] + y
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return
    dfs(nx, ny, d, count + 1)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = list(input() for _ in range(n))
    result = "NO"
    for i in range(n):
        for j in range(n):
            for k in range(8):
                dfs(i, j, k, 1 if graph[i][j] == "o" else 0)

    print(f"#{test_case} {result}")
