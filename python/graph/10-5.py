# 그래프 이론
# 신장 트리(spanning tree): 모든 노드를 포함하면서 사이클이 존재하지 않는 그래프
# 크루스칼 알고리즘(Kruskal): 최소 신장 트리 알고리즘(가중치 합이 최소인 신장 트리) 
# O(ElogE)
'''
1. 비용에 따라 간선 오름차순 정렬
2. 비용이 적은 간선부터 사이클 발생 유무 확인(그리디)
 1) 사이클 x: 트리에 추가(union)
 2) 사이클 o: 트리에 추가 x(continue)
3. 모든 간선에 대해 2. 반복
'''

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
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25 

출력 샘플
159
'''