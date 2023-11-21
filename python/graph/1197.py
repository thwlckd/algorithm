# 최소 스패닝 트리
# 크루스칼 알고리즘(Kruskal): 최소 신장 트리 알고리즘(가중치 합이 최소인 신장 트리) 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

# 루트 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# a-b가 속한 집합 union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())  # vertex, edge
parent = [0] * (v + 1)
edges = []
result = 0
for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용순으로 정렬하기 위해 [0]: cost

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):  # 사이클 미발생 조건
        union_parent(parent, a, b)
        result += cost
        
print(result)

'''
입력 샘플
3 3
1 2 1
2 3 2
1 3 3

출력 샘플
3
'''