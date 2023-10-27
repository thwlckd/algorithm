# 정확한 순위
# 2회차

from collections import Counter

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [True] * n
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (graph[i][j], graph[j][i]) == (INF, INF):
            result[i - 1] = False
            break

counter = Counter(result)
print(counter[True])
