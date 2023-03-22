# 그래프
# 행성 터널
# 크루스칼
# 터널을 연결할 때 드는 비용 = min(|x1-x2|, |y1-y2|, |z1-z2|) -> x, y, z 각 좌표축 별로 최소 비용으로 정렬한것들의 N-1번째 까지의 값들의 합

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

n = int(input())

x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, input().split())
    # x, y, z 각각에 대해 임의의 루트 번호 지정
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

parent = [0] * n
for i in range(n):
    parent[i] = i

x.sort()
y.sort()
z.sort()

edges = []
for i in range(1, n):
    edges.append((abs(x[i][0]-x[i-1][0]), x[i-1][1], x[i][1]))
    edges.append((abs(y[i][0]-y[i-1][0]), y[i-1][1], y[i][1]))
    edges.append((abs(z[i][0]-z[i-1][0]), z[i-1][1], z[i][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)

'''
입력 예시
5
11 -15 -15
14 -5 -15
-1 -1 -5
20 -4 -1
19 -4 19
출력 예시
4
'''