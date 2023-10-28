# 벽 부수고 이동하기

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


def bfs():
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([(0, 0, 0)])
    while q:
        x, y, flag = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][flag]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if graph[nx][ny] == 1 and flag == 0:
                q.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1
            elif graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                q.append((nx, ny, flag))
                visited[nx][ny][flag] = visited[x][y][flag] + 1
    return -1


print(bfs())
