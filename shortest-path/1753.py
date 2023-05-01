# 최단경로
# 다익스트라

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for i in range(e):
    a, b, c = map(int, input().split())  # a에서 b까지 거리 c
    graph[a].append((b, c))

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:  # 현재 노드를 지나는 더 짧은 경로를 알고 있음
            continue
        # 인접 노드 탐색
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 인접 노드를 경유하는 더 짧은 경로 발견
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra()
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
입력 샘플
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

출력 샘플
0
2
3
7
INF
'''