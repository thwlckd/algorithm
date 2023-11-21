# 미로 탐색
# bfs 풀이

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append([0, 0, 1])
while q:
    x, y, count = q.popleft()
    if x == n - 1 and y == m - 1:
        print(count)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
            if graph[nx][ny] == 1:
                q.append((nx, ny, count + 1))
                graph[nx][ny] = 2  # visited
