# 그래프 이론
# 서로소 집합을 이용한 무방향 그래프 사이클 판별

# 루트 찾기
# 경로 압축 기법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# a-b union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())  # vertex, edge
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

cycle = False
# 입력에 대한 union
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):  # 사이클 발생시 종료
        cycle = True
        break
    else:  
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 없음")
'''
입력 샘플
3 3
1 2
1 3
2 3

출력 샘플
사이클 발생
'''


