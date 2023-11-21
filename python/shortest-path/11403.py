# 경로 찾기
# 플로이드-워셜
# 가중치 없는 방향 그래프

INF = int(1e9)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# Dij = OR(Dij, Dik AND Dkj): 0 or 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()

'''
입력 샘플
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
출력 샘플
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
'''