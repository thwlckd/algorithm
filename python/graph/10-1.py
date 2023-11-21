# 그래프 이론
# 서로소 집합 알고리즘: union / find 수행
# 루트를 찾기 위해서 재귀적으로 부모를 거슬러 올라감

# 특정 원소가 속한 집합(루트) 찾기
# 경로 압축 기법
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속합 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 자신을 부모로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()
print("부모 테이블: ", end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
입력 샘플
6 4
1 4
2 3
2 4
5 6

출력 샘플
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 1 1 5 5
'''