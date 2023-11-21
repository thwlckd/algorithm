# 적록색약

import sys

sys.setrecursionlimit(int(1e6))

n = int(input())
graph = []
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, visited, flag):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 or visited[nx][ny]:
            continue
        if flag:
            if graph[nx][ny] == graph[x][y]:
                dfs(nx, ny, visited, True)
        else:
            if (
                graph[nx][ny] == graph[x][y]
                or graph[x][y] in ["R", "G"]
                and graph[nx][ny] in ["R", "G"]
            ):
                dfs(nx, ny, visited, False)


count1 = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs(i, j, visited1, True)
            count1 += 1
        if not visited2[i][j]:
            dfs(i, j, visited2, False)
            count2 += 1

print(count1, count2)
