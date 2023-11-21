# 최단 경로
# 미래 도시: 1 -> k -> x 최단 거리
# 플로이드 워셜
# 1 <= N, M <= 100 -> 입력 작음 -> 구현이 간단한 플로이드 워셜 사용

INF = int(1e9)
n, m = map(int, input().split())  # 노드, 간선
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())  # 연결된 두 회사의 번호(egde = 1, 양방향 연결)
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, input().split())  # 1 -> k -> x 

# Dij = min(Dij, Dik + Dkj)
for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

'''
입력 예시
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력 예시
3
'''