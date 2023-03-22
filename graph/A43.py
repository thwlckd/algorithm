# 그래프
# 어두운 길
# 크루스칼

def find(root, x):
    if root[x] != x:
        root[x] = find(root, root[x])
    return root[x]

def union(root, x, y):
    x = find(root, x)
    y = find(root, y)
    if x < y:
        root[y] = x
    else:
        root[x] = y

v, e = map(int, input().split())
graph = []
sum = 0
for i in range(e):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
    sum += cost
parent = [0] * v
for i in range(v):
    parent[i] = i

graph.sort()

result = 0
for now in graph:
    c, x, y = now
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += c
print(sum-result)

'''
입력 예시
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
출력 예시
51
'''