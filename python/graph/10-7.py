# 그래프 이론
# 팀 결성
# 서로소 집합: union,find

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for i in range(m):
    func, a, b = map(int, input().split())  # func 0: union / 1: find
    if func == 0:
        union(parent, a, b)
    elif func == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
    else:
        break

'''
입력 샘플
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
출력 샘플
NO
NO
YES
'''    