# DFS
# 청소년 상어

import sys
import copy
sys.setrecursionlimit(int(1e6))

n = 4
graph = [[0] * n for _ in range(n)]  # 맵
direction = [[0] * n for _ in range(n)]  # 맵에서 번호별 방향
data = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n*2):
        if j % 2 == 0:
            graph[i][j//2] = data[j]
        else:
            direction[i][j//2] = data[j]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(graph, index):
    for i in range(4):
        for j in range(4):
            if graph[i][j] == index:
                return (i, j)
    return -1

# 물고기 이동
def move_fish(graph, direction, shark_x, shark_y):
    for i in range(1, 17):
        pos = find_fish(graph, i)
        if pos == -1:
            continue
        x, y = pos[0], pos[1]
        step = direction[x][y]
        for j in range(8):
            nx = x + dx[(j+step-1)%8]
            ny = y + dy[(j+step-1)%8]
            if 0 <= nx < n and 0 <= ny < n:  # 이동 가능한 경우
                if (nx, ny) != (shark_x, shark_y):
                    next = graph[nx][ny]
                    direction[x][y] = (j+step-1)%8+1
                    # 물고기 위치, 방향 교환
                    graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                    direction[nx][ny], direction[x][y] = direction[x][y], direction[nx][ny]
                    break

# 이동 가능한 상어 위치 찾기
def find_shark(graph, direction, x, y):
    pos = []
    step = direction[x][y]
    for _ in range(4):
        x += dx[step-1]
        y += dy[step-1]
        if 0 <= x < n and 0 <= y < n and graph[x][y] != -1:
            pos.append((x, y))
    return pos

result = 0
# 상어 이동 / DFS
def move_shark(graph, direction, x, y, ate):
    global result
    graph = copy.deepcopy(graph)
    direction = copy.deepcopy(direction)

    ate += graph[x][y]
    graph[x][y] = -1
    
    move_fish(graph, direction, x, y)
    # print(graph, "move_fish")
    # print(direction, "direction")
    positions = find_shark(graph, direction, x, y)

    # 상어 이동 불가
    if len(positions) == 0:
        result = max(result, ate)
        return
    
    # 상어의 이동 가능 경로 DFS
    for nx, ny in positions:
        move_shark(graph, direction, nx, ny, ate)
    
move_shark(graph, direction, 0, 0, 0)
print(result)


'''
입력 예시 1
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
출력 예시 1
33
입력 예시 2
2 6 10 8 6 7 9 4
1 7 16 6 4 2 5 8
3 7 8 6 7 6 14 8
12 7 15 4 11 3 13 3
출력 예시 2
39
'''