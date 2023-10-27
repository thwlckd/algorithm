# 미래 도시
# 2회차

n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

destination, midpoint = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance1 = graph[1][midpoint]
distance2 = graph[midpoint][destination]
if distance1 != INF and distance2 != INF:
    print(distance1 + distance2)
else:
    print(-1)
