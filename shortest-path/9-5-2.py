# 전보

import heapq

n, m, city = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
INF = int(1e9)
distance = [INF] * (n + 1)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue
        for adjacent in graph[node]:
            cost = adjacent[1] + dist
            if distance[adjacent[0]] > cost:
                distance[adjacent[0]] = cost
                heapq.heappush(heap, (cost, adjacent[0]))


dijkstra(city)
count = -1
total = 0
for i in range(1, n + 1):
    if distance[i] != INF:
        count += 1
        total = max(total, distance[i])

print(count, total)
