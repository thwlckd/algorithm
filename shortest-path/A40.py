# 숨바꼭질
# 다익스트라

import heapq
import sys
from collections import Counter
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

dijkstra()

cost = max(distance[1:])
counter = Counter(distance)
print(distance)
print(distance.index(cost), cost, counter[cost])

# # BFS 구현
# from collections import deque, Counter
# INF = int(1e9)

# def bfs():
#     q = deque()
#     for i in range(len(graph[1])):
#         q.append(graph[1][i])
#     distance = [INF] * (n + 1)
#     distance[1] = 0
#     for i in range(len(graph[1])):
#         distance[graph[1][i]] = 1
#     cost = 2
#     while q:
#         now = q.popleft()
#         cost = distance[now]
#         for i in range(len(graph[now])):
#             if distance[graph[now][i]] <= cost:  # 이미 더 짧은 경로에 대해 처리 완료
#                 continue
#             q.append(graph[now][i])
#             distance[graph[now][i]] = cost + 1
#             print("distance[{}] = {}".format(graph[now][i], cost + 1))
#     return distance


# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# result = bfs()
# cost = max(result[1:])
# counter = Counter(result)
# print(result)
# print(result.index(cost), cost, counter[cost])

'''
입력 예시
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
출력 예시
4 2 3
'''