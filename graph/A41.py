# 그래프 이론 문제
# 서로소 집합

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
        root[x] == y

v, e = map(int, input().split())
graph = [[] for i in range(v + 1)]
root = [0] * (v + 1)
for i in range(1, v + 1):
    root[i] = i

for i in range(1, v + 1):
    graph[i].append(0)
    graph[i] = graph[i] + list(map(int, input().split()))
plan = list(map(int, input().split()))

for i in range(1, v + 1):
    for j in range(i + 1, v + 1):
        if graph[i][j] == 1:
            union(root, i, j)

result = "YES"
for i in range(1, len(plan)):
    if find(root, plan[i]) != find(root, plan[i-1]):
        result = "NO"
        break

print(result)

'''
입력 예제
5 4
0 1 0 1 1 
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
출력 예제
YES
'''