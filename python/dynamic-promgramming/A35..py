# DP
# 못생긴 수

n = int(input())

ugly = [1]
i2, i3, i5 = 0, 0, 0
ugly2 = 2
ugly3 = 3
ugly5 = 5
for i in range(1, n):
    ugly.append(min(ugly2, ugly3, ugly5))
    if ugly[i] == ugly2:
        i2 += 1
        ugly2 = ugly[i2] * 2
    if ugly[i] == ugly3:
        i3 += 1
        ugly3 = ugly[i3] * 3
    if ugly[i] == ugly5:
        i5 += 1
        ugly5 = ugly[i5] * 5

print(ugly[n-1])

'''
입력 예시
10
출력 예시
12
'''