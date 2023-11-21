# BFS
# 특정 거리의 도시 찾기: 모든 가중치 1 -> BFS

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
                
INF = int(1e9)
n, e, length, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
distance[start] = 0
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([start])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == INF:
            q.append(next)
            distance[next] = distance[now] + 1

if length not in distance:
    print("-1")
else:
    for i in range(1, n + 1):
        if distance[i] == length:
            print(i)

'''
입력 샘플
4 4 2 1
1 2
1 3
2 3
2 4
출력 샘플
4
입력 샘플
4 3 2 1
1 2
1 3
1 4
출력 샘플
-1
'''