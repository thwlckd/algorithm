# 알파벳

import sys

input = sys.stdin.readline

row, column = map(int, input().split())
graph = []
for i in range(row):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = set()
visited.add(graph[0][0])
total = 1


def dfs(x, y, count):
    global total
    total = max(total, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (
            nx < 0
            or nx > row - 1
            or ny < 0
            or ny > column - 1
            or graph[nx][ny] in visited
        ):
            continue
        visited.add(graph[nx][ny])
        dfs(nx, ny, count + 1)
        visited.remove(graph[nx][ny])


dfs(0, 0, total)
print(total)
