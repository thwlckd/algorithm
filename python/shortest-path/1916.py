# 최소비용 구하기
# 다익스트라

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())  # 도시 개수
m = int(input())  # 버스 개수
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())  # 출발도시, 도착도시, 거리
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:  # 현재 노드를 지나는 더 짧은 경로를 알고 있음
            continue
        # 인접 노드 탐색
        for v, e in graph[now]:
            cost = dist + e
            if cost < distance[v]:  # 인접 노드를 경유하는 더 짧은 경로 발견
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra()
print(distance[end])

'''
입력 샘플
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
출력 샘플
4
'''