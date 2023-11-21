# DFS
# 음료수 얼려먹기: 묶음 개수 찾기

n, m = map(int, input().split())

# 2차원 맵 받아오기
graph = list()
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 현재 방문 노드 방문 후 상하좌우 연결 노드 방문
# 한번의 dfs() 호출로 연결된 모든 노드 방문 처리 -> 함수 반환 값으로 노드 묶음 개수 파악
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1  # 현재 노드 방문 처리
        # 재귀적으로 상하좌우 노드에 대한 방문 처리, 반환 값에 영향 x
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)


# n, m = map(int, input().split())
# mtx = []
# for _ in range(n):
#     mtx.append(list(map(int, input().split())))

# def dfs(graph, x, y):
#     if x < 0 or x > n - 1 or y < 0 or y > m - 1:
#         return False
#     elif graph[x][y] != 0:
#         return False
#     else:
#         graph[x][y] = 1
#         dfs(graph, x - 1, y)
#         dfs(graph, x + 1, y)
#         dfs(graph, x, y - 1)
#         dfs(graph, x, y + 1)
#         return True
    
# count = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(mtx, i, j) == True:
#             count += 1

# print(count)
