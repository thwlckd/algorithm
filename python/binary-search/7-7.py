# 이진 탐색
# 부품 찾기
# 집합을 이용한 풀이

n = int(input())
n_data = set(map(int, input().split()))
m = int(input())
m_data = list(map(int, input().split()))

for i in m_data:
    if i in n_data:
        print("yes", end=' ')
    else:
        print("no", end=' ')