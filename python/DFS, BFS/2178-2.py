# 미로 탐색
# dfs 풀이 -> 지수 시간 복잡도로 시간 초과 나지만 구현 가능

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = int(1e6)


def dfs(x, y, count):
    global total
    if x == n - 1 and y == m - 1:
        total = min(total, count)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                dfs(nx, ny, count + 1)
                graph[nx][ny] = 1


dfs(0, 0, 1)
print(total)
