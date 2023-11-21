# 카드 정렬하기

import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

sum = 0
while len(data) > 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    heapq.heappush(data, a+b)
    sum += a + b

print(sum)

'''
예제 입력
3
10
20
40
예제 출력
100
'''