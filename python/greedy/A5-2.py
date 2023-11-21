# 볼링공 고르기
# 2회차 풀이

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        if data[i] != data[j]:
            result += 1

print(result)
