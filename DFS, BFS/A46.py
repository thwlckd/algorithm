# BFS
# 아기 상어

from collections import deque
                
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[now_x][now_y] = 0
size = 2

# 최단거리 테이블 구하기
def bfs():
    q = deque()
    # 상 좌 우 하
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    x, y = now_x, now_y
    q.append((x, y))  # 현재 좌표
    distance = [[-1] * n for _ in range(n)]
    distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] == -1 and graph[nx][ny] <= size:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    return distance

# 다음으로 먹을 물고기 찾기
def find(distance):
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= graph[i][j] < size:  # 방문 가능 and 먹을 수 있는 사이즈
                if distance[i][j] < min_dist:
                    min_dist = distance[i][j]
                    x, y = i, j
    if min_dist == 1e9:
        return None
    return x, y, min_dist

result = 0
ate = 0
while True:
    next = find(bfs())
    if next == None:
        print(result)
        break
    else:
        now_x, now_y = next[0], next[1]
        ate += 1
        result += next[2]
        graph[now_x][now_y] = 0
        if ate >= size:
            ate = 0
            size += 1

'''
입력 예시
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
출력 예시
14
'''