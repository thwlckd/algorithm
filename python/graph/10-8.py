# 그래프 이론
# 도시 분할 계획
# 크루스칼 -> 최소 신장 트리 -> 비용이 가장 큰 edge 제거

# 루트 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 그래프 합치기
def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())  # a-b 비용 c
    edges.append((c, a, b))

edges.sort()  # 비용 오름차순 정렬
result = 0
max = 0

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):  # 사이클 발생 하지 않는 조건
        union(parent, a, b)
        result += cost
        max = cost

print(result - max)

'''
입력 샘플
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
출력 샘플
'''
