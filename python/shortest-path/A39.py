# 최단 경로
# 다익스트라

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, n):
    q = []
    distance = [[INF] * n for _ in range(n)]  # 최단거리 테이블
    distance[0][0] = graph[0][0] 
    heapq.heappush(q, (graph[0][0], 0, 0))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        d, x, y = heapq.heappop(q)
        if distance[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                cost = d + graph[nx][ny]
                if cost < distance[nx][ny]:  # 더 짧은 경로 발견
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance[n-1][n-1]

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    result.append(dijkstra(graph, n))
print(result)


'''
입력 예시
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
출력 예시
20
19
36
'''