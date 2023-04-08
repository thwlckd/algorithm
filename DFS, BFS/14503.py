# 로봇 청소기
# 구현에 가까운 문제

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # NxM
x, y, d = map(int, input().split())  # 초기 좌표(x, y), 방향 d(0북, 1동, 2남, 3서)
if d == 1:
    d = 3
elif d == 3:
    d = 1
graph = []  # 청소 전 0, 벽 1, 청소 후 2 
for i in range(n):
    graph.append(list(map(int, input().split())))

# 북서남동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, d):
    q = deque()
    q.append((x, y, d))
    count = 0
    while q:
        check = False
        x, y, d = q.popleft()
        if graph[x][y] == 0:
            graph[x][y] = 2
            count += 1
            # print(x, y, d)
        elif graph[x][y] == 1:
            # print(x, y, d)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0:
                check = True
        if check == True:
            for i in range(4):
                nd = (d+1+i) % 4
                nx = x + dx[nd]
                ny = y + dy[nd]
                if graph[nx][ny] == 0:
                    q.append((nx, ny, nd))
                    break
        else:
            q.append((x - dx[d], y - dy[d], d))
    return count

print(bfs(x, y, d))
# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end=' ')
#     print()
'''
입력 예시
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
출력 예시
57
'''