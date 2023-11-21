# DP
# 병사 배치하기
# LIS(Longest Increasing Subsequence): 값들이 증가하는 형태의 가장 긴 부분 수열
# D[i] = max(D[i], D[j] + 1) if array[j] < array[i]  ->  D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이


n = int(input())
array = list(map(int, input().split()))
array.reverse()  # 순서를 뒤집어 LIS 문제로 변환
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))

'''
입력 샘플
7
15 11 4 8 5 2 4
출력 샘플
2
'''