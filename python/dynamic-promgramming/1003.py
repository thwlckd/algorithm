# dp
# 케이스 나열해 보기 -> 규칙 찾기

t = int(input())  # 테스트 케이스

dp = [0, 1, 1]
for i in range(3, 41):
  dp.append(dp[i-1] + dp[i-2])  # 0와 1의 출력 횟수도 피보나치를 따름

for _ in range(t):
  n = int(input())
  if n == 0:
    print(1, 0)
  elif n == 1:
    print(0, 1)
  else:
    print(dp[n-1], dp[n])
