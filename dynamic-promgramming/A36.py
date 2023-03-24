# DP
# 편집 거리
# dp[i][j]: 최소 편집 거리를 담을 2차원 테이블
# dp[i][j] = dp[i-1][j-1]: 행과 열에 해당하는 문자가 같으면, 왼쪽 위에 해당하는 수를 그대로 대입
# dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]): 행과 열에 해당하는 문자가 서로 다르면, 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당하는 수 중에서 가장 작은 수에 1을 더해 대입

s1 = input()
s2 = input()
n1 = len(s1)
n2 = len(s2)

dp = [[0] * (n2+1) for _ in range(n1+1)]
for i in range(n2+1):  # 1행 초기화
    dp[0][i] = i
for i in range(n1+1):  # 1열 초기화
    dp[i][0] = i

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
            
print(dp[n1][n2])

'''
입력 샘플 1
cat
cut
출력 샘플 1
1
입력 샘플 2
sunday
saturday
출력 샘플 2
3
'''