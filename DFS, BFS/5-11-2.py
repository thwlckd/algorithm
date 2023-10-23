from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] += graph[x][y]

    return graph[n - 1][m - 1]


print(bfs(0, 0))
