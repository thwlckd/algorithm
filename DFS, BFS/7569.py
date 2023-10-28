# 토마토

from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))

done = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                done.append((i, j, k, 0))
q = deque(done)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
count = 0
while q:
    z, x, y, count = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or nz < 0 or nz > h - 1:
            continue
        if graph[nz][nx][ny] == 0:
            q.append((nz, nx, ny, count + 1))
            graph[nz][nx][ny] = 1

flag = True
for i in range(h):
    for j in range(n):
        for h in range(m):
            if graph[i][j][h] == 0:
                flag = False

print(count) if flag else print(-1)
