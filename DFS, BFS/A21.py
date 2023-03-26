# BFS
# 인구이동

from collections import deque

def bfs(x, y, index):
    united = []  # 한 연합의 연합국에 대한 좌표 리스트
    united.append((x, y))
    union[x][y] = index
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    sum = graph[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    sum += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = sum // count

    return count
    
n, l, r = map(int, input().split())  # NxN, 왼쪽 인구차이, 오른쪽 인구차이
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = 0
while True:
    union = [[-1]* n for _ in range(n)]  # 연합 관리 리스트(동일 연합: 동일한 값)
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n * n:
        break
    count += 1

print(count)

'''
입력 샘플 1
2 20 50
50 30
20 40
출력 샘플 1
1
입력 샘플 2
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
출력 샘플 2
3
'''