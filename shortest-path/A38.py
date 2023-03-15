# 최단 경로
# 플로이드 워셜

from collections import Counter
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for i in range(1, n + 1):
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

'''
입력 샘플
6 6
1 5
3 4
4 2
4 6
5 2
5 4
출력 샘플'''

