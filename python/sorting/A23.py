# 정렬
# 국영수

import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    name, a, b, c = input().split()
    data.append((name, int(a), int(b), int(c)))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
# data.sort(key = lambda x: x[0])
# data.sort(key = lambda x: x[3], reverse=True)
# data.sort(key = lambda x: x[2])
# data.sort(key = lambda x: x[1], reverse=True)

for i in range(n):
    print(data[i][0])

'''
입력 샘플
12
Jun 50 60 100
Sangk 80 60 50
Suny 80 70 100
Soong 50 60 90
Hae 50 60 100
Kang 60 80 100
Dong 80 60 100
Sei 70 70 70
Wons 70 70 90
Sangh 70 70 80
nsj 80 80 80
Taew 50 60 90
출력 샘플
Dong
Sangk
Suny
nsj
Wons
Sangh
Sei
Kang
Hae
Jun
Soong
Taew
'''
