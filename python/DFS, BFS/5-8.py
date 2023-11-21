# DFS: 스택, 재귀 함수 이용 / 해당 분기 완벽 탐색 후 다음 분기로 넘어가는 방식 ex) 경로의 특징을 저장하는 문제
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원)
visited = [False] * 9

# DFS 함수 호출
dfs(graph, 1, visited)



# def dfs(tree, node, visited):
#     visited[node] = True
#     print(node, end=" ")
#     for i in tree[node]:
#         if visited[i] == False:
#             dfs(tree, i, visited)

# tree = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9
# dfs(tree, 1, visited)
