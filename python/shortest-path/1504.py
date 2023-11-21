# 특정하나 최단 경로

import heapq
import sys

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
u, v = map(int, input().split())
INF = int(1e9)


def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    if start == end:
        return 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for adjacent in graph[now]:
            cost = adjacent[1] + dist
            if cost < distance[adjacent[0]]:
                distance[adjacent[0]] = cost
                heapq.heappush(q, (cost, adjacent[0]))
    return distance[end]


path1 = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, n)
path2 = dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, n)
path = min(path1, path2)
print(path) if path < INF else print(-1)
