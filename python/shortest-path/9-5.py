# 최단 경로
# 전보
# 다익스트라
# 1 <= N <= 30000, 1 <= M <= 200000 -> 우선순위 큐 사용

import heapq

INF = int(1e9)
n, m, start = map(int, input().split())  # 노드, 간선, 출발자
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b까지 c거리
    graph[a].append((b, c))

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 인접 노드 탐색
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra()

count = 0
max_dist = 0
for i in distance:
    if i != INF:
        count += 1
        max_dist = max(max_dist, i)
        # if i > max_dist:
        #     max_dist = i
print("{} {}".format(count - 1, max_dist))

'''
입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
'''