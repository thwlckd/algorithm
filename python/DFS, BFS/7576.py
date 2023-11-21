# 토마토

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

done = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            done.append((i, j, 0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque(done)
count = 0
while q:
    x, y, count = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            q.append((nx, ny, count + 1))

flag = False
for now in graph:
    if 0 in now:
        flag = True
        break

print(-1) if flag else print(count)
