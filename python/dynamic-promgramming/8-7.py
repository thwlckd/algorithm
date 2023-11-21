# 다이나믹 프로그래밍
# 바닥 공사
# an = an-1 + 2an-2

n = int(input())
d = [0] * (n + 1)
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + 2 * d[i - 2]
print(d[n]%796796)
