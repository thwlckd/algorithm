# 파티

import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for adjacent in graph[now]:
            cost = adjacent[1] + dist
            if cost < distance[adjacent[0]]:
                distance[adjacent[0]] = cost
                heapq.heappush(heap, (cost, adjacent[0]))

    return distance


total = 0
back = dijkstra(x)
for i in range(1, n + 1):
    go = dijkstra(i)
    total = max(total, go[x] + back[i])

print(total)
