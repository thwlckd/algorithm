# 네트워크 연결
# 최소 신장 트리 -> 크루스칼

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = int(input())
graph = [[] for i in range(v + 1)]
edge = []
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i
for i in range(e):
    a, b, c = map(int, input().split())  # a-b 비용 c
    edge.append((c, a, b))

edge.sort()
result = 0
for now in edge:
    cost, a, b = now
    if find(a) != find(b):  # 사이클 발생 하지 않을 조건
        result += cost
        union(a, b)

print(result)

'''
입력 샘플
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
출력 샘플
23
'''