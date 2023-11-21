# BFS: 큐, 큐 자료구조 이용 / 루트에서 인접한 노드부터 탐색하는 방식 ex) 미로찾기, 최단거리 문제
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

from collections import deque

def bfs(graph, start, visited):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 노드와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

# BFS 함수 호출
bfs(graph, 1, visited)



# from collections import deque

# def bfs(graph, node, visited):
#     visited[node] = True
#     queue = deque([node])
#     while(len(queue) != 0):
#         for i in graph[queue[0]]:
#             if visited[i] == False:
#                 queue.append(i)
#                 visited[i] = True
#         print(queue[0], end=' ')
#         queue.popleft()

# graph = [
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

# bfs(graph, 1, visited)
