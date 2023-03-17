# BFS
# 경쟁적 전염

from collections import deque

n, k = map(int, input().split())  # NxN, 1~k 바이러스
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()  # 낮은 번호의 바이러스가 먼저 증식
q = deque(data)

target_s, target_x, target_y = map(int, input().split())  # s초, (x, y)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])

'''
입력 샘플 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2
출력 샘플 1
3
입력 샘플 2
3 3
1 0 2
0 0 0
3 0 0
1 2 2
출력 샘플 2
0
'''