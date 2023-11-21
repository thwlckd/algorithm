# 최단 경로
# 플로이드 워셜
# O(V^3)

INF = int(1e9)
n, m = map(int, input().split())  # 노드, 간선
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자신에 대한 거리 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b까지 거리 c
    graph[a][b] = c

# Dij = min(Dik, Dik + Dkj)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

'''
입력 예시
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력 예시
0 4 8 6 
3 0 7 9
5 9 0 4
7 11 2 0
'''