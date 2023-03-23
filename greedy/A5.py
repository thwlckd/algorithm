# 그리디
# 볼링공 고르기

# n, m = map(int, input().split())
# weight = list(map(int, input().split()))

# count = 0
# memo = [[False] * n for _ in range(n)]
# for i in range(n):
#     for j in range(i+1, n):
#         if weight[i] != weight[j] and memo[i][j] == False:
#             memo[i][j] = True
#             count += 1

# print(count)

# 무게별 경우의 수 = A가 고른 공과 무게가 같은 공의 개수 * B가 선택 가능한 경우의 수
n, m = map(int, input().split())
weight = list(map(int, input().split()))

array = [0] * 11  # 1~10 무게를 담을 수 있는 리스트
for x in weight:
    array[x] += 1  # 무게별 볼링공 카운트

count = 0
for i in range(1, m+1):
    n -= array[i]  # B 선택 경우의 수
    count += array[i] * n
print(count)

'''
입력 예시 1
5 3
1 3 2 3 2
출력 예시 1
8
입력 예시 2
8 5
1 5 4 3 2 4 5 2
출력 예시 2
25
'''