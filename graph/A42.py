# 그래프 이론
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
        root[x] = y

g = int(input())
p = int(input())
g_list = []
for _ in range(p):
    g_list.append(int(input()))
root = [0] * (g + 1)
for i in range(g + 1):
    root[i] = i
cnt = 0
for gate in g_list:
    root_gate = find(root, gate)
    if root_gate != 0:
        union(root, root_gate, root_gate - 1)
        cnt += 1
    else:
        print(cnt)
        break

'''
입력 샘플
4
6
2
2
3
3
4
4
출력 샘플
'''