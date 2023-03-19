# DP
# 퇴사
# dp[i] = max(p[i] + dp[t[i]] + i], max_value)  ->  max_value: 뒤에서 부터 계산할 때, 현재까지의 최대 상담 금액

n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 리스트 뒤에서부터 진행되는 DP
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)  # dp[time]: 현재 상담을 마친 일자부터의 최대 이윤
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)

'''
입력 예시 1
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
출력 예시 1
45
입력 예시 2
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
출력 예시 2
55
'''