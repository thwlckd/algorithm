# 상금 헌터
# 카카오 코드 페스티벌 2018 예선 A번

import sys
input = sys.stdin.readline

t = int(input())
rate = []
for i in range(t):
    rate.append(list(map(int, input().split())))

money = [[0, 500, 300, 200, 50, 30 ,10], [0, 512, 256, 128, 64, 32]]

def rate_17(x):
    if x == 0:
        return 0
    num = 0
    for i in range(1, 7):
        num = i * (i + 1) / 2
        if x <= num:
            return i
    return 0

def rate_18(x):
    if x == 0:
        return 0
    num = 0
    for i in range(1, 6):
        num += 2**(i - 1)
        if x <= num:
            return i
    return 0
        
for now in rate:
    a, b = now
    a = rate_17(a)
    b = rate_18(b)
    print(money[0][a]*10000 + money[1][b]*10000)

'''
입력 샘플
6
8 4
13 19
8 10
18 18
8 25
13 16
출력 샘플
1780000
620000
1140000
420000
820000
620000
'''