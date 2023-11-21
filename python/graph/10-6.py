# 그래프 이론
# 위상 정렬(Topology Sort): 방향 그래프를 방향성에 맞게 순서대로 나열, 순서가 정해진 일련의 작업을 차례로 수행
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클 존재
# 여러 가지 답안 존재 가능
# O(V + E)
'''
1. 진입차수가 0인 노드를 큐에 삽입
2. 큐가 빌 때까지 다음 과정 반복
 1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
 2) 새롭게 진입차수가 0이 된 노드를 큐에 삽입
'''

from collections import deque

v, e = map(int , input().split())
indegree = [0] * (v + 1)  # 진입차수
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append((b))  # a -> b
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이된 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()

'''
입력 샘플
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

출력 샘플
1 2 5 3 6 4 7
'''
