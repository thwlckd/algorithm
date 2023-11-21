# BFS
# 미로 탈출: 최단거리(누적거리) 찾기

from collections import deque

n, m = map(int, input().split())
graph = list()
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()  # 현재 방문 노드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:  # 처음 방문하는 경우
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1  # 거리 누적
    # for i in range(n):
    #     for j in range(m):
    #         print("{:<3}".format(graph[i][j]), end='')
    #     print()
    return graph[n-1][m-1]

print(bfs(0,0))


# from collections import deque

# n, m = map(int, input().split())
# mtx = list()
# for i in range(n):
#     mtx.append(list(map(int, input())))

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(graph, x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         print(queue)
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 continue
#             elif graph[nx][ny] == 0:
#                 continue
#             elif graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph

# mtx = bfs(mtx, 0, 0)
# print(mtx)
# print(mtx[n-1][m-1])
